# Run report: time, tokens, and attempts per problem

All figures derived from the verbatim `logs.jsonl` audit trails in [`results/`](results/), including every failed and repair round. Reproduce with `harness/` + the `run_end` records.

Two time/cost columns appear throughout:

- **clean** — productive rounds only (rounds that actually wrote to the proof file); what the work would have cost with no infrastructure failures
- **total** — every round, including rounds killed by API outages, billing lapses, and network timeouts; repair rounds; and (for Grok) rounds that ended without writing anything

## Totals per run

| Run | Final score | Clean time | Total time | Clean cost | Total cost | Output tokens |
|---|---|---|---|---|---|---|
| Claude Fable 5 | 42/42 | 1.8 h | 2.5 h | $38.83 | $51.05 | 705k |
| GPT-5.6 Sol (xhigh) | 42/42 | 1.6 h | 3.8 h | ~$9.74 | ~$20.54 | 236k |
| Kimi K3 | 42/42 | 6.5 h | 17.4 h | ~$14.49 | ~$31.40 | 1,545k |
| GPT-5.6 Sol Pro (xhigh) | 37/42 | 2.1 h | 3.3 h | ~$42.32 | ~$46.44 | 621k |
| GPT-5.6 Sol (max) | 30/42 | 2.1 h | 2.1 h | ~$22.30 | ~$23.42 | 204k |
| Meta Muse Spark 1.1 | 26/42 | 2.3 h | 2.3 h | ~$4.45 | ~$4.45 | 761k |
| DeepSeek V4 Pro | 19/42 | 8.9 h | 8.9 h | ~$6.05 | ~$6.05 | 2,013k |
| GPT-5.6 Sol (default) | 28/42 | 1.0 h | 1.0 h | ~$4.04 | ~$4.04 | 80k |
| xAI Grok 4.5 | 13/42 | 2.6 h | 3.2 h | ~$14.26 | ~$14.60 | 606k |

## Rounds per problem

Each cell is **rounds / productive rounds** — total sessions on the problem, and how many of those actually wrote to the proof file. The gap is infrastructure failures (billing, network), plus — for Grok and DeepSeek — sessions that ended narrating "writing the file" without ever calling the write-tool.

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 1/1 | 1/1 | 2/1 | 1/1 | 2/1 | 2/1 | **9/6** |
| GPT-5.6 Sol (xhigh) | 1/1 | 4/4 | 1/1 | 1/1 | 2/1 | 2/2 | **11/10** |
| Kimi K3 | 1/1 | 1/1 | 6/5 | 1/1 | 1/1 | 4/4 | **14/13** |
| GPT-5.6 Sol Pro (xhigh) | 1/1 | 4/1 | 2/1 | 1/1 | 2/1 | 3/1 | **13/6** |
| GPT-5.6 Sol (max) | 1/1 | 2/1 | 1/1 | 2/1 | 2/1 | 2/1 | **10/6** |
| Meta Muse Spark 1.1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | **6/6** |
| DeepSeek V4 Pro | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | **6/6** |
| GPT-5.6 Sol (default) | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | 1/1 | **6/6** |
| xAI Grok 4.5 | 1/1 | 1/1 | 1/1 | 2/1 | 3/1 | 1/1 | **9/6** |

Reading the interesting rows:

- **Claude Fable 5**, **Muse Spark 1.1**, and **GPT-5.6 Sol (default)** each did exactly one productive round per problem — clean single-pass runs (Fable's three extra rounds were 0–3 min billing-outage deaths that wrote nothing).
- **GPT-5.6 Sol (xhigh)** P2 took four rounds (two network-killed, plus the initial partial and its repair); **P6 took two rounds — both productive** (a 38-min first pass interrupted by a network drop, then a checkpointed continuation that finished it).
- **Kimi K3** P3 took six rounds (two hit the 150-min cap with the answer known but proofs unwritten, one died to a billing outage, one solved to 5/7, then a network-killed repair and the repair that reached 7/7); P6 took four.
- **DeepSeek V4 Pro** stayed 1 round / 1 productive per problem, but its logs show the no-write guard firing *within* rounds — like Grok, it repeatedly tried to end turns claiming to write files without a tool call; the guard forced the write inline, so no extra rounds were spawned. It is also the slowest run in the table (534 min = 8.9 h) and spent the most output tokens (2.0M), yet at the lowest cost ($6.05), since DeepSeek's per-token price is a fraction of the others'.
- **xAI Grok 4.5** P4 and P5 show the tool-adherence failure: 2 rounds / 1 productive and 3 rounds / 1 productive. The non-productive rounds each ended with Grok claiming to write `current.md` while making zero tool calls. A harness guard (refuse "done" until the file exists) was added to force a real write.
- **GPT-5.6 Sol Pro (xhigh)** P2 shows 4 rounds / 1 productive — the widest gap in the table, but none of the extra rounds were the model's doing: its first (productive) P2 session was accidentally killed by the orchestrator at turn 50 of 80 while still working, and two follow-up attempts died to OpenRouter credit exhaustion, before a clean full re-run produced the verified 7/7, 215-line proof. That single productive round is the most expensive cell in the whole benchmark — a 50-turn, 4.56M-prompt, 253k-completion geometry proof (~$30 of the run's cost). P6 shows 3/1 for a similar reason plus its degenerate-null first session (2 turns, zero reasoning tokens, a 15-line stub); one fair retry solved it 7/7. The clean-vs-total gap for this run (2.1 h / $42.32 vs 3.3 h / $46.44) is almost entirely those interrupted P2/P6 sessions.
- **GPT-5.6 Sol (max)** ran a clean 1 productive round per problem. Its P3 is the fastest cell in the whole table — 1.2 min, 982 completion tokens: the base model at *max* effort simply gave up on the combinatorics capstone after one look, writing only the standard endgame reduction (graded 1/7). Its P2, by contrast, is the second-costliest geometry cell (54 min, 3.3M prompt) — the price of the 7/7 proof it *did* close, over the full 80-turn budget.

## Wall-clock minutes per problem (all rounds)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 5 | 27 | 73 | 8 | 10 | 26 | 150 |
| GPT-5.6 Sol (xhigh) | 7 | 106 | 27 | 10 | 20 | 60 | 231 |
| Kimi K3 | 20 | 85 | 491 | 40 | 28 | 381 | 1045 |
| GPT-5.6 Sol Pro (xhigh) | 7 | 74 | 51 | 17 | 17 | 35 | 199 |
| GPT-5.6 Sol (max) | 6 | 54 | 1 | 27 | 16 | 23 | 127 |
| Meta Muse Spark 1.1 | 2 | 41 | 51 | 10 | 5 | 31 | 140 |
| DeepSeek V4 Pro | 17 | 82 | 103 | 61 | 107 | 164 | 534 |
| GPT-5.6 Sol (default) | 5 | 15 | 15 | 5 | 6 | 14 | 60 |
| xAI Grok 4.5 | 8 | 37 | 77 | 21 | 48 | 4 | 195 |

## Completion (output) tokens per problem

Includes billed reasoning tokens where the provider bills them as output.

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 16,826 | 141,363 | 331,025 | 39,027 | 55,114 | 121,922 | 705,277 |
| GPT-5.6 Sol (xhigh) | 8,488 | 113,253 | 43,259 | 20,623 | 14,497 | 36,052 | 236,172 |
| Kimi K3 | 27,657 | 171,310 | 846,626 | 70,540 | 47,550 | 381,100 | 1,544,783 |
| GPT-5.6 Sol Pro (xhigh) | 37,709 | 320,804 | 81,729 | 39,738 | 37,669 | 102,903 | 620,552 |
| GPT-5.6 Sol (max) | 16,911 | 111,653 | 982 | 38,450 | 17,154 | 19,104 | 204,254 |
| Meta Muse Spark 1.1 | 17,047 | 183,399 | 224,090 | 85,835 | 46,114 | 204,340 | 760,825 |
| DeepSeek V4 Pro | 66,946 | 295,827 | 326,465 | 174,111 | 510,163 | 639,183 | 2,012,695 |
| GPT-5.6 Sol (default) | 6,050 | 17,860 | 16,574 | 9,084 | 9,227 | 21,420 | 80,215 |
| xAI Grok 4.5 | 30,212 | 127,445 | 273,455 | 72,444 | 95,009 | 7,053 | 605,618 |

## Prompt tokens per problem

Dominated by cache reads — each turn resends the conversation, so these scale with turn count, not unique content. (Grok's P2/P3 are huge because it churned the full 80-turn budget on both.)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | 65k | 2,189k | 1,939k | 194k | 302k | 763k | 5,453k |
| GPT-5.6 Sol (xhigh) | 13k | 2,523k | 43k | 30k | 18k | 64k | 2,690k |
| Kimi K3 | 180k | 2,916k | 7,011k | 1,336k | 180k | 5,193k | 16,817k |
| GPT-5.6 Sol Pro (xhigh) | 94k | 4,751k | 265k | 57k | 111k | 286k | 5,565k |
| GPT-5.6 Sol (max) | 17k | 3,321k | 1k | 50k | 56k | 15k | 3,459k |
| Meta Muse Spark 1.1 | 32k | 125k | 456k | 32k | 19k | 312k | 976k |
| DeepSeek V4 Pro | 199k | 3,781k | 1,447k | 149k | 1,834k | 2,470k | 9,880k |
| GPT-5.6 Sol (default) | 15k | 157k | 79k | 20k | 12k | 45k | 326k |
| xAI Grok 4.5 | 60k | 3,024k | 2,207k | 55k | 68k | 70k | 5,485k |

## Cost per problem (USD, all rounds)

| Run | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|--|--|--|--|--|--|--|
| Claude Fable 5 | $1.11 | $11.16 | $23.45 | $2.61 | $3.61 | $9.11 | $51.05 |
| GPT-5.6 Sol (xhigh) | $0.32 | $16.01 | $1.51 | $0.77 | $0.52 | $1.40 | $20.54 |
| Kimi K3 | $0.50 | $4.00 | $16.13 | $1.71 | $0.80 | $8.26 | $31.40 |
| GPT-5.6 Sol Pro (xhigh) | $1.60 | $33.38 | $3.78 | $1.48 | $1.69 | $4.52 | $46.44 |
| GPT-5.6 Sol (max) | $0.59 | $19.96 | $0.03 | $1.40 | $0.79 | $0.65 | $23.42 |
| Meta Muse Spark 1.1 | $0.11 | $0.94 | $1.52 | $0.40 | $0.22 | $1.26 | $4.45 |
| DeepSeek V4 Pro | $0.14 | $1.90 | $0.91 | $0.22 | $1.24 | $1.63 | $6.05 |
| GPT-5.6 Sol (default) | $0.25 | $1.32 | $0.89 | $0.37 | $0.33 | $0.87 | $4.04 |
| xAI Grok 4.5 | $0.30 | $6.81 | $6.05 | $0.55 | $0.71 | $0.18 | $14.60 |

## Observations

- **Problem difficulty is legible in the token counts.** P3 (combinatorics capstone) and P6 (number-theory finale) consumed the majority of every run's budget. P1, P4, and P5 were dispatched in minutes.
- **Effort spent ≠ correctness.** The challenger models poured heavy reasoning into the hard problems and still couldn't close them: Grok spent $6.81 and 3M prompt tokens on P2 (scored 2/7); DeepSeek spent 82 min and 3.8M prompt tokens on P2 (also 2/7) and 639k output tokens on P6 (1/7); Muse *and DeepSeek* both spent heavily on P3 and got the answer *wrong* — the same wrong answer. Meanwhile GPT-5.6 Sol at default effort spent the least of anyone and matched the challengers' ballpark.
- **Grok's P6 is the cheapest hard-problem cell in the table** ($0.18, 7k output tokens) — not because it was easy for Grok, but because it gave up early with an explicit non-proof ("Full proof: (Not yet complete.)").
- **Infrastructure and tool-adherence noise is fully disclosed.** Across the experiment, rounds died to billing lapses, network drops, and read timeouts; Grok additionally lost three rounds to ending without writing. All are preserved in `scratch/` and included in the "total" columns; none contributed mathematics.
