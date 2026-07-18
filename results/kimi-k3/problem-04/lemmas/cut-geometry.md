# Lemma: the cevian cut (angle bookkeeping)

**Statement.** Let the current triangle have vertices $X,Y,Z$ with angles
$A=\angle YXZ$ at $X$, $B=\angle XYZ$ at $Y$, $C=\angle XZY$ at $Z$, so
$A+B+C=180^\circ$. Let $P$ be an interior point of side $YZ$
and cut along $XP$ (this is exactly Mulan's move with cut vertex $X$: $P$ on the
perimeter, cut to the opposite vertex). Write $\alpha=\angle YXP$. Then:

1. The two resulting triangles have angle multisets
   $$H_1=\{B,\ \alpha,\ 180^\circ-B-\alpha\}\quad(\triangle XYP),\qquad
     H_2=\{C,\ A-\alpha,\ B+\alpha\}\quad(\triangle XZP).$$
2. Conversely, for every real $\alpha\in(0,A)$ there is an interior point $P$ of
   $YZ$ realizing $\angle YXP=\alpha$. Hence Mulan can, from a triangle with an
   angle $A$ at a chosen vertex, produce the pair $(H_1,H_2)$ above for any
   $\alpha\in(0,A)$, with the roles of $B$ and $C$ interchangeable (swap the
   labeling of $Y,Z$).

**Proof.**
(1) In $\triangle XYP$: since $P\in YZ$, the ray $YP$ coincides with the ray
$YZ$, so $\angle XYP=\angle XYZ=B$. The angle at $X$ is $\alpha$ by definition;
hence the angle at $P$ is $180^\circ-B-\alpha$. In $\triangle XZP$: similarly
$\angle XZP=C$, the angle at $X$ is $A-\alpha$, so the angle at $P$ is
$180^\circ-C-(A-\alpha)=180^\circ-A-C+\alpha=B+\alpha$, using $A+B+C=180^\circ$.

(2) The function $P\mapsto \angle YXP$ is continuous on the closed segment $YZ$;
as $P\to Y$ the ray $XP$ tends to the ray $XY$, so $\angle YXP\to 0$; as
$P\to Z$ the ray $XP$ tends to $XZ$, so $\angle YXP\to\angle YXZ=A$. By the
intermediate value theorem every value of $(0,A)$ is attained at an interior
point $P$ (different from the vertices). $\blacksquare$
