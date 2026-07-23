# Primewise Euclidean invariant

## Idea
Fix a prime $p$ and write the $p$-adic exponents at two selected places as $a=v_p(m)$ and $b=v_p(n)$. The move sends these exponents to
\[
\min(a,b),\qquad \max(a,b)-\min(a,b)=|a-b|.
\]
This is a Euclidean-algorithm operation, and
\[
\gcd(a,b)=\gcd(\min(a,b),|a-b|).
\]
Therefore the gcd of all $2026$ exponents at prime $p$ is invariant.

## Status
Successful.

## Details
Set
\[
G_p=\gcd(v_p(A_1),\ldots,v_p(A_{2026})),
\]
with $\gcd(0,\ldots,0)=0$. The displayed two-variable identity proves that every move preserves $G_p$. At a terminal board, all entries but one are $1$, so its exponent list at $p$ is a permutation of
\[
(v_p(M),0,\ldots,0).
\]
Its gcd is $v_p(M)$. Thus $v_p(M)=G_p$ for every prime $p$, and unique factorization gives
\[
M=\prod_p p^{G_p}.
\]
Only primes dividing the initial product have nonzero $G_p$, so this is a finite product. The formula proves choice-independence.
