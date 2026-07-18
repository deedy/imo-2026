# imo-2026-01 — tracking file
## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- **Lexicographic termination potential (successful):** track the total number of prime factors with multiplicity and, secondarily, the number of nonunit entries. Every move strictly decreases this pair lexicographically.
- **Prime-adic valuation invariant (successful):** for each prime $p$, a move changes the selected valuations $(a,b)$ into $(\min(a,b),|a-b|)$, preserving the gcd of all $p$-adic valuations.
- **Product alone (insufficient):** the product of all entries is generally not invariant; it is divided by the selected pair's gcd. It helps motivate the first coordinate of the termination potential but cannot determine the final value.

## Current best
Let the initial entries be $a_1,\dots,a_{2026}$. Every play terminates with exactly one nonunit, and its value is
\[
\boxed{M=\prod_{p}p^{\gcd\bigl(v_p(a_1),\dots,v_p(a_{2026})\bigr)}},
\]
where the product is over all primes and the gcd of an all-zero list is $0$. This finite product is determined solely by the initial board.

## Full proof
Let the entries currently on the board be $x_1,\dots,x_{2026}$. We first prove termination.

For a positive integer $t$, let $\Omega(t)$ denote the number of prime factors of $t$, counted with multiplicity, with $\Omega(1)=0$. Define
\[
 S=\sum_{i=1}^{2026}\Omega(x_i),
 \qquad
 N=\#\{i:x_i>1\}.
\]
We compare pairs $(S,N)$ lexicographically: the first coordinate is compared first, and the second coordinate is used only when the first coordinates are equal.

Suppose a move selects $m,n>1$, and put $d=\gcd(m,n)$. The product of the two new entries is
\[
 d\cdot\frac{\operatorname{lcm}(m,n)}d
 =\operatorname{lcm}(m,n)
 =\frac{mn}{d}.
\]
Since $\Omega(uv)=\Omega(u)+\Omega(v)$ for positive integers $u,v$, the contribution of these two positions to $S$ changes from
\[
 \Omega(m)+\Omega(n)

to
\[
 \Omega(m)+\Omega(n)-\Omega(d).
\]
If $d>1$, then $\Omega(d)>0$, so $S$ strictly decreases. If $d=1$, the new entries are $1$ and $mn$. Thus $S$ stays unchanged, while the two selected nonunits are replaced by exactly one nonunit, so $N$ strictly decreases. Hence every move strictly decreases $(S,N)$ lexicographically.

There cannot be infinitely many such decreases. Indeed, the nonnegative integer $S$ can decrease only finitely many times, and during any interval in which $S$ is fixed, the nonnegative integer $N$ decreases at every move. Therefore every sequence of moves is finite.

When no further move is possible, at most one entry is greater than $1$, since any two entries greater than $1$ could be selected. On the other hand, a move can never leave no entry greater than $1$: if the second new entry
\[
 \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}
\]
equals $1$, then $\operatorname{lcm}(m,n)=\gcd(m,n)$, which forces $m=n$, and the first new entry is then $m>1$; if the second new entry is not $1$, it is itself greater than $1$. Since initially there are entries greater than $1$, every configuration reached has at least one such entry. Consequently, every terminal configuration has exactly one entry $M>1$. This proves part (a).

It remains to show that $M$ is independent of the moves. Fix a prime $p$. For every positive integer $x$, write $v_p(x)$ for its exponent in the prime factorization of $x$. Define
\[
 G_p=\gcd\bigl(v_p(x_1),\dots,v_p(x_{2026})\bigr),
\]
using the convention that the gcd of an all-zero list is $0$.

We claim that $G_p$ is invariant under every move. If
\[
 a=v_p(m),\qquad b=v_p(n),
\]
then the valuations at the two selected positions become
\[
 v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
 v_p\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
 =\max(a,b)-\min(a,b)=|a-b|.
\]
Assume without loss of generality that $a\le b$. Then
\[
 \gcd\bigl(\min(a,b),|a-b|\bigr)
 =\gcd(a,b-a)=\gcd(a,b).
\]
Taking the gcd also with all valuations at the unchanged positions therefore gives the same value before and after the move. Thus $G_p$ is indeed invariant.

Let the initial entries be $a_1,\dots,a_{2026}$. At the end, all entries except $M$ equal $1$, so their $p$-adic valuations are $0$. The final value of the invariant is consequently
\[
 \gcd(v_p(M),0,\dots,0)=v_p(M).
\]
Its initial value was $\gcd(v_p(a_1),\dots,v_p(a_{2026}))$. Hence, for every prime $p$,
\[
 v_p(M)=\gcd\bigl(v_p(a_1),\dots,v_p(a_{2026})\bigr).
\]
By unique prime factorization,
\[
 M=\prod_p p^{\gcd(v_p(a_1),\dots,v_p(a_{2026}))}.
\]
Only primes dividing at least one initial entry can have a nonzero exponent in this product, so it is finite. The formula involves only the initial entries and not the sequence of moves. Therefore the value of $M$ is independent of all choices, proving part (b). $\square$
