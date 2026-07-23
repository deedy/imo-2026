# imo-2026-01 — tracking file
## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- **Lexicographic descent:** Tracking the product $P$ of all entries and the number $r$ of entries greater than $1$ gives a lexicographically decreasing pair $(P,r)$. This was consolidated into the single positive-integer potential $P2^r$.
- **Prime-adic exponent invariant:** For each prime $p$, a selected pair of exponents $(a,b)$ changes to $(\min(a,b),|a-b|)$. The gcd of all $p$-adic exponents is invariant and determines the exponent of $p$ in the terminal number.
- **Exponent-sum exploration:** The sum of the $p$-adic exponents is nonincreasing, but it can stay unchanged when one selected entry is not divisible by $p$, so it is not by itself a termination argument. It nevertheless helps motivate separating termination from the choice-independent invariant.
- **Computational sanity check:** Exhaustive exploration of all move trees for $705$ small initial multisets (sizes $2$ through $4$, entries at most $10$) confirmed strict potential descent and the stated terminal formula.

## Current best
The problem is solved. If the initial entries are $x_1,\ldots,x_{2026}$, then every play terminates with one nonunit, and its choice-independent value is
\[
M=\prod_p p^{\gcd\bigl(v_p(x_1),\ldots,v_p(x_{2026})\bigr)},
\]
where the gcd of an all-zero list is $0$; only finitely many factors differ from $1$.

## Full proof
Let $N=2026$. At any stage, denote the entries on the board by
\[
y_1,y_2,\ldots,y_N,
\]
and define
\[
P=\prod_{i=1}^N y_i,
\qquad
r=\#\{i:y_i>1\},
\qquad
\Phi=P2^r.
\]
Thus $\Phi$ is a positive integer.

### (a) Termination and the number of remaining nonunits
Suppose a legal move selects $m,n>1$, and write
\[
d=\gcd(m,n).
\]
Using $\gcd(m,n)\operatorname{lcm}(m,n)=mn$, the product of the two replacement entries is
\[
d\cdot\frac{\operatorname{lcm}(m,n)}d
=\operatorname{lcm}(m,n)
=\frac{mn}{d}.
\]
Consequently, if $P'$ denotes the product after the move, then
\[
P'=\frac Pd.
\]

If $d=1$, then the replacement pair is $(1,mn)$. Hence two nonunits are replaced by exactly one nonunit, so $r'=r-1$. Therefore
\[
\Phi'=P'2^{r'}=P2^{r-1}=\frac{\Phi}{2}<\Phi.
\]

If $d>1$, then the first replacement entry $d$ is greater than $1$, while the second is a positive integer. Thus the two selected nonunits are replaced by either one or two nonunits, and in particular $r'\le r$. It follows that
\[
\Phi'=\frac Pd2^{r'}\le \frac Pd2^r=\frac{\Phi}{d}<\Phi.
\]

Hence every legal move strictly decreases the positive integer $\Phi$. There is no infinite strictly decreasing sequence of positive integers, so every sequence of moves is finite.

When no further move is possible, there cannot be two entries greater than $1$, because any such two entries could be selected. Thus a terminal board has at most one nonunit. On the other hand, a move can never eliminate all nonunits: indeed, the product of its two replacement entries is $\operatorname{lcm}(m,n)>1$, so those entries cannot both be $1$. Since initially all entries are greater than $1$, at least one nonunit remains at every stage. Therefore, when the process terminates, exactly one entry $M$ is greater than $1$.

### (b) Independence of the choices
Let the initial entries be $x_1,\ldots,x_N$. Fix a prime $p$. For a current board $y_1,\ldots,y_N$, define
\[
G_p=\gcd\bigl(v_p(y_1),\ldots,v_p(y_N)\bigr),
\]
with the convention that the gcd of an all-zero list is $0$.

Suppose the two entries selected in a move have $p$-adic exponents
\[
a=v_p(m),\qquad b=v_p(n).
\]
The two replacement entries have exponents
\[
v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
=\max(a,b)-\min(a,b)=|a-b|.
\]
Furthermore,
\[
\gcd\bigl(\min(a,b),|a-b|\bigr)=\gcd(a,b).
\]
To verify this identity, if $a\ge b$, an integer divides both $a$ and $b$ if and only if it divides both $b$ and $a-b$; the case $b\ge a$ is symmetric. This also covers the cases in which one or both exponents are zero.

Thus the gcd of the two altered exponents does not change. Taking its gcd with all the unaltered exponents shows that $G_p$ is invariant under every move.

At the terminal board, all entries except $M$ equal $1$. Since $v_p(1)=0$, the terminal value of this invariant is
\[
\gcd(0,\ldots,0,v_p(M),0,\ldots,0)=v_p(M).
\]
It must equal its initial value, so for every prime $p$,
\[
v_p(M)=\gcd\bigl(v_p(x_1),\ldots,v_p(x_N)\bigr).
\]
Therefore
\[
\boxed{M=\prod_p p^{\gcd(v_p(x_1),\ldots,v_p(x_N))}}.
\]
For every prime not dividing any initial entry, the exponent in this product is $0$, so the product is finite. The right-hand side depends only on the initial board, and uniqueness of prime factorization now proves that the terminal value $M$ is independent of every choice made during the process. $\square$
