# Asymptotic comparison of arithmetic orbits

## Idea
After the orbit identity is known, compare two positive arithmetic-progression orbits very far out. Select one term from each orbit so that their values differ by a bounded amount. The RMS--AM gap between these values tends to zero, while the functional inequality says that this gap is at least the difference of the two orbit increments.

## Status
Successful; proves that all positive displacements $f(t)-t$ are the same.

## Details
Suppose $d(u)=a>0$ and $d(v)=b>0$, with $a>b$. Let
\[
p_n=u+na,
\qquad m_n=\left\lfloor\frac{p_n-v-b}{b}\right\rfloor,
\qquad q_n=v+(m_n+1)b.
\]
For large $n$, $m_n\ge0$, and $0\le p_n-q_n<b$. Along the two orbits,
\[
f(p_n)=p_n+a,
\qquad f(v+m_nb)=q_n.
\]
Using the first functional inequality at $(x,y)=(p_n,v+m_nb)$ yields
\[
p_n+q_n+a-b\le \sqrt{2(p_n^2+q_n^2)}.
\]
Hence
\[
0<a-b\le
\frac{(p_n-q_n)^2}{\sqrt{2(p_n^2+q_n^2)}+p_n+q_n}.
\]
The numerator is bounded by $b^2$, while the denominator tends to infinity. This contradiction excludes $a>b$; symmetry excludes $b>a$.
