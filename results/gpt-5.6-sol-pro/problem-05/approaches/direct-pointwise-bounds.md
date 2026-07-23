# Direct pointwise bounds

## Idea
Try substitutions such as $x=y$ and direct manipulation of each half of the inequality to bound $f(x)$ pointwise, without using iteration.

## Status
Incomplete as a standalone route; retained as a dead end.

## Details
For $d(t)=f(t)-t$, squaring the upper half gives
\[
(x-y)^2+4y d(y)+2d(y)^2\ge2d(x)(x+y)+d(x)^2.
\]
At $x=y=t$ this becomes
\[
4t d(t)+2d(t)^2\ge4t d(t)+d(t)^2,
\]
which reduces only to $d(t)^2\ge0$ and gives no rigidity.

The lower half becomes
\[
(x+y+d(x))^2\ge4x(y+d(y)).
\]
At $x=y=t$ this yields
\[
(2t+d(t))^2\ge4t(t+d(t)),
\]
again the tautology $d(t)^2\ge0$. Thus the diagonal substitution loses all information.

Other fixed choices produce inequalities coupling $d(x)$ and $d(y)$, but without regularity assumptions they do not provide continuity or monotonicity. The decisive extra structure comes from the equality substitution $x=f(y)$, which turns these pointwise comparisons into arithmetic orbit information.
