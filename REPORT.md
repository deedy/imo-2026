# Run report: time, tokens, and attempts per problem

All figures derived from the verbatim `logs.jsonl` audit trails in [`results/`](results/), including every failed and repair round. Reproduce with `harness/` + the `run_end` records.

Two time/cost columns appear throughout:

- **clean** — successful rounds only (what the work would have cost with no infrastructure failures)
- **total** — every round, including rounds killed by API outages, billing lapses, and network timeouts, plus repair rounds

## Totals per run

| Run | Final score | Clean time | Total time | Clean cost | Total cost | Output tokens |
|---|---|---|---|---|---|---|
| Claude Fable 5 | 42/42 | 1.8 h | 2.5 h | $38.83 | $51.05 | 705k |
| GPT-5.6 Sol (xhigh) | 42/42 | 1.6 h | 3.8 h | ~$9.74 | ~$20.54 | 236k |
| Kimi K3 | 42/42 | 6.5 h | 17.4 h | ~$14.49 | ~$31.40 | 1,545k |
| GPT-5.6 Sol (default) | 28/42 | 1.0 h | 1.0 h | ~$4.04 | ~$4.04 | 80k |

## Attempts per problem

An **attempt** is a substantive session on the problem — a fresh solve, a resumed solve, or a repair round. Rounds killed purely by infrastructure (billing outage, network drop) before doing new work are counted separately and are not the model's doing.

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Substantive | Infra-killed rounds |
|---|--|--|--|--|--|--|--|--|
| Claude Fable 5 | 1 | 1 | 1 | 1 | 1 | 1 | **6** | 3 (billing outage) |
| GPT-5.6 Sol (xhigh) | 1 | 2 | 1 | 1 | 1 | 1 | **7** | 4 (network) |
| Kimi K3 | 1 | 1 | 4 | 1 | 1 | 2 | **10** | 4 (network, billing) |
| GPT-5.6 Sol (default) | 1 | 1 | 1 | 1 | 1 | 1 | **6** | 0 |

**Claude Fable 5 solved every problem in a single attempt.** GPT-5.6 Sol (xhigh) needed a second attempt only on P2. Kimi K3 needed four on P3 (two hit the 150-minute cap with the answer known but proofs unwritten) and two on P6.

## Wall-clock minutes per problem (all rounds)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 5 | 27 | 73 | 8 | 10 | 26 | 150 |
| GPT-5.6 Sol (xhigh) | 7 | 106 | 27 | 10 | 20 | 60 | 231 |
| Kimi K3 | 20 | 85 | 491 | 40 | 28 | 381 | 1045 |
| GPT-5.6 Sol (default) | 5 | 15 | 15 | 5 | 6 | 14 | 60 |

## Completion (output) tokens per problem

Includes billed reasoning tokens where the provider bills them as output (Kimi K3, GPT-5.6 Sol).

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 16,826 | 141,363 | 331,025 | 39,027 | 55,114 | 121,922 | 705,277 |
| GPT-5.6 Sol (xhigh) | 8,488 | 113,253 | 43,259 | 20,623 | 14,497 | 36,052 | 236,172 |
| Kimi K3 | 27,657 | 171,310 | 846,626 | 70,540 | 47,550 | 381,100 | 1,544,783 |
| GPT-5.6 Sol (default) | 6,050 | 17,860 | 16,574 | 9,084 | 9,227 | 21,420 | 80,215 |

## Prompt tokens per problem

Dominated by cache reads — each turn resends the conversation, so these scale with turn count, not with unique content.

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 65k | 2,189k | 1,939k | 194k | 302k | 763k | 5,453k |
| GPT-5.6 Sol (xhigh) | 13k | 2,523k | 43k | 30k | 18k | 64k | 2,690k |
| Kimi K3 | 180k | 2,916k | 7,011k | 1,336k | 180k | 5,193k | 16,817k |
| GPT-5.6 Sol (default) | 15k | 157k | 79k | 20k | 12k | 45k | 326k |

## Cost per problem (USD, all rounds)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | $1.11 | $11.16 | $23.45 | $2.61 | $3.61 | $9.11 | $51.05 |
| GPT-5.6 Sol (xhigh) | $0.32 | $16.01 | $1.51 | $0.77 | $0.52 | $1.40 | $20.54 |
| Kimi K3 | $0.50 | $4.00 | $16.13 | $1.71 | $0.80 | $8.26 | $31.40 |
| GPT-5.6 Sol (default) | $0.25 | $1.32 | $0.89 | $0.37 | $0.33 | $0.87 | $4.04 |

## Round-by-round histories (problems needing more than one round)

| Run | Problem | Rounds, chronologically |
|---|---|---|
| Claude Fable 5 | P3 | 39m billing outage → 34m **completed** |
| Claude Fable 5 | P5 | 3m billing outage → 8m **completed** |
| Claude Fable 5 | P6 | 0m billing outage → 26m **completed** |
| GPT-5.6 Sol (xhigh) | P2 | 64m network → 7m **completed** (partial, 4/7) → 24m network (repair, checkpointed) → 11m **completed** (repair, 7/7) |
| GPT-5.6 Sol (xhigh) | P5 | 10m network → 9m **completed** |
| GPT-5.6 Sol (xhigh) | P6 | 38m network → 22m **completed** |
| Kimi K3 | P3 | 116m time cap → 117m time cap → 108m billing outage → 45m **completed** (5/7) → 92m network (repair) → 14m **completed** (repair, 7/7) |
| Kimi K3 | P6 | 131m network → 70m **completed** (3/7) → 92m network (repair) → 88m **completed** (repair, 7/7) |

## Observations

- **Problem difficulty is legible in the token counts.** P3 and P6 (the combinatorics capstone and the number-theory finale) consumed the overwhelming majority of every run's budget. P1, P4, and P5 were dispatched by every model in minutes.
- **Efficiency and correctness are not the same axis.** GPT-5.6 Sol at default effort was the cheapest run by 5× and the worst by 14 points; at `xhigh` it reached 42/42 for ~$20. Kimi K3 spent 6.5× the output tokens of Fable to reach the same final score.
- **P2 was GPT-5.6 Sol's expensive problem** ($16.01 of its $20.54, 106 of its 231 minutes) — the geometry crux it initially could not close. It is Claude Fable 5's second-cheapest hard problem, solved synthetically in 27 minutes.
- **Infrastructure noise was substantial and is fully disclosed**: 11 rounds across the experiment died to billing lapses, network drops, and read timeouts. All are preserved in `scratch/` and included in the "total" columns; none contributed mathematics.
