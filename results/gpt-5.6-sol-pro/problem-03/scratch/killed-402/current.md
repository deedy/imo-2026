# imo-2026-03 — tracking file
## Status
partial

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- Reduced the final claiming phase to taking pieces in nonincreasing order: Liu Bang receives the odd-ranked lengths. Thus his share is $(1+D)/2$, where $D=y_1-y_2+y_3-\cdots$ for the sorted final lengths.
- Reformulated the marking phase as a minimax refinement problem: Liu chooses at most $n+1$ initial interval lengths, and Xiang subdivides them using at most $n$ cuts so as to minimize their sorted alternating sum $D$.
- The first guess (lengths proportional to $2,\ldots,2,1$) fails for $n=2$ because Xiang can split the short piece in half and make $D=0$.
- Enumerated all final piece-order types and solved the corresponding linear programs numerically for $n=1,2$. The optima are respectively initial lengths proportional to $(2,1)$ and $(4,2,1)$, with guaranteed alternating sums $1/3$ and $1/7$. This strongly suggests the general geometric construction $(2^n,2^{n-1},\ldots,1)/(2^{n+1}-1)$ and answer $c=2^n/(2^{n+1}-1)$.
- In the geometric construction, Xiang can split each of the first $n$ intervals into two equal halves, producing two copies of every size $2^{n-1},\ldots,1$ plus the original final $1$; the alternating sum is exactly $1/(2^{n+1}-1)$. This shows the candidate lower-bound construction would be sharp against that particular response, but the key gap is to prove no other response can lower the alternating sum further.

## Current best
The conjectured explicit answer is
\[
 c=\frac{2^n}{2^{n+1}-1}.
\]
Equivalently, the conjectured optimal guaranteed sorted alternating sum is $1/(2^{n+1}-1)$. Liu's candidate strategy is to mark the stick into consecutive intervals whose lengths are $2^n,2^{n-1},\ldots,1$, normalized by their sum. Computation confirms the minimax claim for $n=1,2$. Two proof obligations remain: prove every refinement of this geometric partition by at most $n$ cuts has alternating sum at least the smallest original length, and prove that for every initial partition into at most $n+1$ intervals Xiang has a refinement by at most $n$ cuts whose alternating sum is at most $1/(2^{n+1}-1)$.

## Full proof
A complete proof has not yet been obtained. The following reduction is established.

Let the final piece lengths in nonincreasing order be $y_1\ge\cdots\ge y_m$. In the claiming phase, choosing a currently longest piece is optimal: if all later play is fixed, taking a shorter piece while a longer one remains can only decrease the mover's final total; equivalently, backward induction on the number of pieces gives the standard alternating greedy allocation. Hence Liu receives $y_1+y_3+\cdots$, while Xiang receives $y_2+y_4+\cdots$. Since their sum is $1$, Liu's total is
\[
 \frac{1+D(y)}2,\qquad D(y):=y_1-y_2+y_3-y_4+\cdots.
\]
Thus it remains to determine the maximum, over initial partitions obtainable with at most $n$ marks, of the minimum $D$ over refinements using at most $n$ further cuts.
