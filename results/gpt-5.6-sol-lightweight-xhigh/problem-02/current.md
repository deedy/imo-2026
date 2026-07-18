# imo-2026-02 — tracking file
## Status
solved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Angle coordinates:** Put $x=\angle KBA=\angle ACL$, $y=\angle LBK=\angle LNC$, and $z=\angle LCK=\angle BMK$. The two small triangles $BMK$ and $CNL$ give explicit coordinates for $K$ and the relation between $L$ and $N$.
- **Raw Cartesian and complex elimination:** Both verify the theorem, but unorganized expansion produces expressions too long for a rigorous olympiad write-up.
- **Tangent/homogeneous vector factorization:** This gives a compact exact relation between the desired circle determinant and the remaining line-incidence equation.
- **Complex unit-exponential factorization:** This independently gives the same relation. Its one-line “substitute and simplify” proof was too terse.
- **Invariant reorganization (current):** Instead of expanding the coordinates of $N$, write $L=\lambda N$, reduce both determinants to $K\cdot L$, $[K,L]$, and $|L|^2$, and then compare the four coefficients of the ray parameter. This yields a short invariant expansion and an explicit four-row coefficient check, completing the factorization.

## Current best
A complete analytic proof is given below. After normalizing $A=0$, $B=2$, the three given angle equalities provide explicit coordinates for $K,L,N$. The remaining incidence condition is $[K-2N,e^{i(x+z)}N]=0$. A proved determinant factorization shows that the difference of the powers of $M$ and $N$ with respect to $(AKL)$ is a scalar multiple of this incidence determinant. Hence the powers are equal, which is exactly $OM=ON$.

## Full proof
We identify the Euclidean plane with $\mathbb C$. After a similarity and, if necessary, a reflection, take
\[
 A=0,\qquad B=2,\qquad M=1,
\]
with $C$ in the upper half-plane. Lower-case letters will also denote the complex coordinates of the corresponding upper-case points. Put
\[
 x=\angle KBA=\angle ACL,\qquad
 y=\angle LBK=\angle LNC,\qquad
 z=\angle LCK=\angle BMK.
\]
All three numbers are positive. Moreover, the nondegenerate triangles $BMK$ and $CNL$ give
\[
 0<x+z<\pi,\qquad 0<x+y<\pi. \tag{1}
\]
In particular, the sines occurring below are nonzero.

Because $K$ is inside triangle $BMC$, the ray $BK$ lies above $BA$. Since $K$ is inside $\angle LBA$ and $\angle LBK=y$, the ray $BL$ is obtained by turning through $x+y$ from $BA$ toward the interior of $\angle ABC$. Hence, with $t=BL>0$,
\[
 l=2-te^{-i(x+y)}. \tag{2}
\]
In triangle $BMK$, we have $BM=1$, the angles at $B,M$ are $x,z$, respectively, and the angle at $K$ is $\pi-x-z$. The sine rule and the direction of $MK$ therefore give
\[
 k=1+\frac{\sin x}{\sin(x+z)}e^{iz}. \tag{3}
\]
Also $C=2N$. In triangle $CNL$, the angles at $C,N$ are $x,y$: indeed, $C,N,A$ are collinear and $\angle NCL=\angle ACL=x$, while $\angle LNC=y$. Thus the sine rule gives
\[
 \frac{NL}{CN}=\frac{\sin x}{\sin(x+y)}.
\]
The ray $NL$ is obtained from $NC$ by a clockwise turn through $y$, so
\[
 l=n+\frac{\sin x}{\sin(x+y)}e^{-iy}n=\lambda n,
 \qquad
 \lambda=1+\frac{\sin x}{\sin(x+y)}e^{-iy}. \tag{4}
\]
Finally, $L$ lies inside $\angle ACK$ and $\angle ACL=x$, $\angle LCK=z$. Consequently the direction of $CK$ is obtained from that of $CA=-n$ by turning through $x+z$ toward the interior of $\angle ACB$. It follows that $k-2n$ is a real multiple of $e^{i(x+z)}n$. If
\[
 [u,v]=\operatorname{Im}(\bar u v),
\]
this is precisely
\[
 Q:=[k-2n,e^{i(x+z)}n]=0. \tag{5}
\]

We shall use the following algebraic identity, proved below.

**Factorization lemma.** Under (2)--(4),
\[
\begin{aligned}
D:={}&[k,l](|n|^2-1)-[k,n-1]|l|^2+[l,n-1]|k|^2\\
={}&\frac{\sin x\,(t\sin x+\sin y)}
{\sin(x+y)\sin(x+z)}
[k-2n,e^{i(x+z)}n]. \tag{6}
\end{aligned}
\]

Assuming the lemma, (5) and (6) yield $D=0$. It remains to explain why this is the desired conclusion. Let $o$ be the coordinate of the circumcenter $O$. Since the circle $(AKL)$ passes through the origin, its power function is
\[
 \mathcal P(w)=|w-o|^2-|o|^2=|w|^2-2\operatorname{Re}(\bar o w).
\]
The equations $\mathcal P(k)=\mathcal P(l)=0$ are
\[
 2O\mathbin\cdot K=|k|^2,\qquad 2O\mathbin\cdot L=|l|^2. \tag{7}
\]
The equality $\mathcal P(n)=\mathcal P(1)$ is equivalently
\[
 2O\mathbin\cdot(N-M)=|n|^2-1. \tag{8}
\]
The determinant of the three equations (7)--(8), viewed as equations in the two coordinates of $2O$, is
\[
\det\begin{pmatrix}
 \operatorname{Re}k&\operatorname{Im}k&|k|^2\\
 \operatorname{Re}l&\operatorname{Im}l&|l|^2\\
 \operatorname{Re}(n-1)&\operatorname{Im}(n-1)&|n|^2-1
\end{pmatrix}=D.
\]
Because $A,K,L$ are noncollinear, the first two rows determine $O$ uniquely; hence $D=0$ implies (8). Therefore
\[
 |ON|^2-|OM|^2=\mathcal P(n)-\mathcal P(1)=0,
\]
and so $OM=ON$.

### Verification of the factorization lemma
First suppose that $\cos y\cos z\ne0$. We have $0<x<\pi/2$: indeed, the ray $BK$ is inside $\angle ABC$ and the ray $CL$ is inside $\angle ACB$, so $x$ is smaller than both of those angles, while the latter cannot both be at least $\pi/2$. Put
\[
 p=\tan x,\qquad q=\tan y,\qquad s=\tan z,
 \qquad r=t\cos x\cos y. \tag{15}
\]
The signs of $q,s,r$ will not matter. By (1), $p+q$ and $p+s$ are nonzero. Dividing the coordinate formulas (2)--(4) by the appropriate products of cosines gives
\[
 K=\left(\frac{2p+s}{p+s},\frac{ps}{p+s}\right),\qquad
 L=(2-r(1-pq),r(p+q)), \tag{16}
\]
and
\[
 L=\lambda N,\qquad
 \lambda=U+iV,\qquad
 U=\frac{2p+q}{p+q},\qquad V=-\frac{pq}{p+q}. \tag{17}
\]
Set
\[
 W=U^2+V^2,\qquad P=K\mathbin\cdot L,\qquad C=[K,L].
\]
Since $N=\bar\lambda L/W$, we obtain
\[
 K\mathbin\cdot N=\frac{UP+VC}{W},\qquad
 [K,N]=\frac{UC-VP}{W},\qquad
 |N|^2=\frac{|L|^2}{W},\qquad
 [L,N]=-\frac{V|L|^2}{W}. \tag{18}
\]
Using $[K,N-1]=[K,N]+K_y$ and $[L,N-1]=[L,N]+L_y$ in the definition of $D$, and then substituting (18), yields
\[
 WD=C\bigl((1-U)|L|^2-W\bigr)
  +|L|^2\{V(P-|K|^2)-WK_y\}+WL_y|K|^2. \tag{19}
\]

We also replace rotation through $x+z$ by the nonzero real multiple
\[
 T=(1-ps)+i(p+s)=\frac{e^{i(x+z)}}{\cos x\cos z}.
\]
Put $Q_T=[K-2N,TN]$. If $T=\alpha+i\beta$, then
$[X,TY]=\alpha[X,Y]+\beta X\mathbin\cdot Y$. Applying this with
$\alpha=1-ps$, $\beta=p+s$, and using (18), gives
\[
 WQ_T=C\bigl((1-ps)U+(p+s)V\bigr)
 +P\bigl((p+s)U-(1-ps)V\bigr)-2(p+s)|L|^2. \tag{20}
\]

For completeness, we now verify the polynomial identity obtained from (19)--(20). Abbreviate
\[
 d=p+q,\qquad e=p+s,\qquad a=1-pq,
 \qquad g=(1+p^2)(1+q^2),\qquad j=\frac pd.
\]
Write $K=(u,v)$. Formula (16) gives the two useful linear relations
\[
 v=p(2-u),\qquad e(u-1)=p. \tag{21}
\]
Writing $P=P_0+P_1r$ and $C=C_0+C_1r$, direct multiplication in (16) gives
\[
 P_0=2u,\quad P_1=-au+dv,
 \qquad C_0=-2v,\quad C_1=du+av, \tag{22}
\]
whereas
\[
 |L|^2=4-4ar+gr^2,\quad L_y=dr,
 \quad U=1+j,\quad V=-qj,
 \quad W=1+2j+j^2(1+q^2). \tag{23}
\]
Define
\[
 X=C_0+q(P_0-|K|^2),\qquad Y=C_1+qP_1,
 \qquad Z=-jX-Wv,\qquad Z_1=-jY. \tag{24}
\]
From (19) and (22)--(24), collection by powers of $r$ gives
\[
 WD=A_0+A_1r+A_2r^2+A_3r^3, \tag{25}
\]
where
\[
\begin{aligned}
 A_0&=-WC_0+4Z,\\
 A_1&=-WC_1-4aZ+4Z_1+Wd|K|^2,\\
 A_2&=gZ-4aZ_1,\\
 A_3&=gZ_1.
\end{aligned} \tag{26}
\]
Similarly, on putting
\[
 \alpha=(1-ps)U+eV=(1-p(e-p))(1+j)-eqj,
\]
\[
 \beta=eU-(1-ps)V=e(1+j)+(1-p(e-p))qj,
\]
formula (20) gives
\[
 WQ_T=B_0+B_1r+B_2r^2, \tag{27}
\]
where
\[
 B_0=C_0\alpha+P_0\beta-8e,
 \qquad B_1=C_1\alpha+P_1\beta+8ea,
 \qquad B_2=-2eg. \tag{28}
\]
Thus
\[
 de\,WD=p\bigl(q+p(1+q^2)r\bigr)WQ_T \tag{29}
\]
is equivalent to the following four coefficient equalities:
\[
\begin{aligned}
 deA_0&=pqB_0,\\
 deA_1&=p\{qB_1+p(1+q^2)B_0\},\\
 deA_2&=p\{qB_2+p(1+q^2)B_1\},\\
 deA_3&=p^2(1+q^2)B_2. \tag{30}
\end{aligned}
\]
Here is an explicit check, included to leave no algebra hidden. Let $R_i$ be the left side minus the right side in the $i$-th equality in (30), numbered from $0$ to $3$. Substitution from (21)--(28), using first $v=p(2-u)$, gives
\[
 R_0=\frac{4pq(1+p^2)}d\bigl(e(u-1)-p\bigr)(du-2p-q), \tag{31}
\]
\[
 R_1=\frac{1+p^2}{d}\bigl(e(u-1)-p\bigr)F_1,
 \qquad
 R_2=\frac{p(1+p^2)(1+q^2)}d\bigl(e(u-1)-p\bigr)F_2,
 \qquad R_3=0, \tag{32}
\]
where
\[
\begin{aligned}
 F_1={}&5p^3q^2u-10p^3q^2+4p^3u-8p^3
       +5p^2q^3u-4p^2q^3+4p^2qu\\
     &\quad+pq^2u+2pq^2+q^3u,\\
 F_2={}&p^3qu-2p^3q+p^2q^2u+4p^2+pqu+2pq+q^2u.
\end{aligned}
\]
(The displayed expressions follow by ordinary expansion of the short formulas (22)--(28).) The second relation in (21) makes every expression in (31)--(32) zero, proving (30), hence (29).

Because $W\ne0$ and $de\ne0$, (29) gives
\[
 D=\frac{p\{q+p(1+q^2)r\}}{de}\,Q_T. \tag{33}
\]
Now
\[
 Q_T=\frac{Q}{\cos x\cos z}
\]
and, using (15),
\[
 \frac{p\{q+p(1+q^2)r\}}{(p+q)(p+s)\cos x\cos z}
 =\frac{\sin x\,(t\sin x+\sin y)}
 {\sin(x+y)\sin(x+z)}. \tag{34}
\]
Indeed, substitute $p=\sin x/\cos x$, $q=\sin y/\cos y$, $s=\sin z/\cos z$, and $r=t\cos x\cos y$; cancellation gives (34). Equations (33)--(34) prove (6) when $\cos y\cos z\ne0$.

Finally, both sides of (6), with $k,l,n,\lambda$ defined by (2)--(4), are continuous functions of $(x,y,z,t)$ wherever $\sin(x+y)\sin(x+z)\ne0$. Every point with $\cos y\cos z=0$ is a limit of points satisfying the same sine nonvanishing conditions and $\cos y\cos z\ne0$. Therefore (6) follows there by continuity as well. This completes the proof of the factorization lemma and of the theorem.
