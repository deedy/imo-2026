# Prime-divisor transversals

## Idea
Replace each integer by its finite set of prime divisors. The recursion implies that the resulting family is pairwise intersecting. A finite-blocker lemma then says that all finite sets meeting every member of this family are exactly those containing one of finitely many fixed finite sets. Translating back, the integers having gcd greater than 1 with every sequence term form a finite union of sets of multiples, hence a periodic set.

## Status
Successful.

## Details
For each \(i\), let \(P_i\) be the set of prime divisors of \(a_i\). If \(i<j\), the recursion gives \(\gcd(a_i,a_j)>1\), hence \(P_i\cap P_j\ne\varnothing\). Apply the finite-blocker lemma to \(\{P_i:i\ge1\}\). There are finite prime sets \(B_1,\ldots,B_s\) such that a finite prime set \(X\) meets every \(P_i\) iff it contains some \(B_j\). Therefore an integer \(x>1\) has gcd greater than 1 with all \(a_i\) iff it is divisible by one of \(b_j=\prod_{p\in B_j}p\). This set is periodic modulo \(M=\operatorname{lcm}(b_1,\ldots,b_s)\).

The sequence is exactly the increasing enumeration, beginning at \(a_1\), of this periodic set: a skipped integer would have been eligible at the step immediately preceding it. If there are \(K\) admissible residue classes modulo \(M\), every interval \((x,x+M]\) contains exactly \(K\) members. Hence translating a term by \(M\) advances exactly \(K\) places, so \(a_{n+K}=a_n+M\) for all \(n\).
