# imo-2026-06 — tracking file

## Status
solved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- **Minimal-hitting-set (transversal) framework** (previous session): $S_n=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$; $H_n$ = minimal transversals of $\{\mathrm{supp}(a_1),\dots,\mathrm{supp}(a_n)\}$; $a_{n+1}$ = successor of $a_n$ in $S_n$ = $\min_{h\in H_n}$ next multiple of $h$. Gap bound $a_{n+1}-a_n\le \mathrm{rad}(a_1)$; Lemmas A–D (min-value permanent exists; disjoint pairs die; pure-power terms; permanents = radicals of pure-power terms). Empirics: shrinkage of $H_n$ always stops; stable $H$ pairwise intersecting; $a_{n+T}=a_n+L$ verified for 100+ values of $a_1$.
- **(THIS SESSION) Self-dual intersecting clutter — complete resolution.** The permanents (= minimal elements of $S_\infty$) form a family $\mathcal C$ of finite prime-sets that is (i) an antichain, (ii) pairwise intersecting, (iii) self-dual: every minimal transversal of $\mathcal C$ is a member of $\mathcal C$. Then a purely combinatorial theorem (proved below) says: **any such family is finite.** Finiteness of permanents ⇒ $S_\infty$ = multiples of finitely many permanents ⇒ $S_\infty$ periodic mod $L$ ⇒ $a_{n+T}=a_n+L$. This bypasses the old "shrinkage stops" crux entirely (Lemmas A–D, gap bounds, potentials are NOT needed for the final proof — only for intuition).

## Current best
Complete proof assembled (see Full proof below). Structure: (1) the sequence is exactly the increasing enumeration of $S_\infty\cap[a_1,\infty)$; (2) if $S_\infty$ has finitely many minimal elements, conclusion follows with $L=\mathrm{lcm}$ of minimals, $T$ = count per period; (3) the minimal elements (permanents) form an antichain of finite prime sets that is pairwise intersecting and self-dual; (4) **combinatorial core theorem**: any antichain of finite sets that is intersecting and self-dual is finite — proved by an infinite-descent/peeling process (transversal-minimal $T$ inside a finite $I\cup Z_s$ would be a member properly contained in another member, contradicting the antichain property). Numerical checks of the framework and of permanents' intersecting+self-dual properties in `code/`.

## Full proof

**Notation.** For an integer $m\ge 2$, $\mathrm{supp}(m)$ = set of prime divisors of $m$. For a finite set $s$ of primes, $\pi(s):=\prod_{p\in s}p$ (a squarefree integer). A set $s$ of primes is a *transversal* of a family $\mathcal F$ of sets if $s\cap F\neq\emptyset$ for every $F\in\mathcal F$.

### Step 1: The sequence enumerates $S_\infty\cap[a_1,\infty)$

Let $S_\infty:=\{m\ge 1:\gcd(m,a_i)>1\text{ for all }i\ge 1\}$.

*Claim.* $(a_n)_{n\ge1}$ is the increasing enumeration of $S_\infty\cap[a_1,\infty)$.

*Proof.* Every term lies in $S_\infty$: for $i<j$, the defining property of $a_j$ (smallest integer $>a_{j-1}$ with $\gcd(a_j,a_{i'})>1$ for all $i'\le j-1$) applied with $i'=i$ gives $\gcd(a_j,a_i)>1$; also $\gcd(a_i,a_i)=a_i>1$. So any two terms share a factor $>1$, i.e. every term is in $S_\infty$; also $a_n\ge a_1$ as the sequence is strictly increasing.

Conversely let $x\in S_\infty$, $x\ge a_1$, and suppose $x$ is not a term. Then $x>a_1$ (else $x=a_1$ is a term), and since the terms form an infinite strictly increasing sequence of integers, there is a unique $n$ with $a_n<x<a_{n+1}$. By definition $a_{n+1}$ is the smallest integer $>a_n$ in $S_n:=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$. But $x\in S_\infty\subseteq S_n$ and $x>a_n$, so $a_{n+1}\le x$ — contradiction. $\blacksquare$

### Step 2: Reduction to finiteness of the minimal elements of $S_\infty$

$S_\infty$ is closed under taking multiples. Let $\mathcal M$ be the set of its minimal elements under divisibility. Every $m\in S_\infty$ is a multiple of some element of $\mathcal M$: among the divisors of $m$ lying in $S_\infty$ (a nonempty finite set) the smallest is a minimal element. Hence $S_\infty=\bigcup_{h\in\mathcal M}h\mathbb Z^+$.

*Claim.* If $\mathcal M$ is finite, the problem's conclusion holds.

*Proof.* Write $\mathcal M=\{h_1,\dots,h_k\}$ and $L:=\mathrm{lcm}(h_1,\dots,h_k)\ge 1$. Since each $h_i\mid L$, for every positive integer $m$: $m\in S_\infty\iff$ some $h_i\mid m\iff$ some $h_i\mid m+L\iff m+L\in S_\infty$. Let $T:=\#\bigl(S_\infty\cap[a_1,a_1+L)\bigr)$; since $a_1\in S_\infty$ (Step 1), $T\ge 1$. The map $x\mapsto x+L$ is an order-preserving bijection $S_\infty\cap[a_1,\infty)\to S_\infty\cap[a_1+L,\infty)$; iterating, each block $[a_1+jL,a_1+(j+1)L)$ ($j\ge0$) contains exactly $T$ elements of $S_\infty$, namely $a_1+jL,\dots,a_T+jL$. By Step 1 the terms in that block are exactly $a_{jT+1},\dots,a_{jT+T}$, so $a_{jT+r}=a_r+jL$ for $1\le r\le T$, $j\ge0$. Writing $n=jT+r$: $a_{n+T}=a_{(j+1)T+r}=a_r+(j+1)L=a_n+L$ for every $n\ge1$. $\blacksquare$

### Step 3: The minimal elements form an intersecting, self-dual antichain of finite sets

Every $h\in\mathcal M$ is squarefree: if $p^2\mid h$ for a prime $p$, then $h/p\in S_\infty$ (since $\mathrm{supp}(h/p)=\mathrm{supp}(h)$ still meets every $\mathrm{supp}(a_i)$), contradicting minimality. So each $h\in\mathcal M$ has the form $h=\pi(t)$ for a finite set of primes $t=\mathrm{supp}(h)$. For squarefree $h=\pi(t)$ we have $h\in S_\infty$ iff $t$ is a transversal of $\{\mathrm{supp}(a_i):i\ge1\}$, and $h$ minimal under divisibility iff $t$ is minimal under inclusion (a proper divisor of a squarefree $h$ lying in $S_\infty$ is exactly a proper sub-transversal). Hence
$$\mathcal C:=\{\mathrm{supp}(h):h\in\mathcal M\}$$
is exactly the family of minimal (under inclusion) transversals of $\{\mathrm{supp}(a_i):i\ge1\}$. It is an antichain of finite sets: if $t\subseteq t'$ are both minimal transversals, then $t=t'$.

*Claim 3.1 (intersecting).* Any two members of $\mathcal C$ intersect.

*Proof.* Let $t\in\mathcal C$. Every multiple of $\pi(t)$ lies in $S_\infty$ (its support contains $t$, hence meets every $\mathrm{supp}(a_i)$). Choose $k\ge1$ with $\pi(t)^k\ge a_1$; by Step 1, $\pi(t)^k$ is a term $a_j$, and $\mathrm{supp}(a_j)=t$. Every $t'\in\mathcal C$ is a transversal of $\{\mathrm{supp}(a_i)\}$, so $t'\cap t=t'\cap\mathrm{supp}(a_j)\neq\emptyset$. $\blacksquare$

*Claim 3.2 (self-dual).* Every minimal transversal of the family $\mathcal C$ belongs to $\mathcal C$.

*Proof.* Let $T$ be a minimal (under inclusion) transversal of $\mathcal C$. For each $i$, $a_i\in S_\infty$ is a multiple of some $\pi(t)$ with $t\in\mathcal C$; then $t\subseteq\mathrm{supp}(a_i)$, and $T$ meeting $t$ implies $T$ meets $\mathrm{supp}(a_i)$. Hence $\pi(T)\in S_\infty$, so $\pi(T)$ is a multiple of some $\pi(t')$ with $t'\in\mathcal C$, i.e. $t'\subseteq T$. By Claim 3.1 $t'$ meets every member of $\mathcal C$, so $t'$ is a transversal of $\mathcal C$ contained in $T$; minimality of $T$ gives $T=t'\in\mathcal C$. $\blacksquare$

### Step 4: Combinatorial core theorem

**Theorem.** Let $\mathcal C$ be a family of finite subsets of a countable ground set such that
(i) (antichain) no member contains another;
(ii) (intersecting) any two members intersect;
(iii) (self-dual) every minimal transversal of $\mathcal C$ is a member of $\mathcal C$.
Then $\mathcal C$ is finite.

*Proof.* Suppose $\mathcal C$ is infinite.

(a) *Every transversal $W$ of $\mathcal C$ contains a minimal transversal.* Consider transversals contained in $W$ ordered by reverse inclusion. If $(T_\alpha)$ is a chain of transversals, then $T:=\bigcap_\alpha T_\alpha$ meets every $e\in\mathcal C$: indeed $\{e\cap T_\alpha\}$ is a chain (under inclusion) of nonempty subsets of the finite set $e$; its distinct members are pairwise comparable subsets of a finite set, so there are finitely many of them, hence the chain has a least member, which is nonempty and equals $e\cap T=\bigcap_\alpha(e\cap T_\alpha)$. So chains have lower bounds; by Zorn's lemma there is a minimal transversal contained in $W$.

Fix a member $t\in\mathcal C$. By (ii) every member meets the finite set $t$, so
$$\mathcal C=\bigsqcup_{\emptyset\neq I\subseteq t}\mathcal C_I,\qquad \mathcal C_I:=\{e\in\mathcal C:e\cap t=I\},$$
a finite union; hence some $\mathcal C_I$ is infinite. Fix such an $I$.

(b) *Key observation.* If $g\in\mathcal C$ is disjoint from $I$, then $g$ meets every member of $\mathcal C_I$ at a point outside $t$: $g\cap e\neq\emptyset$ by (ii), and $g\cap e\cap t=(g\cap t)\cap(e\cap t)=(g\cap t)\cap I=\emptyset$ since $g\cap I=\emptyset$.

Fix an enumeration of the countable family $\mathcal C$. We inductively build distinct points $z_1,z_2,\dots$ outside $t$ and infinite families $\mathcal F_s=\{e\in\mathcal C_I:e\supseteq Z_s\}$, $Z_s:=\{z_1,\dots,z_s\}$, starting from $\mathcal F_0:=\mathcal C_I$.

*Stage $s+1$* ($s\ge0$), with $\mathcal F_s$ infinite.

**Case A:** no member of $\mathcal C$ is disjoint from $I\cup Z_s$. Then $I\cup Z_s$ is a transversal; by (a) it contains a minimal transversal $T$, and $T\in\mathcal C$ by (iii). Every $e\in\mathcal F_s$ satisfies $e\supseteq I\cup Z_s\supseteq T$, so by (i) $e=T$; hence $\mathcal F_s\subseteq\{T\}$, contradicting that $\mathcal F_s$ is infinite. Case A is impossible.

**Case B:** some member is disjoint from $I\cup Z_s$; let $g_s$ be the one of smallest index. Since $g_s\cap I=\emptyset$, observation (b) says $g_s$ meets every $e\in\mathcal F_s$ outside $t$; as $g_s$ is finite and $\mathcal F_s$ infinite, some point $r\in g_s\setminus t$ lies in infinitely many members of $\mathcal F_s$. Put $z_{s+1}:=r$ (note $r\notin Z_s$ as $g_s\cap Z_s=\emptyset$) and $\mathcal F_{s+1}:=\{e\in\mathcal F_s:z_{s+1}\in e\}$, which is infinite.

Thus the process runs for all $s<\omega$, producing $Z_\omega:=\{z_1,z_2,\dots\}$.

(c) *Every member of $\mathcal C$ meets $I\cup Z_\omega$.* Suppose $g$ is disjoint from $I\cup Z_\omega$; then $g$ is disjoint from $I\cup Z_s$ at every stage, hence always eligible. At stage $s+1$ the least eligible member $g_s$ receives $z_{s+1}\in g_s$, so $g_s$ is ineligible at all later stages; moreover $g_{s+1}$ was eligible at stage $s+1$ (it is disjoint from $I\cup Z_{s+1}\supseteq I\cup Z_s$), so $\mathrm{index}(g_{s+1})\ge\mathrm{index}(g_s)$, and $g_{s+1}\neq g_s$ (since $z_{s+1}\in g_s$ but $z_{s+1}\notin g_{s+1}$). Hence $\mathrm{index}(g_s)$ is strictly increasing, therefore unbounded — but $\mathrm{index}(g)\ge\mathrm{index}(g_s)$ for all $s$, contradiction.

So $I\cup Z_\omega$ is a transversal; by (a) it contains a minimal transversal $T$, and $T\in\mathcal C$ by (iii). Since $T$ is finite and $Z_\omega=\bigcup_s Z_s$, there is a finite $s$ with $T\subseteq I\cup Z_s$. The family $\mathcal F_{s+1}$ is infinite; pick $e\in\mathcal F_{s+1}$, $e\neq T$. Then $e\supseteq I\cup Z_{s+1}\supseteq I\cup Z_s\supseteq T$, so $e\supsetneq T$, contradicting (i). $\blacksquare$

### Conclusion

By Step 3 and Step 4, $\mathcal C$ (equivalently $\mathcal M$) is finite. By Step 2, there exist positive integers $T$ and $L$ with $a_{n+T}=a_n+L$ for every positive integer $n$. $\blacksquare$
