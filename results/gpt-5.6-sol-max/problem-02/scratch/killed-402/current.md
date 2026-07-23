# imo-2026-02 — tracking file
## Status
partial

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Midpoint-doubling / auxiliary triangles (active and promising).** Reflect $B$ in $K$ to a point $P$, and reflect $C$ in $L$ to a point $Q$. Then $MK\parallel AP$ and $NL\parallel AQ$. This converts all three angle equalities into angle data for the auxiliary triangles $ABP$ and $ACQ$ and yields explicit sine-rule formulae for $K,L$.
- **Coordinate/trigonometric translation (active).** Place $A=0$, $AB$ on the positive real axis, and $AC$ at argument $\alpha$. Derived a compatibility equation in the four relevant angles. It remains to factor/simplify it and connect it rigorously to the circumcenter condition.
- **Direct synthetic angle chase (paused).** Looked for immediate cyclic quadrilaterals and spiral similarities among $A,B,C,K,L,M,N$; no complete configuration has yet emerged.

## Current best
Let $x=\angle KBA=\angle ACL$, $y=\angle LBK=\angle LNC$, and $z=\angle LCK=\angle BMK$, and put $\alpha=\angle BAC$, $AB=c$, $AC=b$. If $P=2K-B$ and $Q=2L-C$, then $MK\parallel AP$ and $NL\parallel AQ$. With the configuration's orientations, the sine rule gives $AP=c\sin x/\sin(x+z)$ and $AQ=b\sin x/\sin(x+y)$, hence explicit complex-coordinate expressions for $K,L$. Imposing the remaining directions of $BL$ and $CK$ gives two scalar equations and therefore one compatibility relation among $\alpha,x,y,z$. The main open gaps are (i) verifying/factoring this relation with all orientation and interior inequalities handled and (ii) deriving from it that the circumcenter of $AKL$ lies on the perpendicular bisector of $MN$.

## Full proof
We record the established reduction. Set
\[
 x=\angle KBA=\angle ACL,\qquad y=\angle LBK=\angle LNC,
 \qquad z=\angle LCK=\angle BMK,
\]
and $\alpha=\angle BAC$, $AB=c$, $AC=b$. Let $P$ be the reflection of $B$ in $K$, and let $Q$ be the reflection of $C$ in $L$. In triangle $ABP$, the points $M,K$ are the midpoints of $AB,BP$, so $MK\parallel AP$. Likewise, in triangle $ACQ$, $N,L$ are the midpoints of $AC,CQ$, so $NL\parallel AQ$. Thus (subject to the directed-angle orientations, which still need to be written out rigorously)
\[
 \angle PBA=x,\quad \angle BAP=z,
 \qquad \angle ACQ=x,\quad \angle QAC=y.
\]
The sine rule consequently gives
\[
 AP=c\frac{\sin x}{\sin(x+z)},\qquad
 AQ=b\frac{\sin x}{\sin(x+y)}.
\]
Putting $A=0$, $B=c$, and $C=be^{i\alpha}$, this yields
\[
 K=\frac c2\left(1+\frac{\sin x}{\sin(x+z)}e^{iz}\right),
 \qquad
 L=\frac b2e^{i\alpha}\left(1+\frac{\sin x}{\sin(x+y)}e^{-iy}\right).
\]
A preliminary directed-line calculation using $\arg(BL)=\pi-x-y$ and $\arg(CK)=\alpha+\pi+x+z$ gives
\[
2c\sin(x+y)=b\left(\sin(\alpha+x+y)+
 \frac{\sin x\sin(\alpha+x)}{\sin(x+y)}\right),
\]
\[
2b\sin(x+z)=c\left(\sin(\alpha+x+z)+
 \frac{\sin x\sin(\alpha+x)}{\sin(x+z)}\right).
\]
These formulas are currently provisional pending a complete orientation check. Their product eliminates $b/c$ and is the compatibility relation to be analyzed. The proof is not yet complete.
