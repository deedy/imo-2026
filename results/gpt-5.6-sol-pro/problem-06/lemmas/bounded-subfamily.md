# A bounded-rank subfamily of the minimal supports is finite

## Statement
Let $\mathcal C$ be the inclusion-minimal members of a self-dual finite-set family $\mathcal F$, where
\[
S\in\mathcal F\iff S\text{ meets every member of }\mathcal F.
\]
Then, for every positive integer $K$, only finitely many members of $\mathcal C$ have cardinality at most $K$.

## Proof
Suppose instead that there are infinitely many distinct $E\in\mathcal C$ with $|E|\le K$. By the infinite sunflower lemma, there are distinct $E_1,E_2,\ldots$ among them and a finite set $R$ such that $E_i\cap E_j=R$ whenever $i\ne j$. Thus the petals $E_i\setminus R$ are pairwise disjoint.

Fix any $H\in\mathcal C$. Since $\mathcal C$ is intersecting, $H$ meets every $E_i$. If $H$ did not meet $R$, it would have to contain at least one element from each of the infinitely many pairwise disjoint petals. This is impossible because $H$ is finite. Hence every $H\in\mathcal C$ meets $R$.

Every member of $\mathcal F$ contains a member of $\mathcal C$, so $R$ meets every member of $\mathcal F$. Self-duality gives $R\in\mathcal F$. Therefore $R$ contains some $H_0\in\mathcal C$. But $H_0\subseteq R\subseteq E_i$ for every $i$. Since $H_0,E_i\in\mathcal C$ and $\mathcal C$ is an antichain, this implies $H_0=E_i$ for every $i$, contradicting that the $E_i$ are distinct.
