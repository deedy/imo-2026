# Ratio and direct quadratic bounds

## Idea
Try to rewrite the inequalities in terms of ratios such as $f(t)/t$, or square both sides to obtain pairwise quadratic restrictions.

## Status
Abandoned as a main route; useful only for preliminary intuition.

## Details
Squaring the two given inequalities (all quantities are positive) gives
\[
(f(x)+y)^2\le 2(x^2+f(y)^2),
\qquad
(f(x)+y)^2\ge 4xf(y).
\]
For a linear trial $f(t)=ct$, the first of these becomes
\[
(cx+y)^2\le2(x^2+c^2y^2)\qquad(x,y>0).
\]
The associated quadratic form must be nonnegative. Its matrix is
\[
\begin{pmatrix}2-c^2&-c\\-c&2c^2-1\end{pmatrix},
\]
whose determinant is
\[
(2-c^2)(2c^2-1)-c^2=-2(c^2-1)^2.
\]
Thus a linear solution requires $c=1$. This points toward slope $1$, but it misses the additive family $f(t)=t+C$ and does not control nonlinear functions.

Writing $f(t)=t r(t)$ similarly produces constraints involving two independent scales $x/y$, and optimizing those constraints gives bounds rather than the exact orbit structure. The decisive simplification is instead the equality-producing substitution $x=f(y)$.
