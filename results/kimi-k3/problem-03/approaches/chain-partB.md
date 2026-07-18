# Approach: Part B (upper bound) via the chain theorem

**Idea.** XY views LB's pieces as a pool and uses two moves (1 cut each): bisect $x$ (the halves $x/2,x/2$ cancel in $D$ by parity — net effect: delete $x$) and cancel $x>y$ (cut $x$ into $y$ and $x-y$; the new $y$ cancels the old — net effect: delete $x,y$, add $x-y$). Iterated cancels along a decreasing sequence $b_1\ge\dots\ge b_r$ compute the nested absolute difference (chain value) $v(B)$ and consume $B$ at $\le r-1$ cuts; bisecting the other $n+1-r$ pieces costs $n+1-r$ cuts, total $\le n$, leaving $D=v(B)$. So XY forces $D\le T_n$ iff every composition of $1$ into $n+1$ parts has a nonempty subset with chain value $\le T_n$.

**Status: complete, proved (Lemma 4.1 + Theorem 4.2 in `current.md`; lemma files `lemmas/realizability.md`, `lemmas/chain-theorem.md`).**

**Key steps.**
1. Pigeonhole: $2^{n+1}$ subset sums in $[0,1]$ give an adjacent gap $g\le\frac{1}{2^{n+1}-1}=T_n$ with no subset sum strictly inside.
2. Realizability lemma: an adjacent gap $g=\Sigma P-\Sigma N$ is always the chain value of *some* ordering of $P\cup N$ — greedy scheduling (positive running sum ⟵ draw from $N$, negative ⟵ draw from $P$) can never get stuck: a stuck state either produces a subset sum strictly inside the gap (contradicting adjacency) or forces the total to have the wrong sign. Equal-sum case ($g=0$): same greedy, no hypothesis needed.
3. The chain strategy's cuts are at distinct interior points of LB's original pieces, so XY can mark them simultaneously.

**Why the naive route fails.** The pigeonhole gives a *signed* sum $|\sum\delta_i a_i|\le T_n$ ($\delta\in\{-1,0,1\}$), but the minimum signed sum is not always a chain value (`code/signed.py`: differs in 4/300 families at $n=4$). The fix is to realize only *adjacent* gaps, which are always chain-realizable.

**Verification.** `code/partB.py` (2000 random families, $n=1..4$; adversarial search maximizes min-chain$/S$ to exactly $T_n$ at the geometric family); `code/agr.py` (all adjacent gaps realizable, 180 families).
