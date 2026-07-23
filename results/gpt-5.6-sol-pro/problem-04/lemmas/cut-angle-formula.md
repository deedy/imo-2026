# Lemma: normalized angle triples after a cevian cut

## Statement
Let a triangle have angles $a,b,c$ in some fixed angular unit, with total $s=a+b+c$. Cut from the vertex of angle $a$ to the interior of the opposite side, splitting $a$ into $x$ and $a-x$, where $0<x<a$. Then, after assigning $b$ to the child adjacent to the part $x$, the two resulting triangles have angle triples
\[
(b,x,s-b-x),\qquad(c,a-x,b+x).
\]
Conversely, every real $x$ with $0<x<a$ is realized by exactly one ray from that vertex meeting the interior of the opposite side.

## Proof
In the child containing the angles $b$ and $x$, the third angle is $s-b-x$, because a triangle's angle sum is $s$. The angle at the cut point in the other child is supplementary to this third angle, so in the chosen unit it equals
\[
s-(s-b-x)=b+x.
\]
The other two angles in that child are $c$ and $a-x$, proving the formulas.

For $0<x<a$, the unique ray inside the original angle that makes angle $x$ with the side adjacent to $b$ lies strictly inside the angular region. It must meet the opposite side in its interior: a ray inside a convex triangle exits the triangle through the side not incident with its starting vertex, and strictness excludes either endpoint. Thus the cut exists. Uniqueness follows from uniqueness of the ray with prescribed direction. $\square$
