# IMO 2026 — Autonomous AI Model Comparison

Frontier models solving all six problems of the [International Mathematical Olympiad 2026](problems/), fully autonomously, with complete per-turn audit trails and **independently verified grading**.

Seven runs across five models and two harness designs:

| Run | Harness | P1 | P2 | P3 | P4 | P5 | P6 | **Graded** | Time | Cost |
|---|---|--|--|--|--|--|--|--|--|--|
| **Claude Fable 5** | AutoFyn | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 7.1 h | $32.39 |
| **GPT-5.6 Sol** | AutoFyn | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 3.7 h | $5.96 |
| **Claude Fable 5** | lightweight | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 1.8 h | $38.83 |
| **Kimi K3** | lightweight | 7 | 7 | 5 | 7 | 7 | 3 | **36/42** | 12.7 h | ~$28.20 |
| **GPT-5.6 Sol** | lightweight | 7 | 4 | 2 | 7 | 7 | 1 | **28/42** | 1.0 h | ~$4.04 |
| Claude Opus 4.8 | AutoFyn (partial archive) | 7 | – | 3 | – | 7 | 7 | 24/28 | — | — |
| Claude Opus 4.5 | AutoFyn | 6 | 4 | 2 | 5 | 4 | 2 | **23/42** | — | — |

*Scores are IMO-style 0–7 from six independent verifier agents that re-derived key algebra symbolically, machine-tested combinatorial claims, and constructed explicit counterexamples to failed lemmas — **not** the models' self-reports (40 of 41 attempted entries self-reported "solved"). See [grades/](grades/) for per-problem verdicts with named defects.*

## Headline findings

- **Three verified 42/42 runs.** Both AutoFyn runs, and Claude Fable 5 even in the bare single-context harness — where it was also fastest (1.8 h).
- **The harness effect is model-dependent.** GPT-5.6 Sol: verified 42/42 inside AutoFyn's orchestrated verify-loop, but 28/42 in the lightweight loop — its 60-minute sweep produced confident write-ups whose crux steps fail under scrutiny (P6's central lemma is refuted by an explicit counterexample). Claude Fable 5 showed no such degradation.
- **Self-reports inflate.** Graders confirmed only 33 of 40 "solved" claims as complete proofs. All stated answers to the compute-and-prove problems agree across every run.
- **Kimi K3's 36/42** came the hard way: 12.7 h including three failed rounds on P3 whose in-context reasoning was lost to time caps before checkpoint-discipline countermeasures were added to the harness.

## Repository layout

```
problems/    the six problem statements (+ problems.json with metadata)
results/     one directory per run: per-problem current.md (the proof), approaches/,
             lemmas/, code/ (the model's own verification scripts), scratch/, and
             logs.jsonl — a complete per-turn audit trail (every tool call, verbatim)
grades/      per-problem grading verdicts (JSON): score, justification, named defects
pdfs/        typeset solution PDFs (30) + the comparison report
harness/     the lightweight tool-loop harnesses (Kimi K3 / GPT via OpenRouter /
             Claude Fable 5 via Anthropic SDK) — same prompt, tools, and caps
```

## Methodology

- **AutoFyn runs** ([SignalPilot-Labs/AutoFyn](https://github.com/SignalPilot-Labs/AutoFyn)): multi-agent orchestration with round-based context resets and reviewer roles. Its day-1 solutions (P1–P3) were additionally verified by three past IMO medalists.
- **Lightweight runs**: a deliberately minimal single-context agent loop (this repo, `harness/`): three tools (bash / write_file / read_file), no orchestration, no reviewer, network blocked, identical system prompt and time caps (150 min/problem) across all three models. Problem statements were fed verbatim; models were instructed to solve from first principles and to verify claims numerically before committing them to the proof.
- **Grading**: one verifier agent per problem graded all runs blind to cost/time, instructed to hunt for gaps, verify algebra symbolically, and machine-test doubtful claims; several defects were confirmed by explicit counterexample or exact minimax computation. Grader outputs are in `grades/` verbatim.

## Caveats

- Graders are Claude-based agents, not human medalists; treat scores as strong but not authoritative. (The two 42/42 AutoFyn runs are corroborated by human medalist review on day 1.)
- Harnesses differ between AutoFyn and lightweight runs; time/cost comparisons across harnesses are indicative, not controlled. Within the lightweight harness the three runs are directly comparable.
- Kimi K3 cost is estimated from logged tokens at list pricing (cache split assumed at the 93% hit rate observed in metered runs); GPT lightweight cost from OpenRouter list pricing.

## Provenance

All runs executed July 17–18, 2026, driven by Claude Code (Claude Fable 5) as the orchestrating agent. Every model turn, tool call, and result is recorded verbatim in the corresponding `logs.jsonl`; prior failed rounds are preserved under each problem's `scratch/`. Problem statements © IMO; sourced from [tempcollab/proval](https://github.com/tempcollab/proval).
