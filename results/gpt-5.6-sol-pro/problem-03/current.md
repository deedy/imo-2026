# imo-2026-03 — tracking file
## Status
partial

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- **Ordered-draft reduction (proved):** for fixed final lengths $x_1\ge\cdots\ge x_m$, largest-remaining-piece strategies give Liu the game value $x_1+x_3+\cdots=\frac12(1+D)$, where $D=x_1-x_2+x_3-\cdots$. A complete proof is in `lemmas/draft-value.md`.
- **Layer-cake/parity formulation (active):** $D=\int_0^\infty (N(t)\bmod2)\,dt$, where $N(t)$ is the number of pieces of length at least $t$.
- **Pairing/graph formulation (exploratory):** if all but one final pieces can be paired by equal length, then $D$ is the singleton length. Xiang's refinements can be represented as distributions of paired weights among Liu's initial intervals.
- **Integer-grid brute force (conjecture found):** dependency-free exhaustive searches for $n=2,3,4$ point to Liu's optimal initial lengths being proportional to $1,2,4,\ldots,2^n$. The grid output is stored under `scratch/grid_n*.txt`; grid effects make the computed excess slightly exceed the continuous limit.
- **Small case $n=1$ (proved):** the optimal initial lengths are $1/3,2/3$, and $c_1=2/3$.

## Current best
The conjectured explicit answer is
\[
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
Equivalently, the conjectured optimal guaranteed alternating excess is $D=1/(2^{n+1}-1)$. Liu should cut the stick into lengths $1,2,4,\ldots,2^n$, normalized by their sum $2^{n+1}-1$. The remaining open gap is a complete proof of the partition-refinement theorem: among all multisets of at most $n+1$ initial lengths totaling $1$, the maximum possible minimum alternating excess after at most $n$ splits is $1/(2^{n+1}-1)$.

## Full proof
The complete general proof is not yet available. The established reduction follows.

Let the final lengths be $x_1\ge\cdots\ge x_m$. If Liu always takes a largest remaining piece, then before his $j$th move at most $2j-2$ pieces have disappeared, so he receives at least $x_{2j-1}$. Conversely, if Xiang always takes a largest remaining piece, then on his $j$th move he receives at least $x_{2j}$, leaving Liu at most $\sum_jx_{2j-1}$. Hence the value of the claiming phase is
\[
F=x_1+x_3+\cdots=\frac{1+D}{2},\qquad D=x_1-x_2+x_3-x_4+\cdots.
\]
Writing $N(t)=\#\{i:x_i\ge t\}$ and integrating horizontal layers gives
\[
D=\int_0^\infty \bigl(N(t)\bmod2\bigr)\,dt.
\]
It remains to prove the stated extremal refinement theorem.

For $n=1$, let Liu's two initial pieces have lengths $a\ge b=1-a$. After Xiang cuts one piece, there are three pieces and Liu receives the largest plus the smallest, i.e. $1$ minus the middle piece. If $a\le2/3$, Xiang can cut the $a$-piece into lengths arbitrarily close to $a-b$ and $b$, so the middle length can approach $b$ and Liu's infimum payoff is $1-b=a$. If $a\ge2/3$, no cut can create two pieces both exceeding $a/2$, while cutting the $a$-piece nearly in half makes the middle length approach $a/2$; hence Liu's infimum payoff is $1-a/2$. Their maximum is $2/3$ at $a=2/3$.
