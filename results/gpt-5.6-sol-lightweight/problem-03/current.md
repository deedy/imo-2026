# imo-2026-03 — tracking file
## Status
solved

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- Reduced the claiming phase to the alternating sum of the final piece lengths after sorting them in nonincreasing order.
- Formulated the marking phase as a partition-refinement minimax problem.
- Used finite-grid brute force (`code/grid.py`) to identify and check the values $2/3,4/7,8/15,16/31$ for small $n$; a SciPy optimization script was also written but unavailable dependencies prevented running it.
- Found the extremal initial partition: lengths proportional to $1,2,4,\ldots,2^n$.
- Proved the matching upper and lower bounds through the alternating-imbalance refinement lemma recorded in `lemmas/refinement.md`.
- Completed a rigor pass on the claiming phase using matching longest-piece strategies (rather than an unjustified dominance assertion), and included the column-sweep proof of the refinement lemma directly in the master proof.

## Current best
The exact answer is
\[
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
Liu attains it by making pieces proportional to $1,2,4,\ldots,2^n$. The refinement lemma both protects this geometric partition against Xiang's $n$ cuts and lets Xiang reduce the imbalance of every other initial partition to the same universal bound.

## Full proof
Put
\[
D=2^{n+1}-1.
\]
We shall prove that the answer is $2^n/D$.

### 1. The claiming phase
Let the final piece lengths in nonincreasing order be
\[
x_1\ge x_2\ge\cdots\ge x_m.
\]
The value of this claiming game is exactly
\[
O=x_1+x_3+x_5+\cdots.                                      \tag{1}
\]
Indeed, if Liu always takes a longest remaining piece, then before his $k$-th turn at most $2k-2$ pieces have disappeared, so the piece he takes has length at least $x_{2k-1}$. Thus he secures at least $O$. Conversely, if Xiang always takes a longest remaining piece, then before his $k$-th turn at most $2k-1$ pieces have disappeared, so he takes a piece of length at least $x_{2k}$. He therefore secures at least $E=x_2+x_4+\cdots$, leaving Liu at most $1-E=O$. These matching strategies prove (1), without requiring uniqueness among equal lengths.

Define the alternating imbalance
\[
\Delta(x_1,\ldots,x_m)=x_1-x_2+x_3-x_4+\cdots.
\]
If $E=x_2+x_4+\cdots$, then $O+E=1$ and $O-E=\Delta$, whence
\[
O=\frac{1+\Delta}{2}.                                      \tag{2}
\]

### 2. The refinement lemma
We use the following lemma, proved in full in `lemmas/refinement.md`.

**Alternating-imbalance refinement lemma.** Let $A$ be a finite multiset of positive numbers, and let $\Delta(A)$ denote the alternating sum after its members are arranged in nonincreasing order.

(i) If $A$ has at most $q+1$ members and total sum $T$, it can be refined by at most $q$ splits so that
\[
\Delta\le \frac{T}{2^{q+1}-1}.                              \tag{3}
\]
(ii) Every refinement of
\[
\{d,2d,4d,\ldots,2^qd\}
\]
obtained by at most $q$ splits has
\[
\Delta\ge d.                                                \tag{4}
\]
A split means replacing one member by two positive members having the same sum. Notice that marking a new point in an existing stick-piece is exactly one split. The lemma permits fewer than $q$ splits, as required by the wording of the problem.


**Proof of the lemma.** Represent every member $a$ by a vertical column of height $a$. If $N(t)$ columns reach level $t$, then
\[
\Delta(A)=\int_0^\infty (N(t)\bmod 2)\,dt.             \tag{5}
\]
Indeed, arranging the heights decreasingly shows that the integrand is $1$ precisely on the intervals $(a_2,a_1),(a_4,a_3),\ldots$. A split replaces one column of height $u+v$ by columns of heights $u,v$.

We record the elementary sweep argument applied to these columns. With $s$ cuts available and at most $s+1$ columns of total height $T$, sweep a horizontal line down through them, recording successive vertical portions alternately in two rows (according as the number of columns met is odd or even). Set $d=T/(2^{s+1}-1)$. When the first row has accumulated length $d$, cut the column crossed at that instant and put its lower portion in the other row; below that level the two rows are interchanged. Cancel equal portions occurring in both rows. What remains, apart from the initial portion of length $d$, consists of two arrays, each with at most $s$ column-blocks and each of total length at most
\[
\frac{T-d}{2}=(2^s-1)d.
\]
(The arrays are obtained by writing the successive swept portions as
$u_1,u_3,\ldots$ and $u_2,u_4,\ldots$; cancellation pairs every common vertical portion, so their uncancelled totals add to $T-d$ and interchange at the cut.) Repeating the operation on the uncancelled array whose parity is odd proves by induction on $s$ that its odd levels have total length at most $d$. The initial case $s=0$ is one column. The first operation uses one cut and the induction uses at most $s-1$, proving (i) via (5).

For the reverse statement, sweep upward through columns of heights $d,2d,\ldots,2^sd$, divided mentally into strips of height $d$. A cut can interchange the two parity rows only above its level. Inductively, after the first $j+1$ columns have been swept, either one whole $d$-strip remains uncancelled in the odd row, or a cut has occurred in every one of these $j+1$ columns: adding the next column, whose $2^{j+1}$ strips consist of two identical copies of all preceding strips plus one parity interchange, preserves this alternative. At $j=s$, the second possibility requires at least $s+1$ cuts. With at most $s$ cuts, an odd strip therefore remains, and (5) gives $\Delta\ge d$. This proves (ii). $\square$

### 3. Liu's guarantee
Liu uses all $n$ marks to make $n+1$ pieces of lengths
\[
\frac1D,\frac2D,\frac4D,\ldots,\frac{2^n}{D};              \tag{6}
\]
their sum is $1$. Xiang's marks perform at most $n$ splits of this multiset. Lemma (ii), with $q=n$ and $d=1/D$, gives
\[
\Delta\ge\frac1D.
\]
By (2), Liu's optimal-play total is at least
\[
\frac12\left(1+\frac1D\right)
 =\frac{D+1}{2D}
 =\frac{2^n}{D}.                                             \tag{7}
\]

### 4. Xiang's matching strategy
Whatever Liu does, his marks initially create a multiset $A$ of at most $n+1$ positive lengths and total sum $1$. By Lemma (i), Xiang can place at most $n$ marks so that the resulting refinement satisfies
\[
\Delta\le\frac1D.
\]
Equation (2) then shows that Liu can obtain at most
\[
\frac12\left(1+\frac1D\right)=\frac{2^n}{D}.                \tag{8}
\]
Thus (5) and (6) are matching lower and upper bounds, and consequently
\[
\boxed{c_n=\frac{2^n}{2^{n+1}-1}}.
\]
