# Termination by a decreasing potential

## Idea
Track both the product of all entries and the number of nonunit entries. A move with nontrivial gcd lowers the product; a move with gcd $1$ leaves the product unchanged but combines two nonunits into one.

## Status
Successful.

## Details
Let the current entries be $x_1,\dots,x_N$, and put
\[
P=\prod_{i=1}^N x_i,\qquad r=\#\{i:x_i>1\}.
\]
If a selected pair is $(m,n)$ and $d=\gcd(m,n)$, then the product of the new pair is
\[
d\cdot \frac{\operatorname{lcm}(m,n)}d
=\operatorname{lcm}(m,n)=\frac{mn}{d}.
\]
Thus the new total product is $P'=P/d$.

One can use the lexicographic pair $(P,r)$: if $d>1$, then $P'<P$; if $d=1$, then the replacement is $(1,mn)$, so $P'=P$ and $r'=r-1$.

For an even cleaner one-variable potential, define
\[
\Phi=P2^r.
\]
If $d=1$, then $\Phi'=\Phi/2$. If $d>1$, the new pair has at most two nonunits, so $r'\le r$, and
\[
\Phi'=\frac Pd2^{r'}\le \frac1d P2^r<\Phi.
\]
Hence every move strictly decreases the positive integer $\Phi$, proving termination.

At every move, the product of the two replacement entries is $\operatorname{lcm}(m,n)>1$, so at least one of them is a nonunit. Therefore the board never loses all of its nonunits. A terminal board has fewer than two nonunits, and consequently has exactly one.
