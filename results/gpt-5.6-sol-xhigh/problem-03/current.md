# imo-2026-03 — tracking file
## Status
solved

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- Reduced the claiming stage to the alternating discrepancy of the sorted final lengths. If $x_1\ge\cdots\ge x_k$, the draft value for Liu Bang is $x_1+x_3+\cdots=(1+D)/2$, where $D=x_1-x_2+x_3-\cdots$.
- Obtained the preliminary upper bound $D\le 1/(2n+1)$ by making equal pairs of pieces; this is not sharp for $n\ge2$.
- Tested several candidate initial partitions for small $n$. For $n=2$, the failed candidate proportional to $(1,1,3)$ and the successful discrepancy $1/7$ suggested a powers-of-two construction.
- Recast the lower bound as a sparse weighted-multigraph problem: paired final pieces become weighted edges between their original Liu Bang intervals. A tree component forces a nonzero signed sum of powers of two.
- Proved the matching upper bound by pigeonholing the $2^{n+1}$ subset sums of arbitrary initial interval lengths, then realizing two close subset sums as equal pairs using a common refinement with at most $n$ further cuts.
- Ran random checks for $1\le n\le8$ on the powers-of-two lower construction and on the subset-sum gap bound; these supported the proved formula but were not used in place of proof.

## Current best
The explicit answer is $\displaystyle \boxed{c=\frac{2^n}{2^{n+1}-1}}$. Equivalently, the optimal alternating discrepancy between the two players' totals is $1/(2^{n+1}-1)$. Liu Bang attains it by making initial pieces proportional to $1,2,4,\ldots,2^n$, while Xiang Yu's matching strategy follows from two subset sums of the initial piece lengths differing by at most $1/(2^{n+1}-1)$.

## Full proof
Put
\[
d=\frac1{2^{n+1}-1}.
\]
We first establish three facts that will be used in both directions.

### 1. Value of the claiming stage

Suppose that, after all cuts, the piece lengths in nonincreasing order are
\[
x_1\ge x_2\ge\cdots\ge x_k>0,
\]
and define their **alternating discrepancy** by
\[
D(x_1,\ldots,x_k)=x_1-x_2+x_3-x_4+\cdots.
\]
We claim that under optimal play the difference between Liu Bang's total and Xiang Yu's total is exactly $D$.

For a multiset $X$ of lengths, let $V(X)$ be the maximum difference between the current player's eventual total and the other player's eventual total. Backward induction gives
\[
V(X)=\max_{x\in X}\bigl(x-V(X\setminus\{x\})\bigr). \tag{1}
\]
We prove by induction on $|X|$ that $V(X)=D(X)$, where the elements of $X$ are put in nonincreasing order when $D$ is evaluated. This is immediate for the empty multiset. Suppose the result holds for smaller multisets and write $X=(x_1,\ldots,x_k)$. Choosing $x_1$ in (1) gives
\[
x_1-D(x_2,\ldots,x_k)=D(x_1,\ldots,x_k).
\]
If instead $x_j$ is chosen, direct cancellation shows that
\[
D(X)-\bigl(x_j-D(X\setminus\{x_j\})\bigr)
=
\begin{cases}
2\bigl((x_1-x_2)+\cdots +(x_{j-2}-x_{j-1})\bigr),&j\text{ odd},\\[1mm]
2\bigl((x_1-x_2)+\cdots +(x_{j-3}-x_{j-2})+(x_{j-1}-x_j)\bigr),&j\text{ even}.
\end{cases} \tag{2}
\]
Here an empty sum is $0$. Every term on the right is nonnegative, so no choice is better than $x_1$. This proves the claim.

The two players' totals sum to $1$. Therefore Liu Bang's value in the claiming stage is
\[
\frac{1+D}{2}. \tag{3}
\]
Thus it remains to prove that the minimax value of $D$ in the marking stage is $d$.

### 2. A pairing interpretation of $D$

If there are an even number of lengths, the minimum, over all partitions of the pieces into pairs, of the sum of the absolute differences within the pairs is $D$. If there are an odd number, the analogous minimum—pair all but one piece and add the singleton's length to the pairwise differences—is again $D$.

To prove this, first consider $2r$ lengths. In any pairing in which $x_1$ and $x_2$ are not together, suppose their pairs are $(x_1,x_j)$ and $(x_2,x_\ell)$. Replacing these by $(x_1,x_2)$ and $(x_j,x_\ell)$ does not increase the cost: if $\ell<j$, the old cost minus the new cost is
\[
(x_1-x_j+x_2-x_\ell)-(x_1-x_2+x_\ell-x_j)=2(x_2-x_\ell)\ge0,
\]
and if $j<\ell$ it is similarly $2(x_2-x_j)\ge0$. Induction therefore shows that the adjacent pairing
\[
(x_1,x_2),(x_3,x_4),\ldots,(x_{2r-1},x_{2r})
\]
has minimum cost, namely $D$. For an odd number of lengths, append an extra length $0$ and apply the even case; pairing a piece with $0$ is precisely the same as declaring that piece the singleton.

In particular, if the final pieces can be grouped into equal pairs together with some remaining pieces whose total length is at most $d$, then
\[
D\le d. \tag{4}
\]
Indeed, retain the equal pairs, pair the remaining pieces arbitrarily, and leave one as a singleton if necessary. Since $|u-v|\le u+v$, this pairing has cost at most the total length of the remaining pieces.

### 3. A common-refinement construction

We need the following cutting fact. Let $A$ and $B$ be two disjoint nonempty collections of initial intervals, with total lengths $p\ge q>0$. Then using at most
\[
|A|+|B|-1 \tag{5}
\]
cuts within these intervals, it is possible to create equal pairs, each containing one piece from an interval of $A$ and one from an interval of $B$, while leaving unpaired material only in $A$, of total length $p-q$.

To see this, order the intervals of $A$. Take them in that order until a total length $q$ has been selected, using an initial portion of the last selected interval if necessary. Suppose $r$ intervals of $A$ are involved. Concatenate their selected portions to make one abstract interval $[0,q]$, and concatenate the $s=|B|$ intervals to make another copy of $[0,q]$. Superimpose the two sets of division points. The common refinement has at most
\[
E\le r+s-1
\]
cells. Cut the physical intervals at these refinement points and pair the corresponding cells of the two copies.

On the $B$ side this requires $E-s$ cuts. If the last selected $A$-portion is a whole interval, the $A$ side requires $E-r$ cuts, for a total at most $r+s-2$. If that portion is proper, its unused tail contributes one additional piece, so the total number of cuts is
\[
(E-s)+(E-r+1)\le r+s-1\le |A|+|B|-1.
\]
All material not in an equal pair lies on the $A$ side and has total length $p-q$, proving the cutting fact.

### 4. Liu Bang can force $D\ge d$

Liu Bang makes exactly $n$ marks so that the resulting $n+1$ consecutive intervals have lengths
\[
d,2d,4d,\ldots,2^n d. \tag{6}
\]
They have total length $(2^{n+1}-1)d=1$.

Consider any response by Xiang Yu using at most $n$ marks. After all the cuts, arrange the final pieces in adjacent pairs that attain the pairing cost $D$, as in Section 2, with one singleton if necessary. Construct a weighted multigraph whose vertices $0,1,\ldots,n$ correspond to Liu Bang's initial intervals. For each pair of final pieces of lengths $u,v$, draw an edge between the vertices of their initial intervals and give it weight $\min(u,v)$. If both pieces came from the same initial interval, this is a loop, whose weight is counted twice in the weighted degree. For each pair, regard the excess $|u-v|$ as residual material at the vertex containing the larger piece; a singleton is entirely residual.

There are at most $2n+1$ final pieces, so this graph has at most $n$ edges. If $\deg_w(i)$ is the weighted degree of vertex $i$ and $r_i\ge0$ is its total residual, then all material from initial interval $i$ has been accounted for, and hence
\[
2^i d=\deg_w(i)+r_i. \tag{7}
\]
Moreover, by the definition of the adjacent pairing,
\[
D=\sum_{i=0}^n r_i. \tag{8}
\]

A multigraph on $n+1$ vertices with at most $n$ edges has a connected component which is a tree, where an isolated vertex is allowed. Indeed, every connected component with $v$ vertices has at least $v-1$ edges; if none had exactly $v-1$, the total number of edges would be at least the total number of vertices, namely $n+1$.

Let $P\sqcup Q$ be the bipartition of such a tree component. It has no loops, and every edge has one endpoint in each part, so
\[
\sum_{i\in P}\deg_w(i)=\sum_{i\in Q}\deg_w(i).
\]
Subtracting (7) over its two parts gives
\[
d\left(\sum_{i\in P}2^i-\sum_{i\in Q}2^i\right)
=
\sum_{i\in P}r_i-\sum_{i\in Q}r_i. \tag{9}
\]
The integer in parentheses is nonzero: in a nonempty signed sum of distinct powers of two, the largest power is greater than the sum of all smaller powers. Its absolute value is therefore at least $1$. It follows from (9) that
\[
d\le \left|\sum_{i\in P}r_i-\sum_{i\in Q}r_i\right|
\le\sum_{i=0}^n r_i=D. \tag{10}
\]
Thus Liu Bang's construction guarantees $D\ge d$.

### 5. Xiang Yu can force $D\le d$

Consider any initial marking by Liu Bang, and let the positive initial interval lengths be $a_1,\ldots,a_m$, where $m\le n+1$.

If $m\le n$, Xiang Yu bisects every initial interval. This takes at most $n$ cuts and produces only equal pairs, so $D=0\le d$ by Section 2.

It remains to consider $m=n+1$. Form all $2^{n+1}$ subset sums
\[
\sum_{i\in S}a_i,\qquad S\subseteq\{1,\ldots,n+1\}.
\]
They lie in $[0,1]$. When put in nondecreasing order, two consecutive subset sums differ by at most
\[
\frac1{2^{n+1}-1}=d. \tag{11}
\]
Choose distinct subsets $S,T$ giving such a pair, and cancel their intersection. We obtain disjoint subsets
\[
A=S\setminus T,\qquad B=T\setminus S,
\]
not both empty, such that
\[
\left|\sum_{i\in A}a_i-
\sum_{i\in B}a_i\right|\le d. \tag{12}
\]

If one of $A,B$ is empty, let $C$ be the nonempty one. By (12), the total length of the intervals indexed by $C$ is at most $d$. Xiang Yu leaves those intervals alone and bisects every interval outside $C$. This uses
\[
n+1-|C|\le n
\]
cuts and leaves equal pairs together with pieces of total length at most $d$. Hence $D\le d$ by (4).

Now suppose both $A$ and $B$ are nonempty. Apply the common-refinement construction of Section 3 to these two collections, putting the one with larger total length first. By (12), it creates equal pairs and leaves unpaired material of total length at most $d$, using at most $|A|+|B|-1$ cuts. Bisect every interval outside $A\cup B$. The total number of cuts is at most
\[
(|A|+|B|-1)+(n+1-|A|-|B|)=n. \tag{13}
\]
Again, all pieces except for material of total length at most $d$ occur in equal pairs, so (4) yields $D\le d$.

Thus Xiang Yu can always force $D\le d$. Combined with Section 4, the marking-stage minimax discrepancy is exactly $d$. Finally, (3) gives
\[
c=\frac{1+d}{2}
=\frac12\left(1+\frac1{2^{n+1}-1}\right)
=\boxed{\frac{2^n}{2^{n+1}-1}}.
\]
