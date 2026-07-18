# Valuation-gcd invariant

## Statement
Fix a prime $p$. For a board of positive integers $x_1,\ldots,x_N$, set
\[
G_p=\gcd\bigl(v_p(x_1),\ldots,v_p(x_N)\bigr),
\]
where all arguments are nonnegative integers and the gcd of a list consisting only of zeros is $0$. If two entries $m,n>1$ are replaced by
\[
\gcd(m,n),\qquad \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)},
\]
then $G_p$ is unchanged.

## Proof
Put $a=v_p(m)$ and $b=v_p(n)$. The exponents of $p$ in the replacement entries are
\[
\min(a,b)
\quad\text{and}\quad
\max(a,b)-\min(a,b)=|a-b|.
\]
Suppose without loss of generality that $a\le b$. Then
\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b-a)=\gcd(a,b),
\]
because an integer divides both $a$ and $b-a$ if and only if it divides both $a$ and $b$. Taking the gcd together with all unchanged exponents thus gives the same $G_p$ before and after the move. This also covers $a=0$, $b=0$, and $a=b$. $\square$