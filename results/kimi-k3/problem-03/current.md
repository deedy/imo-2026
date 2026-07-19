# imo-2026-03 — tracking file

## Status
solved

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- Modeling: claiming game with "pick any piece" — optimal play = greedy (proved below, brute-force verified). Game reduces to: LB picks a composition of $1$ into $\le n+1$ pieces, XY subdivides with $\le n$ cuts; payoff $D$ = alternating sum; LB share $=(1+D)/2$.
- Grid computation: $c_1=2/3, c_2=4/7, c_3=8/15$ ⇒ conjecture $c_n = \frac{2^n}{2^{n+1}-1}$, LB plays geometric pieces $\frac{2^{i-1}}{2^{n+1}-1}$. (Confirmed as the answer.)
- Odd-set identity: $D(M)=|\{t:N(t)\text{ odd}\}|$ (layer cake). Basis of the matching formula.
- **Matching formula** (proved below; verified code/tests2.py, 300 tests): $D(M)=\min_\mu\big(\sum_{\{x,y\}\in\mu}|x-y|+\sum_{z\text{ unmatched}}z\big)$.
- **Part A** (LB guarantee): super-increasing family (margin $\delta$, $m$ pieces), subdivided with $\le m-1$ cuts ⇒ $D\ge\delta$. Proof: matching formula + loop-augmented component graph + counting ($e\le m-1$ ⇒ tree component exists) + tree inequality ($|\sum_{i\in C}\epsilon_i a_i|\le\operatorname{cost}(C)$) + margin. Verified 1500 random trials. (Fix vs. earlier sketch: self-pairs count as *loops*, making their component cyclic; with this, the tree inequality is per-component correct.)
- NM ("some same-parent merge never increases $D$") — FALSE in general ({1,3}, cut 3→1.5+1.5: $D$ drops 2→1, only merge raises it). Induction-via-merging abandoned; matching route used instead.
- **Part B** (XY counterstrategy): parity view of cuts: bisect $x$ (=remove $x$), cancel $x>y$ (=remove $x,y$, add $x-y$), 1 cut each. Chains = nested abs values on a subset. Chain theorem: any $m$ positive reals with sum $S$ have a nonempty subset **and an ordering of it** with chain value $\le S/(2^m-1)$; proved by pigeonhole on $2^m$ subset sums + **greedy-scheduling realizability lemma** (adjacent gaps are chain-realizable). Verified n=1..4 (2000 random each) + adversarial local search (extremum = geometric family, value exactly $T_n S$); AGR checked 180 families, 0 failures.
- Dominance "min-subdiv = min-halve/cancel": false on coarse grids (grid artifacts only); irrelevant — for Part B we only need halve/cancel sequences, which are valid subdivisions.
- Independent-review audit (final session): Lemma 1.1 turn-parity fix (second player secures $\operatorname{even}(M'')$, not $\operatorname{odd}(M'')$) re-verified line-by-line for all $j$ and by exact minimax on 304 multisets (reviewer example $\{3,2,1\}$: second player gets exactly $2=\operatorname{even}(M)$); Theorem 4.2 ordering fix confirmed — the theorem produces the ordering and the strategy processes it. Four presentation patches applied (empty-multiset base case in Lemma 1.1; isolated-vertex components in Theorem 3.1; precise induction step in the sharpness remark; running-piece validity in XY's strategy).

## Current best
**Answer: $c = \dfrac{2^n}{2^{n+1}-1}$.** Proved in full below. Lower bound (LB guarantee): LB cuts into geometric pieces $\frac{2^{i-1}}{2^{n+1}-1}$ ($i=1,\dots,n+1$); any refinement by $\le n$ further cuts has alternating sum $D\ge \frac{1}{2^{n+1}-1}$ (Theorem 3.1). Upper bound (XY counterstrategy): for any LB composition, XY either bisects all pieces (if fewer than $n+1$) forcing $D=0$, or uses a sub-$T_n$ chain on some subset, suitably ordered (Theorem 4.2, via pigeonhole + realizability), to force $D\le \frac{1}{2^{n+1}-1}$. Hence LB gets exactly $\frac12\!\left(1+\frac{1}{2^{n+1}-1}\right)=\frac{2^n}{2^{n+1}-1}$ under optimal play.

## Full proof

**Setup and notation.** After all marks are made, the stick is cut into a finite multiset $M$ of positive piece lengths summing to $1$. For a multiset $M=\{p_1\ge p_2\ge\dots\ge p_m\}$ sorted in decreasing order, define the *alternating sum*
$$D(M)=p_1-p_2+p_3-p_4+\dots=\sum_{i=1}^{m}(-1)^{i+1}p_i,$$
and write $\operatorname{odd}(M)=\sum_{i\text{ odd}}p_i$, $\operatorname{even}(M)=\sum_{i\text{ even}}p_i$ for the sums of the odd- and even-indexed pieces. Note $\operatorname{odd}+\operatorname{even}=\sum M$ and $\operatorname{odd}-\operatorname{even}=D(M)\ge 0$ (since $D=(p_1-p_2)+(p_3-p_4)+\dots\ge 0$).

### 1. The claiming game

**Lemma 1.1 (value of the claiming game).** *In the claiming game played on a multiset $M$ of positive reals — two players alternately take any remaining piece, each maximising his own total — the first player can guarantee a total of at least $\operatorname{odd}(M)$, and the second player can guarantee a total of at least $\operatorname{even}(M)$. Since $\operatorname{odd}(M)+\operatorname{even}(M)=\sum M$, under optimal play the first player obtains exactly $\operatorname{odd}(M)=\frac{\sum M + D(M)}{2}$ and the second player exactly $\operatorname{even}(M)$. In particular, in the game of the problem Liu Bang, who moves first, obtains exactly $\operatorname{odd}(M)$.*

*Proof.* Induction on $m=|M|$, with the convention $\operatorname{odd}(\emptyset)=\operatorname{even}(\emptyset)=0$ (needed when $m=2$, since the inductive step passes to a multiset of size $m-2$). If $m\le1$ both claims are immediate: for $m=1$ the first player takes $p_1=\operatorname{odd}(M)$ and the second player gets $0=\operatorname{even}(M)$. Now let $m\ge 2$ and sort $M=\{p_1\ge\dots\ge p_m\}$.

*First player's guarantee.* The first player takes $p_1$. Suppose the second player then takes $p_j$ ($j\ge 2$). On the remainder $M'=M\setminus\{p_1,p_j\}$ the first player moves first, so by induction he secures at least $\operatorname{odd}(M')$ from $M'$, for a total of $p_1+\operatorname{odd}(M')$. The sorted order of $M'$ is $p_2,\dots,p_{j-1},p_{j+1},\dots,p_m$; its odd-indexed elements are the $p_i$ with $i$ even, $2\le i\le j-1$, together with the $p_i$ with $i$ odd, $i\ge j+1$. Therefore
$$\bigl(p_1+\operatorname{odd}(M')\bigr)-\operatorname{odd}(M)
=\sum_{\substack{i\ \mathrm{even}\\ 2\le i\le j-1}}p_i-\sum_{\substack{i\ \mathrm{odd}\\ 3\le i\le j}}p_i
=(p_2-p_3)+(p_4-p_5)+\dots\ge 0,$$
the right-hand side being a sum of consecutive differences, ending with $(p_{j-2}-p_{j-1})$ if $j$ is even and with $(p_{j-1}-p_j)$ if $j$ is odd (empty if $j=2$). So the first player secures at least $\operatorname{odd}(M)$ no matter what the second player does.

*Second player's guarantee.* Suppose the first player takes $p_j$. The second player takes a largest remaining piece $\ell$ ($\ell=p_1$ if $j\ge2$, $\ell=p_2$ if $j=1$). On the remainder $M''=M\setminus\{p_j,\ell\}$ it is the first player's turn, so the second player of the original game is the **second** player on $M''$; by induction he secures at least $\operatorname{even}(M'')$ from $M''$, for a total of at least $\ell+\operatorname{even}(M'')$.

If $j=1$: $M''=\{p_3,\dots,p_m\}$, whose even-indexed elements are $p_4,p_6,\dots$; hence
$$\ell+\operatorname{even}(M'')=p_2+(p_4+p_6+\dots)=\operatorname{even}(M).$$

If $j\ge2$: $M''=M\setminus\{p_1,p_j\}$ has sorted order $p_2,\dots,p_{j-1},p_{j+1},\dots,p_m$; its even-indexed elements are the $p_i$ with $i$ odd, $3\le i\le j-1$, together with the $p_i$ with $i$ even, $i\ge j+1$. Hence
$$\bigl(\ell+\operatorname{even}(M'')\bigr)-\operatorname{even}(M)
=p_1+\sum_{\substack{i\ \mathrm{odd}\\ 3\le i\le j-1}}p_i-\sum_{\substack{i\ \mathrm{even}\\ 2\le i\le j}}p_i
=(p_1-p_2)+(p_3-p_4)+\dots\ge 0,$$
a sum of consecutive differences, ending with $(p_{j-1}-p_j)$ if $j$ is even and with $(p_{j-2}-p_{j-1})$ if $j$ is odd (it reduces to $p_1-p_2$ if $j=2$). So the second player secures at least $\operatorname{even}(M)$ no matter what the first player does. $\blacksquare$

Since $\operatorname{odd}(M)+\operatorname{even}(M)=\sum M=1$, LB's share under optimal play equals $\operatorname{odd}(M)=\frac{1+D(M)}2$. Consequently the whole game is equivalent to the following one-dimensional optimization:

> **Reduction.** LB chooses a composition of $1$ into $m\le n+1$ positive parts (his $m-1\le n$ marks). XY then refines this composition with at most $n$ further cuts (each of XY's marks lies in the interior of one current piece and splits it in two; conversely every such refinement is achievable, with all marks distinct, since cut points are interior to pieces). LB's resulting share is $\frac{1+D(M)}2$, where $M$ is the final multiset of pieces.

We therefore must compute $D^*=\max_{\text{LB}}\min_{\text{XY}}D(M)$; the answer will be $c=\frac{1+D^*}2$.

### 2. Two representations of $D$

**Lemma 2.1 (odd-set identity).** *For a finite multiset $M$ of positive reals and $t\ge0$ let $N(t)=\#\{x\in M:x>t\}$. Then*
$$D(M)=\bigl|\{t\ge0:N(t)\ \text{is odd}\}\bigr|,$$
*the Lebesgue measure of the "odd set".*

*Proof.* Sort $M=\{p_1\ge\dots\ge p_m\}$ and put $p_{m+1}=0$. For $t\in[p_{i+1},p_i)$ we have $N(t)=i$ (ties give empty intervals, which do not affect the measure). Hence $|\{t:N(t)\text{ odd}\}|=\sum_{i\text{ odd}}(p_i-p_{i+1})=D(M)$. $\blacksquare$

A *matching* $\mu$ of $M$ is a collection of disjoint unordered pairs $\{x,y\}$ of elements of $M$ (elements may be left unpaired); its *cost* is
$$\operatorname{cost}(\mu)=\sum_{\{x,y\}\in\mu}|x-y|+\sum_{z\text{ unmatched}}z .$$

**Lemma 2.2 (matching formula).** $D(M)=\min_{\mu}\operatorname{cost}(\mu)$, *the minimum over all matchings of $M$.*

*Proof.* For $t\ge0$ and a matching $\mu$ let $c_\mu(t)$ be the number of pairs of $\mu$ with exactly one element $>t$, plus the number of unmatched elements $>t$. Since $|x-y|=\int_0^\infty\mathbf 1[\text{exactly one of }x,y>t]\,dt$ and $z=\int_0^\infty\mathbf 1[z>t]\,dt$, we have $\operatorname{cost}(\mu)=\int_0^\infty c_\mu(t)\,dt$. If $b(t)$ denotes the number of pairs with both elements $>t$, then $N(t)=2b(t)+c_\mu(t)$, so $c_\mu(t)\equiv N(t)\pmod 2$ and $c_\mu(t)\ge0$; in particular $c_\mu(t)\ge\mathbf 1[N(t)\text{ odd}]$ for every $t$. Integrating and using Lemma 2.1 gives $\operatorname{cost}(\mu)\ge D(M)$ for every $\mu$. Equality is attained by the *adjacent* matching: sorting $M=\{p_1\ge\dots\ge p_m\}$ and pairing $(p_1,p_2),(p_3,p_4),\dots$ gives cost $\sum_{i\text{ odd}}(p_i-p_{i+1})=D(M)$. $\blacksquare$

**Corollary 2.3 (parity cancellation).** *If $M$ contains two equal elements $x,x$, then $D(M)=D(M\setminus\{x,x\})$. Consequently, if every value in $M$ occurs with even multiplicity, then $D(M)=0$.*

*Proof.* In the decreasing ordering of $M$ the two copies of $x$ occupy two adjacent positions $j,j+1$ and contribute $(-1)^{j+1}x+(-1)^{j+2}x=0$; removing them shifts all later elements by two positions, preserving the sign of each term. $\blacksquare$

### 3. Part A: the geometric split (lower bound)

Put $T_n=\dfrac{1}{2^{n+1}-1}$. LB marks $n$ points dividing the stick into $n+1$ pieces of lengths
$$a_i=2^{\,i-1}T_n\qquad(i=1,\dots,n+1),\qquad \sum_{i=1}^{n+1}a_i=(2^{n+1}-1)T_n=1 .$$

**Definition.** Positive reals $a_1\le a_2\le\dots\le a_m$ are *super-increasing with margin $\delta>0$* if $a_1\ge\delta$ and $a_i\ge\delta+\sum_{j<i}a_j$ for every $i\ge2$.

The family above is super-increasing with margin $\delta=T_n$: indeed $a_1=T_n$ and $\sum_{j<i}a_j=(2^{i-1}-1)T_n=a_i-T_n$, so $a_i=\delta+\sum_{j<i}a_j$.

**Theorem 3.1.** *Let $a_1\le\dots\le a_m$ be super-increasing with margin $\delta$, and let $M$ be obtained from these pieces by at most $m-1$ cuts (each cut splits one current piece into two positive pieces). Then $D(M)\ge\delta$.*

*Proof.* By Lemma 2.2 it suffices to show that **every** matching $\mu$ of $M$ has $\operatorname{cost}(\mu)\ge\delta$. Fix $\mu$. Each element of $M$ is a fragment of exactly one piece $a_i$. Build a multigraph $G$ on the vertex set $\{1,\dots,m\}$:
- for each pair $\{x,y\}\in\mu$ whose fragments come from two **different** pieces $i\ne j$, add an edge $\{i,j\}$;
- for each pair $\{x,y\}\in\mu$ whose two fragments come from the **same** piece $i$, add a **loop** at $i$.

Unmatched fragments create no edges. Write $e$ for the total number of edges (loops included) and $u$ for the number of unmatched fragments. Counting fragments in two ways, with $c\le m-1$ the number of cuts:
$$2e+u=\#\{\text{fragments}\}=m+c\le 2m-1,$$
so $e\le m-1$ (as $e$ is an integer and $u\ge0$). Let $C$ range over the connected components of $G$ — **including isolated vertices** (a piece all of whose fragments are unmatched is such a component, with $e_C=0$, $v_C=1$); connectivity ignores loops, but loops still count as edges of their component. Let $e_C,v_C$ be the numbers of edges and vertices of $C$; then $\sum_C v_C=m$ and $\sum_C e_C=e$. If $e_C\ge v_C$ held for **every** component, summing would give $e\ge m$, contradicting $e\le m-1$. Hence some component $C$ has $e_C\le v_C-1$. A connected multigraph on $v_C$ vertices has at least $v_C-1$ edges, with equality only if it is a tree (a loop or a parallel edge would force $e_C\ge v_C$); so $C$ is a tree. In particular $C$ has **no loops**, i.e. no self-pair of fragments occurs inside $C$: every pair of $\mu$ within $C$ is a cross-pair between two different pieces of $C$, and these cross-pairs are exactly the $v_C-1$ edges of the tree.

*Tree inequality.* A tree is bipartite: choose signs $\epsilon_i\in\{\pm1\}$ for $i\in C$ so that $\epsilon_i=-\epsilon_j$ whenever $\{i,j\}$ is an edge. We claim
$$\Big|\sum_{i\in C}\epsilon_i a_i\Big|\le\operatorname{cost}(C),\qquad \operatorname{cost}(C):=\sum_{\substack{\{x,y\}\in\mu\\ \text{within }C}}|x-y|+\sum_{\substack{z\text{ unmatched}\\ \text{in }C}}z .$$
Indeed, expand each $a_i$ as the sum of its fragments and group the signed sum $\sum_{i\in C}\epsilon_i a_i$ according to $\mu$. A cross-pair $\{x,y\}$ with $x$ from $i$ and $y$ from $j$ contributes $\epsilon_i x+\epsilon_j y=\epsilon_i(x-y)$, of absolute value $|x-y|$; an unmatched fragment $z$ of piece $i$ contributes $\epsilon_i z$, of absolute value $z$. By the triangle inequality $\big|\sum_{i\in C}\epsilon_i a_i\big|\le\sum_{\text{cross-pairs}}|x-y|+\sum_{\text{unmatched}}z=\operatorname{cost}(C)$.

*Margin.* Let $k$ be the largest index in $C$. Then, using the reverse triangle inequality and the margin property,
$$\Big|\sum_{i\in C}\epsilon_i a_i\Big|\ge a_k-\sum_{i\in C\setminus\{k\}}a_i\ge\delta,$$
because $C\setminus\{k\}\subseteq\{1,\dots,k-1\}$: if $k\ge2$ then $a_k\ge\delta+\sum_{j<k}a_j\ge\delta+\sum_{i\in C\setminus\{k\}}a_i$, and if $k=1$ then $C=\{1\}$ and $a_1\ge\delta$.

Combining, $\operatorname{cost}(\mu)\ge\operatorname{cost}(C)\ge\big|\sum_{i\in C}\epsilon_i a_i\big|\ge\delta$. Since $\mu$ was arbitrary, Lemma 2.2 gives $D(M)\ge\delta$. $\blacksquare$

**Corollary 3.2 (lower bound).** *With the geometric split, whatever XY does, $D(M)\ge T_n$, so LB guarantees a share of at least*
$$\frac{1+T_n}{2}=\frac12\cdot\frac{2^{n+1}}{2^{n+1}-1}=\frac{2^n}{2^{n+1}-1}.$$

*Proof.* The final multiset $M$ is a refinement of the geometric family (which is super-increasing with margin $T_n$) by at most $n=m-1$ cuts (with $m=n+1$); Theorem 3.1 applies. $\blacksquare$

### 4. Part B: Xiang Yu's counterstrategy (upper bound)

Now fix **any** composition of $1$ into $m\le n+1$ positive pieces $a_1\le\dots\le a_m$ chosen by LB. We exhibit an XY strategy ($\le n$ cuts) forcing $D\le T_n$.

**Case $m\le n$.** XY bisects every piece: $m\le n$ cuts. Each piece $x$ becomes two pieces $x/2,x/2$, so every value occurs with even multiplicity in the final multiset; by Corollary 2.3, $D=0$.

**Case $m=n+1$.** This rests on two lemmas about *chains*. For a nonempty ordered tuple $(e_1,\dots,e_r)$ of positive reals define its *chain value* (nested absolute difference) by
$$v(e_1,\dots,e_r)=\bigl|\dots\bigl||e_1-e_2\bigr|-e_3\bigr|-\dots-e_r\bigr|.$$
A *chain* on a nonempty multiset $B$ is a choice of an ordering $(e_1,\dots,e_r)$ of its elements, and the chain value of $B$ for that ordering is $v(e_1,\dots,e_r)$.

**Lemma 4.1 (realizability lemma).** *Let $P,N$ be disjoint finite multisets of positive reals, with sums $\Sigma P,\Sigma N$, and $P\cup N\ne\emptyset$.*
- *(a) If $\Sigma P=\Sigma N$, then some ordering of $P\cup N$ has nested absolute difference $0$.*
- *(b) If $v:=\Sigma P-\Sigma N>0$ and no subset of $P\cup N$ has sum strictly between $\Sigma N$ and $\Sigma P$, then some ordering of $P\cup N$ has nested absolute difference $v$.*

*Proof.* We construct an ordering $e_1,\dots,e_r$ of $P\cup N$ by a greedy process. Set $E_0=0$. At step $k$, while elements remain: if $E_{k-1}>0$, append any remaining element $e_k\in N$ and put $E_k=E_{k-1}-e_k$; if $E_{k-1}<0$, append any remaining element $e_k\in P$ and put $E_k=E_{k-1}+e_k$; if $E_{k-1}=0$, append any remaining element from either (nonempty) side, with the corresponding sign.

We claim this process never gets stuck, i.e. the side it must draw from is never empty while the other side is nonempty. Indeed, suppose the process halts with a remaining part $P'\subseteq P$ and $N'\subseteq N$, not both empty, and let $I\subseteq P$ and $J\subseteq N$ be the parts already processed, so the current signed sum is $E=\Sigma I-\Sigma J$.

- *Halt with $E>0$:* this requires $N$ exhausted ($J=N$) and $P'\ne\emptyset$. Then $E=\Sigma I-\Sigma N>0$, so $\Sigma I>\Sigma N$, while $\Sigma I=\Sigma P-\Sigma P'<\Sigma P$ (as $P'\ne\emptyset$ and all elements are positive). Hence $\Sigma I$ lies strictly between $\Sigma N$ and $\Sigma P$: impossible — in case (b) by the hypothesis, and in case (a) because $\Sigma I\le\Sigma P=\Sigma N$ would give $E\le0$.
- *Halt with $E<0$:* this requires $P$ exhausted ($I=P$) and $N'\ne\emptyset$. Then the full signed sum is $\Sigma P-\Sigma N=E-\Sigma N'<0$, contradicting $\Sigma P-\Sigma N=v>0$ in case (b) and $\Sigma P-\Sigma N=0$ in case (a).
- *Halt with $E=0$:* then both sides are empty (at $E=0$ either nonempty side may be drawn from), so nothing remains — the process is finished, not stuck.

Hence the process consumes all of $P\cup N$ and ends at $E_r=\Sigma P-\Sigma N$.

Finally we check that the nested absolute difference of the ordering $e_1,\dots,e_r$ equals $|E_r|$. Define $R_1=e_1$ and $R_k=|R_{k-1}-e_k|$; we claim $R_k=|E_k|$ for all $k$. This holds for $k=1$ since $E_1=\pm e_1$. Inductively: if $E_{k-1}\ge0$ and $e_k\in N$, then $E_k=E_{k-1}-e_k$ and $|E_k|=\big||E_{k-1}|-e_k\big|=|R_{k-1}-e_k|=R_k$; if $E_{k-1}<0$ and $e_k\in P$, then $E_k=-|E_{k-1}|+e_k$ and again $|E_k|=\big||E_{k-1}|-e_k\big|=R_k$; if $E_{k-1}=0$ then $|E_k|=e_k=|0-e_k|=R_k$. Thus the chain value is $R_r=|E_r|=|\Sigma P-\Sigma N|$, which is $0$ in case (a) and $v$ in case (b). $\blacksquare$

**Theorem 4.2 (chain theorem).** *Let $a_1,\dots,a_m$ be positive reals with sum $S$. Then there exist a nonempty sub-multiset $B\subseteq\{a_1,\dots,a_m\}$ and an ordering $(e_1,\dots,e_r)$ of the elements of $B$ whose chain value satisfies $v(e_1,\dots,e_r)\le\dfrac{S}{2^m-1}$.*

*Proof.* Consider the $2^m$ subset sums $s(I)=\sum_{i\in I}a_i$ ($I\subseteq\{1,\dots,m\}$); they lie in $[0,S]$. Sort them as $0=t_0\le t_1\le\dots\le t_{2^m-1}=S$ (with multiplicity). The $2^m-1$ consecutive gaps sum to $t_{2^m-1}-t_0\le S$, so some consecutive gap satisfies
$$g:=t_{j+1}-t_j\le\frac{S}{2^m-1}.$$
By definition of the sorted list, **no subset sum lies strictly between $t_j$ and $t_{j+1}$**. Pick **distinct** subsets $A\ne B$ with $s(A)=t_{j+1}$, $s(B)=t_j$ (the sorted list has one entry per subset, so its two entries $t_j,t_{j+1}$ come from two distinct subsets), and set $P=\{a_i:i\in A\setminus B\}$, $N=\{a_i:i\in B\setminus A\}$ (as multisets). Then $P\cup N\ne\emptyset$ and $\Sigma P-\Sigma N=s(A)-s(B)=g\ge0$.

If $g=0$, Lemma 4.1(a) gives an ordering of $P\cup N$ with chain value $0\le\frac{S}{2^m-1}$.

If $g>0$: any subset $J$ of $P\cup N$ with $\Sigma N<\Sigma J<\Sigma P$ would lift to the subset $J\cup(A\cap B)$ of $\{a_1,\dots,a_m\}$ whose sum lies strictly between $s(B)$ and $s(A)$, a contradiction. So the hypothesis of Lemma 4.1(b) holds, and some ordering of $P\cup N$ has chain value $g\le\frac{S}{2^m-1}$. $\blacksquare$

(The bound is sharp: for $a_i=2^{i-1}$ the subset sums are exactly $0,1,\dots,2^m-1$, so every gap equals $1=\frac{S}{2^m-1}$; and for every nonempty subset $B$ and every ordering $(e_1,\dots,e_r)$ of $B$ the chain value is at least $1$. Indeed, an easy induction on $r$ shows that $v(e_1,\dots,e_r)=\bigl|\sum_{i=1}^r\delta_i e_i\bigr|$ for some signs $\delta_i\in\{\pm1\}$: if $v(e_1,\dots,e_{r-1})=|Y|$ with $Y$ a signed sum, then $\bigl||Y|-e_r\bigr|$ equals $|Y-e_r|$ when $Y\ge0$ and $|{-Y}-e_r|$ when $Y<0$, and both are absolute values of signed sums (negating all signs of a signed sum gives a signed sum). A signed sum of distinct powers of $2$ is a nonzero integer, since the largest power present exceeds the sum of all strictly smaller powers, so the chain value is a positive integer, hence $\ge1=\frac{S}{2^m-1}$.)

**XY's strategy from a chain.** Let $B$ be a nonempty subset of LB's pieces and $(e_1,\dots,e_r)$ an ordering of $B$ with chain value $v:=v(e_1,\dots,e_r)\le T_n$ (Theorem 4.2 with $S=1$, $m=n+1$). XY plays as follows. He maintains a *running piece* of size $v_{\text{run}}$ (initially the piece $e_1$, so $v_{\text{run}}=e_1$) and processes $e_2,\dots,e_r$ in this order. To process $e_k$ with current running value $v=v_{\text{run}}$:
- if $v=0$ (no running piece exists): declare the as-yet-untouched piece $e_k$ the new running piece ($v_{\text{run}}:=e_k$); no cut;
- if $v=e_k>0$: set the running piece and the piece $e_k$ aside as an **equal pair** (they will cancel in $D$ by Corollary 2.3); $v_{\text{run}}:=0$; no cut;
- if $v\ne e_k$ and both are positive: cut the **larger** of the two pieces $\{v_{\text{run}},e_k\}$ at distance $\min(v,e_k)$ from one end, producing pieces of sizes $\min(v,e_k)$ and $|v-e_k|$. Set the piece of size $\min(v,e_k)$ aside together with the smaller of the two original pieces: they form an **equal pair**. The piece of size $|v-e_k|$ becomes the new running piece; $v_{\text{run}}:=|v-e_k|$. One cut.

In each case the new running value equals $|v-e_k|$, so after processing $e_k$ the running value equals $v(e_1,\dots,e_k)$, and at the end $v_{\text{run}}=v\le T_n$ (with no running piece left if $v=0$).

After processing all of $B$, XY bisects every piece outside $B$ ($n+1-r$ cuts). The total number of cuts is at most $(r-1)+(n+1-r)=n$. All cut points are distinct: each cut is made inside a piece never cut before — at every moment the running piece has never been cut (it is either an as-yet-untouched original piece, namely $e_1$ or some $e_j$ declared running in the $v=0$ case, or the fresh fragment produced by the immediately preceding cut), pieces set aside are never touched again, and each $e_k$ is processed once. Every cut lies in the interior of one of LB's original pieces (in the third case $0<\min(v,e_k)<\max(v,e_k)$ since $v\ne e_k$ and both are positive, so the cut is interior to the piece being cut; bisections are interior too), so all of XY's marks differ from LB's marks and XY can place them all simultaneously.

In the final multiset, the pieces other than the (possible) last running piece split into disjoint pairs of equal pieces — the two halves of each bisected outside piece, each tie pair, and each equal pair formed above. Removing these pairs one at a time (Corollary 2.3) leaves the singleton $\{v\}$ if $v>0$, and leaves $\emptyset$ if $v=0$; in both cases
$$D(M)=v\le T_n,\qquad\text{so LB's share is at most }\frac{1+T_n}{2}=\frac{2^n}{2^{n+1}-1}.$$

### 5. Conclusion

Combining Corollary 3.2 (LB guarantees $\frac{1+T_n}{2}$ via the geometric split) with Section 4 (XY always holds LB to at most $\frac{1+T_n}{2}$), the largest value LB can guarantee is
$$\boxed{\,c=\frac{1+T_n}{2}=\frac{2^n}{2^{n+1}-1}\,}.$$
Sanity checks: $n=1$: $c=\frac23$ (LB marks at $\frac13$; any cut of the long piece leaves $D\ge\frac13$); $n=2$: $c=\frac47$; $n=3$: $c=\frac8{15}$ — all matching exhaustive grid computation.
