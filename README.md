# IMO 2026 — Autonomous AI Model Comparison

Frontier and challenger models solving all six problems of the [International Mathematical Olympiad 2026](problems/), fully autonomously, with complete per-turn audit trails and **independently verified grading**.

Nine runs across seven models, all in the identical minimal agent harness:

| Run | P1 | P2 | P3 | P4 | P5 | P6 | **Graded** | Time | Cost |
|---|--|--|--|--|--|--|--|--|--|
| **Claude Fable 5** (default `high` effort) | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 2.5 h | $51.05 |
| **GPT-5.6 Sol** (xhigh effort)† | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 3.8 h | ~$20.54 |
| **Kimi K3** (default effort)† | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** | 17.4 h | ~$31.40 |
| **GPT-5.6 Sol Pro** (xhigh effort)§ | 7 | 7 | 2 | 7 | 7 | 7 | **37/42** | 2.1 h | ~$42.32 |
| **GPT-5.6 Sol** (**max** effort) | 7 | 7 | 1 | 7 | 7 | 1 | **30/42** | 2.1 h | ~$23.43 |
| **GPT-5.6 Sol** (default effort) | 7 | 4 | 2 | 7 | 7 | 1 | **28/42** | 1.0 h | ~$4.04 |
| **Meta Muse Spark 1.1** (xhigh effort) | 7 | 2 | 1 | 7 | 7 | 2 | **26/42** | 2.3 h | ~$4.45 |
| **DeepSeek V4 Pro** (max effort)‡ | 7 | 2 | 1 | 1 | 7 | 1 | **19/42** | 8.9 h | ~$6.05 |
| **xAI Grok 4.5** (xhigh effort)‡ | 7 | 2 | 2 | 0 | 1 | 1 | **13/42** | 3.2 h | ~$14.60 |

*Time and cost are totals across **all** rounds, including rounds killed by API outages and network failures — see [REPORT.md](REPORT.md) for per-problem attempts, tokens, and a clean-vs-total breakdown. † includes repair rounds: after initial grading, these runs were shown the reviewer's specific defect findings (never other solutions) and given further sessions; every repaired score was re-verified as strictly as the original. § GPT-5.6 Sol Pro and GPT-5.6 Sol (max) ran **single-pass, with no reviewer-feedback repair rounds** — their scores are both first-pass and final. Two of Sol Pro's problems needed a fresh session for reasons unrelated to the model's mathematics: **(P6)** its first session was a degenerate null bail (it ended after 2 turns with zero reasoning and a 15-line stub while its P5 in the same run solved cleanly), archived and given **one fair fresh retry** that solved it 7/7; **(P2)** its first session was accidentally killed by the orchestrator at turn 50 of 80 while it was still actively working (my error, not a model bail), and two follow-up attempts died to OpenRouter credit exhaustion — so P2 was re-run from scratch to a full completion (215-line proof, crux identity machine-verified to close symbolically = 7/7). All interrupted sessions are archived in `results/gpt-5.6-sol-pro/problem-0N/scratch/`; no reviewer input or hints were ever given. Sol Pro's time/cost here are productive-round figures (excluding those interrupted reruns); see [REPORT.md](REPORT.md) for the clean-vs-total breakdown. Its P2 is genuinely token-heavy (a 50-turn, 4.6M-prompt geometry proof), which is why its cost exceeds the base `xhigh` run despite fewer problems solved. ‡ Grok 4.5 and DeepSeek V4 Pro both repeatedly ended turns claiming to "write the file" without ever calling the write-tool; a harness guard was added to force an actual write before finishing — no mathematical hints, purely a tool-adherence fix. (For DeepSeek the guard caught it inline, so it still used one round per problem.) Scores are IMO-style 0–7 from independent verifier agents that re-derived key algebra symbolically, machine-tested combinatorial claims, and constructed explicit counterexamples to failed lemmas — **not** the models' self-reports. See [grades/](grades/) for per-problem verdicts with named defects.*

### First pass (before any repair round)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | **Total** |
|---|--|--|--|--|--|--|--|
| **Claude Fable 5** | 7 | 7 | 7 | 7 | 7 | 7 | **42/42** |
| **GPT-5.6 Sol** (xhigh effort) | 7 | 4 | 7 | 7 | 7 | 7 | **39/42** |
| **Kimi K3** | 7 | 7 | 5 | 7 | 7 | 3 | **36/42** |
| **GPT-5.6 Sol Pro** (xhigh effort) | 7 | 7 | 2 | 7 | 7 | 7 | **37/42** |
| **GPT-5.6 Sol** (**max** effort) | 7 | 7 | 1 | 7 | 7 | 1 | **30/42** |
| **GPT-5.6 Sol** (default effort) | 7 | 4 | 2 | 7 | 7 | 1 | **28/42** |
| **Meta Muse Spark 1.1** | 7 | 2 | 1 | 7 | 7 | 2 | **26/42** |
| **DeepSeek V4 Pro** | 7 | 2 | 1 | 1 | 7 | 1 | **19/42** |
| **xAI Grok 4.5** | 7 | 2 | 2 | 0 | 1 | 1 | **13/42** |

The clean single-shot comparison: **Claude Fable 5 is the only run graded 42/42 without any repair round.** Meta Muse Spark 1.1, DeepSeek V4 Pro, xAI Grok 4.5, GPT-5.6 Sol Pro, and GPT-5.6 Sol (max) ran single-pass (no reviewer-feedback repair rounds); their scores are both first-pass and final. (Sol Pro's P6 shown here is its fair-retry result after a degenerate null first session — see the scoreboard footnote §.)

## Headline findings

- **Claude Fable 5: verified 42/42 — and the fastest run (1.8 h).** Full rigor with no reviewer, no orchestration, no second chances, including the only fully synthetic P2 geometry proof among all runs.
- **Review feedback closes the loop.** Given only a reviewer's defect findings, GPT-5.6 Sol (xhigh) repaired its P2 and Kimi K3 repaired both its P3 and its P6 finiteness crux (inventing a new compactness theorem from the greedy killing property) — bringing all three models to verified 42/42. Every fix was re-graded as adversarially as the originals: exact minimax, independent reimplementation across dozens of seeds, and counterexample-family exclusion checks.
- **Reasoning effort buys rigor.** GPT-5.6 Sol jumped 28 → 39/42 going from default to `xhigh` effort in the identical harness: P3 and P6 became verified 7s (a previously false lemma replaced by a correct argument), and its P2 failure became an honestly self-declared `partial` instead of a confident invalid proof. Depth improved calibration, not just correctness.
- **…but the returns stop, and neither "bigger knob" clearly beat base Sol at `xhigh`.** Two follow-up runs probed the obvious upgrades. (1) **Cranking effort past `xhigh` to `max`** (the highest OpenRouter exposes: `max` > `xhigh` > `high` > …) on the *same* base `gpt-5.6-sol` scored **30/42 single-pass — below** the model's own 39/42 first-pass at `xhigh`. The extra reasoning budget didn't buy more solved problems; it just reshuffled which ones fell (max effort *did* uniquely crack the P2 geometry that `xhigh` first missed, but then bailed on P6 and P3). (2) The higher **`gpt-5.6-sol-pro` tier at equal `xhigh` effort** scored **37/42**, edging out base Sol's 39/42 first-pass only after you account for the fact that both its remaining losses were on the two genuinely hardest problems — it solved the P2 geometry (7/7, crux identity closed symbolically) and the P6 number-theory finale (7/7), and its **only real miss was the P3 combinatorics capstone** (2/7 — correct answer, no proof). Across all four base-and-Pro Sol runs the totals cluster in the 30–39 band with *different* problems cracked each time: at this frontier, *which* of the two hardest problems (geometry P2, combinatorics P3, number-theory P6) a given run closes is stochastic, and neither more effort nor the higher tier reliably closes all of them in one pass. Note Sol Pro's P2 needed a fair re-run after an orchestrator error killed its first (productive) session mid-proof — see the scoreboard footnote §.
- **Sol Pro got P3's answer *right* where the challengers got it wrong.** Even scoring only 2/7 on P3 (proof incomplete), GPT-5.6 Sol Pro correctly determined the answer c = 2ⁿ/(2ⁿ⁺¹−1) — verified by exact minimax — whereas Meta Muse Spark 1.1 and DeepSeek V4 Pro both confidently produced the *false* c = (n+1)/(2n+1). Knowing the right answer but not proving it is a categorically better failure than proving the wrong one.
- **Kimi K3 earned its 42/42 the hard way**: 17.4 h and multiple repair rounds, with early in-context reasoning lost to time caps before checkpoint-discipline countermeasures were added to the harness — but its final P6 compactness argument was original, load-bearing mathematics verified by independent reimplementation.
- **A clear capability tier break among the challengers.** Added later, the two newest models land far below the frontier tier on first pass — **Meta Muse Spark 1.1 at 26/42**, **DeepSeek V4 Pro at 19/42**, and **xAI Grok 4.5 at 13/42**. All solve the routine problems (P1; Muse also P4/P5, DeepSeek also P5) but none closes the geometry (P2), combinatorics capstone (P3), or number-theory finale (P6). Strikingly, **Muse and DeepSeek independently produced the *same wrong* P3 answer** (c=(n+1)/(2n+1), false for all n≥2, confirmed by exact minimax); DeepSeek additionally failed to even identify P4's answer (θ=180/n) that most models proved. Every "solved" claim any challenger made on a hard problem collapsed under verification — except DeepSeek's P5, which held up as a genuinely complete proof.
- **Grok 4.5 has a tool-adherence problem.** On P4 and P5 it repeatedly ended its turn narrating "📥 Writing final `current.md`…" while making **zero tool calls**, silently producing nothing in a bare agentic loop. It needed a harness guard (refuse "done" until the file actually exists) to emit gradeable output — a failure mode none of the other five models showed. Even then its written proofs were the weakest of the field. **DeepSeek V4 Pro showed the same tool-adherence tic** (the guard caught it inline) and was by far the slowest run — 8.9 h and 2.0M output tokens, the most compute of any run — yet landed at 19/42; its one bright spot was a fully verified P5. Notably it was also the *cheapest* run at ~$6.05, since DeepSeek's per-token price is a fraction of the others'.
- **Self-reports inflate.** Nearly every run claimed every attempted problem "solved"; graders confirmed only the scores above, with every deduction documented as a named, checkable defect. The three frontier runs agree on all four compute-and-prove answers; the challengers diverge — Muse and DeepSeek got P3's answer wrong (and DeepSeek P4's), which is a deeper failure than an unproven-but-correct claim.

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

- **The harness** (`harness/`): a deliberately minimal single-context agent loop — three tools (bash / write_file / read_file), no orchestration, no reviewer, network blocked, identical system prompt and time caps (150 min/problem) for every model. Problem statements were fed verbatim; models were instructed to solve from first principles and to verify claims numerically before committing them to the proof. **Reasoning settings**: Claude Fable 5 ran with its always-on adaptive thinking at the API's default effort (`high`; no `effort` parameter passed); Kimi K3 ran at its API default (no effort control exposed); GPT-5.6 Sol ran **four ways** in the identical harness — the base `gpt-5.6-sol` model at OpenRouter's default effort (`medium`), at `xhigh`, and at `max` (the highest OpenRouter accepts; the API's own enum orders them `max` > `xhigh` > `high` > `medium` > `low` > `minimal` > `none`), plus the higher `gpt-5.6-sol-pro` tier at `xhigh`; Meta Muse Spark 1.1 and xAI Grok 4.5 both ran at `xhigh`. Runs that died to infrastructure failures (API outages, billing) — or, for Grok, to ending a turn without writing its file — were resumed from their on-disk checkpoints; all prior rounds are preserved in each problem's `scratch/`. One further null session was treated the same way: GPT-5.6 Sol Pro's P6 first attempt ended after two turns with zero reasoning tokens and a 15-line stub (a degenerate bail, not a graded attempt — its P5 in the same run solved cleanly), so that session was archived to `scratch/` and P6 given one fresh retry, which produced the verified 7/7. No reviewer feedback or hints were given to any single-pass run.
- **Grading**: one verifier agent per problem, instructed to hunt for gaps, verify algebra symbolically, and machine-test doubtful claims; several defects were confirmed by explicit counterexample or exact minimax computation. Grader outputs are in `grades/` verbatim.

## Caveats

- Graders are Claude-based agents, not human medalists; treat scores as strong but not authoritative.
- All runs share the identical harness, so they are directly comparable. The four GPT-5.6 Sol runs isolate two clean controlled variables: reasoning effort on the base model (`medium` → `xhigh` → `max`) and model tier at fixed effort (base vs `-pro`, both at `xhigh`). These are single runs per setting, so treat mid-30s-vs-39 gaps as within the noise band of a stochastic agentic run, not a precise ranking — the robust signal is that neither knob reliably closed the two hardest problems (P2, P3).
- Claude Fable 5 cost is as metered by the Anthropic API. Kimi K3 cost is estimated from logged tokens at list pricing (cache split assumed at a 93% hit rate); all GPT-5.6 Sol runs (default / xhigh / max / Sol Pro), Meta Muse Spark 1.1, and xAI Grok 4.5 costs from OpenRouter list pricing (Sol and Sol Pro both $5/M prompt, $30/M completion) applied to total logged tokens.

## Provenance

All runs executed July 17–23, 2026 (the GPT-5.6 Sol Pro and GPT-5.6 Sol `max`-effort runs added July 22–23), driven by Claude Code (Claude Fable 5) as the orchestrating agent. Every model turn, tool call, and result is recorded verbatim in the corresponding `logs.jsonl`. Problem statements © IMO; sourced from [tempcollab/proval](https://github.com/tempcollab/proval).
