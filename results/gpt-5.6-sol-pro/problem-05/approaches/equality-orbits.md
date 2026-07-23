# Equality substitution and arithmetic orbits

## Idea
Force equality by choosing the first variable to equal the function value appearing on the other side. Then analyze the resulting iteration law.

## Status
Successful; this is the first part of the final proof.

## Details
Set $x=f(y)$. The outer terms of the chain are both $f(y)$, since
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y)
\quad\text{and}\quad
\sqrt{f(y)f(y)}=f(y).
\]
Thus
\[
\frac{f(f(y))+y}{2}=f(y),
\qquad
f(f(y))=2f(y)-y.
\]
For $d(y)=f(y)-y$, this is
\[
d(f(y))=d(y).
\]
It follows inductively that
\[
f^n(y)=y+n d(y)\qquad(n\ge0).
\]
If $d(y)<0$, a sufficiently large iterate is nonpositive, contradicting the codomain. Hence $d(y)\ge0$ everywhere.

This identifies every orbit as an arithmetic progression whose step is its displacement. The remaining issue is to prove that different orbits cannot have different nonnegative steps.
