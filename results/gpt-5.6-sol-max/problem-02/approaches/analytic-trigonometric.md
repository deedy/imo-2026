# Analytic/trigonometric approach

## Idea
Orient $ABC$ counterclockwise and introduce
\[
\alpha=\angle BAC,\quad\beta=\angle ABC,\quad\gamma=\angle ACB,
\]
and
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,
\quad z=\angle LCK=\angle BMK.
\]
The ray orders forced by the interior assumptions are $BA,BK,BL,BC$ at $B$ and $CA,CL,CK,CB$ at $C$.

Let $AB=c,AC=b,BC=a$. Sine-law calculations give
\[
BK=r=\frac c2\frac{\sin z}{\sin(x+z)},\qquad
CL=d=\frac b2\frac{\sin y}{\sin(x+y)}.
\]
On the other hand, triangles $BCK$ and $BCL$ give
\[
r=a\frac{\sin(\gamma-x-z)}{\sin(\alpha+2x+z)},\qquad
d=a\frac{\sin(\beta-x-y)}{\sin(\alpha+2x+y)}. \tag{1}
\]
These are two separate trigonometric constraints on $z$ and $y$.

Use unit vectors along $AB,AC$ as an oblique basis. If a point is $s\mathbf e_{AB}+t\mathbf e_{AC}$, a circle through $A$ has equation
\[
s^2+t^2+2st\cos\alpha-ps-qt=0. \tag{2}
\]
Its centre is $O$ with $p=2O\cdot\mathbf e_{AB}$ and $q=2O\cdot\mathbf e_{AC}$. Thus $OM=ON$ is equivalent to
\[
2bq-2cp=b^2-c^2. \tag{3}
\]
The coordinates of $K,L$ are
\[
K=\left(c-r\frac{\sin(\alpha+x)}{\sin\alpha},
 r\frac{\sin x}{\sin\alpha}\right),
\quad
L=\left(d\frac{\sin x}{\sin\alpha},
 b-d\frac{\sin(\alpha+x)}{\sin\alpha}\right). \tag{4}
\]
Substitution into (2), followed by use of (1), should prove (3). The remaining task is to find a clean factorization/trigonometric simplification suitable for an olympiad proof.

## Status
In progress. All formulas above have been derived directly; algebraic factorization remains.
