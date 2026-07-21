# IMO 2026 — Autonomous AI Model Comparison

Frontier and challenger models solving all six problems of the [International Mathematical Olympiad 2026](problems/), fully autonomously, with complete per-turn audit trails and **independently verified grading**.

Six runs across five models, all in the identical minimal agent harness:

| Run | P1 | P2 | P3 | P4 | P5 | P6 | **Graded** | Time | Cost |
|---|--|--|--|--|--|--|--|--|--|
| **Claude Fable 5** (default `high` effort) | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 2.5 h | $51.05 |
| **GPT-5.6 Sol** (xhigh effort)† | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 3.8 h | ~$20.54 |
| **Kimi K3** (default effort)† | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 17.4 h | ~$31.40 |
| **GPT-5.6 Sol** (default effort) | 7 | 4 | 2 | 7 | 7 | 1 | **28/42** | 1.0 h | ~$4.04 |
| **Meta Muse Spark 1.1** (xhigh effort) | 7 | 2 | 1 | 7 | 7 | 2 | **26/42** | 2.3 h | ~$4.45 |
| **xAI Grok 4.5** (xhigh effort)‡ | 7 | 2 | 2 | 0 | 1 | 1 | **13/42** | 3.2 h | ~$14.60 |

*Time and cost are totals across **all** rounds, including rounds killed by API outages and network failures — see [REPORT.md](REPORT.md) for per-problem attempts, tokens, and a clean-vs-total breakdown. † includes repair rounds: after initial grading, these runs were shown the reviewer's specific defect findings (never other solutions) and given further sessions; every repaired score was re-verified as strictly as the original. ‡ Grok 4.5 repeatedly ended turns claiming to "write the file" without ever calling the write-tool (P4, P5); a harness guard was added to force an actual write before finishing — no mathematical hints, purely a tool-adherence fix. Scores are IMO-style 0–7 from independent verifier agents that re-derived key algebra symbolically, machine-tested combinatorial claims, and constructed explicit counterexamples to failed lemmas — **not** the models' self-reports. See [grades/](grades/) for per-problem verdicts with named defects.*

### First pass (before any repair round)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | **Total** |
|---|--|--|--|--|--|--|--|
| **Claude Fable 5** | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** |
| **GPT-5.6 Sol** (xhigh effort) | 7 | 4 | 7 | 7 | 7 | 7 | **39/42** |
| **Kimi K3** | 7 | 7 | 5 | 7 | 7 | 3 | **36/42** |
| **GPT-5.6 Sol** (default effort) | 7 | 4 | 2 | 7 | 7 | 1 | **28/42** |
| **Meta Muse Spark 1.1** | 7 | 2 | 1 | 7 | 7 | 2 | **26/42** |
| **xAI Grok 4.5** | 7 | 2 | 2 | 0 | 1 | 1 | **13/42** |

The clean single-shot comparison: **Claude Fable 5 is the only run graded 42/42 without any repair round.** Meta Muse Spark 1.1 and xAI Grok 4.5 ran single-pass (no repair rounds); their scores are both first-pass and final.

## Headline findings

- **Claude Fable 5: verified 42/42 — and the fastest run (1.8 h).** Full rigor with no reviewer, no orchestration, no second chances, including the only fully synthetic P2 geometry proof among all runs.
- **Review feedback closes the loop.** Given only a reviewer's defect findings, GPT-5.6 Sol (xhigh) repaired its P2 and Kimi K3 repaired both its P3 and its P6 finiteness crux (inventing a new compactness theorem from the greedy killing property) — bringing all three models to verified 42/42. Every fix was re-graded as adversarially as the originals: exact minimax, independent reimplementation across dozens of seeds, and counterexample-family exclusion checks.
- **Reasoning effort buys rigor.** GPT-5.6 Sol jumped 28 → 39/42 going from default to `xhigh` effort in the identical harness: P3 and P6 became verified 7s (a previously false lemma replaced by a correct argument), and its P2 failure became an honestly self-declared `partial` instead of a confident invalid proof. Depth improved calibration, not just correctness.
- **Kimi K3 earned its 42/42 the hard way**: 17.4 h and multiple repair rounds, with early in-context reasoning lost to time caps before checkpoint-discipline countermeasures were added to the harness — but its final P6 compactness argument was original, load-bearing mathematics verified by independent reimplementation.
- **A clear capability tier break among the challengers.** Added later, the two newest models land far below the frontier tier on first pass — **Meta Muse Spark 1.1 at 26/42**, **xAI Grok 4.5 at 13/42**. Both solve the routine problems (P1; Muse also P4/P5) but neither closes the geometry (P2), combinatorics capstone (P3), or number-theory finale (P6). Muse got P3 *wrong* (conjectured c=(n+1)/(2n+1), false for all n≥2, confirmed by exact minimax), and every "solved" claim either model made on a hard problem collapsed under verification.
- **Grok 4.5 has a tool-adherence problem.** On P4 and P5 it repeatedly ended its turn narrating "📥 Writing final `current.md`…" while making **zero tool calls**, silently producing nothing in a bare agentic loop. It needed a harness guard (refuse "done" until the file actually exists) to emit gradeable output — a failure mode none of the other five models showed. Even then its written proofs were the weakest of the field.
- **Self-reports inflate.** Nearly every run claimed every attempted problem "solved"; graders confirmed only the scores above, with every deduction documented as a named, checkable defect. All stated answers to the compute-and-prove problems agree across every run.

## Repository layout

```
problems/    the six problem statements (+ problems.json with metadata)
results/     one directory per run: per-problem current.md (the proof), approaches/,
             lemmas/, code/ (the model's own verification scripts), scratch/, and
             logs.jsonl — a complete per-turn audit trail (every tool call, verbatim)
grades/      per-problem grading verdicts (JSON): score, justification, named defects
REPORT.md    per-problem attempts, wall-clock time, tokens, and cost
pdfs/        typeset per-problem solution PDFs + the comparison report
solutions/   one combined PDF per model (title page + all six problems)
harness/     the agent harnesses (Kimi K3 / GPT via OpenRouter / Claude Fable 5 via
             Anthropic SDK) — same prompt, tools, and caps across all runs
```

## Methodology

- **The harness** (`harness/`): a deliberately minimal single-context agent loop — three tools (bash / write_file / read_file), no orchestration, no reviewer, network blocked, identical system prompt and time caps (150 min/problem) for every model. Problem statements were fed verbatim; models were instructed to solve from first principles and to verify claims numerically before committing them to the proof. **Reasoning settings**: Claude Fable 5 ran with its always-on adaptive thinking at the API's default effort (`high`; no `effort` parameter passed); Kimi K3 ran at its API default (no effort control exposed); GPT-5.6 Sol ran twice — once at OpenRouter's default reasoning effort (`medium`) and once at `xhigh`, the maximum accepted; Meta Muse Spark 1.1 and xAI Grok 4.5 both ran at `xhigh`. Runs that died to infrastructure failures (API outages, billing) — or, for Grok, to ending a turn without writing its file — were resumed from their on-disk checkpoints; all prior rounds are preserved in each problem's `scratch/`.
- **Grading**: one verifier agent per problem, instructed to hunt for gaps, verify algebra symbolically, and machine-test doubtful claims; several defects were confirmed by explicit counterexample or exact minimax computation. Grader outputs are in `grades/` verbatim.

## Caveats

- Graders are Claude-based agents, not human medalists; treat scores as strong but not authoritative.
- All runs share the identical harness, so they are directly comparable; the one controlled difference between the two GPT-5.6 Sol runs is the reasoning-effort setting.
- Claude Fable 5 cost is as metered by the Anthropic API. Kimi K3 cost is estimated from logged tokens at list pricing (cache split assumed at a 93% hit rate); GPT-5.6 Sol, Meta Muse Spark 1.1, and xAI Grok 4.5 costs from OpenRouter list pricing.

## Provenance

All runs executed July 17–18, 2026, driven by Claude Code (Claude Fable 5) as the orchestrating agent. Every model turn, tool call, and result is recorded verbatim in the corresponding `logs.jsonl`. Problem statements © IMO; sourced from [tempcollab/proval](https://github.com/tempcollab/proval).
