# imo-2026-03 — tracking file

## Status
solved

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- **Reduction of the picking phase** to the classical alternating-selection game: value to the first player = sum of odd-ranked pieces (sorted descending); equivalently $V=(1+D)/2$ where $D$ is the alternating sum of the sorted piece lengths. Proved (Lemma 2 below) and verified by minimax search (`code/verify_lemmaA.py`).
- **Brute force on integer grids** (`code/brute.c`): computed max–min $D$ over all Liu Bang configurations and all Xiang Yu refinements for $n=1$ ($N=12$), $n=2$ ($N=42$), $n=3$ ($N=30,45$), $n=4$ ($N=62$), and single-configuration check for $n=5$ ($N=126$). All match $D^*=1/(2^{n+1}-1)$, i.e. $c=2^n/(2^{n+1}-1)$, with the geometric configuration $(2^n,\dots,2,1)\cdot u$ among the optimizers.
- **Dead ends (recorded honestly):** (a) a "parity-measure" integral formula $D=\mu\{t:\#\{\text{parts}>t\}\text{ odd}\}$ — correct but did not directly yield the lower bound; (b) attempts to prove the upper bound by induction on the operation-recursion (halve largest / cut off a copy of the second largest) with the potential $s/(2^m-1)$ — fails in the "flat top" case without strengthening; (c) an "integrality of the optimal response" reduction — vertices of the arrangement need not be integral. See `approaches/`.
- **Successful ideas:** lower bound by a *tree-pairing / signed subset-sum* argument (Lemma 4); upper bound by *subset-sum pigeonhole + cross-pairing cuts* (Lemma 5). Both verified numerically (`code/verify_lemmaC.py`, `code/verify_lemmaD.py`, exact rational arithmetic for the constructed strategy).

## Current best
**Answer:** 
$$c \;=\; \frac{2^n}{2^{n+1}-1}.$$
Liu Bang's optimal marking cuts the stick into pieces of lengths $2^n u, 2^{n-1}u,\dots,2u,u$ where $u=\frac1{2^{n+1}-1}$; he then always claims a longest unclaimed piece. Complete proof below.

## Full proof

Throughout, fix $n\ge 1$ and set
$$u=\frac{1}{2^{n+1}-1},\qquad c=\frac{2^{n}}{2^{n+1}-1}=\frac{1+u}{2}.$$

### 0. Setup and notation

Liu Bang (L) marks a set $P_L$ of at most $n$ points in the open interval $(0,1)$; then Xiang Yu (Y) marks a set $P_Y$ of at most $n$ further points of $(0,1)$, disjoint from $P_L$. The stick is cut at $P_L\cup P_Y$; the resulting pieces are the maximal subintervals, a finite multiset of positive lengths summing to $1$. Then the players alternately claim pieces, L first.

For a finite multiset $A$ of nonnegative reals let $a_1\ge a_2\ge\cdots\ge a_M$ be its elements in non-increasing order (this **sequence of values** is uniquely determined by $A$). Define
$$O(A)=\sum_{i\text{ odd}}a_i,\qquad E(A)=\sum_{i\text{ even}}a_i,\qquad D(A)=\sum_{i=1}^{M}(-1)^{i-1}a_i=O(A)-E(A).$$
Since $O(A)+E(A)=\Sigma(A)$ (the total), if $\Sigma(A)=1$ then
$$O(A)=\frac{1+D(A)}{2}. \tag{0.1}$$
Grouping consecutive terms gives
$$D(A)=\sum_{i=1}^{\lfloor M/2\rfloor}(a_{2i-1}-a_{2i})\;+\;\begin{cases}a_M,&M\text{ odd}\\0,&M\text{ even,}\end{cases} \tag{0.2}$$
so $0\le D(A)$, and trivially $D(A)\le \Sigma(A)$.

### 1. Lemma 1 (equal pairs cancel)
*For any finite multiset $X$ and any $y\ge 0$:* $D\bigl(X\uplus\{y,y\}\bigr)=D(X)$.

**Proof.** Let $x_1\ge\cdots\ge x_r$ be the sorted values of $X$ and let $p$ be the number of $x_i\ge y$. Then the sorted value sequence of $X\uplus\{y,y\}$ is $x_1,\dots,x_p,\,y,\,y,\,x_{p+1},\dots,x_r$. Its alternating sum is
$$\sum_{i\le p}(-1)^{i-1}x_i+(-1)^{p}y+(-1)^{p+1}y+\sum_{i>p}(-1)^{(i+2)-1}x_i=D(X). \qquad\blacksquare$$

By induction, adjoining any number of equal pairs to a multiset does not change $D$; in particular a multiset consisting only of equal pairs and a sub-multiset $L$ has $D=D(L)\le\Sigma(L)$.

### 2. Lemma 2 (value of the picking phase)
*Let $A$ be the multiset of piece lengths, $\Sigma(A)=1$. In the alternating claiming phase:*
1. *The first player has a strategy guaranteeing himself a total $\ge O(A)$, against every play of the opponent.*
2. *The second player has a strategy guaranteeing herself a total $\ge E(A)$, against every play of the opponent.*

*Consequently, under (0.1), the first player can guarantee exactly $\tfrac{1+D(A)}2$ from the picking phase and no more.*

**Proof.** Write $A:\ a_1\ge\cdots\ge a_M$. We first record two inequalities. For $2\le j\le M$, removing $a_1$ and $a_j$ from $A$ leaves the sorted sequence $a_2,\dots,a_{j-1},a_{j+1},\dots,a_M$, in which $a_i$ has rank $i-1$ for $i<j$ and rank $i-2$ for $i>j$; hence
$$O(A\setminus\{a_1,a_j\})=\sum_{\substack{2\le i\le j-1\\ i\ \mathrm{even}}}a_i+\sum_{\substack{i>j\\ i\ \mathrm{odd}}}a_i .$$
Comparing with $O(A)-a_1=\sum_{3\le i\le j,\ i\ \mathrm{odd}}a_i+\sum_{i>j,\ i\ \mathrm{odd}}a_i$ and pairing terms,
$$O(A\setminus\{a_1,a_j\})-\bigl(O(A)-a_1\bigr)=
\begin{cases}(a_2-a_3)+\cdots+(a_{j-2}-a_{j-1}),& j\text{ even}\\[2pt]
(a_2-a_3)+\cdots+(a_{j-1}-a_j),& j\text{ odd}\end{cases}\;\ge 0. \tag{2.1}$$
Similarly, removing one element $a_j$ leaves $a_i$ at rank $i$ for $i<j$ and rank $i-1$ for $i>j$, so $O(A\setminus\{a_j\})=\sum_{i<j,\ i\ \mathrm{odd}}a_i+\sum_{i>j,\ i\ \mathrm{even}}a_i$, and
$$O(A\setminus\{a_j\})-E(A)=\begin{cases}(a_1-a_2)+\cdots+(a_{j-2}-a_{j-1}),& j\text{ odd}\\[2pt]
(a_1-a_2)+\cdots+(a_{j-1}-a_j),& j\text{ even}\end{cases}\;\ge 0. \tag{2.2}$$

*Proof of 1.* Strategy: always claim a currently longest unclaimed piece. We show by strong induction on $|B|$: if it is your turn and the unclaimed multiset is $B$, this strategy nets you at least $O(B)$ from $B$. For $|B|\le 1$ this is clear. Otherwise you take $b_1$ (a largest element). If nothing remains, you got $b_1=O(B)$. Otherwise the opponent takes some $b_j$ ($j\ge2$), and by induction you gain at least $O(B\setminus\{b_1,b_j\})\ge O(B)-b_1$ by (2.1) from the rest. Total $\ge O(B)$.

*Proof of 2.* Strategy: after the opponent's first claim $a_j$, it is your turn on $A\setminus\{a_j\}$; play the greedy strategy of part 1 to get at least $O(A\setminus\{a_j\})\ge E(A)$ by (2.2).

Finally, part 1 gives the first player $\ge O(A)$; part 2 gives the second player $\ge E(A)$, i.e. caps the first player at $1-E(A)=O(A)$. $\blacksquare$

Thus, once the cutting is done and produces the multiset $A$, the quantity Liu Bang can guarantee from that position is exactly $\tfrac{1+D(A)}{2}$, and Xiang Yu can prevent more. So the whole game reduces to:

> **Reduced game.** L chooses a multiset $q_1,\dots,q_m$ ($m\le n+1$) of positive reals summing to $1$ (the pieces cut by his marks). Y then refines it: she distributes $K\le n$ cuts among the pieces, splitting a piece of length $q$ receiving $k$ cuts into $k+1$ positive parts summing to $q$. If $A$ is the final multiset of parts, L's guaranteed amount is $\frac{1+D(A)}{2}$: he wants $D(A)$ large, she wants it small.

(Y's marks are automatically distinct from L's, because each of her marks is interior to one of L's pieces; conversely any refinement of the pieces is realizable by valid marks.)

### 3. The signed subset-sum property of the geometric configuration

Let L's configuration be the **geometric configuration**
$$q_j=2^j u\quad (j=0,1,\dots,n),\qquad \sum_j q_j=(2^{n+1}-1)u=1 .$$
Its key property: for every nonempty $J\subseteq\{0,\dots,n\}$ and signs $s_j\in\{\pm1\}$,
$$\Bigl|\sum_{j\in J}s_j\,2^j u\Bigr|\;\ge\;u. \tag{3.1}$$
Indeed, with $j^*=\max J$, $\bigl|\sum_{j\in J}s_j2^j\bigr|\ge 2^{j^*}-\sum_{j<j^*}2^j=1$.

### 4. Lemma 4 (lower bound: Y cannot push $D$ below $u$)
*Let $A$ be any refinement of the geometric configuration obtained by at most $n$ cuts. Then $D(A)\ge u$.*

**Proof.** Say Y used $K\le n$ cuts, so $A$ has $M=(n+1)+K\le 2n+1$ parts; each part lies inside a unique original piece. Fix a non-increasing enumeration $a_1\ge a_2\ge\cdots\ge a_M$ of the **parts as physical objects** (ties broken arbitrarily); $D(A)$ is its alternating sum. Form the pairs $P_i=\{a_{2i-1},a_{2i}\}$ for $1\le i\le\lfloor M/2\rfloor$, with slack $\varepsilon_i=a_{2i-1}-a_{2i}\ge0$; if $M$ is odd, $a_M$ is unpaired. By (0.2),
$$D(A)=\sum_i\varepsilon_i+[M\text{ odd}]\,a_M. \tag{4.1}$$

Build a multigraph $G$ with vertex set $V=\{0,1,\dots,n\}$ (the original pieces) and one edge per pair $P_i$, joining the two pieces containing the two parts of $P_i$ (a loop if they lie in the same piece). Then
$$|E|=\Bigl\lfloor \tfrac M2\Bigr\rfloor\le n<n+1=|V| .$$
Every connected multigraph on $v$ vertices has at least $v-1$ edges, with equality only if it is a **simple tree** (take a spanning tree, which uses $v-1$ loop-free, pairwise distinct edges; with only $v-1$ edges in total there is nothing else). If every component of $G$ contained a cycle or loop it would have at least as many edges as vertices, forcing $|E|\ge|V|$ — impossible. Hence some component $T=(V_T,E_T)$ is a simple tree (possibly a single vertex).

Being a tree, $T$ admits a proper $2$-colouring $s:V_T\to\{\pm1\}$ (endpoints of every edge get opposite signs). Consider
$$\Xi:=\sum_{j\in V_T}s(j)\,q_j=\sum_{j\in V_T}s(j)\,2^ju .$$
By (3.1), $|\Xi|\ge u$.

Now expand $\Xi$ over parts: $q_j$ is the sum of the parts inside piece $j$. Consider any part $x$ inside a piece of $V_T$. Either $x$ is the unpaired $a_M$, or $x$ belongs to a pair $P_i$; the edge $P_i$ is incident to $V_T$, hence (as $T$ is a connected component) both endpoints of $P_i$ lie in $V_T$, and they are distinct pieces because $T$ has no loops. Consequently
$$\Xi=\sum_{P_i\in E_T}\Bigl(s(\pi(a_{2i-1}))\,a_{2i-1}+s(\pi(a_{2i}))\,a_{2i}\Bigr)\;+\;[\,M\text{ odd},\ \pi(a_M)\in V_T\,]\;s(\pi(a_M))\,a_M,$$
where $\pi(x)$ denotes the piece containing $x$. For each edge $P_i\in E_T$ the two signs are opposite, so the corresponding term has absolute value $|a_{2i-1}-a_{2i}|=\varepsilon_i$. Hence, using (4.1),
$$u\le|\Xi|\le\sum_{P_i\in E_T}\varepsilon_i+[M\text{ odd}]\,a_M\le D(A). \qquad\blacksquare$$

**Lower bound conclusion.** Liu Bang marks the $n$ interior points $\;2^nu,\;(2^n+2^{n-1})u,\;\dots,\;(2^{n+1}-2)u\;$, cutting the stick into the geometric pieces $2^nu,\dots,2u,u$. Whatever at most $n$ points Xiang Yu adds, the final multiset $A$ satisfies $D(A)\ge u$ by Lemma 4, and by Lemma 2(1) greedy claiming guarantees Liu Bang at least $\frac{1+D(A)}2\ge\frac{1+u}2=c$, **against every behaviour of Xiang Yu**.

### 5. Lemma 5 (upper bound: Y can always force $D\le u$)
*Whatever at most $n$ points L marks, Y can mark at most $n$ points so that the final multiset $A$ satisfies $D(A)\le u$.*

**Proof.** Let L's marks create pieces $q_1,\dots,q_m>0$, $m\le n+1$, $\sum q_i=1$.

**Case $m\le n$.** Y marks the midpoint of every piece ($m\le n$ interior points, pairwise distinct). The final multiset consists of the equal pairs $\{q_i/2,q_i/2\}$, so $D(A)=D(\varnothing)=0$ by Lemma 1.

**Case $m=n+1$.** Consider the $2^m$ subset sums $\sigma(S)=\sum_{i\in S}q_i$, $S\subseteq\{1,\dots,m\}$. They lie in $[0,1]$, with $\sigma(\varnothing)=0$ and $\sigma(\{1,\dots,m\})=1$; sorting them, the $2^m-1$ consecutive gaps sum to $1$, so some gap is at most $\frac1{2^m-1}=u$: there are $S\ne S'$ with $0\le\sigma(S')-\sigma(S)\le u$. Put $A^\*=S'\setminus S$ and $B^\*=S\setminus S'$; these are disjoint, not both empty, and
$$\Delta:=\sigma(A^\*)-\sigma(B^\*)=\sigma(S')-\sigma(S)\in[0,u].$$
Since $\Delta\ge0$, $A^\*=\varnothing$ would force $B^\*=\varnothing$; hence $A^\*\neq\varnothing$.

*Sub-case $B^\*=\varnothing$* (so $\sigma(A^\*)=\Delta\le u$). Y halves each of the $m-|A^\*|\le m-1=n$ pieces not in $A^\*$ and marks nothing else. The final multiset is (equal pairs) $\uplus\{q_i:i\in A^\*\}$, so by Lemma 1, $D(A)=D(\{q_i\}_{i\in A^\*})\le\sigma(A^\*)=\Delta\le u$.

*Sub-case $A^\*,B^\*\ne\varnothing$.* Write $A^\*=\{i_1,\dots,i_p\}$, $B^\*=\{j_1,\dots,j_q\}$, and set partial sums
$$\alpha_0=0,\ \alpha_k=q_{i_1}+\cdots+q_{i_k}\ (1\le k\le p),\qquad \beta_0=0,\ \beta_k=q_{j_1}+\cdots+q_{j_k}\ (1\le k\le q),$$
so $\alpha_p=\sigma(A^\*)$ and $\beta_q=\sigma(B^\*)=\alpha_p-\Delta$. Identify the pieces of $A^\*$, concatenated, with the interval $[0,\alpha_p)$ (piece $i_k\leftrightarrow[\alpha_{k-1},\alpha_k)$), and the pieces of $B^\*$ with $[0,\beta_q)$. Y marks:
- the midpoint of each of the $m-p-q$ pieces outside $A^\*\cup B^\*$;
- inside the $A^\*$-row: every point of $\{\beta_1,\dots,\beta_{q-1},\beta_q\}\cap(0,\alpha_p)$ that is **not** equal to some $\alpha_k$ — at most $q$ points, each interior to exactly one $A^\*$-piece;
- inside the $B^\*$-row: every point of $\{\alpha_1,\dots,\alpha_{p-1}\}\cap(0,\beta_q)$ that is not equal to some $\beta_k$ — at most $p-1$ points.

Total marks $\le (m-p-q)+q+(p-1)=m-1=n$. All are interior points of L's pieces (so distinct from L's marks), and pairwise distinct (distinct positions along the rows; positions in different pieces are different points of the stick).

Let $\Gamma:\ 0=\gamma_0<\gamma_1<\cdots<\gamma_r=\beta_q$ be the sorted distinct values of $(\{\alpha_k\}_{k=0}^{p}\cup\{\beta_k\}_{k=0}^{q})\cap[0,\beta_q]$. By construction, the cut grid of the $A^\*$-row restricted to $[0,\beta_q]$ is exactly $\Gamma$ (all $\beta_k\le\beta_q$ are either marked in the $A^\*$-row or coincide with an $\alpha_k$; note $\beta_q\le\alpha_p$), and the cut grid of the $B^\*$-row on $[0,\beta_q]$ is also exactly $\Gamma$. Hence:
- for each $0\le t<r$, the interval $(\gamma_t,\gamma_{t+1})$ produces **one part of length $\gamma_{t+1}-\gamma_t$ on the $A^\*$-side and one on the $B^\*$-side** — an equal pair;
- no $A^\*$-part straddles $\beta_q$ (the point $\beta_q$ belongs to the $A^\*$-grid, or equals $\alpha_p$); the remaining $A^\*$-parts fill $[\beta_q,\alpha_p)$, a leftover multiset $L$ with $\Sigma(L)=\Delta$ (empty if $\Delta=0$);
- pieces outside $A^\*\cup B^\*$ produce equal pairs $\{q_i/2,q_i/2\}$.

The final multiset is therefore (equal pairs) $\uplus\,L$, and by Lemma 1,
$$D(A)=D(L)\le\Sigma(L)=\Delta\le u. \qquad\blacksquare$$

**Upper bound conclusion.** Whatever Liu Bang's marks, Xiang Yu marks as in Lemma 5 and then, in the claiming phase, plays the greedy second-player strategy of Lemma 2(2). She thereby secures at least $E(A)=\frac{1-D(A)}2\ge\frac{1-u}{2}$, so Liu Bang ends with at most $\frac{1+D(A)}{2}\le\frac{1+u}2=c$, **no matter how he picks**. (In the case $m \le n$ he even gets at most $1/2 < c$.)

### 6. Conclusion

Liu Bang has a strategy (geometric marking + greedy claiming) guaranteeing at least $c$; Xiang Yu has, against every strategy of Liu Bang, a reply (Lemma 5 marking + greedy claiming) that caps him at $c$. Therefore the largest total length Liu Bang can guarantee is exactly
$$\boxed{\,c=\dfrac{2^{n}}{2^{n+1}-1}\,}.$$

*(Numerically verified: $n=1:\,2/3$, $n=2:\,4/7$, $n=3:\,8/15$, $n=4:\,16/31$ by exhaustive grid search; $n=5:\,32/63$ for the geometric configuration; plus 40000-trial Monte Carlo for Lemma 4 and 4000 exact-arithmetic random tests of the Lemma 5 construction.)*
