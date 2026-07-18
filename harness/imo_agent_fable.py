"""Agentic harness: Claude Fable 5 solves IMO 2026 problems (lightweight loop, Anthropic SDK).

Same tools, system prompt, and caps as the Kimi K3 / GPT-5.6 Sol harnesses.
Usage: uv run --with anthropic imo_agent_fable.py <problem_num> [...]  (ANTHROPIC_API_KEY from env)
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import httpx

MODEL = "claude-fable-5"
MAX_TURNS = 80
SOFT_WARN_S = 100 * 60
HARD_STOP_S = 150 * 60
CKPT_NUDGE_TURNS = 4
CMD_TIMEOUT = 240
MAX_RESULT_CHARS = 20_000
LOG_TRUNCATE = 800
MAX_TOKENS = 64_000

SCRIPT_DIR = Path(__file__).resolve().parent
PROBLEMS = {p["problem_id"]: p for p in json.load(open(SCRIPT_DIR / "imo2026_problems.json"))}
RESULTS_ROOT = Path("/Users/debarghya/vibedev/AutoFyn/results/imo-2026/claude-fable-5-lightweight")

NET_BLOCK = re.compile(r"curl|wget|https?://|nc |ncat|ssh |scp ", re.IGNORECASE)

client = anthropic.Anthropic(
    timeout=httpx.Timeout(connect=30, read=1200, write=60, pool=30),
    max_retries=0,  # our own retry loop below
)

TOOLS = [
    {
        "name": "bash",
        "description": (
            "Run a shell command in the problem workspace. Returns exit code, stdout, stderr. "
            f"Killed after {CMD_TIMEOUT}s. No network access — offline computation only."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"],
        },
    },
    {
        "name": "write_file",
        "description": "Create or overwrite a file in the workspace (parents auto-created). Path relative to workspace root.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
            "required": ["path", "content"],
        },
    },
    {
        "name": "read_file",
        "description": "Read a file from the workspace. Path relative to workspace root.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
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
        self.usage = {"input": 0, "output": 0, "cache_write": 0, "cache_read": 0}

    def record(self, obj: dict) -> None:
        self.records.append(obj)
        with open(self.dir / "logs.jsonl", "w") as f:
            for r in self.records:
                f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n")

    def add_usage(self, u) -> None:
        self.usage["input"] += u.input_tokens or 0
        self.usage["output"] += u.output_tokens or 0
        self.usage["cache_write"] += getattr(u, "cache_creation_input_tokens", 0) or 0
        self.usage["cache_read"] += getattr(u, "cache_read_input_tokens", 0) or 0

    def cost_usd(self) -> float:
        return round(
            self.usage["input"] * 10 / 1e6
            + self.usage["cache_write"] * 12.5 / 1e6
            + self.usage["cache_read"] * 1 / 1e6
            + self.usage["output"] * 50 / 1e6,
            2,
        )

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


def stream_turn(messages):
    """One streamed Fable turn. Returns the final Message. Thinking is always on
    (no thinking param needed); summarized display keeps a readable audit trail."""
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        thinking={"type": "adaptive", "display": "summarized"},
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=messages,
        cache_control={"type": "ephemeral"},
    ) as stream:
        for _ in stream:
            pass
        return stream.get_final_message()


def create_with_retry(messages):
    delay = 10
    for attempt in range(6):
        try:
            return stream_turn(messages)
        except (anthropic.RateLimitError, anthropic.APIConnectionError,
                anthropic.APITimeoutError, anthropic.InternalServerError, httpx.HTTPError) as e:
            if attempt == 5:
                raise
            log(f"[api error] {truncate(str(e), 300)} — retrying in {delay}s")
            time.sleep(delay)
            delay *= 2


def blocks_to_log(content) -> list:
    out = []
    for b in content:
        if b.type == "thinking":
            out.append({"type": "thinking", "chars": len(b.thinking or "")})
        elif b.type == "text":
            out.append({"type": "text", "text": b.text})
        elif b.type == "tool_use":
            out.append({"type": "tool_use", "name": b.name, "input": b.input})
        else:
            out.append({"type": b.type})
    return out


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
    messages = [{"role": "user", "content": task}]
    run.record({
        "record_type": "run", "problem_id": run.pid, "model_name": MODEL,
        "provider_name": "anthropic",
        "harness": "claude-code lightweight tool-loop (not AutoFyn); same prompt/tools/caps as kimi-k3 harness",
        "started_at": started, "system_prompt": SYSTEM_PROMPT, "custom_prompt": task,
    })

    status, warned = "max_turns", False
    turns_since_ckpt = 0
    for turn in range(1, MAX_TURNS + 1):
        elapsed = time.monotonic() - t0
        if elapsed > HARD_STOP_S:
            status = "hard_time_limit"
            log(f"[{run.pid}] hard time limit reached at turn {turn}")
            break
        if elapsed > SOFT_WARN_S and not warned:
            warned = True
            messages.append({
                "role": "user",
                "content": "TIME WARNING: your session ends soon. Ensure current.md contains your best "
                "complete, rigorous write-up now. Finish verification, finalize the document, then reply "
                "with your final summary message (no tool calls).",
            })
            log(f"[{run.pid}] soft time warning injected")

        try:
            resp = create_with_retry(messages)
        except Exception as e:
            status = f"api_failure: {truncate(str(e), 200)}"
            log(f"[{run.pid}] {status}")
            break

        run.add_usage(resp.usage)
        thinking_chars = sum(len(b.thinking or "") for b in resp.content if b.type == "thinking")
        texts = [b.text for b in resp.content if b.type == "text"]
        tool_uses = [b for b in resp.content if b.type == "tool_use"]
        messages.append({"role": "assistant", "content": resp.content})  # pass blocks back unchanged

        log(f"[{run.pid}] === turn {turn} ({elapsed/60:.0f}m, {thinking_chars} thinking chars) ===")
        for t in texts:
            if t.strip():
                log(f"[{run.pid}] [assistant] {truncate(t, LOG_TRUNCATE)}")

        if resp.stop_reason == "refusal":
            status = "refusal"
            run.record({"record_type": "refusal", "ts": now_iso(), "turn": turn})
            break

        if resp.stop_reason == "max_tokens":
            run.record({"record_type": "max_tokens_continue", "ts": now_iso(), "turn": turn})
            messages.append({"role": "user", "content": "Your response hit the output limit. Continue."})
            continue

        if not tool_uses:
            status = "completed"
            run.record({"record_type": "final_message", "ts": now_iso(), "turn": turn,
                        "content": "\n".join(texts)})
            break

        results = []
        for tu in tool_uses:
            result = run.dispatch(tu.name, tu.input)
            preview = tu.input.get("command") or tu.input.get("path") or ""
            log(f"[{run.pid}] [tool] {tu.name}: {truncate(str(preview), 200)}")
            log(f"[{run.pid}] [result] {truncate(result, LOG_TRUNCATE)}")
            run.record({"record_type": "tool_call", "ts": now_iso(), "turn": turn,
                        "tool_name": tu.name, "input_data": tu.input,
                        "output_data": truncate(result, MAX_RESULT_CHARS)})
            results.append({"type": "tool_result", "tool_use_id": tu.id,
                            "content": truncate(result, MAX_RESULT_CHARS)})
            if tu.name == "write_file" and str(tu.input.get("path", "")).lstrip("./") == "current.md":
                turns_since_ckpt = -1
        messages.append({"role": "user", "content": results})

        turns_since_ckpt += 1
        if turns_since_ckpt >= CKPT_NUDGE_TURNS:
            turns_since_ckpt = 0
            messages.append({
                "role": "user",
                "content": f"CHECKPOINT REMINDER: you have not updated current.md in {CKPT_NUDGE_TURNS} "
                "turns. Write your current progress (partial proofs, established lemmas, open gaps) "
                "into current.md NOW, then continue. Anything not on disk is lost if the session dies.",
            })
            log(f"[{run.pid}] checkpoint nudge injected")

    if status.startswith(("hard_time_limit", "api_failure")):
        log(f"[{run.pid}] emergency write-up pass")
        messages.append({
            "role": "user",
            "content": "SESSION ENDING NOW. In your next one or two turns, use write_file to save "
            "everything of value from your reasoning into current.md (and lemmas/ files if warranted): "
            "your best proofs or partial proofs, exact statements of what is established vs. missing. "
            "Do not do any new mathematics. Then reply with a one-line final message.",
        })
        try:
            for extra in range(3):
                resp = create_with_retry(messages)
                run.add_usage(resp.usage)
                messages.append({"role": "assistant", "content": resp.content})
                tool_uses = [b for b in resp.content if b.type == "tool_use"]
                if not tool_uses:
                    run.record({"record_type": "emergency_final", "ts": now_iso(),
                                "content": "\n".join(b.text for b in resp.content if b.type == "text")})
                    status += "+salvage_writeup"
                    break
                results = []
                for tu in tool_uses:
                    result = run.dispatch(tu.name, tu.input)
                    log(f"[{run.pid}] [salvage-tool] {tu.name}")
                    run.record({"record_type": "tool_call", "ts": now_iso(), "turn": f"salvage-{extra}",
                                "tool_name": tu.name, "input_data": tu.input,
                                "output_data": truncate(result, MAX_RESULT_CHARS)})
                    results.append({"type": "tool_result", "tool_use_id": tu.id,
                                    "content": truncate(result, MAX_RESULT_CHARS)})
                messages.append({"role": "user", "content": results})
        except Exception as e:
            log(f"[{run.pid}] emergency write-up failed: {truncate(str(e), 150)}")

    run.record({
        "record_type": "run_end", "ts": now_iso(), "status": status,
        "duration_minutes": round((time.monotonic() - t0) / 60, 1),
        "usage": run.usage, "cost_usd": run.cost_usd(),
    })
    log(f"######## {run.pid} END status={status} usage={run.usage} cost=${run.cost_usd()} ########")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        run_problem(int(arg))
    log("WORKER DONE")
