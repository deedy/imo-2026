# Quadratic rigidity lemma

## Statement

Let \(f:\mathbb R_{>0}\to\mathbb R_{>0}\), and put \(g(t)=f(t)-t\). Suppose

1. \(g(f(t))=g(t)\) for every \(t>0\); and
2. for every \(u,v>0\),
   \[
   |g(u)-g(v)|\le \bigl(\sqrt{f(u)}-\sqrt{f(v)}\bigr)^2.
   \]

Then \(g\) is constant, provided all forward iterates of \(f\) are positive.

## Proof

The first assumption gives inductively
\[
f^n(t)=t+ng(t)\qquad(n\ge0).
\]
As all these numbers are positive, \(g(t)\ge0\).

We first show that \(f\) is strictly increasing. Take \(u>v\), put \(h=u-v>0\), \(d=g(u)-g(v)\), and \(\Delta=f(u)-f(v)=h+d\). If \(\Delta=0\), the displayed estimate gives \(d=0\), contradicting \(h>0\). If \(\Delta<0\), then \(d<-h\), while
\[
|d|\le(\sqrt{f(u)}-\sqrt{f(v)})^2
=|\Delta|\frac{|\sqrt{f(u)}-\sqrt{f(v)}|}{\sqrt{f(u)}+\sqrt{f(v)}}<|\Delta|.
\]
But \(|\Delta|=|d|-h<|d|\), a contradiction. Hence \(\Delta>0\).

Every iterate \(f^n\) is therefore strictly increasing. For \(u>v\),
\[
u+ng(u)>v+ng(v)
\]
for every positive integer \(n\). Letting \(n\to\infty\) gives \(g(u)\ge g(v)\), so \(g\) is nondecreasing.

We next prove continuity. Fix \(t>0\). The right limit \(L=\lim_{s\downarrow t}g(s)\) exists and is finite by monotonicity. Passing to the limit in the quadratic estimate for \(s,t\) gives, with \(J=L-g(t)\ge0\) and \(X=f(t)>0\),
\[
J\le(\sqrt{X+J}-\sqrt X)^2.
\]
If \(J>0\), the right side is strictly smaller than \(J\), a contradiction. Thus \(J=0\). The same argument at the left limit, now with \(J=g(t)-\lim_{s\uparrow t}g(s)\), proves left continuity.

Finally fix \(0<a<b\), and partition \([a,b]\) into \(N\) equal subintervals with endpoints \(x_0,\ldots,x_N\). Put
\[
d_i=g(x_i)-g(x_{i-1})\ge0,\qquad \Delta_i=f(x_i)-f(x_{i-1})>0.
\]
The quadratic estimate gives
\[
d_i\le \frac{\Delta_i^2}{(\sqrt{f(x_i)}+\sqrt{f(x_{i-1})})^2}
\le \frac{\Delta_i^2}{4f(a)}.
\]
Consequently
\[
0\le g(b)-g(a)\le
\frac{\max_i\Delta_i}{4f(a)}\sum_i\Delta_i
=rac{\max_i\Delta_i}{4f(a)}(f(b)-f(a)).
\]
Since the continuous function \(f\) is uniformly continuous on \([a,b]\), \(\max_i\Delta_i\to0\) as \(N\to\infty\). Hence \(g(b)=g(a)\). Since \(a,b\) were arbitrary, \(g\) is constant. \(\square\)
