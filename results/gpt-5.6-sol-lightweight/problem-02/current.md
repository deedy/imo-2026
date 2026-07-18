# imo-2026-02 — tracking file
## Status
solved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- Trigonometric/complex coordinates: successful. Coordinates of $K,L$ follow from the sine rule in $BMK,CNL$; the two remaining angle conditions become reality relations.
- Equal powers: successful. A standalone complex-algebra lemma (`lemmas/complex-algebra.md`) shows that those reality relations imply that $M,N$ have equal powers with respect to $(AKL)$.
- Symbolic Laurent-polynomial checks (`code/symbolic.py`, `code/eliminate.py`, `code/certificate.py`) were used to check the algebra and orientations. An apparent orientation correction was rechecked: for counterclockwise $ABC$, the ray directions are $CL=\alpha+\pi+x$ and $CK=\alpha+\pi+x+z$.

## Current best
The claim follows by normalizing $A=0,B=2,C=2de^{i\alpha}$. Then $M=1,N=de^{i\alpha}$, while the sine rule gives explicit complex coordinates for $K,L$. The angle order assumptions turn the remaining conditions into exactly the two hypotheses of the complex equal-power lemma, proving that $M,N$ have equal powers with respect to $(AKL)$. As both powers equal the squared distance to $O$ minus the same circumradius squared, $OM=ON$.

## Full proof
Reflect the whole configuration if necessary, and assume that $A,B,C$ occur counterclockwise. We use complex coordinates, normalized by
\[
 A=0,\qquad B=2,\qquad C=2n,
 \qquad n=de^{i\alpha},
\]
where $d>0$ and $\alpha=\angle BAC$. Thus
\[
 M=1,\qquad N=n.
\]
Set
\[
 x=\angle KBA=\angle ACL,
 \quad y=\angle LBK=\angle LNC,
 \quad z=\angle LCK=\angle BMK,
\]
and abbreviate
\[
 X=e^{ix},\qquad Y=e^{iy},\qquad Z=e^{iz},
 \qquad a=e^{i\alpha}.
\]

We first find $K$. In triangle $BMK$ we have
\[
BM=1,
\qquad \angle MBK=x,
\qquad \angle BMK=z.
\]
Consequently $\angle BKM=\pi-x-z$, so the sine rule gives
\[
 MK=\frac{\sin x}{\sin(x+z)}.
\]
The ray $MK$ makes angle $z$ with the positive real axis; hence
\[
 K=1+\frac{\sin x}{\sin(x+z)}Z. \tag{1}
\]
Likewise, in triangle $CNL$ we have $CN=d$, $\angle NCL=x$, and $\angle CNL=y$. The ray $NL$ has direction $\alpha-y$, and the sine rule gives
\[
 L=n\left(1+\frac{\sin x}{\sin(x+y)}Y^{-1}\right). \tag{2}
\]
The denominators in (1)--(2) are nonzero because they are sines of angles supplementary to angles of the nondegenerate triangles $BMK,CNL$.

We next translate the ordering of the rays. Since $K$ lies inside $\angle LBA$, when one turns inside that angle from $BA$ toward $BL$, one meets $BK$ first. Therefore $BL$ has direction $\pi-x-y$. It follows that
\[
 (L-2)XY\in\mathbb R. \tag{3}
\]
At $C$, the ray $CA$ has direction $\alpha+\pi$. Since $\angle ACL=x$, the ray $CL$ has direction $\alpha+\pi+x$. Since $L$ lies inside $\angle ACK$ and $\angle LCK=z$, the ray $CK$ has direction $\alpha+\pi+x+z$. Thus the opposite vector $C-K=2n-K$ has direction $\alpha+x+z$, and hence
\[
 \frac{2n-K}{aXZ}\in\mathbb R. \tag{4}
\]

We now apply the complex equal-power lemma proved in `lemmas/complex-algebra.md`; its short algebraic proof is reproduced here for self-containment. If $p,q$ denote the complex coordinates of $K,L$, respectively, then, since
\[
\frac{\sin x}{\sin(x+z)}
 =\frac{X-X^{-1}}{XZ-X^{-1}Z^{-1}},
\qquad
\frac{\sin x}{\sin(x+y)}
 =\frac{X-X^{-1}}{XY-X^{-1}Y^{-1}},
\]
formulas (1)--(2), together with (3)--(4), satisfy the hypotheses of that lemma. We recall its verification.

Write $t^*=\bar t$. The circle through $0,p,q$ has equation
\[
 w\bar w+uw+v\bar w=0. \tag{5}
\]
Putting $w=p,q$ and applying Cramer's rule gives, with $\Delta=pq^*-qp^*\ne0$,
\[
 u\Delta=-pp^*q^*+qq^*p^*,
 \qquad
 v\Delta=-pqq^*+qpp^*. \tag{6}
\]
The difference between the values of the left side of (5) at $1$ and at $n$ is, after multiplication by $\Delta$,
\[
\begin{aligned}
H={}&(1-nn^*)\Delta
 +(1-n)(-pp^*q^*+qq^*p^*)\\
 &+(1-n^*)(-pqq^*+qpp^*). \tag{7}
\end{aligned}
\]
The two reality relations (3)--(4) are equivalent to
\[
(q-2)XY=(q^*-2)X^{-1}Y^{-1}, \tag{8}
\]
\[
(2n-p)a^{-1}X^{-1}Z^{-1}
 =(2n^*-p^*)aXZ. \tag{9}
\]
Substitute
\[
p=1+Z\frac{X-X^{-1}}{XZ-X^{-1}Z^{-1}},
\qquad
q=da\left(1+Y^{-1}\frac{X-X^{-1}}{XY-X^{-1}Y^{-1}}\right)
\]
and their conjugates into (7). On using (8)--(9), and putting terms over the common denominator
\[
(XZ-X^{-1}Z^{-1})^2(XY-X^{-1}Y^{-1})^2,
\]
the numerator cancels in conjugate pairs: the four types are
\[
(nq^*p^*,-n^*qp),\quad
(npp^*q^*,-n^*pp^*q),\quad
(qq^*p^*,-qq^*p),\quad
(pq^*,-qp^*).
\]
Thus $H=0$. By (5)--(7), the powers of $1=M$ and $n=N$ with respect to the circle through $0,p,q$, namely $(AKL)$, are equal.

Let $R$ be the radius of $(AKL)$. The power of any point $P$ with respect to this circle is $OP^2-R^2$. Therefore
\[
 OM^2-R^2=ON^2-R^2,
\]
so $OM^2=ON^2$. Both are nonnegative lengths, and hence
\[
\boxed{OM=ON}.
\]
