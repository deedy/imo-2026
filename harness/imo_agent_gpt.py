"""Agentic harness: GPT-5.6 Sol (via OpenRouter) solves IMO 2026 problems, archiving AutoFyn-style artifacts.

Usage: MOONSHOT_API_KEY=sk-... uv run --with openai imo_agent.py <problem_num> [<problem_num> ...]

For each problem N, K3 works in results/imo-2026/kimi-k3/problem-0N/ and must
maintain current.md (proof document) plus optional approaches/, lemmas/, code/,
scratch/. Every tool call is recorded verbatim to logs.jsonl.
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx
from openai import APIConnectionError, APIError, APITimeoutError, OpenAI, RateLimitError

MODEL = "openai/gpt-5.6-sol"
MAX_TURNS = 80
SOFT_WARN_S = 100 * 60
HARD_STOP_S = 150 * 60
CKPT_NUDGE_TURNS = 4
CMD_TIMEOUT = 240
MAX_RESULT_CHARS = 20_000
LOG_TRUNCATE = 800

SCRIPT_DIR = Path(__file__).resolve().parent
PROBLEMS = {p["problem_id"]: p for p in json.load(open(SCRIPT_DIR / "imo2026_problems.json"))}
RESULTS_ROOT = Path("/Users/debarghya/vibedev/AutoFyn/results/imo-2026/gpt-5.6-sol-lightweight")

NET_BLOCK = re.compile(r"curl|wget|https?://|nc |ncat|ssh |scp ", re.IGNORECASE)

# Streaming client: reasoning turns can exceed any total-request timeout, so we
# bound the gap between chunks instead, and do our own retries (max_retries=0).
client = OpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
    timeout=httpx.Timeout(connect=30, read=1200, write=60, pool=30),
    max_retries=0,
)

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "bash",
            "description": (
                "Run a shell command in the problem workspace. Returns exit code, stdout, stderr. "
                f"Killed after {CMD_TIMEOUT}s. No network access — offline computation only."
            ),
            "parameters": {
                "type": "object",
                "properties": {"command": {"type": "string"}},
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Create or overwrite a file in the workspace (parents auto-created). Path relative to workspace root.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from the workspace. Path relative to workspace root.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
]

SYSTEM_PROMPT = """You are a world-class mathematician solving an IMO 2026 problem with complete rigor, working autonomously in a dedicated workspace directory.

STRICT INTEGRITY RULE: solve the problem yourself from first principles. You have NO internet access and must not attempt any network request. Do not rely on remembering a published solution; every claim must be proved in your write-up.

Deliverables (all paths relative to the workspace root):
- `current.md` — REQUIRED master document, structured exactly as:
  `# <problem-id> — tracking file` / `## Status` (solved | partial | unsolved) / `## Problem` (verbatim statement) / `## Approaches tried` (bulleted log) / `## Current best` (one-paragraph summary; for compute-and-prove problems state the explicit final answer here) / `## Full proof` (the complete, self-contained, rigorous proof in markdown+LaTeX).
- `approaches/<slug>.md` — one file per substantive approach you pursue (its idea, status, and details).
- `lemmas/<slug>.md` — standalone lemmas cited by the proof (statement + proof).
- `code/` — Python scripts you write to sanity-check claims (brute-force small cases, random testing, symbolic checks). Run them with `python3` or `uv run --with sympy,numpy python3 ...`. Numeric verification of key identities/formulas is strongly encouraged before you commit to them in the proof — but computation never substitutes for proof.
- `scratch/` — free scratch space for exploration notes.

Working discipline:
- UPDATE `current.md` AFTER EVERY SIGNIFICANT ADVANCE. The disk is the source of truth; if the session dies, only what is on disk survives. Never leave your best result only in conversation.
- Attack the problem from multiple angles; record dead ends honestly in `## Approaches tried`.
- Rigor bar: an IMO grader awarding 7/7. No gaps, no "clearly", every case handled. For compute-and-prove problems both the answer and its optimality/completeness must be proved.
- When (and only when) `current.md` contains your final complete write-up, reply with a short final message (NO tool calls) summarizing status and the answer."""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def log(text: str) -> None:
    print(text, flush=True)


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n... [truncated, {len(text)} chars total]"


class ProblemRun:
    def __init__(self, num: int):
        self.pid = f"imo-2026-{num:02d}"
        self.problem = PROBLEMS[self.pid]
        self.dir = RESULTS_ROOT / f"problem-{num:02d}"
        self.dir.mkdir(parents=True, exist_ok=True)
        (self.dir / "scratch").mkdir(exist_ok=True)
        self.records = []
        self.usage = {"prompt": 0, "completion": 0}

    def record(self, obj: dict) -> None:
        self.records.append(obj)
        with open(self.dir / "logs.jsonl", "w") as f:
            for r in self.records:
                f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n")

    def safe_path(self, rel: str) -> Path:
        p = (self.dir / rel).resolve()
        if not p.is_relative_to(self.dir):
            raise ValueError(f"path escapes workspace: {rel}")
        return p

    def tool_bash(self, command: str) -> str:
        if NET_BLOCK.search(command):
            return "error: network access is not permitted in this run"
        try:
            proc = subprocess.run(
                command, shell=True, cwd=self.dir, capture_output=True, text=True, timeout=CMD_TIMEOUT
            )
        except subprocess.TimeoutExpired:
            return f"error: command timed out after {CMD_TIMEOUT}s"
        out = proc.stdout or ""
        if proc.stderr:
            out += "\n[stderr]\n" + proc.stderr
        return f"exit code: {proc.returncode}\n{out}"

    def dispatch(self, name: str, args: dict) -> str:
        try:
            if name == "bash":
                return self.tool_bash(args["command"])
            if name == "write_file":
                p = self.safe_path(args["path"])
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(args["content"])
                return f"wrote {len(args['content'])} chars to {args['path']}"
            if name == "read_file":
                p = self.safe_path(args["path"])
                return p.read_text() if p.is_file() else f"error: no such file: {args['path']}"
            return f"error: unknown tool {name}"
        except Exception as e:
            return f"error: {e}"


def valid_tool_calls(tool_calls):
    """Tool calls whose ids are set and whose argument JSON parses completely."""
    out = []
    for i in sorted(tool_calls):
        tc = tool_calls[i]
        if not (tc["id"] and tc["function"]["name"]):
            return out  # a later call may be mid-stream; keep only the complete prefix
        try:
            json.loads(tc["function"]["arguments"])
        except json.JSONDecodeError:
            return out
        out.append(tc)
    return out


def stream_turn(messages):
    """One streamed completion.

    Returns (assistant_message_dict, usage_or_None, salvaged: bool). If the stream
    dies mid-generation but produced usable output (complete tool calls, or
    substantial content), the partial turn is returned with salvaged=True instead
    of throwing the work away and regenerating from scratch.
    """
    stream = client.chat.completions.create(
        model=MODEL, messages=messages, tools=TOOLS,
        stream=True, stream_options={"include_usage": True},
    )
    content, reasoning, usage = "", "", None
    tool_calls = {}
    stream_error = None
    try:
        for chunk in stream:
            if getattr(chunk, "usage", None):
                usage = chunk.usage
            if not chunk.choices:
                continue
            d = chunk.choices[0].delta
            if d is None:
                continue
            if d.content:
                content += d.content
            rc = ((d.model_extra or {}).get("reasoning_content") or (d.model_extra or {}).get("reasoning"))
            if rc:
                reasoning += rc
            for tc in d.tool_calls or []:
                slot = tool_calls.setdefault(
                    tc.index, {"id": "", "type": "function", "function": {"name": "", "arguments": ""}}
                )
                if tc.id:
                    slot["id"] = tc.id
                if tc.function:
                    if tc.function.name:
                        slot["function"]["name"] = tc.function.name
                    if tc.function.arguments:
                        slot["function"]["arguments"] += tc.function.arguments
    except Exception as e:
        stream_error = e

    calls = valid_tool_calls(tool_calls)
    if stream_error is not None:
        if "insufficient balance" in str(stream_error).lower():
            raise RuntimeError(f"FATAL: account balance exhausted: {stream_error}")
        # Salvageable only if the partial turn can drive the loop forward.
        if not calls and len(content) < 200:
            raise stream_error
        log(f"[salvage] stream died ({truncate(str(stream_error), 120)}) — keeping partial turn "
            f"({len(content)} content chars, {len(calls)} complete tool calls)")

    msg = {"role": "assistant", "content": content}
    if reasoning:
        msg["_reasoning_chars"] = len(reasoning)  # logged, stripped before sending
    if calls:
        msg["tool_calls"] = calls
    return msg, usage, stream_error is not None


def create_with_retry(messages):
    delay = 10
    for attempt in range(6):
        try:
            return stream_turn(messages)
        except RuntimeError:
            raise
        except (RateLimitError, APIConnectionError, APITimeoutError, APIError, httpx.HTTPError) as e:
            if "insufficient balance" in str(e).lower():
                raise RuntimeError(f"FATAL: account balance exhausted: {e}")
            if attempt == 5:
                raise
            log(f"[api error] {truncate(str(e), 300)} — retrying in {delay}s")
            time.sleep(delay)
            delay *= 2


def run_problem(num: int) -> None:
    run = ProblemRun(num)
    p = run.problem
    started = now_iso()
    t0 = time.monotonic()
    log(f"\n######## {run.pid} START {started} ########")

    task = (
        f"Problem {run.pid} (domain: {p['domain']}, task type: {p['task']}"
        + (f", expected answer form: {p['answer_type']}" if p.get("answer_type") not in (None, "none") else "")
        + f"):\n\n{p['statement']}"
    )
    if os.environ.get("IMO_CONTINUE"):
        task += (
            "\n\nNOTE: previous sessions ran out of time on this problem. Your workspace already contains "
            "the verified answer, the verified strategy, and extensive numerical confirmation (read "
            "current.md first; skim code/). THE COMPUTATIONAL PHASE IS OVER — do not write or run any new "
            "exploration code except at most a quick check of a specific identity you are about to use in "
            "prose. This session is for PROOF-WRITING ONLY: prove the open gaps listed in current.md, "
            "drafting the argument INTO current.md section by section AS YOU GO (write a section, then "
            "think about the next — never hold more than one section in your head). Prior sessions lost "
            "hours of correct reasoning by never writing it down. A complete rigorous write-up of even one "
            "of the two bounds is worth more than another session of unwritten thinking about both."
        )
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]
    run.record(
        {
            "record_type": "run",
            "problem_id": run.pid,
            "model_name": MODEL,
            "provider_name": "moonshot",
            "harness": "claude-code lightweight tool-loop (not AutoFyn)",
            "started_at": started,
            "system_prompt": SYSTEM_PROMPT,
            "custom_prompt": task,
        }
    )

    status, final_text, warned = "max_turns", None, False
    turns_since_ckpt = 0
    for turn in range(1, MAX_TURNS + 1):
        elapsed = time.monotonic() - t0
        if elapsed > HARD_STOP_S:
            status = "hard_time_limit"
            log(f"[{run.pid}] hard time limit reached at turn {turn}")
            break
        if elapsed > SOFT_WARN_S and not warned:
            warned = True
            messages.append(
                {
                    "role": "user",
                    "content": "TIME WARNING: your session ends soon. Ensure current.md contains your best complete, "
                    "rigorous write-up now. Finish verification, finalize the document, then reply with your final "
                    "summary message (no tool calls).",
                }
            )
            log(f"[{run.pid}] soft time warning injected")

        try:
            assistant, usage, salvaged = create_with_retry(messages)
        except Exception as e:
            status = f"api_failure: {truncate(str(e), 200)}"
            log(f"[{run.pid}] {status}")
            break

        if usage:
            run.usage["prompt"] += usage.prompt_tokens
            run.usage["completion"] += usage.completion_tokens
        messages.append(assistant)

        log(
            f"[{run.pid}] === turn {turn} ({elapsed/60:.0f}m, "
            f"{assistant.pop('_reasoning_chars', 0)} reasoning chars"
            + (", SALVAGED" if salvaged else "") + ") ==="
        )
        if assistant.get("content"):
            log(f"[{run.pid}] [assistant] {truncate(assistant['content'], LOG_TRUNCATE)}")

        if salvaged and not assistant.get("tool_calls"):
            messages.append(
                {
                    "role": "user",
                    "content": "Your last message was cut off by a network error mid-stream. Continue "
                    "from where it left off. Checkpoint any results you have derived so far into "
                    "current.md before doing further reasoning.",
                }
            )
            run.record({"record_type": "salvage_note", "ts": now_iso(), "turn": turn})
            continue

        if not assistant.get("tool_calls"):
            status, final_text = "completed", assistant.get("content")
            run.record(
                {"record_type": "final_message", "ts": now_iso(), "turn": turn, "content": final_text}
            )
            break

        for tc in assistant["tool_calls"]:
            name = tc["function"]["name"]
            try:
                args = json.loads(tc["function"]["arguments"])
            except json.JSONDecodeError as e:
                args, result = {}, f"error: invalid JSON arguments: {e}"
            else:
                result = run.dispatch(name, args)
            preview = args.get("command") or args.get("path") or ""
            log(f"[{run.pid}] [tool] {name}: {truncate(preview, 200)}")
            log(f"[{run.pid}] [result] {truncate(result, LOG_TRUNCATE)}")
            run.record(
                {
                    "record_type": "tool_call",
                    "ts": now_iso(),
                    "turn": turn,
                    "tool_name": name,
                    "input_data": args,
                    "output_data": truncate(result, MAX_RESULT_CHARS),
                }
            )
            messages.append(
                {"role": "tool", "tool_call_id": tc["id"], "content": truncate(result, MAX_RESULT_CHARS)}
            )
            if name == "write_file" and args.get("path", "").lstrip("./") == "current.md":
                turns_since_ckpt = -1  # reset below

        turns_since_ckpt += 1
        if turns_since_ckpt >= CKPT_NUDGE_TURNS:
            turns_since_ckpt = 0
            messages.append(
                {
                    "role": "user",
                    "content": f"CHECKPOINT REMINDER: you have not updated current.md in {CKPT_NUDGE_TURNS} "
                    "turns. Write your current progress (partial proofs, established lemmas, open gaps) "
                    "into current.md NOW, then continue. Anything not on disk is lost if the session dies.",
                }
            )
            log(f"[{run.pid}] checkpoint nudge injected")

    # Emergency write-up: if the run is dying with work potentially stranded in
    # context, give the model a short window to dump its state to disk.
    if status.startswith(("hard_time_limit", "api_failure")) and "FATAL" not in status:
        log(f"[{run.pid}] emergency write-up pass")
        messages.append(
            {
                "role": "user",
                "content": "SESSION ENDING NOW. In your next one or two turns, use write_file to save "
                "everything of value from your reasoning into current.md (and lemmas/ files if warranted): "
                "your best proofs or partial proofs, exact statements of what is established vs. missing. "
                "Do not do any new mathematics. Then reply with a one-line final message.",
            }
        )
        try:
            for extra in range(3):
                assistant, usage, _ = create_with_retry(messages)
                if usage:
                    run.usage["prompt"] += usage.prompt_tokens
                    run.usage["completion"] += usage.completion_tokens
                messages.append(assistant)
                if not assistant.get("tool_calls"):
                    run.record({"record_type": "emergency_final", "ts": now_iso(),
                                "content": assistant.get("content")})
                    status += "+salvage_writeup"
                    break
                for tc in assistant["tool_calls"]:
                    name = tc["function"]["name"]
                    try:
                        args = json.loads(tc["function"]["arguments"])
                    except json.JSONDecodeError as e:
                        args, result = {}, f"error: invalid JSON arguments: {e}"
                    else:
                        result = run.dispatch(name, args)
                    log(f"[{run.pid}] [salvage-tool] {name}: {truncate(args.get('path') or args.get('command') or '', 150)}")
                    run.record({"record_type": "tool_call", "ts": now_iso(), "turn": f"salvage-{extra}",
                                "tool_name": name, "input_data": args,
                                "output_data": truncate(result, MAX_RESULT_CHARS)})
                    messages.append({"role": "tool", "tool_call_id": tc["id"],
                                     "content": truncate(result, MAX_RESULT_CHARS)})
        except Exception as e:
            log(f"[{run.pid}] emergency write-up failed: {truncate(str(e), 150)}")

    run.record(
        {
            "record_type": "run_end",
            "ts": now_iso(),
            "status": status,
            "duration_minutes": round((time.monotonic() - t0) / 60, 1),
            "prompt_tokens": run.usage["prompt"],
            "completion_tokens": run.usage["completion"],
        }
    )
    log(f"######## {run.pid} END status={status} ({run.usage['prompt']}p/{run.usage['completion']}c tokens) ########")
    if status.startswith("api_failure: FATAL"):
        sys.exit(2)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        run_problem(int(arg))
    log("WORKER DONE")
