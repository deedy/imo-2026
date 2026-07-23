# Infinite sunflower lemma

## Statement
Let $K$ be a nonnegative integer. Every infinite family of distinct finite sets, each of cardinality at most $K$, contains an infinite subfamily $E_1,E_2,\ldots$ and a finite set $R$ such that
\[
E_i\cap E_j=R\qquad(i\ne j).
\]

## Proof
We use induction on $K$. For $K=0$ there is no infinite family of distinct sets, so the assertion is vacuous.

Assume $K\ge1$. If some element $x$ belongs to infinitely many sets of the family, restrict to those sets and delete $x$ from each. The resulting sets are still distinct and have cardinality at most $K-1$. By induction, infinitely many of them form a sunflower with some root $R'$. Restoring $x$ gives a sunflower with root $R'\cup\{x\}$.

It remains to consider the case in which every element belongs to only finitely many sets of the family. We can then select infinitely many pairwise disjoint sets greedily. Indeed, after finitely many sets have been selected, their union is finite; because each element of that union belongs to only finitely many sets, only finitely many members of the original family meet the union. There is therefore another member disjoint from all sets already selected. The resulting infinite subfamily is a sunflower with empty root.
