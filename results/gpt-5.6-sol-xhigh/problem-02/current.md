# imo-2026-02 — tracking file
## Status
partial

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Angle coordinates:** Put $x=\angle KBA=\angle ACL$, $y=\angle LBK=\angle LNC$, and $z=\angle LCK=\angle BMK$. The two small triangles $BMK$ and $CNL$ give explicit coordinates for $K$ and the relation between $L$ and $N$.
- **Raw Cartesian and complex elimination:** Both verify the theorem, but unorganized expansion produces expressions too long for a rigorous olympiad write-up.
- **Tangent/homogeneous vector factorization:** This gives a compact exact relation between the desired circle determinant and the remaining line-incidence equation.
- **Complex unit-exponential factorization:** This independently gives the same relation. Its one-line “substitute and simplify” proof was too terse.
- **Invariant reorganization (current):** Instead of expanding the coordinates of $N$, write $L=\lambda N$, reduce both determinants to $K\cdot L$, $[K,L]$, and $|L|^2$, and then compare the four coefficients of the ray parameter. This has reduced the open algebra to a small coefficient table.

## Current best
The complete geometric reduction is written below. The factorization lemma is now reduced, for generic $y,z$, to tangent variables $p=\tan x,q=\tan y,s=\tan z$ and a scaled ray parameter $r$. Writing $\lambda=U+iV$, $W=|\lambda|^2$, $P=K\cdot L$, $C=[K,L]$, and using the non-unit rotation $T=(1-ps)+i(p+s)$, direct invariant calculations give
\[
WD=C((1-U)|L|^2-W)+|L|^2\{V(P-|K|^2)-WK_y\}+W L_y|K|^2,
\]
\[
WQ=C((1-ps)U+(p+s)V)+P((p+s)U-(1-ps)V)-2(p+s)|L|^2.
\]
Here $P,C$ are linear and $|L|^2$ is quadratic in $r$; their explicit formulas are now recorded in (12). It remains only to display and verify the resulting four coefficient equalities proving
\[
(p+q)(p+s)D=p\bigl(p(1+q^2)r+q\bigr)Q.
\]
Continuity then handles $\cos y\cos z=0$ and conversion back gives the desired trigonometric coefficient.

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

We shall use the following algebraic identity, whose coefficient verification is being completed below.

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
For the moment suppose $\cos y\cos z\ne0$. Since $x$ is smaller than both $\angle ABC$ and $\angle ACB$, and these two angles cannot both be at least $\pi/2$, we have $0<x<\pi/2$. Put
\[
 p=\tan x,\qquad q=\tan y,\qquad s=\tan z,
 \qquad r=t\cos x\cos y.
\]
Then (2)--(4), in Cartesian coordinates, become
\[
 K=\left(\frac{2p+s}{p+s},\frac{ps}{p+s}\right),\quad
 L=(2-r(1-pq),r(p+q)),\quad L=\lambda N,
\]
where
\[
 \lambda=U+iV,
 \qquad U=\frac{2p+q}{p+q},\qquad V=-\frac{pq}{p+q}.
\]
Set $W=U^2+V^2$, $P=K\cdot L$, and $C=[K,L]$. Since $N=\bar\lambda L/W$, we have
\[
 K\cdot N=\frac{UP+VC}{W},\qquad [K,N]=\frac{UC-VP}{W},
 \qquad |N|^2=\frac{|L|^2}{W}. \tag{9}
\]
Also $[L,N]=-V|N|^2$. Substitution of (9) into the definition of $D$ gives
\[
 WD=C((1-U)|L|^2-W)+|L|^2\{V(P-|K|^2)-WK_y\}+WL_y|K|^2. \tag{10}
\]
The non-unit complex multiplier
\[
 T=(1-ps)+i(p+s)=\frac{e^{i(x+z)}}{\cos x\cos z}
\]
will be used in place of the rotation $e^{i(x+z)}$. If $Q_T=[K-2N,TN]$, (9) similarly gives
\[
 WQ_T=C((1-ps)U+(p+s)V)+P((p+s)U-(1-ps)V)-2(p+s)|L|^2. \tag{11}
\]
For the coefficient comparison, abbreviate
\[
 d=p+q,\qquad e=p+s,\qquad a=1-pq,\qquad
 H=(2p+q)^2+p^2q^2.
\]
The elementary quantities needed in (10)--(11) are
\[
 W=\frac H{d^2},\quad |K|^2=\frac{(2p+s)^2+p^2s^2}{e^2},\quad
 |L|^2=4-4ar+(1+p^2)(1+q^2)r^2,
\]
\[
 P=\frac{2(2p+s)+r\{-a(2p+s)+psd\}}e,
 \qquad
 C=\frac{-2ps+r\{d(2p+s)+psa\}}e. \tag{12}
\]
Thus both sides of the required polynomial identity
\[
 de\,WD=p\bigl(q+p(1+q^2)r\bigr)WQ_T \tag{13}
\]
have degree at most three in $r$.  Expanding (10)--(12) and checking the four coefficients of $r$ will complete the proof.  The explicit coefficient table is the only remaining gap.
