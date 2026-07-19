# Lemma (chain theorem, Theorem 4.2)

**Statement.** Let $a_1,\dots,a_m$ be positive reals with sum $S$. Then there exist a nonempty sub-multiset $B\subseteq\{a_1,\dots,a_m\}$ **and an ordering $(e_1,\dots,e_r)$ of the elements of $B$** whose chain value (nested absolute difference, see `realizability.md`)
$$v(e_1,\dots,e_r)=\bigl|\dots\bigl||e_1-e_2\bigr|-e_3\bigr|-\dots-e_r\bigr|\quad\text{satisfies}\quad v(e_1,\dots,e_r)\le\frac{S}{2^m-1}.$$
(N.B. the achieving ordering need not be the sorted one; the statement is "some ordering", and the strategy in Part B processes exactly the ordering produced here.)

**Proof.** The $2^m$ subset sums $s(I)=\sum_{i\in I}a_i$ lie in $[0,S]$. Sort them as $0=t_0\le t_1\le\dots\le t_{2^m-1}=S$ (one entry per subset). The $2^m-1$ consecutive gaps sum to $\le S$, so some gap $g:=t_{j+1}-t_j\le\frac{S}{2^m-1}$, and **no subset sum lies strictly between $t_j$ and $t_{j+1}$**. Pick **distinct** subsets $A\ne B$ with $s(A)=t_{j+1}$, $s(B)=t_j$ (possible: the list has one entry per subset) and set $P=\{a_i:i\in A\setminus B\}$, $N=\{a_i:i\in B\setminus A\}$. Then $P\cup N\ne\emptyset$ and $\Sigma P-\Sigma N=g\ge0$.

- If $g=0$: realizability lemma (a) gives an ordering of $P\cup N$ with chain value $0$.
- If $g>0$: if some subset $J$ of $P\cup N$ had $\Sigma N<\Sigma J<\Sigma P$, then $J\cup(A\cap B)$ (disjoint union, since $J\subseteq A\triangle B$) would be a subset of $\{a_1,\dots,a_m\}$ with sum strictly between $s(B)$ and $s(A)$ — contradiction. So realizability lemma (b) applies and gives an ordering of $P\cup N$ with chain value $g\le\frac{S}{2^m-1}$. $\blacksquare$

**Sharpness.** For $a_i=2^{i-1}$ ($i=1..m$), subset sums are exactly $0,1,\dots,2^m-1$ (binary), so every adjacent gap is $1=\frac{S}{2^m-1}$. Moreover, for every nonempty subset $B$ and every ordering $(e_1,\dots,e_r)$ of $B$, the chain value is $\ge1$: inductively $v(e_1,\dots,e_r)=\bigl|\sum_i\delta_i e_i\bigr|$ for some signs $\delta_i\in\{\pm1\}$ (the step: $|X-e_r|=|\pm X-e_r|$), and a signed sum of distinct powers of $2$ is a nonzero integer (the largest power present exceeds the sum of all strictly smaller ones), hence has absolute value $\ge1$. So no chain beats $\frac{S}{2^m-1}$ for this family.

**Application (Part B of the IMO problem).** With $m=n+1$ pieces summing to $1$: Xiang Yu finds a subset $B$ and an ordering $(e_1,\dots,e_r)$ with $v(e_1,\dots,e_r)\le T_n=\frac{1}{2^{n+1}-1}$, realizes the chain **processing the elements in that order** with $\le|B|-1$ cancel-cuts (cut the larger of $\{v_{\text{run}},e_k\}$ into $\min$ and difference; equal pairs cancel in $D$; ties need no cut), and bisects the $n+1-|B|$ remaining pieces — at most $n$ cuts total, at distinct interior points markable simultaneously. The final multiset minus the last running piece splits into equal pairs, so $D=v\le T_n$ by parity cancellation. Hence LB's share $\le\frac{1+T_n}{2}=\frac{2^n}{2^{n+1}-1}$.

**Verification.** `code/partB.py` — min chain value $\le T_nS$ for 2000 random families, $n=1..4$; adversarial local search maximizes the ratio to exactly $T_n$ at the geometric family. `code/agr.py` — adjacent gaps realizable (0 failures).
