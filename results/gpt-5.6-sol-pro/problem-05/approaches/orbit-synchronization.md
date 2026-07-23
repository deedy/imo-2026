# Synchronizing positive-displacement orbits

## Idea
The orbit relation alone permits many arithmetic progressions with different steps. Compare two such progressions at points which tend to infinity but remain a bounded distance apart. The leading terms in the upper inequality then compare their steps.

## Status
Successful; it proves that all strictly positive displacements coincide.

## Details
Write $d(t)=f(t)-t$. Squaring and expanding the upper inequality yields, with $a=d(x)$ and $b=d(y)$,
\[
(x-y)^2+4yb+2b^2\ge 2a(x+y)+a^2. \tag{1}
\]
Suppose $d(u)=a>0$ and $d(v)=b>0$. The orbit formula gives
\[
d(u+ma)=a,\qquad d(v+nb)=b.
\]
Let $X_m=u+ma$ and choose
\[
n_m=\left\lfloor\frac{X_m-v}{b}\right\rfloor,
\qquad Y_m=v+n_m b.
\]
For all large $m$, $n_m\ge0$, while $0\le X_m-Y_m<b$. Thus both points tend to infinity, their quotient tends to $1$, and their displacement values remain $a,b$.

Apply (1) to $(X_m,Y_m)$, divide by $Y_m$, and pass to the limit. The bounded difference term vanishes and one obtains $4b\ge4a$. Apply (1) in the reversed order, divide by $X_m$, and pass to the limit to get $4a\ge4b$. Therefore $a=b$.

The use of the floor function works whether or not $a/b$ is rational; no density or Diophantine approximation theorem is needed.
