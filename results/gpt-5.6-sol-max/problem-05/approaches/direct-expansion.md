# Direct algebraic expansion

## Idea
Write $f(t)=t+d(t)$ and square each side of the chain to seek pointwise bounds on $d(x)$ and $d(y)$.

## Status
Not used in the final proof.

## Details
With $u=f(y)=y+d(y)$, the upper inequality is equivalent to
\[
2(x^2+u^2)\ge (x+u+d(x)-d(y))^2.
\]
After rearrangement this can be expressed as
\[
\bigl(d(x)-d(y)\bigr)igl(2(x+u)+d(x)-d(y)\bigr)
\le (x-u)^2.
\]
When $d(x)\ge d(y)$, this gives a useful upper bound on their difference. The lower inequality similarly becomes
\[
(x+u+d(x)-d(y))^2\ge4xu.
\]
These formulas are valid, but without first exploiting the iteration identity they leave too many interacting quantities. After the orbit identity is known, the upper expansion is exactly the rationalized RMS-gap estimate used in the successful orbit-alignment approach. Thus expansion is best treated as a supporting calculation rather than a standalone route.
