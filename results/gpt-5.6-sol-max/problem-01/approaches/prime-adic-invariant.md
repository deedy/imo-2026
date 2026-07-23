# Prime-adic exponent invariant

## Idea
For each prime separately, the move is one step of the subtractive Euclidean algorithm on the two selected exponents.

## Status
Successful; it determines the terminal number uniquely.

## Details
Fix a prime $p$ and write the exponents of $p$ in the current entries as
\[
e_i=v_p(x_i)\quad (1\le i\le N).
\]
If the selected exponents are $a$ and $b$, the two new exponents are
\[
\min(a,b)\quad\text{and}\quad |a-b|.
\]
The identity
\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b)
\]
shows that
\[
G_p:=\gcd(e_1,\dots,e_N)
\]
is invariant. Here $\gcd(0,t)=t$, including the convention that an all-zero gcd is $0$.

At a terminal board, all but one entries are $1$. If the sole nonunit is $M$, then
\[
G_p=\gcd(0,\dots,0,v_p(M),0,\dots,0)=v_p(M).
\]
It follows that every terminal play has
\[
M=\prod_p p^{\gcd(v_p(x_1),\dots,v_p(x_N))}.
\]
Only primes dividing an initial entry occur in this finite product. This establishes choice-independence by uniqueness of prime factorization.

## Exploratory note
The sum of all $p$-adic exponents is not invariant: for $a\ge b$ it changes from $a+b$ to $a$. It is nonincreasing, but it does not by itself force termination because it is unchanged whenever one selected exponent is zero. This motivated retaining the gcd, which is exactly preserved, and using a separate global potential for termination.
