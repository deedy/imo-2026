# Prime-adic invariant

## Idea
Track, for each prime $p$, the gcd of all $p$-adic valuations on the board.

## Status
Successful; identifies the unique final value.

## Details
If $a=v_p(m)$ and $b=v_p(n)$, then a move replaces these two exponents by
\[
\min(a,b)\quad\text{and}\quad \max(a,b)-\min(a,b)=|a-b|.
\]
Their gcd is unchanged because
\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b).
\]
Consequently, taking the gcd together with all unchanged exponents shows that
\[
g_p=\gcd_i v_p(x_i)
\]
is invariant under every move.

At termination all entries except one, say $M$, equal $1$. Thus the final valuation list for $p$ consists of $v_p(M)$ and zeros, whose gcd is $v_p(M)$. Hence
\[
v_p(M)=g_p=\gcd_i v_p(x_i)
\]
for every prime $p$, and therefore
\[
M=\prod_p p^{\gcd_i v_p(x_i)}.
\]
Only primes dividing at least one initial entry can occur, so this is a finite product. The formula depends only on the initial board.
