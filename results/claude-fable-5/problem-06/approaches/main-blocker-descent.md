# Main approach: blocker structure + geometric descent (SUCCESSFUL)

## Idea
1. **Symmetry & completeness.** All terms are pairwise non-coprime (the gcd condition is imposed against all earlier terms, and later terms are chosen compatible with all earlier ones). Greedy minimality upgrades this to an exact fixed-point description:
   $$S=\{m\ge a_1:\gcd(m,s)>1\ \forall s\in S\}.$$
2. **Transversal language.** With $P(s)$ = prime set of $s$, membership of $m\ (\ge a_1)$ in $S$ is: "$P(m)$ hits every $P(s)$", i.e. $P(m)$ is a transversal of the family $\{P(s):s\in S\}$. Every transversal contains a *minimal* transversal ("member"). Hence
   $$S=[a_1,\infty)\cap\bigcup_{Q\in\mathcal M}d_Q\mathbb Z,\qquad d_Q=\textstyle\prod_{p\in Q}p,$$
   where $\mathcal M$ = set of members. If $\mathcal M$ is **finite**, $S$ is a finite union of APs from $a_1$ on and the required $(T,L)$ exist *for all $n\ge1$* (not merely eventually).
3. **Members pairwise intersect**: realize $m=d_Qp^e,\ m'=d_{Q'}p'^{e'}\in S$ with fresh distinct primes $p,p'$; $\gcd(m,m')>1$ forces $Q\cap Q'\ne\emptyset$.
4. **Greedy gives downward witnesses**: if $m>a_1$, $m\notin S$, some $s\in S$ with $s<m$, $\gcd(s,m)=1$. (The greedy step that skipped $m$ did so because of an earlier term.)
5. **Cheap witness lemma.** For a member $Q$, $|Q|\ge2$, $t\in Q$: take $X=Q\setminus\{t\}$ and $m=\pi(X)^e$ the least power exceeding $a_1$ (so $m\le a_1\pi(X)$). Since no member $\subseteq X$ (antichain), $m\notin S$; the downward witness $s<m$ contains a member $Q'$ disjoint from $X$, with $d_{Q'}\le s<m\le a_1\pi(X)=a_1d_Q/t$; pairwise intersection forces $Q'\cap Q=\{t\}$.
6. **Descent.** If a member contains a prime $q>a_1$, iterate the cheap witness at $t=q$: products of members containing $q$ contract by the factor $a_1/q<1$ each step, yet always $\ge q$. Contradiction. (Singleton members are handled separately: then $\mathcal M=\{\{p\}\}$ and $p\mid a_1$.)
7. Hence every member $\subseteq\{p\le a_1\}$: $\mathcal M$ finite. Take $L=M=\prod_{p\le a_1}p$ and $T$ = number of residues $r$ mod $M$ divisible by some $d_Q$; a block-counting argument gives $a_{n+T}=a_n+L$ for **all** $n$.

## Status
Complete; full details in `current.md`. Numerically verified by `code/verify.py`.
