# Equality substitution and forward orbits

## Idea
Choose the variables so that the two outer quantities in the chain are equal. For fixed $y>0$, setting $x=f(y)$ makes both outer quantities equal to $f(y)$, forcing equality in the middle.

## Status
Successful; this is the structural starting point of the final proof.

## Details
The substitution gives
\[
f(f(y))=2f(y)-y.
\]
If $t_0=t$ and $t_{n+1}=f(t_n)$, then
\[
t_{n+2}-t_{n+1}=t_{n+1}-t_n,
\]
so
\[
t_n=t+n(f(t)-t).
\]
All iterates must remain positive. Therefore $f(t)-t\ge 0$ for every $t>0$. In addition,
\[
f(t+n(f(t)-t))=t+(n+1)(f(t)-t),
\]
so the displacement $f(s)-s$ is constant along every forward orbit. Thus every orbit is either a fixed point or an infinite arithmetic progression with positive common difference.
