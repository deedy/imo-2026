# Lemma: the support family is self-blocking

## Statement
Let $(a_n)$ satisfy the recurrence in the problem, let $P(x)$ be the set of prime divisors of $x$, and put
\[
\mathcal G=\{P(a_n):n\ge1\},\qquad
\mathcal F=\{S:S\text{ is a finite prime set meeting every }G\in\mathcal G\}.
\]
Then $\mathcal G=\mathcal F$. Consequently, for every finite prime set $S$,
\[
S\in\mathcal F\iff S\text{ meets every member of }\mathcal F.
\]

## Proof
The recurrence implies that any two terms have gcd greater than $1$, so the members of $\mathcal G$ are pairwise intersecting. Hence $\mathcal G\subseteq\mathcal F$.

Conversely, let $S\in\mathcal F$. It is nonempty because it meets $P(a_1)$. Take $x>a_1$ with $P(x)=S$. Since $(a_n)$ is strictly increasing and infinite, choose $n$ with $a_n<x\le a_{n+1}$. The definition of $\mathcal F$ says that $x$ has gcd greater than $1$ with every $a_i$, in particular with $a_1,\ldots,a_n$. Hence $x$ is eligible after $a_n$, and the minimality of $a_{n+1}$ gives $a_{n+1}\le x$. Thus $x=a_{n+1}$ and $S=P(x)\in\mathcal G$.

Therefore $\mathcal G=\mathcal F$. Substitution into the definition of $\mathcal F$ gives the final equivalence. ∎