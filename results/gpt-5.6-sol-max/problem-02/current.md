# imo-2026-02 — tracking file
## Status
solved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Power/circle-equation reformulation:** rewrote $OM=ON$ as a linear relation between the coefficients of the circumcircle of $AKL$.
- **Angle parametrization and sine law:** introduced $\alpha,\beta,\gamma,x,y,z$ and derived exact sine-law expressions for $BK$ and $CL$.
- **Normalized-length quadratics:** set $R=2BK/AB$, $D=2CL/AC$ and eliminated $y,z$, obtaining two compact quadratic relations through a common polynomial $F$.
- **Oblique coordinates/full elimination:** verified the identity but initially produced unwieldy algebra; this route also exposed and corrected one false intermediate symbolic claim.
- **Cartesian circle computation:** used simple ray-direction coordinates for $K,L$. Sequential exact polynomial division yielded a sparse certificate expressing the target in terms of the two geometric quadratic relations and the identities $\sin^2+\cos^2=1$.
- **Synthetic/power exploration:** considered equal powers and inversion, but no comparably clear synthetic construction was found.

## Current best
A complete analytic proof has been obtained. With $S=\sin\alpha,C=\cos\alpha,U=\sin x,X=\cos x,V=\sin(\alpha+x)$, $R=2BK/AB$, and $D=2CL/AC$, the angle conditions imply
\[
2U\sin\beta=\sin\gamma\,F(R),\qquad
2U\sin\gamma=\sin\beta\,F(D),
\quad F(T)=V(T^2-2XT+2)-ST.
\]
A verified explicit polynomial identity then gives
\[
b(CP+SQ)-cP=\frac{b^2-c^2}{2}
\]
for the Cartesian coefficients of the circumcircle of $AKL$, which is exactly $OM^2-ON^2=0$. The sparse certificate and its scaling were independently checked by `code/verify_sparse_identity.py`; the ray orders, positivity of every divisor, coordinate directions, and all circle formulas have also been audited in `scratch/audit.md`.

## Full proof
Let
\[
\alpha=\angle BAC,
\qquad \beta=\angle ABC,
\qquad \gamma=\angle ACB,
\]
and set
\[
x=\angle KBA=\angle ACL,
\quad y=\angle LBK=\angle LNC,
\quad z=\angle LCK=\angle BMK.
\]
Also write
\[
a=BC,\qquad b=CA,\qquad c=AB.
\]

Because $K$ lies inside $\angle LBA$, the rays at $B$ occur in the order
\[
BA,\thinspace BK,\thinspace BL,\thinspace BC;
\]
because $L$ lies inside $\angle ACK$, the rays at $C$ occur in the order
\[
CA,\thinspace CL,\thinspace CK,\thinspace CB.
\]
In particular, all angles and sines used below have the indicated positive values.

### 1. Relations forced by the angle conditions

In $\triangle BMK$ we have $BM=c/2$, $\angle MBK=x$, and $\angle BMK=z$. Hence
\[
BK=\frac c2\frac{\sin z}{\sin(x+z)}. \tag{1}
\]
Moreover,
\[
\angle KBC=\beta-x,
\qquad \angle BCK=\gamma-x-z,
\]
so $\angle BKC=\alpha+2x+z$. Thus
\[
BK=a\frac{\sin(\gamma-x-z)}{\sin(\alpha+2x+z)}. \tag{2}
\]
Similarly, sine rule in $\triangle CNL$ and $\triangle BCL$ gives
\[
CL=\frac b2\frac{\sin y}{\sin(x+y)}
=a\frac{\sin(\beta-x-y)}{\sin(\alpha+2x+y)}. \tag{3}
\]

Normalize the circumdiameter of $ABC$ to $1$. Then
\[
a=\sin\alpha,
\qquad b=\sin\beta,
\qquad c=\sin\gamma. \tag{4}
\]
Put
\[
S=\sin\alpha,
\quad C=\cos\alpha,
\quad U=\sin x,
\quad X=\cos x,
\quad V=\sin(\alpha+x)=SX+CU, \tag{5}
\]
and
\[
R=\frac{2BK}{c},
\qquad D=\frac{2CL}{b}. \tag{6}
\]
Thus
\[
R=\frac{\sin z}{\sin(x+z)},
\qquad D=\frac{\sin y}{\sin(x+y)}. \tag{7}
\]

Let $(\theta,t,\rho)$ denote either $(\gamma,z,R)$ or $(\beta,y,D)$. Equating the appropriate expressions in (1)--(3) and using (4) gives
\[
\sin\theta\sin t\sin(\alpha+2x+t)
=2S\sin(x+t)\sin(\theta-x-t). \tag{8}
\]
Since $t>0$, divide by $\sin^2t$. From $\rho=\sin t/\sin(x+t)$,
\[
\cot t=\frac{1/\rho-X}{U}. \tag{9}
\]
Writing all terms in (8) in terms of $\cot t$ and using (9) yields
\[
-\rho^2\sin\theta\,U\sin(\alpha+x)
+\rho\sin\theta\bigl(\cos(\alpha-x)-X\cos(\alpha+2x)\bigr)
-2SU\sin(\theta-x)=0. \tag{10}
\]
We use
\[
\cos(\alpha-x)-X\cos(\alpha+2x)
=U\bigl(2CUX-2SU^2+3S\bigr), \tag{11}
\]
and
\[
\cot\gamma=\frac{b-Cc}{Sc},
\qquad
\cot\beta=\frac{c-Cb}{Sb}. \tag{12}
\]
Dividing (10) by $U\sin\theta$ and applying (11)--(12) gives
\[
2Ub=cF(R),
\qquad 2Uc=bF(D), \tag{13}
\]
where
\[
F(T)=V(T^2-2XT+2)-ST. \tag{14}
\]
Indeed, using $V=SX+CU$ and $U^2+X^2=1$,
\[
F(T)=VT^2-(2CUX-2SU^2+3S)T+2SX+2CU,
\]
which is exactly the expression obtained from (10).

### 2. The circle computation

Place
\[
A=(0,0),\qquad B=(c,0),\qquad C=(bC,bS).
\]
Put $W=\cos(\alpha+x)=CX-SU$. The ray $BK$ has direction $(-X,U)$ and the ray $CL$ has direction $(-W,-V)$, so
\[
K=\left(c-\frac{cRX}{2},\frac{cRU}{2}\right), \tag{15}
\]
\[
L=\left(bC-\frac{bDW}{2},bS-\frac{bDV}{2}\right). \tag{16}
\]
Consequently,
\[
|K|^2=c^2\left(1-RX+\frac{R^2}{4}\right),
\qquad
|L|^2=b^2\left(1-DX+\frac{D^2}{4}\right). \tag{17}
\]

Write the circumcircle of $AKL$ as
\[
\xi^2+\eta^2-P\xi-Q\eta=0. \tag{18}
\]
Its centre is $O=(P/2,Q/2)$. Set
\[
\Delta=K_xL_y-K_yL_x.
\]
Since the circumcentre is defined, $A,K,L$ are noncollinear, hence $\Delta\ne0$. Cramer's rule gives
\[
P=\frac{P_0}{\Delta},
\qquad Q=\frac{Q_0}{\Delta}, \tag{19}
\]
where
\[
P_0=|K|^2L_y-K_y|L|^2,
\qquad
Q_0=K_x|L|^2-|K|^2L_x. \tag{20}
\]
Define
\[
\mathcal T
=2\bigl(b(CP_0+SQ_0)-cP_0\bigr)-(b^2-c^2)\Delta. \tag{21}
\]
Let
\[
E_R=2Ub-cF(R),
\qquad E_D=2Uc-bF(D).
\]
Substituting (14)--(17) and (20)--(21), and collecting terms, gives the polynomial identity
\[
4V\mathcal T
=A_0E_R+B_0E_D+(C^2+S^2-1)G_0+(X^2+U^2-1)H_0, \tag{22}
\]
where
\[
A_0=bc\bigl(C^2DUb-CDUc+DS^2Ub-DSXc+2Sc\bigr),
\]
\[
B_0=bc\bigl(CRUb+RSXb-RUc-2Sb\bigr),
\]
\[
G_0=Ubc^2\bigl(2CDRUXb-2CDUb+2DRSX^2b-DRSb-2DSXb-2RUc\bigr),
\]
\[
H_0=Sbc\bigl(CDRUb^2-CDRUc^2+DRSXb^2-DRSXc^2-2DSb^2+2RSc^2\bigr).
\]
Identity (22) is verified by direct expansion of the displayed expressions.

By (13), $E_R=E_D=0$, and $C^2+S^2=X^2+U^2=1$. Also $V=\sin(\alpha+x)>0$: indeed $0<x<\gamma$, so $0<\alpha+x<\pi$. Hence (22) gives $\mathcal T=0$. By (19) and (21),
\[
b(CP+SQ)-cP=\frac{b^2-c^2}{2}. \tag{23}
\]

Finally,
\[
M=\left(\frac c2,0\right),
\qquad N=\left(\frac{bC}{2},\frac{bS}{2}\right).
\]
Since $O=(P/2,Q/2)$,
\[
\begin{aligned}
OM^2-ON^2
&=-\frac{cP}{2}+\frac{b(CP+SQ)}{2}+\frac{c^2-b^2}{4}\\
&=0
\end{aligned}
\]
by (23). Therefore $OM=ON$.
