# Common-positive-increment lemma

## Statement
Under the hypotheses of the problem, if $f(u)-u>0$ and $f(v)-v>0$, then
\[
f(u)-u=f(v)-v.
\]

## Proof
By the forward-orbit lemma, write $a=f(u)-u>0$ and $b=f(v)-v>0$; then
\[
f(u+na)=u+(n+1)a,
\qquad f(v+mb)=v+(m+1)b
\]
for all integers $n,m\ge0$. Suppose $a>b$. Put
\[
p_n=u+na,
\qquad m_n=\left\lfloor\frac{p_n-v-b}{b}\right\rfloor,
\qquad q_n=v+(m_n+1)b.
\]
For large $n$, $m_n\ge0$, while $0\le p_n-q_n<b$ and $p_n,q_n\to\infty$. Apply the first inequality with $x=p_n$ and $y=v+m_nb$. It gives
\[
p_n+q_n+a-b\le\sqrt{2(p_n^2+q_n^2)}.
\]
Consequently
\[
0<a-b\le
\frac{(p_n-q_n)^2}{\sqrt{2(p_n^2+q_n^2)}+p_n+q_n}.
\]
The right side tends to $0$, a contradiction. Hence $a\le b$. Interchanging $u,v$ gives $b\le a$, and therefore $a=b$. $\square$
