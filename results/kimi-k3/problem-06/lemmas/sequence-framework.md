# Lemma: enumeration of $S_\infty$ and reduction to finitely many minimal elements

Setup: $(a_n)_{n\ge1}$ is the sequence of the problem. For $m\ge2$, $\mathrm{supp}(m)$ is the set of prime divisors of $m$; for a finite set $s$ of primes, $\pi(s):=\prod_{p\in s}p$.

## Lemma 1 (the sequence enumerates $S_\infty\cap[a_1,\infty)$)

Let $S_\infty:=\{m\ge1:\gcd(m,a_i)>1\ \forall i\ge1\}$. Then $(a_n)$ is the increasing enumeration of $S_\infty\cap[a_1,\infty)$.

**Proof.** Every term lies in $S_\infty$: for $i<j$, the defining property of $a_j$ — smallest integer $>a_{j-1}$ such that $\gcd(a_j,a_{i'})>1$ for all $i'\le j-1$ — applied with $i'=i$ gives $\gcd(a_j,a_i)>1$; and $\gcd(a_i,a_i)=a_i>1$. Hence any two terms share a factor $>1$, i.e. every term is in $S_\infty$; also $a_n\ge a_1$ since the sequence increases.

Conversely, let $x\in S_\infty$, $x\ge a_1$, and suppose $x$ is not a term. Then $x>a_1$, and since the terms form an infinite strictly increasing sequence of integers, there is a unique $n$ with $a_n<x<a_{n+1}$. By definition $a_{n+1}$ is the smallest element of $S_n:=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$ exceeding $a_n$. But $x\in S_\infty\subseteq S_n$ and $x>a_n$, so $a_{n+1}\le x$ — contradiction. $\blacksquare$

## Lemma 2 (finitely many minimal elements $\Rightarrow$ conclusion)

$S_\infty$ is closed under taking multiples; let $\mathcal M$ be the set of its minimal elements under divisibility. Every $m\in S_\infty$ is a multiple of some member of $\mathcal M$ (the smallest divisor of $m$ lying in $S_\infty$ is a minimal element), so $S_\infty=\bigcup_{h\in\mathcal M}h\mathbb Z^+$.

If $\mathcal M$ is finite, then there exist positive integers $T,L$ with $a_{n+T}=a_n+L$ for all $n\ge1$.

**Proof.** Write $\mathcal M=\{h_1,\dots,h_k\}$ and $L:=\mathrm{lcm}(h_1,\dots,h_k)\ge1$. Since each $h_i\mid L$, for every $m\ge1$: $m\in S_\infty\iff$ some $h_i\mid m\iff$ some $h_i\mid m+L\iff m+L\in S_\infty$. Let $T:=\#\bigl(S_\infty\cap[a_1,a_1+L)\bigr)$; since $a_1\in S_\infty$ (Lemma 1), $T\ge1$. The map $x\mapsto x+L$ is an order-preserving bijection $S_\infty\cap[a_1,\infty)\to S_\infty\cap[a_1+L,\infty)$; iterating, each block $B_j:=[a_1+jL,a_1+(j+1)L)$ ($j\ge0$) contains exactly $T$ elements of $S_\infty$, namely $a_1+jL,\dots,a_T+jL$. By Lemma 1, the terms in $B_j$ are exactly $a_{jT+1},\dots,a_{jT+T}$; hence $a_{jT+r}=a_r+jL$ for $1\le r\le T$, $j\ge0$. For $n=jT+r$: $a_{n+T}=a_{(j+1)T+r}=a_r+(j+1)L=a_n+L$. $\blacksquare$

## Lemma 3 (the minimal elements form an intersecting self-dual antichain)

Every $h\in\mathcal M$ is squarefree: if $p^2\mid h$ then $h/p\in S_\infty$ (its support equals $\mathrm{supp}(h)$, still meeting every $\mathrm{supp}(a_i)$), contradicting minimality. Hence $\mathcal M$ identifies with the family $\mathcal C$ of minimal (under inclusion) transversals of $\{\mathrm{supp}(a_i):i\ge1\}$, via $h=\pi(t)\leftrightarrow t$. $\mathcal C$ is an antichain of finite sets of primes.

**(3.1) Intersecting.** Any two members of $\mathcal C$ intersect.

*Proof.* Let $t\in\mathcal C$. Every multiple of $\pi(t)$ lies in $S_\infty$ (its support contains $t$, hence meets every $\mathrm{supp}(a_i)$). Choose $k$ with $\pi(t)^k\ge a_1$; by Lemma 1, $\pi(t)^k$ is a term $a_j$, and $\mathrm{supp}(a_j)=t$. Any $t'\in\mathcal C$ is a transversal of $\{\mathrm{supp}(a_i)\}$, so $t'\cap t=t'\cap\mathrm{supp}(a_j)\neq\emptyset$. $\blacksquare$

**(3.2) Self-dual.** Every minimal transversal of the family $\mathcal C$ belongs to $\mathcal C$.

*Proof.* Let $T$ be a minimal (under inclusion) transversal of $\mathcal C$. Each $a_i\in S_\infty$ is a multiple of some $\pi(t)$, $t\in\mathcal C$ (Lemma 2's descent); then $t\subseteq\mathrm{supp}(a_i)$, and $T$ meets $t$, so $T$ meets $\mathrm{supp}(a_i)$. Hence $\pi(T)\in S_\infty$, so $\pi(T)$ is a multiple of some $\pi(t')$, $t'\in\mathcal C$; i.e. $t'\subseteq T$. By (3.1), $t'$ meets every member of $\mathcal C$, so $t'$ is a transversal of $\mathcal C$ contained in $T$; minimality of $T$ gives $T=t'\in\mathcal C$. $\blacksquare$

**Corollary.** $\mathcal C$ is a family of finite subsets of the (countable) set of primes, satisfying antichain, intersecting, and self-dual. By the theorem in `lemmas/self-dual-intersecting-clutter.md`, $\mathcal C$ is finite; hence $\mathcal M$ is finite and Lemma 2 gives the desired $T,L$. $\blacksquare$
