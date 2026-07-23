# Forward-orbit displacement

## Idea
Force equality by setting $x=f(y)$. Since both outer terms of the inequality chain then equal $f(y)$, the middle term must equal the same value.

## Status
Successful.

## Details
The equality substitution gives
\[
f(f(y))=2f(y)-y.
\]
For the displacement $d(t)=f(t)-t$, this says
\[
d(f(y))=d(y).
\]
Inductively, every forward orbit has the explicit form
\[
f^n(y)=y+n d(y),\qquad d(f^n(y))=d(y).
\]
Because every iterate lies in $\mathbb R_{>0}$, a negative $d(y)$ is impossible: the displayed arithmetic progression would eventually be nonpositive. Hence $d(y)\ge0$ everywhere.

This converts an arbitrary functional inequality into a comparison problem for nonnegative step sizes of arithmetic progressions.
