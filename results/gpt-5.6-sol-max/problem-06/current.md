# imo-2026-06 — tracking file

## Status
partial

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Recast the condition using prime-divisor sets. Define $S_n=\{x>1:\gcd(x,a_i)>1\text{ for all }i\le n\}$. Then $S_{n+1}\subseteq S_n$, and $a_{n+1}$ is the least member of $S_n$ above $a_n$.
- Identified a sufficient stabilization criterion: if $S_N$ is pairwise non-coprime, then every later term lies in $S_N$ and imposes no new restriction on it, so $S_n=S_N$ thereafter. The sequence is then the increasing enumeration, starting with $a_1$, of a periodic set of integers.
- Established the bounded-gap observation: every multiple of $a_1$ belongs to every $S_n$, hence $1\le a_{n+1}-a_n\le a_1$.
- Explored finite prime supports and computed examples. For $a_1=15$, the sequence starts $15,18,20,24,30,36,40,42,45,48,50,54,60,\ldots$ and has $(T,L)=(8,30)$. After the first three supports $\{3,5\},\{2,3\},\{2,5\}$, the stable admissible set is the set of numbers divisible by at least two of $2,3,5$.
- The simple hope that a stable admissible set must be a single divisibility class is false; the $a_1=15$ example shows that a finite union of classes is needed.

## Current best
It remains to prove finite stabilization. The problem has been reduced to a combinatorial/arithmetic assertion about the descending admissible sets $S_n$. Each $S_n$ is periodic (its membership depends only on divisibility by the finitely many primes occurring in $a_1,\dots,a_n$), but new primes may enter later terms. A likely route is to use the bounded gaps together with the fact that every term has a prime factor from the fixed finite set $P(a_1)$, or to formulate the process as successively adjoining hyperedges and prove that it reaches a pairwise-intersecting blocker after finitely many steps. Once stabilization is proved, periodicity of the sequence, including the identity from $n=1$, can be derived by choosing a common period divisible by all relevant primes and checking the counting shift.

## Full proof
Not yet complete. Established pieces are as follows.

Let
\[
S_n=\{x>1:\gcd(x,a_i)>1\quad(1\le i\le n)\}.
\]
Every multiple of $a_1$ lies in $S_n$, since each $a_i$ has gcd greater than $1$ with $a_1$. Thus the recurrence is always defined and
\[
a_n<a_{n+1}\le a_n+a_1.
\]
If for some $N$ every two members of $S_N$ have gcd greater than $1$, then all future terms belong to $S_N$. Each such term is non-coprime to every member of $S_N$, so adding it as a constraint does not shrink $S_N$. Hence $S_n=S_N$ for all $n\ge N$, and the recurrence successively lists every member of $S_N$ above the current term. Since $S_N$ is defined by finitely many gcd conditions, it is periodic modulo the product of the finitely many primes dividing $a_1\cdots a_N$. This gives a constant index shift under translation by that modulus. The remaining issue is to prove that such an $N$ exists and then make the all-$n$ indexing argument fully explicit.
