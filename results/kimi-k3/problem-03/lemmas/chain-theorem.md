# Lemma (chain theorem, Theorem 4.2)

**Statement.** Let $a_1,\dots,a_m$ be positive reals with sum $S$. Then some nonempty sub-multiset $B\subseteq\{a_1,\dots,a_m\}$ has chain value (nested absolute difference, see `realizability.md`)
$$v(B)\le\frac{S}{2^m-1}.$$
The bound is sharp: for $a_i=2^{i-1}$ the minimum chain value is exactly $1=\frac{S}{2^m-1}$.

**Proof.** The $2^m$ subset sums $s(I)=\sum_{i\in I}a_i$ lie in $[0,S]$. Sort them as $0=t_0\le t_1\le\dots\le t_{2^m-1}=S$ (one entry per subset). The $2^m-1$ consecutive gaps sum to $\le S$, so some gap $g:=t_{j+1}-t_j\le\frac{S}{2^m-1}$, and **no subset sum lies strictly between $t_j$ and $t_{j+1}$**. Pick $A,B\subseteq\{1,\dots,m\}$ with $s(A)=t_{j+1}$, $s(B)=t_j$ and set $P=\{a_i:i\in A\setminus B\}$, $N=\{a_i:i\in B\setminus A\}$. Then $P\cup N\ne\emptyset$ and $\Sigma P-\Sigma N=g\ge0$.

- If $g=0$: realizability lemma (a) gives an ordering of $P\cup N$ with chain value $0$.
- If $g>0$: if some subset $J$ of $P\cup N$ had $\Sigma N<\Sigma J<\Sigma P$, then $J\cup(A\cap B)$ (disjoint union, since $J\subseteq A\triangle B$) would be a subset of $\{a_1,\dots,a_m\}$ with sum strictly between $s(B)$ and $s(A)$ — contradiction. So realizability lemma (b) applies and gives an ordering of $P\cup N$ with chain value $g\le\frac{S}{2^m-1}$. $\blacksquare$

**Sharpness.** For $a_i=2^{i-1}$ ($i=1..m$), subset sums are exactly $0,1,\dots,2^m-1$ (binary), so every adjacent gap is $1=\frac{S}{2^m-1}$; and every nonempty chain value has the form $\bigl|\sum_{i\in B}\delta_i2^{i-1}\bigr|$ ($\delta_i\in\{\pm1\}$), which is a nonzero integer (the largest index of $B$ dominates: $2^{k-1}>\sum_{i<k}2^{i-1}$), hence $\ge1$.

**Application (Part B of the IMO problem).** With $m=n+1$ pieces summing to $1$: Xiang Yu finds $B$ with $v(B)\le T_n=\frac{1}{2^{n+1}-1}$, realizes the chain with $\le|B|-1$ cancel-cuts (cut the larger of $\{v_{\text{run}},b_k\}$ into $\min$ and difference; equal pairs cancel in $D$; ties need no cut), and bisects the $n+1-|B|$ remaining pieces — at most $n$ cuts total, at distinct interior points markable simultaneously. The final multiset has even multiplicities except possibly the single running piece of size $v(B)$, so $D=v(B)\le T_n$ by parity cancellation. Hence LB's share $\le\frac{1+T_n}{2}=\frac{2^n}{2^{n+1}-1}$.

**Verification.** `code/partB.py` — min chain value $\le T_nS$ for 2000 random families, $n=1..4$; adversarial local search maximizes the ratio to exactly $T_n$ at the geometric family. `code/agr.py` — adjacent gaps realizable (0 failures).
