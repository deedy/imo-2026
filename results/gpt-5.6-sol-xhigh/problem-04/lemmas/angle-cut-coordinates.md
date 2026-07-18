# Angle coordinates for a cevian cut

## Statement
Let $ABC$ be a nondegenerate triangle whose angles, also denoted by $A,B,C$, are measured in degrees. Let $P$ be an interior point of $BC$, and put $x=\angle BAP$. Then $0<x<A$, and the angle triples of the two triangles $ABP$ and $ACP$ are respectively
\[
(B,x,180^\circ-B-x)\quad\text{and}\quad(C,A-x,B+x).
\]
Conversely, every real $x$ with $0<x<A$ is obtained from a unique interior point $P$ of $BC$.

## Proof
The angles of $ABP$ at $B$ and $A$ are $B$ and $x$, so its angle at $P$ is $180^\circ-B-x$. The angles of $ACP$ at $C$ and $A$ are $C$ and $A-x$, so its angle at $P$ is
\[
180^\circ-C-(A-x)=180^\circ-A-C+x=B+x.
\]
Because $AP$ lies strictly inside $\angle BAC$, we have $0<x<A$.

Conversely, for $0<x<A$, draw from $A$ the ray inside $\angle BAC$ making angle $x$ with $AB$. The portion of this ray sufficiently close to $A$ lies in the interior of the convex triangle $ABC$. When the ray first meets the boundary again, it cannot meet $AB$ or $AC$, since its direction is strictly between those two sides. It therefore meets $BC$ at an interior point $P$. Uniqueness follows because a ray and the segment $BC$ have at most one intersection. $\square$
