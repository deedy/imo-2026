# Excluding mixed zero and positive displacement

## Idea
After proving that every positive displacement equals one common number $c$, use the upper inequality to show that the zero-displacement set and positive-displacement set have a forbidden distance gap. A finite chain along an interval contradicts such a partition.

## Status
Successful; this completes the rigidity argument.

## Details
Assume $d(t)\in\{0,c\}$ for all $t>0$, where $c>0$. The expanded upper inequality is
\[
(x-y)^2+4y d(y)+2d(y)^2
\ge 2d(x)(x+y)+d(x)^2. \tag{1}
\]
If $d(p)=c$ and $d(q)=0$, (1) gives
\[
(p-q)^2\ge2c(p+q)+c^2>c^2,
\]
so $|p-q|>c$ for every cross-type pair.

If both types existed, join one point of each type by a finite equally spaced chain whose step is less than $c$. The endpoint labels differ, so some consecutive points have different labels, but their distance is less than $c$. This contradicts the cross-type separation. Therefore either every displacement is zero or every displacement is $c$.
