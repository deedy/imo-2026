# Lemma: termination potential

**Statement.** Consider any finite board containing at least one integer greater than $1$. Under the move
\[
(m,n)\longmapsto\left(\gcd(m,n),\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
\]
applied only to two entries greater than $1$, every sequence of moves is finite. Its terminal state has exactly one entry greater than $1$.

**Proof.** Let $P$ be the product of all board entries and $K$ the number of entries greater than $1$. Put $g=\gcd(m,n)$ for a selected pair. Since $mn=g\operatorname{lcm}(m,n)$, after the move the total product is $P/g$. Also $K$ cannot increase, because two entries greater than $1$ are replaced by only two entries.

If $g>1$, then $P$ strictly decreases and $K$ does not increase. If $g=1$, the outputs are $1$ and $mn$, so $P$ is unchanged and $K$ decreases by one. Hence the positive integer $P+K$ strictly decreases in every move. An infinite sequence of moves is therefore impossible.

A move is possible precisely when $K\ge 2$. Moreover, a move never makes $K=0$: if $g>1$, its first output is $g>1$, while if $g=1$, its second output is $mn>1$. Starting from $K\ge1$, the terminal state consequently has $K=1$. $\square$
