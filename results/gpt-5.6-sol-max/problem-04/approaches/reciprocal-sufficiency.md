# Constructive sufficiency for reciprocal targets

## Idea
Normalize a straight angle to $1$ and set $t=1/n$. First force both children of one cut to contain positive integral multiples of $t$. Then recursively reduce whichever multiple Shan-Yu retains.

## Forcing the first multiple
Let the current triangle have angles $(A,B,C)$ and suppose none equals $1/n$.

For $n\ge3$, choose $A$ largest. Then $A\ge1/3$, and in fact $nA>1$: this is immediate for $n>3$, while for $n=3$, equality $A=1/3$ would force the equilateral triangle, which already has the target angle. Hence the interval
\[
(nC,n(A+C))
\]
has length $nA>1$ and contains an integer $m$. Since $0<C<A+C=1-B<1$, this integer satisfies $1\le m\le n-1$ and
\[
C<\frac mn<A+C.
\]
For $n=2$, choose $B,C<1/2$ (possible unless an angle already equals $1/2$); then the same inequality holds with $m=1$.

Cut from angle $A$, choosing its portion
\[
x=A+C-\frac mn=1-B-\frac mn.
\]
The strict displayed inequalities give $0<x<A$. The two supplementary angles at the cut point are then
\[
1-B-x=\frac mn,\qquad B+x=1-\frac mn=\frac{n-m}{n}.
\]
Thus whichever child Shan-Yu retains contains a positive integral multiple of $1/n$.

## Reduction
If a current triangle has angle $k/n$, split that angle into $1/n$ and $(k-1)/n$. Shan-Yu either retains the child with target angle $1/n$, or retains one with the smaller positive multiple $(k-1)/n$. Induction forces a win after at most $k-1$ such cuts.

## Status
Complete. Together, initialization and reduction prove sufficiency for every integer $n\ge2$.
