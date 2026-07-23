# Separated-partition lemma

## Statement
Let $I\subseteq\mathbb R$ be an interval and let $I=A\sqcup B$. If there is a number $c>0$ such that $|a-b|>c$ for every $a\in A$ and $b\in B$, then at least one of $A,B$ is empty.

## Proof
Suppose instead that $p\in A$ and $q\in B$. Choose an integer $N>|p-q|/c$ and set
\[
t_i=p+\frac{i}{N}(q-p),\qquad i=0,1,\ldots,N.
\]
Every $t_i$ lies in $I$, and consecutive terms have distance $|p-q|/N<c$. Since $t_0\in A$ and $t_N\in B$, there is an index $i$ for which $t_i$ and $t_{i+1}$ belong to different parts: otherwise all consecutive labels, and hence all labels, would agree. This cross-part pair has distance less than $c$, contradicting the hypothesis.
