# imo-2026-01 — tracking file
## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- **Lexicographic descent (successful):** track the product of all board entries and the number of entries greater than $1$. A move with nontrivial gcd decreases the product, while a move with gcd $1$ preserves the product and decreases the number of nonunit entries. Details are in [approaches/lexicographic-descent.md](approaches/lexicographic-descent.md).
- **Prime-adic exponent invariant (successful):** for each prime $p$, the selected exponent pair $(a,b)$ becomes $(\min(a,b),|a-b|)$; the gcd of all $p$-adic exponents is consequently invariant. Details are in [approaches/prime-adic-invariant.md](approaches/prime-adic-invariant.md), with the invariant isolated in [lemmas/valuation-gcd-invariant.md](lemmas/valuation-gcd-invariant.md).
- **Computational sanity check:** random plays on $5000$ small initial boards (four plays per board) all terminated at the value predicted by the valuation formula; see [code/random_verify.py](code/random_verify.py). This check is not used in the proof.

## Current best
The problem is solved. If the initial integers are $x_1,\ldots,x_{2026}$, then every play terminates with exactly one nonunit, and its value is explicitly
\[
M=\prod_{p}p^{\gcd(v_p(x_1),\ldots,v_p(x_{2026}))},
\]
where the gcd of an all-zero list is $0$. Only finitely many factors differ from $1$.

## Full proof
Let the entries at any stage be $y_1,\ldots,y_{2026}$, and define
\[
P=\prod_{i=1}^{2026}y_i,
\qquad
K=\#\{i:y_i>1\}.
\]
All entries are positive integers throughout the process.

### (a) Termination and the number of surviving nonunits
Consider a move involving $m,n>1$, and put $d=\gcd(m,n)$. The product of the two new entries is
\[
d\cdot\frac{\operatorname{lcm}(m,n)}{d}
 =\operatorname{lcm}(m,n)
 =\frac{mn}{d}.
\]
All other entries are unchanged, so the new board product is $P/d$.

If $d>1$, the positive integer $P$ strictly decreases. If $d=1$, the selected entries are replaced by
\[
1\quad\text{and}\quad mn.
\]
In this case $P$ is unchanged, while $K$ decreases by exactly $1$, because two entries greater than $1$ have been replaced by precisely one entry greater than $1$.

Suppose, for contradiction, that some sequence of moves were infinite. Along it, $P$ would be a nonincreasing sequence of positive integers, so from some point onward $P$ would be constant. Every move from that point onward would therefore have $d=1$. But then the nonnegative integer $K$ would decrease by $1$ at every subsequent move, which cannot happen infinitely many times. Thus every sequence of moves is finite.

A move is possible exactly when $K\ge 2$. Hence, when Confucius can no longer move, $K\le 1$. On the other hand, a move can never leave no entry greater than $1$: if $d>1$, its first output $d$ is greater than $1$, while if $d=1$, its second output $mn$ is greater than $1$. Since initially $K=2026>0$, we therefore have $K\ge1$ at every stage. Consequently the terminal board has exactly one entry $M>1$.

### (b) Independence of the choices
Fix a prime $p$. For any positive integer $z$, let $v_p(z)$ denote the exponent of $p$ in its prime factorization. We claim that
\[
G_p=\gcd\bigl(v_p(y_1),\ldots,v_p(y_{2026})\bigr)
\tag{1}
\]
is invariant under every move. Here, as usual, $\gcd(0,r)=r$, and an all-zero gcd is defined to be $0$.

Indeed, let
\[
a=v_p(m),\qquad b=v_p(n)
\]
for the two selected entries. Their two replacements have $p$-adic exponents
\[
v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
 =\max(a,b)-\min(a,b)=|a-b|.
\]
If, without loss of generality, $a\le b$, then
\[
\gcd\bigl(\min(a,b),|a-b|\bigr)
 =\gcd(a,b-a)=\gcd(a,b).
\tag{2}
\]
The last equality holds because an integer divides both $a$ and $b-a$ if and only if it divides both $a$ and $b$. Thus replacing $a,b$ by $\min(a,b),|a-b|$ does not change their gcd. Taking the gcd with all the unchanged exponents proves that (1) is invariant.

Now denote the initial entries by $x_1,\ldots,x_{2026}$ and set
\[
g_p=\gcd\bigl(v_p(x_1),\ldots,v_p(x_{2026})\bigr).
\]
By part (a), the terminal entries are $M$ and $2025$ copies of $1$, in some order. Applying the invariant (1) at the initial and terminal boards gives
\[
g_p
 =\gcd\bigl(v_p(M),0,\ldots,0\bigr)
 =v_p(M)
\tag{3}
\]
for every prime $p$. It follows from unique prime factorization that necessarily
\[
\boxed{M=\prod_p p^{g_p}
      =\prod_p p^{\gcd(v_p(x_1),\ldots,v_p(x_{2026}))}.}
\]
If a prime divides none of the initial entries, its exponent in this product is $0$, so the product has only finitely many nontrivial factors. The displayed value is determined solely by the initial board. Therefore the terminal value $M$ is independent of all choices made by Confucius. $\square$
