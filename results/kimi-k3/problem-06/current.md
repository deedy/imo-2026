# imo-2026-06 — tracking file

## Status
partial — Steps 1–3 and the reduction are complete and rigorous; the combinatorial core theorem (Step 4) has a confirmed gap at its final step (infinite minimal transversals), flagged by independent review. Closing that gap is the sole remaining task. Plan: prove the *compactness* of the transversal hypergraph of $\mathcal C$ (every transversal contains a finite transversal) using the greedy/killing structure (number theory), which is exactly what the broken step needs. Detailed strategy below; first steps of the number-theoretic argument already derived (see "Gap analysis and repair plan").

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- **Minimal-hitting-set (transversal) framework** (session 1): $S_n=\{m:\gcd(m,a_i)>1\ \forall i\le n\}$; $H_n$ = minimal transversals of $\{\mathrm{supp}(a_1),\dots,\mathrm{supp}(a_n)\}$; $a_{n+1}$ = successor of $a_n$ in $S_n$ = $\min_{h\in H_n}$ next multiple of $h$. Gap bound $a_{n+1}-a_n\le \mathrm{rad}(a_1)$; Lemmas A–D (min-value permanent exists; disjoint pairs die; pure-power terms; permanents = radicals of pure-power terms). Empirics: shrinkage of $H_n$ always stops; stable $H$ pairwise intersecting; $a_{n+T}=a_n+L$ verified for 100+ values of $a_1$.
- **Self-dual intersecting clutter** (session 2): permanents (= minimal elements of $S_\infty$) form an antichain $\mathcal C$ of finite prime-sets that is pairwise intersecting and self-dual-for-finite-transversals. Abstract theorem "antichain + intersecting + self-dual ⇒ finite" proved — BUT its proof applies self-duality to a minimal transversal of the infinite set $I\cup Z_\omega$, and in the application self-duality is only verified for FINITE transversals ($\pi(T)$ is undefined for infinite $T$). Moreover, in the relevant case (Case B at every stage) that minimal transversal is PROVABLY infinite: any finite transversal $\subseteq I\cup Z_\omega$ lies in some finite $I\cup Z_s$, which would have triggered Case A at stage $s+1$. **This is the open gap.**
- **(THIS SESSION) Repair via compactness from the killing property.** Reformulate greedy as enumeration + killing (K); derive that every transversal of $\mathcal C$ contains a finite transversal (compactness), which repairs Step 4 (equivalently proves (iii) for infinite transversals: none exist). Key derived fact (C1) below; contradiction still being assembled.

## Current best
Complete except for the compactness crux. Established rigorously (see Full proof): (1) the sequence is exactly the increasing enumeration of $S_\infty\cap[a_1,\infty)$; (2) if $S_\infty$ has finitely many minimal elements, the conclusion follows with $L=\mathrm{lcm}$ of minimals, $T$ = count per period; (3) the minimal elements are squarefree, and their supports $\mathcal C$ form an antichain of finite prime sets that is pairwise intersecting and self-dual for finite transversals; (4a) peeling process: if $\mathcal C$ is infinite, one constructs $t\in\mathcal C$, infinite $\mathcal C_I$, distinct primes $Z_\omega=\{z_1,z_2,\dots\}$ outside $t$ with $\mathcal F_s=\{e\in\mathcal C_I:e\supseteq Z_s\}$ infinite for all $s$, members $g_s$ disjoint from $I\cup Z_s$ with $z_{s+1}\in g_s$, and $I\cup Z_\omega$ a transversal of $\mathcal C$ with no finite sub-transversal. **Remaining:** show number theory (the killing property) forbids such an infinite transversal-without-finite-subtransversal.

## Gap analysis and repair plan (this session's working notes — will be folded into the proof once complete)

**Reformulation of the greedy rule.** The greedy definition is EQUIVALENT to: $(a_n)$ is the increasing enumeration of $S_\infty\cap[a_1,\infty)$ AND
$$\text{(K)}\quad \text{every integer }x\notin S_\infty,\ x>a_1,\ \text{is coprime to some term }a_i<x.$$
[Proof: greedy ⇒ enumeration (Step 1) and any $x\in(a_n,a_{n+1})$ fails the gcd condition with some $i\le n$, i.e. $\gcd(x,a_i)=1$, $a_i\le a_n<x$. Conversely, enumeration + (K): if $y\in(a_n,a_{n+1})$ had $\gcd(y,a_i)>1$ for all $i\le n$, then $y\notin S_\infty$ (enumeration is complete), so (K) gives a term $a_j<y$ coprime to $y$; $a_j<y<a_{n+1}$ forces $j\le n$ — contradiction. So the min in the greedy rule equals $a_{n+1}$.]

**Setup for the contradiction.** Suppose $\mathcal M$ (equivalently $\mathcal C$) infinite. The peeling (valid, purely combinatorial — antichain + intersecting only) yields $t\in\mathcal C$, $\emptyset\neq I\subseteq t$, $\mathcal C_I=\{e:e\cap t=I\}$ infinite, distinct primes $z_1,z_2,\dots\notin t$ with $\mathcal F_s$ infinite, $g_s\in\mathcal C$ disjoint from $I\cup Z_s$, $z_{s+1}\in g_s$, and $W:=I\cup Z_\omega$ a transversal of $\mathcal C$ such that no finite subset is a transversal. KEY NUMBER-THEORETIC FACTS:
- For finite $F\subseteq W$: $F$ contains no member of $\mathcal C$ (else that member meets... wait — if $F\supseteq e\in\mathcal C$ then since some $g$ disjoint from $F$ exists [no finite sub-transversal] we'd contradict intersecting). Hence $\pi(F)\notin S_\infty$.
- Applying (K) to $x=\pi(F)$ (large $F$): some term $a_i<\pi(F)$ is coprime to $\pi(F)$; any permanent $t'\subseteq\mathrm{supp}(a_i)$ then satisfies $t'\cap F=\emptyset$ and $\pi(t')\le a_i<\pi(F)$. Hence
$$\text{(C1)}\quad \forall\text{ finite }F\subseteq W\ (\pi(F)>a_1),\ \exists\,t'\in\mathcal C:\ t'\cap F=\emptyset,\ \pi(t')<\pi(F).$$
- Since $W$ is a transversal, each such $t'$ contains some $w\in W\setminus F$, and $w\le\pi(t')<\pi(F)$.

**Where the contradiction should come from (exploring):**
- (i) Iterating (C1) with $|F|=1$ gives, for each $w_0\in W$, $w_0>a_1$, a strictly decreasing chain $w_0>w_1>\dots>w_k$ in $W$ ending with $w_k\le a_1$. No contradiction yet, but shows $W$'s elements $>a_1$ "descend" to $\le a_1$ along permanents.
- (ii) Stronger: iterate with $F_s=\{w_0,\dots,w_s\}$: get $w_{s+1}\in W\setminus F_s$, $w_{s+1}<\prod_{i\le s}w_i$ AND a permanent $t_{s+1}\ni w_{s+1}$ disjoint from $F_s$ with $\pi(t_{s+1})<\prod F_s$. Still not a contradiction (growth condition too weak) — UNLESS combined with a lower bound on permanents' elements or with disjointness structure.
- (iii) POTENTIAL ROUTE (most promising): use (C1) to show some FIXED finite subfamily of $\mathcal C$ already blocks all of $W$... More precisely: consider $\mathcal C^{<N}:=\{t\in\mathcal C:\pi(t)<N\}$ — finite for each $N$. (C1) says: every finite $F\subseteq W$ is disjoint from some member of $\mathcal C^{<\pi(F)}$. Equivalent: the family $\{t\cap W:t\in\mathcal C\}$ is a family of subsets of $W$ with the finite intersection property w.r.t. complements... Aim: find finite $F\subseteq W$ meeting every $t\in\mathcal C$ with... hmm — actually what we need: a finite $F\subseteq W$ that IS a transversal. Compactness equivalent. Idea: order permanents by $\pi$-value; use (C1) + the extra structural fact that $t'\cap F=\emptyset$ AND $t'$ meets $W$ AND $t'$ meets every member (intersecting) to build either a decreasing $\pi$-value sequence of permanents with pairwise-disjoint... decreasing positive integers must terminate, at which point the terminal permanent's intersection with $W$ plus earlier choices gives a finite transversal. Being worked out in scratch/session3-notes.md.
- (iv) Alternative: gap bound. Previous session recorded $a_{n+1}-a_n\le\mathrm{rad}(a_1)$ (needs re-proof). If gaps are bounded by $R$, then any interval of length $R$ contains a term, so any $x\notin S_\infty$ is killed by a term in $(x-R,x)$. With $W$ as above and $\pi(F)$ growing, killing terms live in $(\pi(F)-R,\pi(F))$ — but permanents below killing terms are $<\pi(F)$ anyway. Unclear if stronger.

## Full proof (steps that are complete; the compactness lemma is being repaired)

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

### Step 3: The minimal elements form an intersecting, finite-self-dual antichain of finite sets

Every $h\in\mathcal M$ is squarefree: if $p^2\mid h$ for a prime $p$, then $h/p\in S_\infty$ (since $\mathrm{supp}(h/p)=\mathrm{supp}(h)$ still meets every $\mathrm{supp}(a_i)$), contradicting minimality. So each $h\in\mathcal M$ has the form $h=\pi(t)$ for a finite set of primes $t=\mathrm{supp}(h)$. For squarefree $h=\pi(t)$ we have $h\in S_\infty$ iff $t$ is a transversal of $\{\mathrm{supp}(a_i):i\ge1\}$, and $h$ minimal under divisibility iff $t$ is minimal under inclusion (a proper divisor of a squarefree $h$ lying in $S_\infty$ is exactly a proper sub-transversal). Hence
$$\mathcal C:=\{\mathrm{supp}(h):h\in\mathcal M\}$$
is exactly the family of minimal (under inclusion) transversals of $\{\mathrm{supp}(a_i):i\ge1\}$. It is an antichain of finite sets: if $t\subseteq t'$ are both minimal transversals, then $t=t'$.

*Claim 3.1 (intersecting).* Any two members of $\mathcal C$ intersect.

*Proof.* Let $t\in\mathcal C$. Every multiple of $\pi(t)$ lies in $S_\infty$ (its support contains $t$, hence meets every $\mathrm{supp}(a_i)$). Choose $k\ge1$ with $\pi(t)^k\ge a_1$; by Step 1, $\pi(t)^k$ is a term $a_j$, and $\mathrm{supp}(a_j)=t$. Every $t'\in\mathcal C$ is a transversal of $\{\mathrm{supp}(a_i)\}$, so $t'\cap t=t'\cap\mathrm{supp}(a_j)\neq\emptyset$. $\blacksquare$

*Claim 3.2 (self-dual for finite transversals).* Every FINITE minimal transversal of the family $\mathcal C$ belongs to $\mathcal C$.

*Proof.* Let $T$ be a FINITE minimal (under inclusion) transversal of $\mathcal C$. For each $i$, $a_i\in S_\infty$ is a multiple of some $\pi(t)$ with $t\in\mathcal C$; then $t\subseteq\mathrm{supp}(a_i)$, and $T$ meeting $t$ implies $T$ meets $\mathrm{supp}(a_i)$. Hence $\pi(T)\in S_\infty$, so $\pi(T)$ is a multiple of some $\pi(t')$ with $t'\in\mathcal C$, i.e. $t'\subseteq T$. By Claim 3.1 $t'$ meets every member of $\mathcal C$, so $t'$ is a transversal of $\mathcal C$ contained in $T$; minimality of $T$ gives $T=t'\in\mathcal C$. $\blacksquare$

### Step 4: Finiteness of $\mathcal C$ — peeling + compactness

**PART 1 (complete): peeling.** Suppose $\mathcal C$ is infinite. Fix $t\in\mathcal C$; by Claim 3.1 every member meets the finite set $t$, so $\mathcal C=\bigsqcup_{\emptyset\neq I\subseteq t}\mathcal C_I$ with $\mathcal C_I:=\{e:e\cap t=I\}$; fix $I$ with $\mathcal C_I$ infinite. Observation (b): if $g\in\mathcal C$ is disjoint from $I$, then $g$ meets every $e\in\mathcal C_I$ outside $t$ (since $g\cap e\neq\emptyset$ and $g\cap e\cap t\subseteq g\cap I=\emptyset$). Enumerate $\mathcal C$ and inductively build distinct $z_1,z_2,\dots\notin t$ with $\mathcal F_s:=\{e\in\mathcal C_I:e\supseteq Z_s\}$ infinite: at stage $s+1$, if some member is disjoint from $I\cup Z_s$, take the least-index such $g_s$; by (b), $g_s$ meets every member of the infinite $\mathcal F_s$ outside $t$; pigeonhole gives $z_{s+1}\in g_s\setminus t$ lying in infinitely many members of $\mathcal F_s$; set $\mathcal F_{s+1}:=\{e\in\mathcal F_s:z_{s+1}\in e\}$. If instead NO member is disjoint from $I\cup Z_s$, then $I\cup Z_s$ is a FINITE transversal of $\mathcal C$ — the process stops with a finite transversal.

So EITHER the process stops at a finite transversal $I\cup Z_s$ of $\mathcal C$, OR it runs forever; in the latter case $W:=I\cup Z_\omega$ is a transversal of $\mathcal C$ (proof: if $g$ were disjoint from $W$, then $g$ is eligible at every stage; the least-eligible choices $g_s$ have strictly increasing indices [shown in lemmas file], so $\mathrm{index}(g_s)\to\infty$, but all are $\le\mathrm{index}(g)$ — contradiction) with NO finite sub-transversal (any finite $F\subseteq W$ lies in some $I\cup Z_s$, and $g_s$ is disjoint from it).

**PART 2 (THE OPEN GAP): compactness.** THEOREM TO PROVE: *every transversal of $\mathcal C$ contains a finite transversal* (equivalently: no infinite transversal without finite sub-transversal exists). This must use the killing property (K) — purely set-theoretic axioms do NOT suffice (star-like configurations satisfy antichain + intersecting + finite-self-duality… [verification pending, see scratch]). Given PART 2, Step 4 concludes: in the "runs forever" case, Part 2 applied to $W$ gives a finite transversal $F\subseteq W$, contradicting the last clause of Part 1. In the "stops" case, $I\cup Z_s$ is a finite transversal; a minimal sub-transversal is finite, hence in $\mathcal C$ (Claim 3.2), and is contained in every member of the infinite $\mathcal F_s$, forcing $\mathcal F_s=\{T\}$ — contradiction. Either way $\mathcal C$ is finite, and Step 2 finishes.

**(K) and its consequence (C1)** [proved in "Gap analysis" above; to be formalized]: every $x\notin S_\infty$, $x>a_1$, is coprime to some term $<x$; applied to $x=\pi(F)$ for finite $F\subseteq W$: some permanent $t'$ has $t'\cap F=\emptyset$ and $\pi(t')<\pi(F)$.

**ASSEMBLY OF CONTRADICTION — IN PROGRESS** (see scratch/session3-notes.md).
