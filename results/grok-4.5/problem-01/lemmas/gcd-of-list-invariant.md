# Lemma: gcd of the multiset of p-valuations is invariant

## Statement
Fix a prime $p$. Suppose a multiset $S=\{a_1,\dots,a_k\}$ of non-negative integers is modified by selecting two entries $\alpha,\beta$ and replacing them by $\min(\alpha,\beta)$ and $|\alpha-\beta|$. Then the gcd of all elements of the multiset is unchanged. Consequently, if the board is modified by a legal move of Confucius, for every prime $p$ the quantity
\[
g_p:=\gcd\bigl(v_p(x):x\text{ currently on the board}\bigr)
\]
is invariant (where we adopt the convention $\gcd(\emptyset)=0$ and $\gcd(0,a)=a$).

## Proof
It is elementary that $\gcd(\alpha,\beta)=\gcd\bigl(\min(\alpha,\beta),|\alpha-\beta|\bigr)$. Replacing two numbers by a pair with the same pairwise gcd does not change the gcd of the whole multiset: if $d$ divides every element of $S$, then $d$ divides both new numbers, so $d$ still divides every element of the new multiset; conversely any common divisor of the new multiset divides the two new numbers and therefore divides their linear combinations $\alpha$ and $\beta$ (since $\alpha=\min+\text{diff}$ or in the other ordering), hence divides every old element.

A legal move of Confucius replaces two board entries $m,n>1$ by $g=\gcd(m,n)$ and $\ell=\operatorname{lcm}(m,n)/\gcd(m,n)$. By the valuation-move lemma this replaces the corresponding pair of $p$-valuations exactly by the pair considered above (or leaves them unchanged for primes not dividing $mn$). Hence $g_p$ is invariant under every legal move.
