# Prime-adic exponent invariant

## Idea
Fix a prime $p$ and write $a=v_p(m)$, $b=v_p(n)$ for the chosen entries. The two replacement entries have exponents
\[
\min(a,b),\qquad \max(a,b)-\min(a,b)=|a-b|.
\]
The elementary Euclidean-algorithm identity
\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b)
\]
shows that the gcd of all $2026$ exponents $v_p(x_i)$ is unchanged by a move.

If the initial entries are $a_1,\ldots,a_{2026}$, define
\[
g_p=\gcd\bigl(v_p(a_1),\ldots,v_p(a_{2026})\bigr),
\]
with the gcd of an all-zero list defined as $0$. At a terminal board $(M,1,\ldots,1)$, the corresponding gcd is
\[
\gcd(v_p(M),0,\ldots,0)=v_p(M).
\]
Therefore
\[
v_p(M)=g_p
\]
for every prime $p$, and hence
\[
M=\prod_p p^{g_p}.
\]
Only primes dividing the initial total product have nonzero $g_p$, so this is a finite product. The formula depends only on the initial board and proves part (b).

## Status
Complete invariant and uniqueness argument, to be combined with the termination proof.