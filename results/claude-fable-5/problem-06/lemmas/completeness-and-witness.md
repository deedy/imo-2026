# Lemmas: completeness of $S$ and downward witnesses

Let $(a_n)$ be the greedy sequence, $S=\{a_n:n\ge1\}$ (strictly increasing, $a_n\to\infty$, all terms $>1$).

## Lemma 1 (pairwise non-coprimality)
For all $s,s'\in S$: $\gcd(s,s')>1$.

*Proof.* If $s=s'$: $\gcd=s>1$. If $s=a_i$, $s'=a_j$, $i<j$: by definition $a_j$ satisfies $\gcd(a_j,a_i)>1$ for all $i<j$. $\square$

## Lemma 2 (completeness / self-consistency)
$$S=\{m\ge a_1:\ \gcd(m,s)>1\ \forall s\in S\}.$$

*Proof.* $\subseteq$: clear from Lemma 1 and $a_n\ge a_1$.

$\supseteq$: Let $m\ge a_1$ be compatible with all of $S$ and suppose $m\notin S$; then $m>a_1$. Let $n=\max\{i:a_i<m\}$ (well defined: $a_1<m$, $a_i\to\infty$). By maximality $a_{n+1}\ge m$, and $a_{n+1}\neq m$ since $m\notin S$, so $a_{n+1}>m$. But $m>a_n$ and $\gcd(m,a_i)>1$ for all $i\le n$, so minimality of $a_{n+1}$ forces $a_{n+1}\le m$ — contradiction. $\square$

## Lemma 3 (downward witness — uses greediness essentially)
If $m>a_1$ and $m\notin S$, then some $s\in S$ satisfies $s<m$ and $\gcd(s,m)=1$.

*Proof.* With $n=\max\{i:a_i<m\}$ as above, $a_n<m<a_{n+1}$. If every $i\le n$ had $\gcd(m,a_i)>1$, then $m$ would be a legal candidate exceeding $a_n$, so $a_{n+1}\le m$, contradiction. Hence some $i\le n$ gives $\gcd(a_i,m)=1$ with $a_i\le a_n<m$. $\square$
