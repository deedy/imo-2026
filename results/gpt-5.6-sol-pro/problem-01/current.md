# imo-2026-01 — tracking file
## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- **Product-and-count descent (successful):** Track the product $P$ of all entries and the number $K$ of nonunit entries. A move with selected gcd $g$ changes $P$ to $P/g$. If $g>1$, the product decreases; if $g=1$, the product is fixed but $K$ decreases. Thus $P+K$ strictly decreases.
- **Prime-adic Euclidean invariant (successful):** For each prime $p$, the selected exponents $(a,b)$ become $(\min(a,b),|a-b|)$. The gcd of the complete list of $p$-adic exponents is invariant under this Euclidean-algorithm step, and at termination it is exactly $v_p(M)$.
- **Exhaustive sanity check:** A Python search over all boards of lengths $2,3,4$ with entries from $2$ through $10$ found that every possible play terminates at the value predicted by the prime-adic formula.

## Current best
Let the initial entries be $A_1,\ldots,A_{2026}$. Every play terminates with one nonunit, and its choice-independent value is
\[
\boxed{M=\prod_p p^{\gcd(v_p(A_1),\ldots,v_p(A_{2026}))}},
\]
where $\gcd(0,\ldots,0)=0$ and the product is effectively only over primes dividing at least one initial entry. Termination follows from strict descent of $P+K$, while the formula follows from preservation, prime by prime, of the gcd of all valuation exponents.

## Full proof
Let a **nonunit** mean an entry greater than $1$. At any stage, define
\[
P=\text{the product of all entries on the blackboard},
\qquad
K=\text{the number of nonunit entries}.
\]
Both $P$ and $K$ are positive integers as long as there is at least one nonunit.

Suppose that Confucius selects $m,n>1$, and put $g=\gcd(m,n)$. Since
\[
mn=\gcd(m,n)\operatorname{lcm}(m,n)=g\operatorname{lcm}(m,n),
\]
the product of the two selected entries changes from $mn$ to
\[
g\cdot\frac{\operatorname{lcm}(m,n)}g
 =\operatorname{lcm}(m,n)=\frac{mn}{g}.
\]
Consequently, the total product changes from $P$ to $P/g$.

The number $K$ cannot increase, since two nonunits are replaced by only two entries. More precisely:

- If $g>1$, then $P/g<P$, while $K$ does not increase.
- If $g=1$, the two new entries are $1$ and $mn$. Because $mn>1$, the product $P$ is unchanged and $K$ decreases by exactly one.

It follows that the positive integer $P+K$ strictly decreases after every move. Hence there cannot be infinitely many moves.

Furthermore, no move can eliminate all nonunits. Indeed, if $g>1$, then the first new entry $g$ is a nonunit; if $g=1$, then the second new entry $mn$ is a nonunit. Since initially there are nonunits, there is therefore always at least one. Once the process stops, there cannot be two nonunits, since any two of them could be selected for another move. Thus at termination there is exactly one nonunit. Denote it by $M$. This proves part (a).

It remains to determine $M$. Write the initial entries as
\[
A_1,A_2,\ldots,A_{2026}.
\]
Fix an arbitrary prime $p$. For any positive integer $x$, let $v_p(x)$ denote the exponent of $p$ in its prime factorization. If the selected entries $m,n$ have exponents
\[
a=v_p(m),\qquad b=v_p(n),
\]
then the two new entries have exponents
\[
v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
v_p\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
 =\max(a,b)-\min(a,b)=|a-b|.
\]
The gcd of these two new exponents equals the gcd of the old exponents. Indeed, if, without loss of generality, $a\ge b$, then
\[
\gcd(\min(a,b),|a-b|)=\gcd(b,a-b)=\gcd(a,b),
\]
because an integer divides both $a$ and $b$ if and only if it divides both $b$ and $a-b$.

Therefore the quantity
\[
G_p=\gcd\bigl(v_p(x_1),v_p(x_2),\ldots,v_p(x_{2026})\bigr),
\]
where $x_1,\ldots,x_{2026}$ are the current entries, is invariant under a move: the gcd of the two altered exponents is preserved, and all the other exponents are unchanged. We use the convention that the gcd of a list consisting entirely of zeros is $0$.

At the end, the entries are $M$ and $2025$ copies of $1$, in some order. Their $p$-adic exponents are consequently $v_p(M)$ and $2025$ zeros. Their gcd is $v_p(M)$. Applying the invariant from the initial board to the final board gives
\[
v_p(M)=\gcd\bigl(v_p(A_1),v_p(A_2),\ldots,v_p(A_{2026})\bigr)
\tag{1}
\]
for every prime $p$.

Only primes dividing the finite product $A_1A_2\cdots A_{2026}$ can occur in (1). Hence unique factorization yields the finite formula
\[
M=\prod_p p^{\gcd(v_p(A_1),v_p(A_2),\ldots,v_p(A_{2026}))}.
\]
The right-hand side depends only on the initial entries, not on any choices of pairs during the process. Therefore the final value of $M$ is independent of all of Confucius's choices, proving part (b). $\square$
