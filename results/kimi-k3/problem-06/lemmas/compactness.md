# Lemma: the killing property (K′) and the Compactness Theorem

Setup: $(a_n)_{n\ge1}$ is the sequence of the problem; $S_\infty:=\{m\ge1:\gcd(m,a_i)>1\ \forall i\ge1\}$; $\mathcal M$ = minimal elements of $S_\infty$ under divisibility; $\mathcal C=\{\mathrm{supp}(h):h\in\mathcal M\}$, an antichain of finite sets of primes (see `sequence-framework.md`, which also proves: **(3.1)** $\mathcal C$ is pairwise intersecting; **(3.2)** every *finite* minimal transversal of $\mathcal C$ belongs to $\mathcal C$). For a finite set of primes $s$, $\pi(s):=\prod_{p\in s}p$.

## Lemma K (killing)

Every integer $x>a_1$ with $x\notin S_\infty$ is coprime to some term $a_i<x$.

**Proof.** By Lemma 1 of `sequence-framework.md`, $x$ is not a term; since the terms increase to infinity and $x>a_1$, there is $n$ with $a_n<x<a_{n+1}$. If $\gcd(x,a_i)>1$ for all $i\le n$ then $x\in S_n$ and $x>a_n$, so the greedy minimality of $a_{n+1}$ gives $a_{n+1}\le x$ — contradiction. So $\gcd(x,a_i)=1$ for some $i\le n$, and $a_i\le a_n<x$. $\blacksquare$

## Lemma K′ (killing for finite sets)

Let $F$ be a finite set of primes with $\pi(F)>a_1$ such that $F$ contains no member of $\mathcal C$. Then there exists $t'\in\mathcal C$ with $t'\cap F=\emptyset$ and $\pi(t')<\pi(F)$.

**Proof.** If $\pi(F)\in S_\infty$, some $h=\pi(t)\in\mathcal M$ divides $\pi(F)$ (smallest divisor of $\pi(F)$ lying in $S_\infty$), so $t\subseteq F$ is a member inside $F$ — excluded. Hence $\pi(F)\notin S_\infty$ and $\pi(F)>a_1$. By Lemma K there is a term $a_i<\pi(F)$ coprime to $\pi(F)$. Some $h'=\pi(t')\in\mathcal M$ divides $a_i$; then $t'\in\mathcal C$, $\pi(t')\le a_i<\pi(F)$, and $\gcd(\pi(t'),\pi(F))\mid\gcd(a_i,\pi(F))=1$, i.e. $t'\cap F=\emptyset$. $\blacksquare$

## Compactness Theorem

*Every transversal of $\mathcal C$ contains a finite transversal; equivalently, $\mathcal C$ has no infinite minimal transversal.*

**Proof.** The two forms are equivalent via the following explicit construction. Given a transversal $W$, enumerate its elements as $w_1,w_2,\dots$ ($W$ is a set of primes, hence countable). Put $W_0:=W$ and for $n\ge1$ let $W_n:=W_{n-1}\setminus\{w_n\}$ if this is still a transversal of $\mathcal C$, else $W_n:=W_{n-1}$. Each $W_n$ is a transversal by induction. Let $T:=\bigcap_n W_n$. For each $e\in\mathcal C$, the sets $e\cap W_n$ are nonempty, decreasing, and contained in the finite set $e$, so they stabilize; hence $e\cap T=\bigcap_n(e\cap W_n)\neq\emptyset$, i.e. $T$ is a transversal $\subseteq W$. It is minimal: if $w=w_n\in T$, then $W_{n-1}\setminus\{w\}$ is not a transversal, so some $e_w\in\mathcal C$ is disjoint from $W_{n-1}\setminus\{w\}$ while meeting $W_{n-1}$; thus $e_w\cap W_{n-1}=\{w\}$, and since $T\subseteq W_{n-1}$ and $w\in T$,
$$e_w\cap T=\{w\}\qquad(\text{private member for }w).$$
If $W$ contained no finite transversal, $T$ would be an infinite minimal transversal with private members. We prove this impossible.

**Descent.** Fix $w\in T$. Build members $M_0,M_1,\dots$ of $\mathcal C$ through $w$: $M_0:=e_w$. Given $M_j\ni w$: if $\pi(M_j)\le a_1w$ stop; else apply Lemma K′ to $F:=M_j\setminus\{w\}$ — it contains no member (a member $e\subseteq F\subsetneq M_j$ contradicts the antichain property) and $\pi(F)=\pi(M_j)/w>a_1$ — obtaining $M_{j+1}\in\mathcal C$ disjoint from $M_j\setminus\{w\}$ with $\pi(M_{j+1})<\pi(M_j)/w$. By (3.1), $M_{j+1}\cap M_j\neq\emptyset$; being disjoint from $M_j\setminus\{w\}$ forces $w\in M_{j+1}$. Since $w\ge2$, the products strictly decrease; the process stops at $t^*_w:=M_k$ with
$$w\in t^*_w,\qquad \pi(t^*_w)\le a_1w.$$

**Pigeonhole.** Each set $t^*_w\setminus\{w\}$ has $\pi(t^*_w\setminus\{w\})\le a_1$, hence is a subset of the finite set of primes $\le a_1$: only finitely many possibilities. As $T$ is infinite, some fixed $P_0$ (with $\pi(P_0)\le a_1$) equals $t^*_w\setminus\{w\}$ for infinitely many distinct $w\in T$; pick $w_1,w_2,\dots$ among them. Then $w_j\notin P_0$ and $t^*_{w_j}=P_0\cup\{w_j\}$.

**$P_0$ is a transversal.** Let $e\in\mathcal C$. By (3.1), $e$ meets each $t^*_{w_j}=P_0\cup\{w_j\}$. If $e\cap P_0=\emptyset$ then $e\cap t^*_{w_j}\subseteq\{w_j\}$, so $w_j\in e$ for all $j$ — infinitely many distinct primes in the finite set $e$: contradiction. Hence $e\cap P_0\neq\emptyset$ for all $e\in\mathcal C$.

**Contradiction.** The finite transversal $P_0$ contains (by deleting redundant elements) a finite minimal transversal $U\subseteq P_0$; by (3.2), $U\in\mathcal C$. Since $U\subseteq P_0$ and $w_1\notin P_0$, we have $w_1\notin U$, while $w_1\in t^*_{w_1}$; hence
$$U\subsetneq P_0\cup\{w_1\}=t^*_{w_1},$$
two members of $\mathcal C$ one properly containing the other — contradicting the antichain property. $\blacksquare$

**Numerical check.** `code/check_Kprime.py`: for $a_1\in[2,44]\cup\{90,105,165,210,330,390,462,510,770,1001,1155,1925,2310\}$, (K) verified for all $x\le 40000$ and (K′) verified for ~1400–1650 random-exhaustive prime sets $F$ per case (including multi-permanent cases 105, 165, 1001, 1155, 1925). All pass.
