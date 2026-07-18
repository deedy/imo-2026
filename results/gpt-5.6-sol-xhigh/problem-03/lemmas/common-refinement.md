# Lemma: matching two collections with few cuts

## Statement
Let $A$ and $B$ be two disjoint nonempty collections of intervals, with respective total lengths $p\ge q>0$. Using at most $|A|+|B|-1$ cuts within these intervals, one can obtain:

1. a collection of equal-length pairs, each pair having one piece from an interval in $A$ and one from an interval in $B$; and
2. unpaired pieces, all from intervals in $A$, whose total length is $p-q$.

Every piece of every interval belongs to one of these two collections.

## Proof
Order the intervals in $A$ arbitrarily. Starting from the first, take whole intervals until their cumulative length first reaches or exceeds $q$. Thus one selects $r$ intervals: the first $r-1$ are used completely, and an initial portion of the last is used so that the selected material has total length exactly $q$. Denote the lengths of these $r$ selected portions by
\[
\alpha_1,\ldots,\alpha_r.
\]
The last portion may be the whole last interval. All unused intervals and the unused tail, if any, have total length $p-q$.

Concatenate abstract intervals of lengths $\alpha_1,\ldots,\alpha_r$ to form one copy of $[0,q]$. Independently concatenate the $s=|B|$ interval lengths to form another copy of $[0,q]$. Superimpose the division points of these two partitions. Their common refinement has $E\le r+s-1$ positive cells. Cut the corresponding physical intervals at the refinement points. Every cell then gives two pieces of the same length, one on each side, and these pieces form the required equal pair.

It remains to count cuts. The intervals in $B$ are divided into $E$ pieces in total, requiring $E-s$ cuts. If the last selected $A$-portion is a whole interval, the selected $A$-intervals are divided into $E$ pieces and require $E-r$ cuts. Thus the total is
\[
2E-r-s\le r+s-2\le |A|+|B|-1.
\]
If the last selected portion is proper, its unused tail is one additional piece, so the $A$ side requires $E-r+1$ cuts. The total is then
\[
2E-r-s+1\le r+s-1\le |A|+|B|-1.
\]
The pieces not used in the equal pairs are exactly the unused $A$ material, of total length $p-q$. ∎
