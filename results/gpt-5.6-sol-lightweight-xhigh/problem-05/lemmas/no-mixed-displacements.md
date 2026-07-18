# No-mixed-displacements lemma

## Statement
Suppose a function satisfying the problem has a constant $c>0$ such that
\[
f(t)-t\in\{0,c\}\qquad(t>0).
\]
If the value $c$ occurs, then $f(t)-t=c$ for every $t>0$.

## Proof
Let
\[
A=\{t>0:f(t)=t\},\qquad B=\{t>0:f(t)=t+c\}.
\]
If a point of $A$ were approached by points $r_k\in B$, put that point equal to $s_k$ for every $k$. If a point of $B$ were approached by points $s_k\in A$, keep that point as $r_k$ for every $k$. In either case we would have $r_k\in B$, $s_k\in A$, and $r_k,s_k\to L>0$.

The first given inequality at $(x,y)=(r_k,s_k)$ implies
\[
r_k+s_k+c=f(r_k)+s_k\le\sqrt{2(r_k^2+s_k^2)}.
\]
Letting $k\to\infty$ gives $2L+c\le2L$, impossible. Thus both $A$ and $B$ are open relative to $\mathbb R_{>0}$. They are disjoint and cover the connected interval $\mathbb R_{>0}$, so one is empty. Since $c$ occurs, $B\ne\varnothing$, whence $A=\varnothing$. $\square$
