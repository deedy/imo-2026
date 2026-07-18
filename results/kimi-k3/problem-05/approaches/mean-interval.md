# Approach: rewrite as an interval for a mean

## Status
Successful; this is the first half of the final proof.

## Idea
For fixed $x,y$, let $v=f(y)$. The given inequalities compare $M=f(x)+y$ with the geometric and quadratic means of the two positive numbers $x$ and $v$. Since
\[
4xv=(x+v)^2-(x-v)^2,\qquad 2(x^2+v^2)=(x+v)^2+(x-v)^2,
\]
the hypothesis is equivalent to
\[
|(f(x)+y)^2-(x+f(y))^2|\le (x-f(y))^2.
\]
This formulation is strong because the right side vanishes when $x=f(y)$. That substitution immediately gives
\[
f(f(y))=2f(y)-y.
\]

## Details and outcome
The equivalence is proved in `lemmas/key-mean-estimate.md`. It removes the square roots and turns the problem into a functional equation plus a quantitative estimate. No continuity, monotonicity, or surjectivity is assumed.
