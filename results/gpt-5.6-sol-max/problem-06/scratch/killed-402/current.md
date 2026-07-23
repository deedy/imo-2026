# imo-2026-06 — tracking file
## Status
unsolved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- **Infinite admissible set / self-dual hypergraph:** Define $S$ to be the integers non-coprime to every sequence term. The greedy sequence is exactly the increasing enumeration of $S$ from $a_1$, and $S$ is closed upward under divisibility. Moreover, its finite prime-support family is self-blocking: a finite set of primes belongs exactly when it meets every member. If this self-blocking family has a finite prime core, then $S$ is periodic and the result follows. Establishing that finite-core lemma is the current main task.
- **Finite-stage stabilization:** Each finite-stage admissible set is periodic; attempted to show only finitely many constraints are essential. This appears equivalent to a compactness/blocker lemma and has not yet been completed.

## Current best
The problem reduces to proving that a self-blocking upward family of finite prime sets is controlled by finitely many primes (or otherwise proving periodicity). Once periodicity of the ultimate admissible set $S$ is established, the sequence, being its full increasing enumeration beginning at $a_1$, satisfies the requested translation relation from the very first term.

## Full proof
A complete proof has not yet been obtained.
