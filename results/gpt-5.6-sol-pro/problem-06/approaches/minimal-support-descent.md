# Minimal-support descent and bounded-rank compactness

## Idea
Pass from accepted integers to their prime supports. The resulting up-family $\mathcal F$ is self-dual: a finite prime set belongs to $\mathcal F$ exactly when it meets every member of $\mathcal F$. Let $\mathcal C$ be its inclusion-minimal members.

Give a prime set the multiplicative weight
\[
w(S)=\prod_{p\in S}p.
\]
If $S\notin\mathcal F$ and $w(S)\ge a_1$, then the squarefree integer $w(S)$ was rejected, and a smaller accepted coprime witness supplies $H\in\mathcal C$ disjoint from $S$ with $w(H)<w(S)$.

For $E\in\mathcal C$ and $p\in E$, apply this to $S=E\setminus\{p\}$ whenever its weight is at least $a_1$. Minimality gives $S\notin\mathcal F$. The resulting $H\in\mathcal C$ is disjoint from $S$; as $E,H$ intersect, it contains $p$, and $w(H)<w(S)$. Iteration strictly decreases weight while retaining $p$, and terminates at an edge $D$ with $w(D\setminus\{p\})<a_1$. Such terminal edges have uniformly bounded cardinality.

A bounded-cardinality subfamily of a self-dual intersecting clutter must be finite. Otherwise the infinite sunflower lemma gives infinitely many edges with common root $R$. Every edge must meet $R$ (a finite edge cannot meet infinitely many disjoint petals), so $R$ is a transversal. Self-duality then makes $R$ contain an edge, contradicting the antichain property because $R$ is contained in every sunflower edge.

Thus the terminal edges are finite in number. Every prime occurring in $\mathcal C$ occurs in one of them, so only finitely many primes occur in $\mathcal C$. Hence $\mathcal C$ itself is finite, and acceptance is periodic modulo the product of these finitely many primes.

## Status
Solved. This is the core proof.
