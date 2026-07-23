# Lemma: forward-orbit structure

## Statement
Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfy the inequality in the problem, and define $d(t)=f(t)-t$. Then, for every $t>0$ and integer $n\ge0$,
\[
f^n(t)=t+n d(t),\qquad d(f^n(t))=d(t),
\]
and $d(t)\ge0$.

## Proof
Set $x=f(y)$ in the given chain. Its leftmost and rightmost terms are both $f(y)$, so its middle term also equals $f(y)$. Thus
\[
\frac{f(f(y))+y}{2}=f(y),
\]
which gives $f(f(y))=2f(y)-y$. Therefore
\[
d(f(y))=f(f(y))-f(y)=f(y)-y=d(y).
\]
Induction now gives both displayed orbit formulas. If $d(t)<0$, then $t+n d(t)\le0$ for some sufficiently large $n$, contradicting $f^n(t)>0$. Hence $d(t)\ge0$. $\square$
