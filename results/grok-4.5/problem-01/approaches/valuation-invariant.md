# Approach: p-adic valuation gcd invariant + potential for termination

## Idea
- Termination / part (a): let $k$ be the number of board entries strictly greater than 1. A move changes $k$ by $0$ or $-1$. When the change is $0$, both replacement numbers exceed 1, forcing $\gcd>1$, so the product $P$ of all board entries is strictly divided by an integer $\ge 2$. Lexicographic potential $(k,P)$ALES descends, and $k$ cannot reach 0.
- Invariance / part (b): for each prime $p$ the quantity $g_p=\gcd$ of the $2026$ values $v_p$ of the board entries is unchanged by any move (because a move replaces a pair of exponents $(\alpha,\beta)$ by $(\min(\alpha,\beta),|\alpha-\beta|)$, which preserves pairwise gcd). At termination the board is $\{M,1,1,\dots,1\}$, so $g_p=v_p(M)$. Hence $M=\prod_p p^{g_p}$ is path-independent.

## Status
Complete and verified on many random simulations.

## Details
See the lemmas and the full proof in `current.md`.
