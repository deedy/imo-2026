# Translation and linear ansatz

## Idea
Test simple candidate families to identify the likely answer before proving rigidity.

## Status
Successful as reconnaissance and final verification, but not a uniqueness proof.

## Details
For $f(t)=t+c$, the middle expression is
\[
\frac{x+y+c}{2}=\frac{x+f(y)}2.
\]
Therefore the required chain is precisely RMS--AM--GM for the two positive numbers $x$ and $f(y)=y+c$. The codomain condition requires $y+c>0$ for every $y>0$, while the orbit argument in the proof ultimately restricts to $c\ge0$; every such $c$ works.

For a homogeneous trial $f(t)=at$ with $a>0$, the forced identity
\[
f(f(y))=2f(y)-y
\]
gives $a^2=2a-1$, hence $(a-1)^2=0$. This points to the identity as the sole homogeneous solution, while translations supply the full nonhomogeneous family.
