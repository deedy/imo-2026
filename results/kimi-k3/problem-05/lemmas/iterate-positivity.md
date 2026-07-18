# Lemma: iterates are arithmetic and $f(t)\ge t$

## Statement
Assume $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfies
\[
f(f(t))=2f(t)-t\qquad(t>0). \tag{2}
\]
Define $f^{[0]}(t)=t$ and $f^{[n+1]}(t)=f(f^{[n]}(t))$, and put $p(t)=f(t)-t$. Then for every $t>0$ and every integer $n\ge0$,
\[
f^{[n]}(t)=t+n p(t). \tag{3}
\]
In particular $p(t)\ge0$ for all $t>0$, and $p(f^{[n]}(t))=p(t)$.

## Proof
Fix $t$ and set $a_n=f^{[n]}(t)$. By (2) applied to $a_n$,
\[
a_{n+2}=f(f(a_n))=2f(a_n)-a_n=2a_{n+1}-a_n.
\]
Since $a_0=t$ and $a_1=t+p(t)$, induction on $n$ proves $a_n=t+n p(t)$ for all $n\ge0$.

Because $f$ maps into $\mathbb R_{>0}$, every $a_n$ is positive. If $p(t)<0$, then $t+n p(t)$ is negative for all sufficiently large $n$, contradicting (3). Hence $p(t)\ge0$. Finally, from (3),
\[
p(f^{[n]}(t))=f(f^{[n]}(t))-f^{[n]}(t)=f^{[n+1]}(t)-f^{[n]}(t)=p(t).
\]
