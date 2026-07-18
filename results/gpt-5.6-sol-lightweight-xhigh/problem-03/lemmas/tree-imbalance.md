# Lemma: a sparse matching leaves a power-of-two imbalance

## Statement
Let a multigraph (loops allowed) have vertices $0,1,\ldots,n$ and at most $n$ edges. Give every edge a nonnegative weight, counting the weight of a loop twice in the weighted degree. Suppose nonnegative residuals $r_i$ satisfy
\[
2^i d=\deg_w(i)+r_i\qquad(0\le i\le n)
\]
for some $d>0$. Then
\[
\sum_{i=0}^n r_i\ge d.
\]

## Proof
Let the connected components have $(v_j,e_j)$ vertices and edges. Every connected component satisfies $e_j\ge v_j-1$. Since the whole graph has $n+1$ vertices and at most $n$ edges, at least one component satisfies $e_j=v_j-1$. Such a component contains neither a loop nor a cycle, so it is a tree; an isolated vertex is permitted.

Let $P\sqcup Q$ be the bipartition of this tree. Each edge has one endpoint in each part, so
\[
\sum_{i\in P}\deg_w(i)=\sum_{i\in Q}\deg_w(i).
\]
It follows that
\[
d\left(\sum_{i\in P}2^i-\sum_{i\in Q}2^i\right)
=
\sum_{i\in P}r_i-\sum_{i\in Q}r_i.
\]
The integer in parentheses is nonzero. Indeed, $P$ and $Q$ are disjoint, and in any nonempty signed sum of distinct powers of two the largest power is greater than the sum of all smaller powers. Its absolute value is therefore at least $1$. Consequently,
\[
d\le \left|\sum_{i\in P}r_i-\sum_{i\in Q}r_i\right|
\le\sum_{i\in P\cup Q}r_i
\le\sum_{i=0}^n r_i.
\]
This proves the lemma. ∎
