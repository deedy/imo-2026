# Lemma: gcd of the prime-adic exponents is invariant

## Statement
Fix a prime $p$. For a board $x_1,\dots,x_N$ of positive integers define
\[
G_p(x_1,\dots,x_N)=\gcd(v_p(x_1),\dots,v_p(x_N)),
\]
where the gcd of an all-zero list is $0$. Then $G_p$ is unchanged by every legal move.

## Proof
Suppose the selected entries have $p$-adic exponents $a$ and $b$. The replacement entries have exponents
\[
v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
=\max(a,b)-\min(a,b)=|a-b|.
\]
We have
\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b).
\]
Indeed, if $a\ge b$, this is the standard identity $\gcd(b,a-b)=\gcd(a,b)$: a nonnegative integer divides both $a,b$ exactly when it divides both $b,a-b$. The case $b\ge a$ is symmetric, and the same argument includes zero exponents.

The gcd of the two altered exponents is therefore unchanged. Taking its gcd with all the unaltered exponents proves that the gcd of the full list is unchanged. $\square$
