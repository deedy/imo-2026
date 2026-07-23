# Arithmetic-orbit lemma

## Statement
Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfy
\[
f(f(t))=2f(t)-t\qquad(t>0).
\]
Define $d(t)=f(t)-t$. Then $d(t)\ge0$ and
\[
f^n(t)=t+n d(t),\qquad d(f^n(t))=d(t)
\]
for every $t>0$ and integer $n\ge0$.

## Proof
The displayed functional relation gives
\[
d(f(t))=f(f(t))-f(t)=f(t)-t=d(t).
\]
Starting with $f^0(t)=t$, induction now gives
\[
f^{n+1}(t)=f^n(t)+d(f^n(t))=t+(n+1)d(t)
\]
and $d(f^n(t))=d(t)$ for all $n\ge0$.

If $d(t)<0$, choose an integer $n>t/(-d(t))$. Then $t+n d(t)<0$, whereas $f^n(t)$ must belong to $\mathbb R_{>0}$. This contradiction proves $d(t)\ge0$.
