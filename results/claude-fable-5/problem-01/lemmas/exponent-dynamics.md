# Lemma (per-prime effect of a move)

**Statement.** Let $m,n>1$ be integers and let $p$ be a prime. Put $a=v_p(m)$, $b=v_p(n)$
(where $v_p$ denotes the $p$-adic valuation). Then
$$v_p\big(\gcd(m,n)\big)=\min(a,b),\qquad v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)=\max(a,b)-\min(a,b),$$
and $\operatorname{lcm}(m,n)/\gcd(m,n)$ is a positive integer.

**Proof.** For every prime $p$ we have $v_p(\gcd(m,n))=\min(a,b)$ and $v_p(\operatorname{lcm}(m,n))=\max(a,b)$
(standard). Since $\min(a,b)\le\max(a,b)$ for every prime, $\gcd(m,n)\mid\operatorname{lcm}(m,n)$, so the quotient
is a positive integer with $v_p=\max(a,b)-\min(a,b)$. $\blacksquare$

# Lemma (gcd invariance of a pair)

**Statement.** For all integers $a,b\ge 0$:
$$\gcd\big(\min(a,b),\ \max(a,b)-\min(a,b)\big)=\gcd(a,b),$$
with the convention $\gcd(0,0)=0$.

**Proof.** WLOG $a\le b$. Then the left side is $\gcd(a,b-a)$. Any integer $d$ divides both $a$ and $b-a$
iff it divides both $a$ and $b$; hence the sets of common divisors of $(a,b-a)$ and of $(a,b)$ coincide,
so the gcd's are equal. (If $a=b=0$, both sides are $0$.) $\blacksquare$
