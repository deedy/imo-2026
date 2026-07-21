# imo-2026-06 — tracking file

## Status
partial

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Computational exploration of many starting values (a1 = 2,3,4,5,6,7,8,9,10,11,14,15,21,25,27,30,33,35,45,49,75,105,...)
  - When a1 is a prime power p^k, the sequence becomes all multiples of p from a1 onwards: T=1, L=p.
  - When a1 is even (or shares factor 2 early), often collapses to all even numbers: T=1, L=2.
  - When a1=15=3*5: period T=8, L=30=2*3*5, residues {0,6,10,12,15,18,20,24} mod 30.
  - When a1=35=5*7: period T=34, L=210=2*3*5*7.
  - Pattern: finitely many "essential" primes seem to determine an eventual modulus L = product of them, and the set of admissible residues is closed under +L.
- Key observation: a number m is a candidate for future terms iff gcd(m, a_i)>1 for all previous a_i. Equivalently, for every previous a_i, m shares a prime factor with a_i.
- Let P_n be the set of all primes dividing at least one of a_1,...,a_n. Then the condition is stronger than "m shares a prime with the product"; m must hit each a_i individually.
- New primes keep appearing (infinitely many, by computational evidence), but they appear as "optional" factors on numbers already forced by the finite set of early primes.
- Conjecture: there is a finite set of primes S (the "core" primes that appear early and cover the sequence) such that L = prod(S) (or lcm of early terms), and eventually the sequence consists exactly of all integers > some point that are divisible by at least one prime from each of certain covering sets — actually more structured: the admissible set becomes a finite union of arithmetic progressions with difference L, and the sequence enumerates them in order.

## Current best
Empirically the sequence is always eventually periodic in the strong sense a_{n+T}=a_n+L. The core idea is that only finitely many primes are "necessary" for the covering condition; later primes appear but don't restrict the admissible residue classes mod L further. Need a rigorous proof that (1) only finitely many primes can ever be forced as new restrictions, or more carefully: the set A of all positive integers m that share a factor with every a_i (i.e., admissible w.r.t. the whole infinite sequence) is a finite union of APs, and the sequence is exactly the increasing enumeration of A ∩ (a1 + ℕ) or similar — but wait, that's circular because A depends on the sequence. Better: track the admissible set after n steps, show it stabilizes in terms of residue classes after finitely many steps.

## Full proof
(Not yet complete.)
