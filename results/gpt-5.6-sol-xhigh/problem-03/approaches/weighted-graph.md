# Weighted-graph / equal-pair approach

## Status
Sharp approach; proof skeleton complete.

## Core reformulation
For final piece lengths, pair pieces (using adjacent pairs in nonincreasing order), with a singleton if their number is odd. For a pair coming from initial intervals $i,j$, draw an edge $ij$ (a loop if $i=j$) with weight equal to the smaller piece. Its matched load is that weight at each endpoint (twice at a loop). The unmatched total is exactly the alternating discrepancy $D$.

Thus at most $n$ pair-edges can match capacities placed on the $n+1$ initial intervals.

## Sharp lower bound
Let the initial capacities, in units of $d=1/(2^{n+1}-1)$, be
\[
1,2,4,\ldots,2^n.
\]
A graph on $n+1$ vertices with at most $n$ edges has a component with fewer edges than vertices; this component is a tree (an isolated vertex is allowed). If its bipartition is $P\sqcup Q$, matched weighted degrees have equal sums on $P,Q$. Hence the residual in that component is at least
\[
\left|\sum_{i\in P}2^i-\sum_{j\in Q}2^j\right|d\ge d.
\]
The signed sum cannot vanish because its largest power exceeds the sum of every smaller power.

## Sharp upper bound
For arbitrary capacities $a_1,\dots,a_{n+1}$ summing to $1$, order their $2^{n+1}$ subset sums. Two consecutive ones differ by at most
\[
d=\frac1{2^{n+1}-1}.
\]
After deleting the intersection, obtain disjoint subsets $A,B$ with
\[
\left|\sum_Aa_i-\sum_Ba_i\right|\le d.
\]
If both are nonempty, scale down the demands on the larger side so that the two totals agree, and realize the two degree sequences by a nonnegative transportation matrix with at most $|A|+|B|-1$ positive entries. Each positive entry gives an equal pair of pieces across the corresponding initial intervals. Every vertex outside $A\cup B$ gets a loop, i.e. its interval is bisected. This uses at most
\[
(|A|+|B|-1)+(n+1-|A|-|B|)=n
\]
pairs/types, and the unmatched total is exactly the subset-sum difference. The incidence count shows the required number of cuts is at most $n$.

If one subset is empty, leave the nonempty subset unsplit and bisect every interval outside it. Pairing the remaining singleton pieces arbitrarily costs at most their total, which is at most $d$.
