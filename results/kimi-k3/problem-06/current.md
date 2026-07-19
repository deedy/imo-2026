# imo-2026-06 — tracking file

## Status
solved — complete proof written below. The previous gap (Step 4 applied self-duality to a provably-infinite minimal transversal while self-duality was only proved for finite ones) is now closed by a new **Compactness Theorem** (Section "Step 4a"), proved from the greedy *killing property* (K′) via a descent + pigeonhole argument. No infinite minimal transversals can exist, so the finiteness of the permanent family $\mathcal C$ follows from the peeling argument using only *finite* self-duality. All steps verified line by line; key new number-theoretic fact (K′) double-checked numerically in `code/check_Kprime.py`.

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- **Minimal-hitting-set (transversal) framework** (session 1): $S_n=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$; permanents = minimal elements of $S_\infty$; reduction of the problem to finiteness of the set of permanents. Empirics: permanent family always finite; $a_{n+T}=a_n+L$ verified for 100+ values of $a_1$.
- **Self-dual intersecting clutter** (session 2): permanents, viewed as sets of primes, form an antichain $\mathcal C$ that is pairwise intersecting and self-dual *for finite transversals*. Abstract finiteness theorem by peeling — but its last step needed self-duality for infinite minimal transversals: **GAP** (confirmed by independent review).
- **Compactness via the killing property (THIS SESSION — successful).** The greedy rule gives a *killing property* (K′): any finite prime-set $F$ with $\pi(F)>a_1$ containing no permanent is avoided by some permanent of smaller product. Using (K′) we prove $\mathcal C$ has **no infinite minimal transversal** (descent on $\pi$ through private members, then pigeonhole on $\pi(t^*\setminus\{w\})\le a_1$, then finite self-duality gives a member strictly inside another member — contradicting the antichain property). With compactness, the peeling's "runs forever" case is impossible, and the "stops" case contradicts antichain + finite self-duality. Hence $\mathcal C$ is finite and Step 2 concludes.

## Current best
Full proof below (final). Final statement proved: with $\mathcal M$ = minimal elements of $S_\infty$ (finite by the proof), $L=\mathrm{lcm}(\mathcal M)$ and $T=\#(S_\infty\cap[a_1,a_1+L))$, one has $a_{n+T}=a_n+L$ for all $n\ge1$.

## Full proof

**Notation.** For an integer $m\ge 2$, $\mathrm{supp}(m)$ = set of prime divisors of $m$. For a finite set $s$ of primes, $\pi(s):=\prod_{p\in s}p$ (a squarefree integer; $\pi(\emptyset)=1$). A set $s$ is a *transversal* of a family $\mathcal F$ if $s\cap F\neq\emptyset$ for every $F\in\mathcal F$; a transversal is *minimal* if no proper subset is a transversal.

### Step 1: The sequence enumerates $S_\infty\cap[a_1,\infty)$

Let $S_\infty:=\{m\ge 1:\gcd(m,a_i)>1\text{ for all }i\ge 1\}$.

*Claim.* $(a_n)_{n\ge1}$ is the increasing enumeration of $S_\infty\cap[a_1,\infty)$.

*Proof.* Every term lies in $S_\infty$: for $i<j$, the defining property of $a_j$ (smallest integer $>a_{j-1}$ with $\gcd(a_j,a_{i'})>1$ for all $i'\le j-1$) applied with $i'=i$ gives $\gcd(a_j,a_i)>1$; also $\gcd(a_i,a_i)=a_i>1$. So any two terms share a factor $>1$, i.e. every term is in $S_\infty$; also $a_n\ge a_1$ as the sequence is strictly increasing.

Conversely let $x\in S_\infty$, $x\ge a_1$, and suppose $x$ is not a term. Then $x>a_1$, and since the terms form an infinite strictly increasing sequence of integers, there is a unique $n$ with $a_n<x<a_{n+1}$. By definition $a_{n+1}$ is the smallest integer $>a_n$ in $S_n:=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$. But $x\in S_\infty\subseteq S_n$ and $x>a_n$, so $a_{n+1}\le x$ — contradiction. $\blacksquare$

### Step 2: Reduction to finiteness of the minimal elements of $S_\infty$

$S_\infty$ is closed under taking multiples. Let $\mathcal M$ be the set of its minimal elements under divisibility. Every $m\in S_\infty$ is a multiple of some element of $\mathcal M$: among the divisors of $m$ lying in $S_\infty$ (a nonempty finite set) the smallest is a minimal element. Hence $S_\infty=\bigcup_{h\in\mathcal M}h\mathbb Z^+$.

*Claim.* If $\mathcal M$ is finite, the problem's conclusion holds.

*Proof.* Write $\mathcal M=\{h_1,\dots,h_k\}$ and $L:=\mathrm{lcm}(h_1,\dots,h_k)\ge 1$. Since each $h_i\mid L$, for every positive integer $m$: $m\in S_\infty\iff$ some $h_i\mid m\iff$ some $h_i\mid m+L\iff m+L\in S_\infty$. Let $T:=\#\bigl(S_\infty\cap[a_1,a_1+L)\bigr)$; since $a_1\in S_\infty$ (Step 1), $T\ge 1$. The map $x\mapsto x+L$ is an order-preserving bijection $S_\infty\cap[a_1,\infty)\to S_\infty\cap[a_1+L,\infty)$; iterating, each block $[a_1+jL,a_1+(j+1)L)$ ($j\ge0$) contains exactly $T$ elements of $S_\infty$, namely $a_1+jL,\dots,a_T+jL$. By Step 1 the terms in that block are exactly $a_{jT+1},\dots,a_{jT+T}$, so $a_{jT+r}=a_r+jL$ for $1\le r\le T$, $j\ge0$. Writing $n=jT+r$: $a_{n+T}=a_{(j+1)T+r}=a_r+(j+1)L=a_n+L$ for every $n\ge1$. $\blacksquare$

### Step 3: The minimal elements form an intersecting, finite-self-dual antichain; the killing property

Every $h\in\mathcal M$ is squarefree: if $p^2\mid h$ for a prime $p$, then $h/p\in S_\infty$ (since $\mathrm{supp}(h/p)=\mathrm{supp}(h)$ still meets every $\mathrm{supp}(a_i)$), contradicting minimality. So each $h\in\mathcal M$ has the form $h=\pi(t)$ for a finite set of primes $t=\mathrm{supp}(h)$. For squarefree $h=\pi(t)$ we have $h\in S_\infty$ iff $t$ is a transversal of $\{\mathrm{supp}(a_i):i\ge1\}$, and $h$ minimal under divisibility iff $t$ is minimal under inclusion. Hence
$$\mathcal C:=\{\mathrm{supp}(h):h\in\mathcal M\}$$
is exactly the family of minimal (under inclusion) transversals of $\{\mathrm{supp}(a_i):i\ge1\}$. It is an antichain of finite sets: if $t\subseteq t'$ are both minimal transversals, then $t=t'$.

*Claim 3.1 (intersecting).* Any two members of $\mathcal C$ intersect.

*Proof.* Let $t\in\mathcal C$. Every multiple of $\pi(t)$ lies in $S_\infty$ (its support contains $t$, hence meets every $\mathrm{supp}(a_i)$). Choose $k\ge1$ with $\pi(t)^k\ge a_1$; by Step 1, $\pi(t)^k$ is a term $a_j$, and $\mathrm{supp}(a_j)=t$. Every $t'\in\mathcal C$ is a transversal of $\{\mathrm{supp}(a_i)\}$, so $t'\cap t=t'\cap\mathrm{supp}(a_j)\neq\emptyset$. $\blacksquare$

*Claim 3.2 (self-dual for finite transversals).* Every FINITE minimal transversal of the family $\mathcal C$ belongs to $\mathcal C$.

*Proof.* Let $U$ be a FINITE minimal (under inclusion) transversal of $\mathcal C$. For each $i$, $a_i\in S_\infty$ is a multiple of some $\pi(t)$ with $t\in\mathcal C$; then $t\subseteq\mathrm{supp}(a_i)$, and $U$ meeting $t$ implies $U$ meets $\mathrm{supp}(a_i)$. Hence $\pi(U)\in S_\infty$, so $\pi(U)$ is a multiple of some $\pi(t')$ with $t'\in\mathcal C$, i.e. $t'\subseteq U$. By Claim 3.1 $t'$ meets every member of $\mathcal C$, so $t'$ is a transversal of $\mathcal C$ contained in $U$; minimality of $U$ gives $U=t'\in\mathcal C$. $\blacksquare$

*Claim 3.3 (the killing property).* **(K)** Every integer $x>a_1$ with $x\notin S_\infty$ is coprime to some term $a_i<x$.

*Proof.* By Step 1, $x$ is not a term; since the terms increase to infinity and $x>a_1$, there is $n$ with $a_n<x<a_{n+1}$. If $\gcd(x,a_i)>1$ for all $i\le n$, then $x\in S_n$ and $x>a_n$, so by the greedy minimality of $a_{n+1}$ we'd have $a_{n+1}\le x$ — contradiction. Hence $\gcd(x,a_i)=1$ for some $i\le n$, and $a_i\le a_n<x$. $\blacksquare$

*Claim 3.4 (K′ — killing property for finite sets).* Let $F$ be a finite set of primes with $\pi(F)>a_1$ such that $F$ contains no member of $\mathcal C$. Then there exists $t'\in\mathcal C$ with $t'\cap F=\emptyset$ and $\pi(t')<\pi(F)$.

*Proof.* If $\pi(F)\in S_\infty$, then by Step 2's descent some $h=\pi(t)\in\mathcal M$ divides $\pi(F)$, so $t\subseteq F$ is a member contained in $F$ — excluded. Hence $\pi(F)\notin S_\infty$, and $\pi(F)>a_1$. By (K) there is a term $a_i<\pi(F)$ with $\gcd(a_i,\pi(F))=1$. Since $a_i\in S_\infty$, some $h'=\pi(t')\in\mathcal M$ divides $a_i$ ($t'\in\mathcal C$); then $\pi(t')\le a_i<\pi(F)$, and $\gcd(\pi(t'),\pi(F))\mid\gcd(a_i,\pi(F))=1$, i.e. $t'\cap F=\emptyset$. $\blacksquare$

### Step 4a: The Compactness Theorem — no infinite minimal transversals

**Theorem.** Every transversal of $\mathcal C$ contains a finite transversal. Equivalently, $\mathcal C$ has no infinite minimal transversal.

*Proof.* We prove the first form; the equivalence is explained at the end. Let $W$ be a transversal of $\mathcal C$; we show that $W$ contains a finite transversal. If $W$ is finite there is nothing to prove, so assume $W$ infinite. Enumerate its elements as $w_1,w_2,\dots$ (possible since $W$ is a set of primes, hence countable). Put $W_0:=W$ and, for $n\ge1$,
$$W_n:=\begin{cases}W_{n-1}\setminus\{w_n\},&\text{if this is still a transversal of }\mathcal C,\\ W_{n-1},&\text{otherwise.}\end{cases}$$
Each $W_n$ is a transversal by induction. Let $T:=\bigcap_{n\ge0}W_n$. For each $e\in\mathcal C$, the sets $e\cap W_n$ are nonempty (as $W_n$ is a transversal), decreasing in $n$, and contained in the finite set $e$; hence they stabilize, and $e\cap T=\bigcap_n(e\cap W_n)\neq\emptyset$. So $T$ is a transversal contained in $W$. Moreover $T$ is minimal: if $w\in T$, say $w=w_n$, then $w$ survived stage $n$, i.e. $W_{n-1}\setminus\{w\}$ is not a transversal; so some $e_w\in\mathcal C$ is disjoint from $W_{n-1}\setminus\{w\}$, while $e_w\cap W_{n-1}\neq\emptyset$; hence $e_w\cap W_{n-1}=\{w\}$, and since $T\subseteq W_{n-1}$ and $w\in T$,
$$e_w\cap T=\{w\}\qquad(\text{a \emph{private member} for }w).$$
Now suppose, for contradiction, that $W$ contains no finite transversal. Then $T$ cannot be finite (it would itself be a finite transversal inside $W$), so $T$ is an infinite transversal in which every point has a private member. We show this is impossible. (For the equivalence stated in the theorem: an infinite minimal transversal would be a transversal containing no finite transversal, since any finite sub-transversal would contradict minimality; and the construction above produces, inside any transversal without a finite sub-transversal, an infinite minimal one.)

**Descent.** Fix $w\in T$. We construct members $M_0,M_1,\dots,M_k$ of $\mathcal C$, all containing $w$, with strictly decreasing products, ending with $\pi(M_k)\le a_1\,w$. Set $M_0:=e_w$ (the private member, $w\in M_0$). Suppose $M_j$ is constructed with $w\in M_j$. If $\pi(M_j)\le a_1w$, stop. Otherwise apply (K′) to $F:=M_j\setminus\{w\}$:
- $F$ contains no member of $\mathcal C$: a member $e\subseteq F\subsetneq M_j$ would contradict the antichain property (both $e,M_j\in\mathcal C$);
- $\pi(F)=\pi(M_j)/w>a_1$.

So (K′) yields $M_{j+1}\in\mathcal C$ disjoint from $M_j\setminus\{w\}$ with $\pi(M_{j+1})<\pi(M_j)/w$. By Claim 3.1, $M_{j+1}\cap M_j\neq\emptyset$, and the intersection is disjoint from $M_j\setminus\{w\}$; hence $w\in M_{j+1}$. Since $w\ge2$, $\pi(M_{j+1})<\pi(M_j)/2$, so the positive integers $\pi(M_j)$ strictly decrease and the process stops at some $M_k=:t^*_w$ with
$$w\in t^*_w,\qquad \pi(t^*_w)\le a_1\,w.$$

**Pigeonhole.** For each $w\in T$, the set $t^*_w\setminus\{w\}$ is a set of primes with $\pi(t^*_w\setminus\{w\})=\pi(t^*_w)/w\le a_1$; every such set is a subset of the (finite) set of primes $\le a_1$, so there are only finitely many possibilities. Since $T$ is infinite, some fixed finite set of primes $P_0$ (with $\pi(P_0)\le a_1$) satisfies
$$t^*_w\setminus\{w\}=P_0\quad\text{for infinitely many distinct }w\in T;\ \text{pick such }w_1,w_2,w_3,\dots$$
Note $w_j\notin P_0$ and $t^*_{w_j}=P_0\cup\{w_j\}$.

**Every member meets $P_0$.** Let $e\in\mathcal C$. By Claim 3.1, $e$ meets each $t^*_{w_j}=P_0\cup\{w_j\}$. If $e\cap P_0=\emptyset$, then $e\cap t^*_{w_j}=e\cap\{w_j\}$, so $w_j\in e$ for every $j=1,2,\dots$ — but the $w_j$ are infinitely many distinct primes and $e$ is finite: contradiction. Hence $e\cap P_0\neq\emptyset$ for every $e\in\mathcal C$, i.e. $P_0$ is a transversal of $\mathcal C$.

**Contradiction.** $P_0$ is a finite transversal; successively deleting redundant elements yields a minimal transversal $U\subseteq P_0$, still finite. By Claim 3.2, $U\in\mathcal C$. Now $U\subseteq P_0$ and $w_1\notin P_0$ give $w_1\notin U$, while $w_1\in t^*_{w_1}$; hence
$$U\ \subsetneq\ P_0\cup\{w_1\}=t^*_{w_1},$$
two members of $\mathcal C$, one properly containing the other — contradicting the antichain property. $\blacksquare$

### Step 4b: Finiteness of $\mathcal C$ — the peeling argument

**Theorem.** $\mathcal C$ is finite.

*Proof.* Suppose $\mathcal C$ is infinite. Fix a member $t\in\mathcal C$. By Claim 3.1 every member meets the finite set $t$, so
$$\mathcal C=\bigsqcup_{\emptyset\neq I\subseteq t}\mathcal C_I,\qquad \mathcal C_I:=\{e\in\mathcal C:e\cap t=I\},$$
a finite union; fix $I$ with $\mathcal C_I$ infinite.

*Observation (b).* If $g\in\mathcal C$ is disjoint from $I$, then $g$ meets every member of $\mathcal C_I$ at a point outside $t$: indeed $g\cap e\neq\emptyset$ (Claim 3.1) and $g\cap e\cap t\subseteq g\cap(e\cap t)=g\cap I=\emptyset$.

Fix an enumeration of the countable family $\mathcal C$. Set $Z_0:=\emptyset$ and $\mathcal F_0:=\mathcal C_I$ (infinite). For $s=0,1,2,\dots$, assuming $\mathcal F_s:=\{e\in\mathcal C_I:e\supseteq Z_s\}$ is infinite, do the following (stage $s+1$):

**Case A: no member of $\mathcal C$ is disjoint from $I\cup Z_s$.** Then $I\cup Z_s$ is a transversal of $\mathcal C$; it is finite, so deleting redundant elements yields a finite minimal transversal $U\subseteq I\cup Z_s$, and $U\in\mathcal C$ by Claim 3.2. Every $e\in\mathcal F_s$ satisfies $e\supseteq I\cup Z_s\supseteq U$; by the antichain property $e=U$. Hence $\mathcal F_s\subseteq\{U\}$, contradicting that $\mathcal F_s$ is infinite. **So Case A cannot occur.**

**Case B: some member is disjoint from $I\cup Z_s$.** Let $g_s$ be such a member of least index in the enumeration. Since $g_s\cap I=\emptyset$, observation (b) says $g_s$ meets every $e\in\mathcal F_s$ outside $t$. The set $g_s\setminus t$ is finite and $\mathcal F_s$ is infinite, so by the pigeonhole principle some point $r\in g_s\setminus t$ lies in infinitely many members of $\mathcal F_s$. Set $z_{s+1}:=r$ (note $r\notin Z_s$ since $g_s\cap Z_s=\emptyset$, and $r\notin t$) and $\mathcal F_{s+1}:=\{e\in\mathcal F_s:z_{s+1}\in e\}$, which is infinite.

Since Case A never occurs, the process runs forever and produces distinct primes $Z_\omega:=\{z_1,z_2,\dots\}$, all outside $t$.

*Claim (c).* $W:=I\cup Z_\omega$ is a transversal of $\mathcal C$ with no finite sub-transversal.

*Proof of (c).* Suppose some $g\in\mathcal C$ is disjoint from $W$. Then $g$ is disjoint from $I\cup Z_s$ for every $s$, so $g$ is eligible at every stage: $\mathrm{index}(g_s)\le\mathrm{index}(g)$ for all $s$. But $g_{s+1}$, being disjoint from $I\cup Z_{s+1}\supseteq I\cup Z_s$, was already eligible at stage $s+1$, so $\mathrm{index}(g_{s+1})\ge\mathrm{index}(g_s)$; equality would force $g_{s+1}=g_s$, impossible since $z_{s+1}\in g_s$ while $g_{s+1}\cap Z_{s+1}=\emptyset$. Hence $(\mathrm{index}(g_s))_{s\ge0}$ is a strictly increasing sequence of positive integers bounded by $\mathrm{index}(g)$ — contradiction. So $W$ is a transversal. If $F\subseteq W$ is finite, then $F\subseteq I\cup Z_s$ for some $s$, and the member $g_s$ is disjoint from $I\cup Z_s\supseteq F$; so $F$ is not a transversal. $\square$

Claim (c) contradicts the Compactness Theorem of Step 4a. Hence the assumption was false and $\mathcal C$ is finite. $\blacksquare$

### Conclusion

By Step 4b, $\mathcal M$ is finite; by Step 2, there exist positive integers $T$ and $L$ (explicitly $L=\mathrm{lcm}(\mathcal M)$, $T=\#(S_\infty\cap[a_1,a_1+L))$) with $a_{n+T}=a_n+L$ for every $n\ge1$. $\blacksquare$

## Verification status of each step
- Step 1, 2: self-contained; numerically confirmed (`code/verify_newproof.py`, `code/bruteforce_check.py`).
- Step 3: 3.1–3.2 numerically confirmed for ~85 values of $a_1$; 3.3 (K) is a direct consequence of greedy minimality; 3.4 (K′) derived from (K) + Step 2 descent — numerically confirmed in `code/check_Kprime.py`.
- Step 4a (Compactness): uses only Claims 3.1, 3.2, 3.4 + antichain; each inference checked above. The descent terminates since $\pi$ drops by a factor $\ge2$ per step; pigeonhole uses finitely many prime-sets of product $\le a_1$.
- Step 4b (peeling): Case A now uses only finite self-duality (minimal sub-transversal of a FINITE transversal is finite); Claim (c) is pure combinatorics; Compactness kills the runs-forever case. **The previously flagged gap is closed.**
