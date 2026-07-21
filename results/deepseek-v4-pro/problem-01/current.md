# imo-2026-01 — tracking file

## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so.
(a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$.
(b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- Brute‑force simulation for small cases to guess the final value $M$ and invariants.
- Discovered that for each prime $p$, the gcd of the exponents of $p$ across all numbers is invariant, and the final $M$ equals $\prod_p p^{\gcd(\text{exponents})}$.
- Termination proved via monovariant $K+\sum\Omega$ strictly decreasing (where $K$ counts numbers $>1$, $\Omega$ counts prime factors with multiplicity).
- Invariant proof uses the fact that on the exponent multiset the move acts as $(\alpha,\beta)\mapsto(\min(\alpha,\beta),|\alpha-\beta|)$, which preserves the gcd of the whole multiset.

## Current best
The final unique integer $M>1$ equals
\[
M = \prod_{p\text{ prime}} p^{\,d_p},\qquad
d_p = \gcd\bigl(v_p(a_1),v_p(a_2),\dots,v_p(a_{2026})\bigr),
\]
where $a_1,\dots,a_{2026}$ are the initial numbers and $v_p(a)$ is the exponent of $p$ in $a$. Both parts are proved below.

## Full proof
Let $N=2026$ and let the initial numbers be $a_1,a_2,\dots,a_N$ (all integers $>1$).  At any moment we denote the numbers on the board by $x_1,\dots,x_N$ (some may become $1$ during the process).  The order of the numbers is irrelevant, so we may treat the board as a multiset.

---
### 1. Termination – proof of part (a)

For a positive integer $t$ let $\Omega(t)$ be the number of prime factors of $t$ counted with multiplicity; set $\Omega(1)=0$.  Define
\[
K = \#\{\,i \mid x_i > 1\,\},\qquad 
S = \sum_{i=1}^{N} \Omega(x_i).
\]
Both $K$ and $S$ are non‑negative integers.

A move picks two distinct indices $i,j$ with $x_i,x_j>1$.  Put $m=x_i$, $n=x_j$.  Let
\[
g=\gcd(m,n),\qquad h=\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}=\frac{mn}{g^{2}}.
\]
The two numbers $m,n$ are replaced by $g$ and $h$.  Write $m=g a$, $n=g b$ with $\gcd(a,b)=1$; then $h=ab$.

We analyse how $K$ and $S$ change.

* **Case 1: $g=1$.**  
  Then $h=mn>1$.  The new pair is $(1,\,mn)$.  Consequently
  \[
  K' = K-1,\qquad
  S' = S-\Omega(m)-\Omega(n)+\Omega(1)+\Omega(mn)=S.
  \]
  (Equality holds because $\gcd(m,n)=1$ implies $\Omega(mn)=\Omega(m)+\Omega(n)$.)

* **Case 2: $g>1$ and $m=n$.**  
  Then $a=b=1$, so $h=1$.  The new pair is $(g,1)$.  Hence
  \[
  K' = K-1,\qquad
  S' = S-2\Omega(m)+\Omega(g)+\Omega(1)=S-\Omega(m)\le S-1.
  \]
  (Here $\Omega(m)=\Omega(g)$ because $m=g$.)

* **Case 3: $g>1$ and $m\neq n$.**  
  Then $a,b$ are not both $1$, so $h=ab>1$.  Both $g>1$ and $h>1$ hold.
  \[
  K' = K,\qquad
  S' = S-\Omega(m)-\Omega(n)+\Omega(g)+\Omega(h).
  \]
  Since $\Omega(m)=\Omega(g)+\Omega(a)$, $\Omega(n)=\Omega(g)+\Omega(b)$ and $\Omega(h)=\Omega(ab)=\Omega(a)+\Omega(b)$ (using $\gcd(a,b)=1$), we obtain
  \[
  S' = S - \Omega(g) \le S-1.
  \]

In every case either $K$ decreases by $1$ (Cases 1, 2) or $K$ stays the same and $S$ decreases by at least $1$ (Case 3).  Therefore the quantity
\[
\Phi = K+S
\]
strictly decreases by at least $1$ with each move.  Being a non‑negative integer, $\Phi$ cannot decrease forever; after finitely many moves the process must stop.

The process stops exactly when fewer than two numbers on the board exceed $1$, i.e. $K\le 1$.  We claim that $K$ can never become $0$.  Indeed, a move can produce at most one $1$ (Cases 1 and 2 yield exactly one $1$; Case 3 yields none), so $K$ decreases by at most $1$ per move.  Initially $K=N\ge 2$.  To reach $K=0$ we would need at least $N$ moves that reduce $K$, but after $N-1$ such moves we already have $K=1$; at that point no further move is possible because a move requires two numbers $>1$.  Hence the process necessarily terminates with $K=1$.  Thus after finitely many moves exactly one integer $M>1$ remains on the board.  This proves part (a).

---
### 2. Invariance of the exponent–gcd – proof of part (b)

Fix an arbitrary prime $p$.  For an integer $t\ge 1$ denote by $v_p(t)$ the exponent of $p$ in the prime factorisation of $t$; set $v_p(1)=0$.

Consider a move on numbers $m,n$ with $\alpha=v_p(m)$, $\beta=v_p(n)$.  Then
\[
v_p(\gcd(m,n)) = \min(\alpha,\beta),\qquad
v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
= \alpha+\beta-2\min(\alpha,\beta)=|\alpha-\beta|.
\]
Thus for the multiset $\mathcal E_p$ of the $N$ values $v_p(x_1),\dots,v_p(x_N)$, a move replaces two elements $\alpha,\beta$ by $\min(\alpha,\beta)$ and $|\alpha-\beta|$, leaving all other elements unchanged.

For a multiset $S$ of non‑negative integers, let $\gcd(S)$ denote the greatest common divisor of its elements, defined as the unique non‑negative integer $d$ such that $d\mid s$ for every $s\in S$ and every common divisor of $S$ divides $d$.  (If all elements are $0$ then $\gcd(S)=0$.)

**Lemma (invariance).** Let $S$ be a multiset of non‑negative integers and let $S'$ be obtained from $S$ by picking two elements $\alpha,\beta$ and replacing them with $\min(\alpha,\beta)$ and $|\alpha-\beta|$.  Then $\gcd(S')=\gcd(S)$.

*Proof.*  Put $d=\gcd(S)$.  From $d\mid\alpha$ and $d\mid\beta$ we get $d\mid\min(\alpha,\beta)$ and $d\mid|\alpha-\beta|$; together with $d$ dividing every other element of $S$ unchanged, we obtain $d\mid\gcd(S')$.

Conversely, let $d'=\gcd(S')$.  Then $d'\mid\min(\alpha,\beta)$ and $d'\mid|\alpha-\beta|$.  If $\alpha\le\beta$, then $\alpha=\min(\alpha,\beta)$ and $\beta=\min(\alpha,\beta)+|\alpha-\beta|$, so $d'\mid\alpha$ and $d'\mid\beta$.  The case $\beta\le\alpha$ is symmetric.  Hence $d'$ divides all elements of $S$, whence $d'\mid d$.

Thus $d'=d$, as claimed. ∎

Apply this lemma to the multiset $\mathcal E_p$.  Initially
\[
\mathcal E_p^{(0)} = \{v_p(a_1),\,v_p(a_2),\,\dots,\,v_p(a_N)\},
\qquad
d_p := \gcd\bigl(\mathcal E_p^{(0)}\bigr).
\]
By the lemma, $d_p$ is invariant throughout the whole process.

When the process ends, part (a) tells us that the board contains exactly one number $M>1$ together with $N-1$ ones.  Hence
\[
\mathcal E_p^{\text{(final)}} = \{\,v_p(M),\,\underbrace{0,\,0,\,\dots,\,0}_{N-1\text{ times}}\,\}.
\]
The gcd of a multiset consisting of a number $v$ and several zeros is $v$ itself (because $\gcd(v,0,\dots,0)=v$; every divisor of $v$ divides $0$, and the largest positive divisor of $v$ is $v$ itself).  Therefore
\[
v_p(M) = \gcd\bigl(\mathcal E_p^{\text{(final)}}\bigr) = d_p \qquad\text{for every prime } p.
\]

Consequently
\[
M = \prod_{p\text{ prime}} p^{\,d_p},
\qquad\text{where}\qquad
d_p = \gcd\bigl(v_p(a_1),v_p(a_2),\dots,v_p(a_N)\bigr).
\]
The right‑hand side depends only on the initial $N$ integers $a_1,\dots,a_N$, not on the particular sequence of moves chosen by Confucius.  This completes part (b).

---
*Remark.*  The number $2026$ plays no special role; the same statements hold for any $N\ge 2$ initial integers greater than $1$.
