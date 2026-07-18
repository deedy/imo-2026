# Dead end: proving finiteness of $\mathcal M$ from set-system axioms alone

## What was tried
From completeness (self-consistency) of $S$ alone one derives that $\mathcal M$ (minimal transversals of $\{P(s)\}$) is a *self-blocking clutter*: a pairwise-intersecting antichain of finite sets such that **every** finite transversal of $\mathcal M$ contains a member of $\mathcal M$ (equivalently $b(\mathcal M)=\mathcal M$). Also self-witnessing: for each member $Q$ and $t\in Q$ there is a member $W$ with $W\cap Q=\{t\}$.

Hoped-for theorem: *every self-blocking clutter of finite sets is finite.* Then done without using greediness beyond completeness.

## Why it fails
An infinite sunflower argument does rule out **bounded-size** infinite self-blocking clutters: if $Q_i=C\sqcup D_i$ ($D_i\ne\emptyset$ pairwise disjoint), a witness $W$ with $W\cap Q_1=\{t\}$, $t\in D_1$, misses the core $C$, hence must meet infinitely many disjoint petals $D_j$ — impossible for a finite set.

But with unbounded member sizes the hoped-for theorem is **false**. Counterexample: ground set $\{x_i,y_i:i\ge1\}$,
$$\mathcal M_\infty=\bigl\{\,U_k(u)=\{u_1,\dots,u_k,x_{k+1},y_{k+1}\}\ :\ k\ge0,\ u_i\in\{x_i,y_i\}\,\bigr\}.$$
One checks: pairwise intersecting; antichain; and every finite transversal contains a member (take the least $i$ with $\{x_i,y_i\}\subseteq X$; transversality of $X$ against the members $U_{j-1}(u)$ forces $X\cap\{x_j,y_j\}\ne\emptyset$ for all $j<i$, producing a member inside $X$). So $\mathcal M_\infty$ is an infinite self-blocking clutter; mapping $x_i,y_i$ to primes produces a completeness-consistent set $S$ that is NOT a finite union of APs.

## Diagnosis and fix
$\mathcal M_\infty$ cannot come from a greedy sequence: for $X=\{x_1,\dots,x_K\}$, every member disjoint from $X$ has product $\gg\pi(X)$, so the integer $m$ with $P(m)=X$ has **no smaller coprime witness** — greedy would have included $m$. This quantitative use of greediness (Lemma 3 of the main proof) becomes the "cheap witness" Lemma 6 and the geometric descent (Lemma 7), which succeed. See `approaches/main-blocker-descent.md`.
