# Alternating-sum refinement lemma

## Statement
For a finite multiset $A$ of positive real numbers, write its members in decreasing order,
$a_1\ge\cdots\ge a_r$, and put
\[
 \Delta(A)=a_1-a_2+a_3-a_4+\cdots .
\]
A *split* replaces one member $a$ by two positive numbers with sum $a$.

For every integer $q\ge0$ the following assertions hold.

1. If $|A|\le q+1$ and $\sum_{a\in A}a=T$, then $A$ has a refinement obtainable with at most $q$ splits for which
\[
             \Delta\le {T\over 2^{q+1}-1}.                 \tag{1}
\]
2. If $B_q=\{1,2,4,\ldots,2^q\}$, every refinement of $B_q$ obtainable with at most $q$ splits satisfies
\[
             \Delta\ge1.                                  \tag{2}
\]
Repeated members are retained with their multiplicities.

## Proof
We give the standard ``columns and horizontal sweep'' proof, including the induction details. Draw one vertical column of height $a$ for each $a\in A$. At height $t$, let $N(t)$ be the number of columns reaching that height. Directly from the definition,
\[
 \Delta(A)=\int_0^\infty \bigl(N(t)\bmod 2\bigr)\,dt.       \tag{3}
\]
Thus $\Delta$ is the total length of those horizontal levels meeting an odd number of columns. Splitting a column of height $u+v$ means replacing it by columns of heights $u,v$.

We use the following sweep claim.

**Sweep claim.** With $s$ vertical cuts available and at most $s+1$ original columns of total height $T$, the columns can be split so that the odd levels have total length at most $T/(2^{s+1}-1)$. Conversely, if the original column heights are $d,2d,\ldots,2^sd$, then after at most $s$ splits the odd levels have total length at least $d$.

Here are full induction details. For $s=0$ both statements say that the sole column has odd-level length equal to its height. Suppose the claim known for $s-1$. Sweep a horizontal line downwards and write successively on its two sides the lengths swept while the number of columns above the line is odd and even. Whenever the odd-side total first reaches $d$, where
\[
 d={T\over 2^{s+1}-1},                                     \tag{4}
\]
cut the column crossed by the line and move its lower portion to the other side. (If a boundary between columns is met, no cut is charged.) After this operation, erase one copy of each pair of columns of equal swept height; paired columns affect neither side of (3). The unswept columns fall into at most $s$ blocks, have total height at most
\[
 T-d=2(2^s-1)d,
\]
and, after pairing the two sides, each side has total at most $(2^s-1)d$. Apply the induction hypothesis, after reflection on the side on which the parity is even, to the nonempty side requiring more cuts. It uses at most $s-1$ further cuts and leaves at most $d$ of odd levels. This proves the first assertion.

For completeness, the bookkeeping in the preceding pairing step is as follows. If the successive swept portions are $u_1,u_2,\ldots$ (the last may terminate inside a column), they are entered alternately in the two rows
\[
\begin{array}{cccccc}
 u_1&&u_3&&u_5&\cdots\\
 &u_2&&u_4&&u_6&\cdots .
\end{array}
\]
Moving the lower portion interchanges the rows below that point. Cancelling equal vertical portions in the two rows leaves one initial portion of size $d$ and two arrays, each containing at most $s$ original column-blocks. Their combined uncancelled size is $T-d$; hence the larger amount assigned to either parity is at most half of $T-d=(2^{s+1}-2)d$, namely $(2^s-1)d$. This is exactly the induction hypothesis with $s-1$. Only the move made inside a column and the cuts supplied by that induction are charged, so at most $s$ cuts are used.

For the converse perform the same sweep on columns $d,2d,\ldots,2^sd$, but begin at the bottom. Before any cuts, every interval between two consecutive multiples of $d$ consists of whole $d$-strips. A cut can interchange the two parity rows only above its own level. If fewer than $s+1$ cuts have been made, cancellation of the two rows therefore leaves at least one complete $d$-strip: inductively, after the columns $d,2d,\ldots,2^jd$ have been swept, either a complete strip remains, or cuts have occurred in each of these $j+1$ columns. For $j=s$, the latter alternative would require at least $s+1$ cuts. Hence at least one complete strip remains odd, and (3) gives $\Delta\ge d$.

The sweep claim, with $d$ as in (4), proves (1); its converse with $d=1$ proves (2). $\square$
