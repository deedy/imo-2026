# Circle-coordinate and trigonometric-factorization approach

## Idea
Introduce the six positive angle parameters
\[
p=\angle KBA=\angle ACL,\ q=\angle LBK=\angle LNC,\ r=\angle LCK=\angle BMK,
\]
\[
x=\angle BAK,\ y=\angle CAL,\ \delta=\angle KAL.
\]
The midpoint and sine-rule relations give
\[
\cot x=\cot p+2\cot r,\quad \cot y=\cot p+2\cot q,
\]
and formulas for $AK/AB$ and $AL/AC$. The remaining two incidences produce the compatibility equation
\[
PQ\sin(p+r+\delta+y)\sin(p+q+\delta+x)=\sin(p+r)\sin(p+q).
\]

For the circle through $A,K,L$, let its second intersections with the oriented lines $AB,AC$ be $D,E$. Its vector equation shows
\[
OM=ON\iff AB\cdot AD-AC\cdot AE=\frac{AB^2-AC^2}{2}.
\]
Solving for $AD,AE$ from the circle equation turns this target into a trigonometric residual $T$. The key exact factorization is
\[
T=\sin(x-y)\left(PQ\sin(p+r+\delta+y)\sin(p+q+\delta+x)-\sin(p+r)\sin(p+q)\right).
\]
The bracket vanishes by compatibility.

## Status
Successful. Full details are in `current.md`; the standalone factorization is in `lemmas/trigonometric-factorization.md`.
