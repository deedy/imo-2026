# imo-2026-06 — tracking file
## Status
unsolved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Began reformulating each term by its set of prime divisors: every new prime-support set must be a transversal of all earlier supports.

## Current best
The process is strictly increasing. The main target is to show that its gap sequence is periodic from the beginning, likely by reducing all future constraints to finitely many prime-divisibility conditions.

## Full proof
Not yet complete.
