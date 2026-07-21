# imo-2026-06 — tracking file

## Status
partial — developing rigorous proof

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$.

## Approaches tried
- Computational exploration: sequences appear to be eventually periodic with constant difference; observed two regimes (arithmetic progression when a single prime dominates, or periodic sequence with period >1 governed by a finite "core" set of primes).
- Minimal hitting set / transversal hypergraph approach: each term's prime set must intersect all previous prime sets; the sequence is exactly the sorted list of numbers whose prime set contains one of the minimal transversals of the infinite family.
- The set of "good" numbers (having gcd>1 with all terms) is closed under taking multiples; the primitive minimal good numbers correspond to minimal transversals.
- Conjecture: There are only finitely many primitive good numbers; they involve only primes from the first few terms. The sequence is the set of all multiples of these primitive numbers, hence periodic.

## Current best
We are constructing a rigorous proof based on the following outline:

1. Let $P(x)$ be the set of prime divisors of $x$. The condition $\gcd(a_{n+1},a_i)>1$ for all $i\le n$ means $P(a_{n+1})\cap P(a_i)\ne\varnothing$ for all $i\le n$.
2. Define the family $\mathcal{F}=\{P(a_n):n\ge 1\}$. A number $x>1$ is "good" iff $P(x)$ is a transversal of $\mathcal{F}$ (i.e., $P(x)\cap E\ne\varnothing$ for every $E\in\mathcal{F}$).
3. The sequence $(a_n)$ consists exactly of all good numbers $\ge a_1$ in increasing order. (Because each $a_n$ is good, and if some good number $x$ were missing, the greedy algorithm would have picked it when the sequence passed below it.)
4. Let $\mathcal{T}$ be the family of minimal transversals of $\mathcal{F}$ (with respect to inclusion). Then a number is good iff its prime set contains some member of $\mathcal{T}$.
5. Therefore the good numbers are the union over $H\in\mathcal{T}$ of the multiples of $\prod_{p\in H}p$. If $\mathcal{T}$ is finite, this is a finite union of arithmetic progressions, and the sequence is periodic.
6. **Key lemma**: $\mathcal{T}$ is finite. Moreover, all members of $\mathcal{T}$ consist of primes that appear in the first three terms of the sequence.
   - *Proof*: Let $p$ be the smallest prime divisor of $a_1$. Then $a_2=a_1+p$, and $P(a_1)\cap P(a_2)=\{p\}$.
   - If all terms are divisible by $p$, the sequence is arithmetic ($T=1$, $L=p$).
   - Otherwise, let $k\ge 3$ be the first index with $p\nmid a_k$. Then $P(a_k)$ contains a minimal transversal $H$ of $\{P(a_1),\dots,P(a_{k-1})\}$ with $p\notin H$.
   - After adding $P(a_k)$, the singleton $\{p\}$ is no longer a transversal. The new minimal transversals are subsets of $\bigcup_{i=1}^k P(a_i)$.
   - One shows that the family $\mathcal{T}$ stabilizes within at most one more step, and that no prime first appearing after $a_k$ can enter any minimal transversal (because such a prime would be redundant—the new term already contains an old minimal transversal hitting all earlier edges).
   - Hence $\mathcal{T}$ is a finite family of subsets of the finite set $\bigcup_{i=1}^{k+1} P(a_i)$.
7. With $\mathcal{T}$ finite, let $M=\operatorname{lcm}\{\prod_{p\in H}p : H\in\mathcal{T}\}$. Then the set of good numbers is a union of residue classes modulo $M$. Let $T$ be the number of good residues modulo $M$ that are $\ge a_1$ in each block? Actually, since the good numbers are exactly the numbers $\ge a_1$ that are $\equiv r\pmod M$ for some residue $r$ in a fixed set $R$, the sorted list satisfies $a_{n+T}=a_n+M$, where $T$ is the number of good residues in a complete system modulo $M$. (We need to check that the density is constant from the start; this holds if $a_1$ itself is the smallest good number, which is true because all smaller numbers are either $\le 1$ or coprime to $a_1$? Actually numbers between $1$ and $a_1$ might be good; but the sequence starts at $a_1$, and the periodicity is checked from $n=1$. We can adjust $T$ and $L$ accordingly.)

We still need to complete the details of step 6 (stabilization of minimal transversals) and step 7 (deriving exact periodicity from the start).

## Full proof
(To be written after completing the rigorous arguments.)
