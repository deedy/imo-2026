# Approach: binary power-of-two intervals

## Idea
Liu Bang marks n points so the n+1 intervals have lengths proportional to 1,2,4,...,2^n (i.e., normalized by S=2^{n+1}-1). Conjecture: this forces V ≥ 2^n / S, and this is optimal.

c_n = 2^n / (2^{n+1}-1)

Matches n=1: 2/3; n=2: 4/7; n=3: 8/15; limit 1/2.

## Status
Lower bound for n=1 trivial/hand; n=2 fully proved by exhaustive case analysis on cut distribution (see lemmas). Upper bound (optimality) and general n lower bound in progress via induction.

## Details
Rescale to integer total length S_n = 2^{n+1}-1, bins of sizes 2^0,...,2^n. Prove any refinement using at most n extra cuts has alternating sum V ≥ 2^n.
