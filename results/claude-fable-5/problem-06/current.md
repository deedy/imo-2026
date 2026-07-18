# imo-2026-06 — tracking file

## Status
solved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- **Simulation / pattern finding** (`code/verify.py`): for many seeds $a_1$ the set $S=\{a_n\}$ is exactly $[a_1,\infty)\cap\bigcup_Q d_Q\mathbb Z$ for a finite family of squarefree moduli $d_Q$ (e.g. $a_1=15$: moduli $6,10,15$; $a_1=385$: moduli $30,66,14,418,231,399,385$), and $a_{n+T}=a_n+L$ holds from $n=1$. This suggested the exact structural characterization.
- **Self-consistency + blocker (hypergraph transversal) reduction**: proved $S=\{m\ge a_1:\gcd(m,s)>1\ \forall s\in S\}$ and hence $S=[a_1,\infty)\cap\bigcup_{Q\in\mathcal M}d_Q\mathbb Z$ where $\mathcal M$ is the set of minimal transversals of the family of prime-divisor sets of elements of $S$. Reduced the problem to: $\mathcal M$ is finite.
- **Dead end — pure set-system arguments** (`approaches/abstract-clutter-dead-end.md`): tried to prove finiteness of $\mathcal M$ from "self-blocking clutter" axioms alone (pairwise intersecting antichain in which every finite transversal contains a member). Found an explicit **infinite** self-blocking clutter of finite sets ($U_k(u)=\{u_1,\dots,u_k,x_{k+1},y_{k+1}\}$, $u_i\in\{x_i,y_i\}$), so the greedy ("smallest next term") property must be used quantitatively, not just the fixed-point property of $S$.
- **Successful approach** (`approaches/main-blocker-descent.md`): from greediness, every non-element of $S$ has a *smaller* coprime witness in $S$. Applied to $m=\pi(Q\setminus\{t\})^e$ this yields a "cheap witness" member $Q'$ with $Q'\cap Q=\{t\}$ and $d_{Q'}<a_1 d_Q/t$. Iterating at a fixed prime $t=q>a_1$ gives a geometric descent $d\mapsto (a_1/q)d$ of member products, an impossibility; hence all primes occurring in members are $\le a_1$, so $\mathcal M$ is finite and $S$ is a finite union of arithmetic progressions from $a_1$ on. Periodicity (from $n=1$!) follows at once.

## Current best
Complete proof. With $\mathcal M$ the (finite, as proved) set of minimal transversals of $\{P(s):s\in S\}$, one may take $L=M:=\prod_{p\le a_1,\ p\text{ prime}}p$ and $T=\#\{r\in\{0,\dots,M-1\}:\ \exists Q\in\mathcal M,\ d_Q\mid r\}\ (\ge 1)$; then $a_{n+T}=a_n+L$ for **every** $n\ge1$. Verified numerically for ~70 seeds (all $2\le a_1\le 60$ and assorted larger ones, ranges up to $4\cdot10^5$).

## Full proof

Throughout, "prime set" means a finite set of prime numbers. For an integer $n>1$ let $P(n)$ denote the set of primes dividing $n$; it is finite and nonempty. For a prime set $X$ put
$$\pi(X):=\prod_{p\in X}p \qquad (\pi(\emptyset)=1).$$
Note that for an integer $m\ge 1$ and a prime set $X$,
$$X\subseteq P(m)\iff \pi(X)\mid m, \tag{0}$$
since $\pi(X)$ is a product of distinct primes.

By its definition the sequence is strictly increasing, so all terms are distinct and $a_n\to\infty$. Let
$$S:=\{a_1,a_2,a_3,\dots\}.$$
Every element of $S$ is $\ge a_1\ge 2$.

### Step 1: Basic properties of $S$

**Lemma 1 (pairwise non-coprimality).** For all $s,s'\in S$ we have $\gcd(s,s')>1$.

*Proof.* If $s=s'$ then $\gcd(s,s')=s>1$. If $s=a_i,\ s'=a_j$ with $i<j$, then $j\ge 2$ and, by the defining property of $a_j$ (applied with $n=j-1$), $\gcd(a_j,a_i)>1$. $\square$

**Lemma 2 (completeness).** $S=\{m\in\mathbb Z:\ m\ge a_1\ \text{and}\ \gcd(m,s)>1\ \text{for all } s\in S\}.$

*Proof.* "$\subseteq$": every element of $S$ is $\ge a_1$, and Lemma 1 applies.

"$\supseteq$": Let $m\ge a_1$ satisfy $\gcd(m,s)>1$ for all $s\in S$, and suppose $m\notin S$. Then $m>a_1$. Since $a_n\to\infty$ and $a_1<m$, the index
$$n:=\max\{i\ge 1:\ a_i<m\}$$
is well defined. By maximality of $n$ we have $a_{n+1}\ge m$, and $a_{n+1}\ne m$ because $m\notin S$; hence $a_{n+1}>m$. On the other hand $m>a_n$ and $\gcd(m,a_i)>1$ for all $i\le n$ (these $a_i$ lie in $S$), so $m$ is an integer greater than $a_n$ having a nontrivial common factor with each of $a_1,\dots,a_n$. By the minimality in the definition of $a_{n+1}$, $a_{n+1}\le m$ — a contradiction. $\square$

**Lemma 3 (downward witnesses; this is where greediness enters).** If $m>a_1$ and $m\notin S$, then there exists $s\in S$ with $s<m$ and $\gcd(s,m)=1$.

*Proof.* Define $n:=\max\{i\ge1:\ a_i<m\}$ as in Lemma 2; as there, $a_n<m<a_{n+1}$. If we had $\gcd(m,a_i)>1$ for every $i\le n$, then $m$ would be a candidate in the definition of $a_{n+1}$, forcing $a_{n+1}\le m$, a contradiction. Hence $\gcd(m,a_i)=1$ for some $i\le n$, and $s:=a_i\le a_n<m$ works. $\square$

### Step 2: Transversals and the structure of $S$

**Definition.** A prime set $X$ is a *transversal* if $X\cap P(s)\ne\emptyset$ for every $s\in S$. A *member* is a transversal $Q$ such that no proper subset of $Q$ is a transversal. Let $\mathcal M$ denote the set of all members, and for $Q\in\mathcal M$ put $d_Q:=\pi(Q)$.

Two immediate remarks:

* $\emptyset$ is not a transversal (as $S\neq\emptyset$ and each $P(s)$ is disjoint from $\emptyset$); hence every member is nonempty, so $d_Q\ge 2$.
* **Every transversal $X$ contains a member.** Indeed, among the finitely many subsets of $X$ that are transversals (a nonempty collection, containing $X$), choose one, $Q$, that is inclusion-minimal in this collection. If some proper subset $Q''\subsetneq Q$ were a transversal, then $Q''\subseteq X$ would contradict the minimal choice of $Q$. So $Q$ is a member. $\;(\ast)$

**Lemma 4 (exact description of $S$).** $\mathcal M\ne\emptyset$, and for every integer $m\ge a_1$:
$$m\in S\iff d_Q\mid m\ \text{for some } Q\in\mathcal M .$$

*Proof.* "$\Leftarrow$": Suppose $d_Q\mid m$, i.e. (by (0)) $Q\subseteq P(m)$. For every $s\in S$, since $Q$ is a transversal, $\emptyset\neq Q\cap P(s)\subseteq P(m)\cap P(s)$, i.e. $\gcd(m,s)>1$. As $m\ge a_1$, Lemma 2 gives $m\in S$.

"$\Rightarrow$": Let $m\in S$. By Lemma 1, $\gcd(m,s)>1$ for every $s\in S$, i.e. $P(m)$ is a transversal. By $(\ast)$ it contains a member $Q$, and $Q\subseteq P(m)$ means $d_Q\mid m$ by (0).

Finally, $P(a_1)$ is a transversal (Lemma 1), so it contains a member; thus $\mathcal M\ne\emptyset$. $\square$

**Lemma 5 (members pairwise intersect).** For all $Q,Q'\in\mathcal M$ we have $Q\cap Q'\ne\emptyset$.

*Proof.* Choose distinct primes $p,p'\notin Q\cup Q'$ (possible: there are infinitely many primes). Choose integers $e,e'\ge1$ with $m:=d_Q\,p^{e}\ge a_1$ and $m':=d_{Q'}\,p'^{e'}\ge a_1$. By Lemma 4 ("$\Leftarrow$"), $m,m'\in S$. By Lemma 1, $\gcd(m,m')>1$, so some prime $u$ lies in
$$P(m)\cap P(m')=(Q\cup\{p\})\cap(Q'\cup\{p'\}).$$
Since $p\ne p'$, $p\notin Q'$ and $p'\notin Q$, necessarily $u\in Q\cap Q'$. $\square$

### Step 3: The key lemma — cheap witnesses

**Lemma 6 (cheap witness).** Let $Q\in\mathcal M$ with $|Q|\ge2$, and let $t\in Q$. Then there exists $Q'\in\mathcal M$ with
$$Q'\cap Q=\{t\}\qquad\text{and}\qquad d_{Q'}<\frac{a_1\,d_Q}{t}.$$

*Proof.* Put $X:=Q\setminus\{t\}$; then $X\ne\emptyset$ and $\pi(X)=d_Q/t\ge2$.

First, **no member is a subset of $X$**: if $M\in\mathcal M$ and $M\subseteq X\subsetneq Q$, then $M$ would be a transversal that is a proper subset of the member $Q$, contradicting the definition of a member.

Let $e\ge1$ be minimal with $m:=\pi(X)^{e}>a_1$. Then
$$m\le a_1\,\pi(X): \tag{1}$$
if $e=1$ this is clear since $m=\pi(X)\le a_1\pi(X)$; if $e\ge2$, minimality of $e$ gives $\pi(X)^{e-1}\le a_1$, so $m=\pi(X)^{e-1}\cdot\pi(X)\le a_1\pi(X)$.

Since $P(m)=X$ contains no member and $m>a_1$, Lemma 4 gives $m\notin S$. By Lemma 3 there exists $s\in S$ with $s<m$ and $\gcd(s,m)=1$, i.e.
$$P(s)\cap X=\emptyset. \tag{2}$$
By Lemma 4 ("$\Rightarrow$") there is a member $Q'\subseteq P(s)$. Then by (2), $Q'\cap X=\emptyset$, and by (0), $d_{Q'}\mid s$, hence using (1):
$$d_{Q'}\le s<m\le a_1\,\pi(X)=\frac{a_1\,d_Q}{t}.$$
By Lemma 5, $Q'\cap Q\ne\emptyset$; since $Q=X\cup\{t\}$ and $Q'\cap X=\emptyset$, this forces $Q'\cap Q=\{t\}$. $\square$

### Step 4: Members contain no prime exceeding $a_1$

**Lemma 7.** Every prime belonging to some member is $\le a_1$.

*Proof.* **Case A: some member is a singleton $\{p\}$.** Let $M\in\mathcal M$ be arbitrary. By Lemma 5, $M\cap\{p\}\ne\emptyset$, i.e. $p\in M$. Then $\{p\}\subseteq M$ is a transversal, and since no proper subset of the member $M$ is a transversal, $M=\{p\}$. Hence $\mathcal M=\{\{p\}\}$. Applying Lemma 4 ("$\Rightarrow$") to $a_1\in S$ gives $p\mid a_1$, so $p\le a_1$, and the lemma holds in this case.

**Case B: every member has at least two elements.** Suppose, for contradiction, that some member $Q_0$ contains a prime $q>a_1$. Define recursively, for $i\ge0$: $Q_{i+1}:=$ the member provided by Lemma 6 applied to $Q:=Q_i$ and $t:=q$. This is legitimate by induction: $q\in Q_i$ (for $i=0$ by assumption; for $i\ge1$ because $Q_i\cap Q_{i-1}=\{q\}$), and $|Q_i|\ge2$ by the Case B hypothesis. Lemma 6 yields
$$d_{Q_{i+1}}<\frac{a_1}{q}\,d_{Q_i}\qquad(i\ge0),\qquad\text{hence}\qquad d_{Q_i}<\Big(\frac{a_1}{q}\Big)^{i}d_{Q_0}\quad(i\ge1).$$
Since $q>a_1$, we have $a_1/q<1$, so $d_{Q_i}\to0$ as $i\to\infty$. But $q\in Q_i$ implies $d_{Q_i}\ge q\ge2$ for all $i$ — a contradiction. $\square$

**Lemma 8 (finiteness).** $\mathcal M$ is finite and nonempty. Moreover, with
$$M:=\prod_{\substack{p\ \mathrm{prime}\\ p\le a_1}}p\;(\ge 2,\ \text{since } a_1\ge 2),$$
every $Q\in\mathcal M$ satisfies $d_Q\mid M$.

*Proof.* By Lemma 7, every member is a subset of the finite set $\Pi:=\{p\ \text{prime}:\ p\le a_1\}$; hence $\mathcal M\subseteq 2^{\Pi}$ is finite. It is nonempty by Lemma 4. Each $d_Q$ is a product of distinct primes $\le a_1$, hence divides $M$. $\square$

### Step 5: Conclusion — exact linear periodicity

Define
$$R:=\{r\in\{0,1,\dots,M-1\}:\ d_Q\mid r\ \text{for some }Q\in\mathcal M\},\qquad T:=|R|,\qquad L:=M.$$
Since $d_Q\mid 0$ for any $Q\in\mathcal M\neq\emptyset$, we have $0\in R$, so $T\ge1$; and $L=M\ge2$. Thus $T,L$ are positive integers.

Because $d_Q\mid M$ for all $Q\in\mathcal M$ (Lemma 8), for any integer $m$ we have $d_Q\mid m\iff d_Q\mid (m\bmod M)$. Hence Lemma 4 can be restated: for every integer $m\ge a_1$,
$$m\in S\iff (m\bmod M)\in R. \tag{3}$$
In particular,
$$\text{for every integer } m\ge a_1:\qquad m\in S\iff m+M\in S. \tag{4}$$

For $k\ge0$ let $I_k:=\{a_1+kM,\ a_1+kM+1,\ \dots,\ a_1+(k+1)M-1\}$, a block of $M$ consecutive integers, all $\ge a_1$. Each $I_k$ contains exactly one integer from each residue class modulo $M$, so by (3),
$$|S\cap I_k|=|R|=T\qquad\text{for every }k\ge0. \tag{5}$$
Also $S\subseteq\bigcup_{k\ge0}I_k$, because $\min S=a_1$.

**Claim.** For every $k\ge0$, the elements of $S$ smaller than $a_1+kM$ are exactly $a_1,a_2,\dots,a_{kT}$ (so $S\cap I_k=\{a_{kT+1}<a_{kT+2}<\dots<a_{(k+1)T}\}$).

*Proof of Claim.* Induction on $k$. For $k=0$ the statement is vacuously true ($S$ has no elements below $a_1$). Assume it for $k$. The elements of $S$ smaller than $a_1+(k+1)M$ are those smaller than $a_1+kM$ — namely $a_1,\dots,a_{kT}$ — together with $S\cap I_k$, which by (5) has exactly $T$ elements, each larger than every element of $S$ below $a_1+kM$. Since $a_1<a_2<\cdots$ enumerates $S$ in increasing order, $S\cap I_k=\{a_{kT+1},\dots,a_{(k+1)T}\}$ and the elements below $a_1+(k+1)M$ are $a_1,\dots,a_{(k+1)T}$. $\square$

By (4), the map $\varphi(m):=m+M$ maps $S\cap I_k$ into $S\cap I_{k+1}$ (if $m\in S\cap I_k$ then $m\ge a_1$, so $m+M\in S$, and clearly $m+M\in I_{k+1}$), and the map $m'\mapsto m'-M$ maps $S\cap I_{k+1}$ into $S\cap I_k$ (if $m'\in S\cap I_{k+1}$ then $m'-M\ge a_1$ and $m'-M\in S$ by (4) applied to $m:=m'-M$). These maps are mutually inverse, so $\varphi:S\cap I_k\to S\cap I_{k+1}$ is a strictly increasing bijection between two $T$-element sets. A strictly increasing bijection between finite sets listed in increasing order matches the $j$-th smallest element to the $j$-th smallest element; combined with the Claim this gives
$$a_{(k+1)T+j}=a_{kT+j}+M\qquad\text{for all }k\ge0,\ 1\le j\le T.$$

Finally, let $n\ge1$ be arbitrary and write $n=kT+j$ with $k\ge0$ and $1\le j\le T$. Then
$$a_{n+T}=a_{(k+1)T+j}=a_{kT+j}+M=a_n+L .$$
Thus $a_{n+T}=a_n+L$ for every positive integer $n$, with the positive integers $T$ and $L$ defined above. $\blacksquare$

### Remarks
* The proof shows more: $S=\{m\ge a_1:\ d_Q\mid m\ \text{for some member }Q\}$ is *exactly* a finite union of arithmetic progressions intersected with $[a_1,\infty)$ — the periodic description is valid from the very first term, which is why no "eventual" qualifier is needed.
* Greediness is used exactly once, in Lemma 3 (every excluded integer has a **smaller** coprime witness in $S$); this is essential: there exist "self-consistent" sets $S$ (satisfying Lemma 2 but not Lemma 3) built from an infinite self-blocking clutter which are not unions of finitely many progressions. See `approaches/abstract-clutter-dead-end.md`.
* Numerical verification: `code/verify.py` confirms Lemmas 4, 5, 7 and the Theorem (with these exact $T,L$ up to replacing $M$ by $\mathrm{lcm}_Q d_Q$, a divisor of $M$; both work) for all $2\le a_1\le60$ and for $a_1\in\{77,91,101,105,121,125,143,169,255,385,663,1001,1155\}$, over ranges up to $4\cdot10^5$.
