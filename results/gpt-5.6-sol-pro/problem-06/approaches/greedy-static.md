# Greedy scan and static family

## Idea
View every integer $m>a_1$ in increasing order and accept it iff it has gcd greater than $1$ with every previously accepted integer. The accepted integers are exactly the terms $a_n$.

If $A$ is the final accepted set, then
\[
m\in A\quad\Longleftrightarrow\quad \gcd(m,a)>1\text{ for every }a\in A
\]
for $m\ge a_1$: the forward implication uses pairwise compatibility, while the reverse implication uses compatibility with all earlier accepted values at the time $m$ was scanned.

In prime-support language, the supports occurring in $A$ form an upward, pairwise-intersecting, self-transversal family of finite sets. Also every support meets the finite set of primes dividing $a_1$.

## Status
Useful structural reformulation, but not by itself yet sufficient to prove finite-prime dependence or periodicity. The numerical condition that a rejected number has a *smaller* accepted witness may be essential.
