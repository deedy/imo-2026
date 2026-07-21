# imo-2026-01 — tracking file

## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- Elementary potential on number of entries $>1$ and total product (for termination) — works.
- $p$-adic valuations: the gcd of the multiset of exponents for each prime is invariant under moves; this determines $M$ uniquely — works.
- Direct simulation of many instances confirms path-independence of $M$ and the closed form $M=\prod_p p^{g_p}$.

## Current best
Parts (a) and (b) are fully proved. The final $M$ equals $\prod_p p^{g_p}$ where $g_p$ is the gcd of the initial $p$-adic valuations of the $2026$ numbers (an invariant of every move). Termination follows from the lexicographic potential $(k,P)$, where $k$ is the number of entries $>1$ and $P$ is the product of all board entries.

## Full proof

We work throughout with an ordered $N$-tuple of positive integers on the blackboard, where $N=2026$; initially every entry is an integer strictly greater than $1$. For integers $m,n>1$ write
\[
g:=\gcd(m,n),\qquad \ell:=\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.
\]
A legal move consists of selecting two distinct board positions whose current entries $m$ and $n$ both exceed $1$, and replacing those two entries by $g$ and $\ell$ (in either order). The elementary identities
\begin{equation}\label{eq:prod}
mn=\gcd(m,n)\cdot\operatorname{lcm}(m,n)\qquad\text{and}\qquad g\cdot\ell=\operatorname{lcm}(m,n)=\frac{mn}{g}
\end{equation}
will be used repeatedly. In particular the product of the two new entries equals $mn/g$. Since $m,n>1$ we have $\operatorname{lcm}(m,n)\ge\max(m,n)>1$, so $g\cdot\ell>1$ and therefore at least one of $g,\ell$ is strictly greater than $1$.

### Preliminary facts on valuations

**Lemma 1** (effect of a move on valuations).  
Fix a prime $p$. Let $\alpha=v_p(m)$ and $\beta=v_p(n)$. Then
\[
v_p(g)=\min(\alpha,\beta),\qquad v_p(\ell)=\max(\alpha,\beta)-\min(\alpha,\beta).
\]
Consequently
\[
\gcd\bigl(v_p(g),v_p(\ell)\bigr)=\gcd(\alpha,\beta).
\]

*Proof.*  
By the standard formulae for the valuations of the gcd and the lcm we have $v_p(g)=\min(\alpha,\beta)$ and $v_p(\operatorname{lcm}(m,n))=\max(\alpha,\beta)$, whence
\[
v_p(\ell)=\max(\alpha,\beta)-\min(\alpha,\beta).
\]
Without loss of generality $\alpha\le\beta$. The new pair of valuations is then $(\alpha,\beta-\alpha)$, and the identity $\gcd(\alpha,\beta-\alpha)=\gcd(\alpha,\beta)$ is elementary. The case $\beta\le\alpha$ is symmetric. $\square$

**Lemma 2** (invariance of the gcd of a multiset of exponents).  
Let $S$ be a finite multiset of non-negative integers. Suppose two elements $\alpha,\beta\in S$ are replaced by $\min(\alpha,\beta)$ and $|\alpha-\beta|$. Then the greatest common divisor of all elements of the multiset remains unchanged.

*Proof.*  
Write $d=\gcd(S)$. Then $d$ divides both $\alpha$ and $\beta$, so $d$ divides both $\min(\alpha,\beta)$ and $|\alpha-\beta|$; hence $d$ still divides every element of the new multiset. Conversely, any common divisor of the new multiset divides both new numbers and therefore divides their sum (equal to $\max(\alpha,\beta)$) and their difference (equal to $|\alpha-\beta|$), and consequently divides both $\alpha$ and $\beta$. It therefore divides every element of the old multiset. $\square$

**Corollary 3.**  
For every prime $p$ define
\[
g_p:=\gcd\bigl\{v_p(x):x\text{ is currently written on the blackboard}\bigr\},
\]
adopting the conventions $\gcd(\emptyset)=0$ and $\gcd(0,a)=a$. Then every legal move leaves each $g_p$ unchanged. In particular, each $g_p$ equals the value computed from the initial board.

*Proof.*  
A legal move replaces a pair of board entries $m,n$ by $g$ and $\ell$. By Lemma 1 the corresponding pair of $p$-adic valuations is replaced by $\min(\alpha,\beta)$ and $|\alpha-\beta|$. Lemma 2 then asserts that the gcd of the full multiset of $N$ valuations is unchanged. (Primes not dividing $mn$ contribute the pair $(0,0)$, which is replaced by $(0,0)$.) $\square$

### Part (a): termination with exactly one entry greater than $1$

Let $k$ denote the number of board entries that are strictly greater than $1$, and let $P$ denote the ordinary product of all $N$ entries currently on the board. Both quantities are positive integers at the outset ($k=N\ge 2$). We claim that every legal move strictly decreases the ordered pair $(k,P)$ in the lexicographic order on $\mathbb{N}\times\mathbb{N}_{>0}$.

Consider a legal move performed on entries $m,n>1$, replaced by $g$ and $\ell$. There are three exhaustive possibilities according to the number of replacement entries that exceed $1$:

1. *Both* $g>1$ and $\ell>1$. Then $k$ is unchanged. From \eqref{eq:prod} the new product equals the old product divided by $g$. We claim $g\ge 2$. Indeed, if $g=1$ then $\ell=\operatorname{lcm}(m,n)=mn>1$, so exactly one of the two replacement numbers would exceed $1$, contradicting the standing assumption of this case. Hence $g\ge 2$ and the new product $P'$ satisfies $P'=P/g\le P/2<P$. The pair $(k,P)$ therefore decreases lexicographically.

2. *Exactly one* of $g,\ell$ exceeds $1$. Then two numbers greater than $1$ are removed and exactly one number greater than $1$ is written, so the new value of $k$ equals the old value minus $1$. The first component of the potential drops, regardless of the behaviour of $P$.

3. *Neither* $g$ nor $\ell$ exceeds $1$. This is impossible: $g\cdot\ell=\operatorname{lcm}(m,n)>1$, so at least one factor is greater than $1$.

Thus every move strictly decreases $(k,P)$ lexicographically. Since both components are positive integers (or non-negative for $k$), only finitely many successive decreases are possible. Consequently only finitely many moves can be performed.

When no further move is possible we necessarily have $k\le 1$, for otherwise two entries greater than $1$ would still be available. It remains to rule out the possibility $k=0$ at termination. Observe that a move decreases $k$ only in case 2 above, and in that case the decrease is by exactly $1$. Starting from $k=N\ge 2$, after any finite sequence of moves we therefore still have $k\ge 1$. (Equivalently: $g\cdot\ell>1$ always, so a move that begins with two entries greater than $1$ never produces two ones; the count of entries greater than $1$ drops by at most one and cannot jump from $2$ to $0$.)

Hence at termination we have exactly $k=1$: precisely one integer $M$ on the blackboard is greater than $1$, and every other entry equals $1$.

This completes the proof of part (a).

### Part (b): uniqueness of $M$

By part (a), every sequence of legal moves terminates after finitely many steps with a board consisting of a single integer $M>1$ together with $N-1$ ones. For this terminal configuration and for every prime $p$,
\[
g_p=\gcd\bigl(v_p(M),v_p(1),\dots,v_p(1)\bigr)=\gcd\bigl(v_p(M),0,\dots,0\bigr)=v_p(M).
\]
By Corollary 3 the integers $g_p$ are independent of the particular sequence of moves; they are completely determined by the initial board. Therefore, for every prime $p$, the $p$-adic valuation of the terminal number $M$ is independent of the sequence of moves. Since a positive integer is uniquely determined by its complete set of $p$-adic valuations, the value of $M$ itself does not depend on the choices of Confucius.

Explicitly, if $a_1,\dots,a_N$ denote the numbers initially written on the blackboard, then
\[
M=\prod_p p^{g_p},\qquad\text{where}\qquad g_p=\gcd\bigl(v_p(a_1),\dots,v_p(a_N)\bigr),
\]
the product running over all primes (only finitely many exponents being positive).

This completes the proof of part (b).

### Remarks
- The same argument applies verbatim to any finite number $N\ge 1$ of initial integers greater than $1$ (when $N=1$ there are no moves and $M$ is already the unique entry).
- While the hypothesis that every initial entry exceeds $1$ guarantees that moves are available at the outset whenever $N\ge 2$, the proofs of the invariance of the $g_p$ and of the shape of the terminal $M$ require only that the entries be positive integers.
