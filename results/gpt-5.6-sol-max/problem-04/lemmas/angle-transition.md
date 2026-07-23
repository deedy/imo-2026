# Lemma: angle transition under a cevian cut

## Statement
Normalize a straight angle to have measure $1$. Let a triangle have angles $(A,B,C)$ at vertices $A_0,B_0,C_0$, respectively, so $A+B+C=1$. Let $P$ be an interior point of side $B_0C_0$, and put
\[
x=\angle B_0A_0P.
\]
Then $0<x<A$, and the angle triples of triangles $A_0B_0P$ and $A_0PC_0$ are, respectively,
\[
(B,x,1-B-x),\qquad (C,A-x,B+x).
\]
Conversely, for every $x$ with $0<x<A$, there is a unique interior point $P$ of $B_0C_0$ giving this split.

## Proof
The ray $A_0P$ lies strictly inside the angle at $A_0$, so its two portions are $x$ and $A-x$. The angle at $B_0$ in the first child is the original angle $B$; hence its angle at $P$ is $1-B-x$. Similarly, the second child retains angle $C$, so its angle at $P$ is
\[
1-C-(A-x)=1-A-C+x=B+x.
\]
This gives the displayed triples.

Conversely, a unique ray in the interior of the angle $B_0A_0C_0$ makes angle $x$ with $A_0B_0$. Since it is strictly between the two side rays, it meets the open segment $B_0C_0$ at a unique point $P$. Thus every $x\in(0,A)$ is geometrically attainable. $\square$
