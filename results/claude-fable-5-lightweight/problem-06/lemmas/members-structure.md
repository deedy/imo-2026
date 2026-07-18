# Lemmas: transversals, members, and the structure of $S$

Notation: $P(n)$ = prime divisors of $n>1$; $\pi(X)=\prod_{p\in X}p$; for integer $m$, $X\subseteq P(m)\iff\pi(X)\mid m$ (squarefree product). A finite prime set $X$ is a **transversal** if $X\cap P(s)\ne\emptyset$ for all $s\in S$; a **member** is a transversal having no proper transversal subset; $\mathcal M$ = all members, $d_Q=\pi(Q)$.

## Facts
- $\emptyset$ is not a transversal; members are nonempty, $d_Q\ge2$.
- Every transversal $X$ contains a member: pick an inclusion-minimal transversal among the finitely many transversal subsets of $X$; its proper subsets are subsets of $X$, hence non-transversal.

## Lemma 4 (exact description of $S$)
$\mathcal M\ne\emptyset$ and for $m\ge a_1$: $m\in S\iff \exists Q\in\mathcal M:\ d_Q\mid m$.

*Proof.* ($\Leftarrow$) $Q\subseteq P(m)$ and $Q$ transversal $\Rightarrow\gcd(m,s)>1\ \forall s\in S$; completeness (Lemma 2) gives $m\in S$. ($\Rightarrow$) $m\in S\Rightarrow P(m)$ is a transversal (Lemma 1) $\Rightarrow$ contains a member. Nonemptiness: $P(a_1)$ is a transversal. $\square$

## Lemma 5 (members pairwise intersect)
$Q,Q'\in\mathcal M\Rightarrow Q\cap Q'\ne\emptyset$.

*Proof.* Pick distinct primes $p,p'\notin Q\cup Q'$ and $e,e'\ge1$ with $m=d_Qp^e\ge a_1$, $m'=d_{Q'}p'^{e'}\ge a_1$. By Lemma 4 both lie in $S$; by Lemma 1 they share a prime $u\in(Q\cup\{p\})\cap(Q'\cup\{p'\})$, and $u\notin\{p,p'\}$, so $u\in Q\cap Q'$. $\square$
