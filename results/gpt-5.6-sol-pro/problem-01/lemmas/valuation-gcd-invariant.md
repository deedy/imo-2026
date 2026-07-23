# Lemma: prime-exponent gcd invariant

**Statement.** Let a board have entries $x_1,\ldots,x_N$, and fix a prime $p$. Define
\[
G_p=\gcd(v_p(x_1),\ldots,v_p(x_N)),
\]
using the convention $\gcd(0,\ldots,0)=0$. Then $G_p$ is invariant under every legal move.

**Proof.** Suppose the selected entries have $p$-adic exponents $a$ and $b$. The two replacement entries have exponents
\[
v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
v_p\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
=\max(a,b)-\min(a,b)=|a-b|.
\]
If, without loss of generality, $a\ge b$, then
\[
\gcd(\min(a,b),|a-b|)=\gcd(b,a-b)=\gcd(a,b),
\]
because an integer divides both $a,b$ if and only if it divides both $b,a-b$. Thus the gcd of the selected pair of exponents is unchanged. Taking the gcd also with all untouched exponents shows that the gcd of the full exponent list is unchanged. $\square$
