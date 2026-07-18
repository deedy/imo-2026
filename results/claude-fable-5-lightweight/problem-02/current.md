# imo-2026-02 — tracking file

## Status
solved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Power-of-a-point reformulation (successful).** Via the median-length formula, $OM=ON \iff \operatorname{pow}(B,\omega)-\operatorname{pow}(C,\omega)=\tfrac12(AB^2-AC^2)$, where $\omega$ is the circumcircle of $AKL$.
- **Auxiliary points $X,Y$ (successful).** $Y:=\text{ray }BK\cap AC$, $X:=\text{ray }CL\cap AB$ (crossbar). The three angle hypotheses translate, via directed angles, into three concyclicities: $B,X,Y,C$ on $\omega_1$; $C,M,K,X$ on $\omega_K$; $B,N,L,Y$ on $\omega_L$ (with tangency of $AB$ to $\omega_K$ at $M$ in the degenerate case $X=M$, and of $AC$ to $\omega_L$ at $N$ when $Y=N$).
- **Affine power identity (the key step).** $F(Z):=\operatorname{pow}(Z,\omega)-\operatorname{pow}(Z,\omega_K)-\operatorname{pow}(Z,\omega_L)+\operatorname{pow}(Z,\omega_1)$ is an affine function of $Z$; it vanishes at the three non-collinear points $A,K,L$, hence identically. Evaluating at $B$ and $C$ gives $\operatorname{pow}(B,\omega)=\vec{BM}\cdot\vec{BX}$ and $\operatorname{pow}(C,\omega)=\vec{CN}\cdot\vec{CY}$; together with $AB\cdot AX=AC\cdot AY$ (power of $A$ w.r.t. $\omega_1$) and the median formula this yields $OM=ON$.
- **Dead end avoided:** first tried radical-axis arguments with the second intersection points $K^*,L^*$ of line $BY$ with $\omega_K$ and of $CX$ with $\omega_L$; it works but requires awkward tangency case analysis. The affine function $F$ replaces all of it.
- Numerical verification: `code/verify.py`, `code/check_signs.py`, `code/verify2.py` confirm every claim (several triangles; generic case; both tangency cases $X=M$ and $Y=N$; all signed-angle sign claims; $F\equiv0$; $OM=ON$) to machine precision.

## Current best
Complete rigorous proof below. Core of the argument: with $X=$ ray $CL\cap AB$, $Y=$ ray $BK\cap AC$, the hypotheses force $B,X,Y,C$, $C,M,K,X$ and $B,N,L,Y$ to be concyclic; then the affine function $\operatorname{pow}(\cdot,\omega)-\operatorname{pow}(\cdot,\omega_K)-\operatorname{pow}(\cdot,\omega_L)+\operatorname{pow}(\cdot,\omega_1)$ vanishes at $A,K,L$, hence everywhere; evaluating at $B,C$ and using $AB\cdot AX=AC\cdot AY$ and the median-length formula gives $OM=ON$.

## Full proof

### 0. Conventions and notation

We identify the plane with $\mathbb{C}$. For $u,v\in\mathbb{C}$ write
$$\langle u,v\rangle=\operatorname{Re}(\bar u v),\qquad u\times v=\operatorname{Im}(\bar u v),$$
the usual dot and cross products of plane vectors.

**Unsigned angles.** For points $P,Q\ne V$, $\ \angle PVQ\in[0^\circ,180^\circ]$ is the ordinary (unsigned) angle, i.e. $\angle PVQ=|\arg\frac{Q-V}{P-V}|$ with $\arg\in(-180^\circ,180^\circ]$.

**Signed ray angles.** For nonzero $u,v$ let $\measuredangle(u\to v):=\arg\frac{v}{u}\in(-180^\circ,180^\circ]$. For rays from $V$ through $P$ and through $Q$ put $\measuredangle(VP\to VQ):=\measuredangle\big((P-V)\to(Q-V)\big)$. Since $\frac{v}{u}=\frac{\bar u v}{|u|^2}$ we have:

> **(0.1)** $|\measuredangle(u\to v)|=\angle(u,v)$ (the unsigned angle), and if $u\times v\neq0$ then the sign of $\measuredangle(u\to v)$ equals the sign of $u\times v$. Moreover $\measuredangle(u\to w)\equiv\measuredangle(u\to v)+\measuredangle(v\to w)\pmod{360^\circ}$ and $\measuredangle(v\to u)\equiv-\measuredangle(u\to v)\pmod{360^\circ}$ (because $\arg$ is additive mod $360^\circ$ under multiplication and $\arg(u/v)=-\arg(v/u)$ mod $360^\circ$).

**Directed line angles.** For lines $\ell_1,\ell_2$ with direction vectors $d_1,d_2\ne 0$ set
$$\angle(\ell_1,\ell_2):=\arg\tfrac{d_2}{d_1}\ \bmod\,180^\circ .$$
This is well defined: replacing $d_i$ by a nonzero real multiple changes $\arg\frac{d_2}{d_1}$ by $0^\circ$ or $180^\circ$. It is additive mod $180^\circ$, and $\angle(\ell_1,\ell_2)\equiv0$ iff $\ell_1\parallel\ell_2$ (including $\ell_1=\ell_2$). If rays $r_1,r_2$ span the lines $\ell_1,\ell_2$, then $\angle(\ell_1,\ell_2)\equiv\measuredangle(r_1\to r_2)\pmod{180^\circ}$. For points we write $\angle(PQ,RS)$ for the directed angle from line $PQ$ to line $RS$.

**Power of a point.** For a circle $\Gamma$ with centre $Z_0$ and radius $\rho>0$ and a point $Z$, $\operatorname{pow}(Z,\Gamma):=|Z-Z_0|^2-\rho^2$.

**Sides of a line.** For a line through $P$ with direction $d$, points $Z_1,Z_2$ are *strictly on the same side* iff $d\times(Z_1-P)$ and $d\times(Z_2-P)$ are nonzero of equal sign; *strictly opposite sides* iff nonzero of opposite signs.

**Interior of a triangle / of an angle.** For an affinely independent triple $P,Q,R$, the (open) interior of triangle $PQR$ is $\{\alpha P+\beta Q+\gamma R:\ \alpha,\beta,\gamma>0,\ \alpha+\beta+\gamma=1\}$; "inside triangle $PQR$" means lying in this set. For $0^\circ<\angle QVR<180^\circ$, "$P$ lies inside angle $QVR$" means: $P$ is strictly on the same side of line $VQ$ as $R$ and strictly on the same side of line $VR$ as $Q$.

Throughout, $b:=AC=|C-A|$, $c:=AB=|B-A|$, and
$$\theta:=\angle KBA=\angle ACL,\qquad \varphi:=\angle LBK=\angle LNC,\qquad \psi:=\angle LCK=\angle BMK ,$$
$\omega$ denotes the circumcircle of triangle $AKL$ and $O$ its centre, $R_\omega=|OA|$ its radius. Since the problem speaks of *triangle* $AKL$ and its circumcentre, the points $A,K,L$ are pairwise distinct and not collinear; this is part of the hypothesis.

Reflections, rotations and translations of the plane preserve all hypotheses and the conclusion, so **we may and do assume that $ABC$ is positively oriented**:
$$\delta:=(B-A)\times(C-A)>0. \tag{0.2}$$

---

### 1. Preliminary lemmas

**Lemma 1 (line–circle intersections and power).**
Let $\Gamma$ be a circle with centre $Z_0$, radius $\rho>0$, and let $\ell$ be a line.
(i) $\ell\cap\Gamma$ has at most two points.
(ii) If $M\in\Gamma$, there is exactly one line through $M$ meeting $\Gamma$ only at $M$ (the **tangent** at $M$); its direction is $i(M-Z_0)$, i.e. it is the line through $M$ perpendicular to $MZ_0$.
(iii) If $Z\in\ell$ and $\ell$ meets $\Gamma$ at $U$ and $V$ — where in the tangent case we set $U=V$ — then
$$\operatorname{pow}(Z,\Gamma)=\langle U-Z,\ V-Z\rangle ,$$
the product of signed lengths $ZU\cdot ZV$ along $\ell$.

*Proof.* Parametrize $\ell=\{Z+td:\ t\in\mathbb{R}\}$ with $|d|=1$, $Z\in \ell$ arbitrary. Then
$$|Z+td-Z_0|^2-\rho^2=t^2+2t\,\langle d,Z-Z_0\rangle+\operatorname{pow}(Z,\Gamma), \tag{1.1}$$
a monic real quadratic in $t$; it has at most two roots, proving (i). For (ii): take $Z=M\in\Gamma$; then $\operatorname{pow}(M,\Gamma)=0$ and the roots are $t=0$ and $t=-2\langle d,M-Z_0\rangle$; they coincide iff $\langle d,M-Z_0\rangle=0$, i.e. iff $d\perp(M-Z_0)$, i.e. iff $d$ is a real multiple of $i(M-Z_0)$; that determines a unique line through $M$. For (iii): if $U=Z+t_1d$, $V=Z+t_2d$ (with $t_1=t_2$ in the tangent case, when (1.1) has a double root), then by Vieta $t_1t_2=\operatorname{pow}(Z,\Gamma)$, and $\langle U-Z,V-Z\rangle=t_1t_2\langle d,d\rangle=t_1t_2$. $\square$

**Lemma 2 (directed inscribed-angle criterion).**
Let $P,Q,R$ be pairwise distinct, non-collinear points and let $\Gamma$ be the (unique) circle through them. Then for every point $S\notin\{P,Q\}$:
$$S\in\Gamma\iff \angle(SP,\,SQ)\equiv\angle(RP,\,RQ)\pmod{180^\circ}.$$

*Proof.* Uniqueness of $\Gamma$ is classical (its centre is the common point of the perpendicular bisectors of $PQ$ and $PR$, which are not parallel).

Put $w:=(Q-R)\overline{(P-R)}\ne0$. Since $\frac{Q-R}{P-R}=\frac{w}{|P-R|^2}$ and $P,Q,R$ are not collinear, $\arg\frac{Q-R}{P-R}\not\equiv0\pmod{180^\circ}$, i.e. $w\notin\mathbb{R}$, so $\operatorname{Im}w\ne0$.

Define $g:\mathbb{C}\to\mathbb{R}$ by $g(Z):=\operatorname{Im}\big[w\,(P-Z)\overline{(Q-Z)}\big]$. Expanding $(P-Z)\overline{(Q-Z)}=P\bar Q-P\bar Z-\bar Q Z+|Z|^2$ shows
$$g(Z)=(\operatorname{Im}w)\,|Z|^2+\lambda(Z)$$
with $\lambda$ a real affine function of $Z\in\mathbb R^2$. Hence $\tfrac{1}{\operatorname{Im}w}\,g(Z)=|Z-Z_1|^2-\rho_1$ for some $Z_1\in\mathbb{C},\rho_1\in\mathbb{R}$, so the zero set $\{g=0\}$ is empty, a single point, or a circle. Now
$$g(P)=0,\qquad g(Q)=0,\qquad g(R)=\operatorname{Im}\big[(Q-R)\overline{(P-R)}(P-R)\overline{(Q-R)}\big]=\operatorname{Im}\big[|P-R|^2|Q-R|^2\big]=0 .$$
So $\{g=0\}$ contains three distinct non-collinear points, hence it is a circle through $P,Q,R$; by uniqueness $\{g=0\}=\Gamma$.

Finally, fix $S\notin\{P,Q\}$. All four numbers $Q-S,\,P-S,\,Q-R,\,P-R$ are nonzero, and
$$\angle(SP,SQ)\equiv\angle(RP,RQ)\pmod{180^\circ}
\iff \arg\Big[\tfrac{Q-S}{P-S}\Big]\equiv\arg\Big[\tfrac{Q-R}{P-R}\Big]\pmod{180^\circ}
\iff \tfrac{Q-S}{P-S}\cdot\overline{\Big(\tfrac{Q-R}{P-R}\Big)}\in\mathbb{R}\setminus\{0\} .$$
Multiplying by the positive real $|P-S|^2|P-R|^2$, the last condition is equivalent to
$(Q-S)\overline{(P-S)}\cdot\overline{(Q-R)}(P-R)\in\mathbb{R}$, i.e. (taking conjugates) to
$w\,(P-S)\overline{(Q-S)}\in\mathbb{R}$, i.e. to $g(S)=0$, i.e. to $S\in\Gamma$. $\square$

**Lemma 3 (directed tangent–chord).**
Let $\Gamma$ be a circle through the pairwise distinct points $M,K,C$, and let $t$ be the tangent to $\Gamma$ at $M$. Then
(i) $\angle(t,\,MK)\equiv\angle(CM,\,CK)\pmod{180^\circ}$;
(ii) if a line $\ell$ through $M$ satisfies $\angle(\ell,\,MK)\equiv\angle(CM,\,CK)\pmod{180^\circ}$, then $\ell=t$; in particular $\ell$ meets $\Gamma$ only at $M$.

*Proof.* (i) Maps $Z\mapsto aZ+\beta$ ($a\ne0$) preserve directed line angles (all direction vectors get multiplied by $a$, so ratios of directions are unchanged), map circles to circles and tangent lines to tangent lines (they are bijections preserving the intersection pattern). Hence we may assume $\Gamma$ is the unit circle centred at $0$. Write $m,k,c\in\Gamma$, so $|m|=|k|=|c|=1$, $\bar m=1/m$ etc. By Lemma 1(ii), $t$ has direction $im$. Consider
$$z:=\frac{(k-m)(m-c)}{m\,(k-c)} .$$
Then
$$\bar z=\frac{(\bar k-\bar m)(\bar m-\bar c)}{\bar m(\bar k-\bar c)}
=\frac{\frac{m-k}{km}\cdot\frac{c-m}{mc}}{\frac1m\cdot\frac{c-k}{kc}}
=\frac{(m-k)(c-m)}{m\,(c-k)}=-z ,$$
so $z$ is purely imaginary; also $z\ne0$. Hence $z/i\in\mathbb{R}\setminus\{0\}$. Now
$$\angle(t,MK)-\angle(CM,CK)\equiv\arg\frac{k-m}{im}-\arg\frac{k-c}{m-c}
=\arg\Big[\frac{(k-m)(m-c)}{im(k-c)}\Big]=\arg\frac{z}{i}\equiv0\pmod{180^\circ}.$$
(ii) From (i), $\angle(\ell,MK)\equiv\angle(t,MK)$, hence $\angle(\ell,t)\equiv0$, so $\ell\parallel t$; both pass through $M$, so $\ell=t$. $\square$

**Lemma 4 (median-length formula).** For any points $O,P,Q$, if $W=\tfrac12(P+Q)$ then
$$4\,|OW|^2=2\,|OP|^2+2\,|OQ|^2-|PQ|^2 .$$

*Proof.* With vectors from $O$: $4|W-O|^2=|{(P-O)+(Q-O)}|^2=|P-O|^2+2\langle P-O,Q-O\rangle+|Q-O|^2$ and $|PQ|^2=|P-O|^2-2\langle P-O,Q-O\rangle+|Q-O|^2$. Add. $\square$

**Lemma 5 (angle addition inside an angle).** Let $V,Q,R$ be points with $0^\circ<\angle QVR<180^\circ$ and let $P$ lie inside angle $QVR$. Then $\angle QVP+\angle PVR=\angle QVR$, and $0^\circ<\angle QVP<\angle QVR$.

*Proof.* Unsigned angles and sides of lines are invariant under translations, rotations and reflections, so we may place $V=0$ and assume the unit vector along $VQ$ is $q=1$ and $\gamma:=\angle QVR\in(0^\circ,180^\circ)$ with unit vector $r=(\cos\gamma,\sin\gamma)$ along $VR$ (reflect in the $x$-axis if needed). Let $p=(\cos\sigma,\sin\sigma)$, $\sigma\in(-180^\circ,180^\circ]$, be the unit vector along $VP$. "$P$ on the same side of line $VQ$ (the $x$-axis) as $R$" means $\sin\sigma>0$, so $\sigma\in(0^\circ,180^\circ)$. "$P$ on the same side of line $VR$ as $Q$" means $r\times p$ and $r\times q$ have the same sign; $r\times q=-\sin\gamma<0$ and $r\times p=\sin(\sigma-\gamma)$; since $\sigma-\gamma\in(-180^\circ,180^\circ)$, the condition $\sin(\sigma-\gamma)<0$ means $\sigma<\gamma$. So $0<\sigma<\gamma$, and then $\angle QVP=\sigma$, $\angle PVR=\gamma-\sigma$, $\angle QVR=\gamma$. $\square$

---

### 2. Position facts

Write points as affine combinations $Z=\alpha_Z A+\beta_Z B+\gamma_Z C$ with $\alpha_Z+\beta_Z+\gamma_Z=1$ (barycentric coordinates w.r.t. $ABC$; not to be confused with the side lengths $b,c$). From $Z-A=\beta_Z(B-A)+\gamma_Z(C-A)$, $Z-B=\alpha_Z(A-B)+\gamma_Z(C-B)$, $Z-C=\alpha_Z(A-C)+\beta_Z(B-C)$ and the cyclic identity
$$(B-A)\times(C-A)=(C-B)\times(A-B)=(A-C)\times(B-C)=\delta \tag{2.1}$$
(direct expansion of all three gives $A\times B+B\times C+C\times A$), we get
$$(B-A)\times(Z-A)=\gamma_Z\,\delta,\qquad (C-B)\times(Z-B)=\alpha_Z\,\delta,\qquad (A-C)\times(Z-C)=\beta_Z\,\delta. \tag{2.2}$$
In particular, by (0.2): $Z$ is strictly on the same side of line $AB$ as $C$ iff $\gamma_Z>0$; strictly on the same side of $BC$ as $A$ iff $\alpha_Z>0$; strictly on the same side of $CA$ as $B$ iff $\beta_Z>0$. The interior of triangle $ABC$ is exactly $\{\alpha_Z,\beta_Z,\gamma_Z>0\}$.

**(P1) $K$ lies strictly inside triangle $ABC$ and $K\notin$ lines $AB$, $BC$, $CM$.**
Indeed $K=\alpha B+\mu M+\gamma C$ with $\alpha,\mu,\gamma>0$, $\alpha+\mu+\gamma=1$ ($B,M,C$ are affinely independent since $M$ is an interior point of $AB$ and $C\notin AB$). As $M=\tfrac12(A+B)$,
$$K=\tfrac{\mu}{2}A+(\alpha+\tfrac{\mu}{2})B+\gamma C,$$
all coefficients positive, so $K$ is interior to $ABC$. In coordinates w.r.t. $B,M,C$: line $BM=AB$ is $\{\gamma=0\}$, line $BC$ is $\{\mu=0\}$, line $CM$ is $\{\alpha=0\}$; the interior has $\alpha,\mu,\gamma>0$.

**(P2) $L$ lies strictly inside triangle $ABC$ and $L\notin$ lines $AC$, $BC$, $BN$.** Same argument with $L=\alpha'B+\nu N+\gamma'C$, $N=\tfrac12(A+C)$: $L=\tfrac{\nu}{2}A+\alpha'B+(\gamma'+\tfrac{\nu}{2})C$; line $NC=AC$ is $\{\alpha'=0\}$, line $BC$ is $\{\nu=0\}$, line $BN$ is $\{\gamma'=0\}$.

In particular $A\ne K$, $A\ne L$ ($A$ is not interior), $K\notin AB$, $L\notin AC$, so
$$0^\circ<\theta=\angle KBA<180^\circ,\qquad 0^\circ<\varphi=\angle LNC<180^\circ,\qquad 0^\circ<\psi=\angle BMK<180^\circ. \tag{2.3}$$

**(P3) Definition and position of $Y$ and $X$.** *The ray from $B$ through $K$ meets segment $AC$ at a point $Y$ with $Y\ne A,C$; the ray from $C$ through $L$ meets segment $AB$ at a point $X$ with $X\ne A,B$.*

*Proof for $Y$.* Let $K$ have barycentric coordinates $(\alpha_K,\beta_K,\gamma_K)$, all positive, by (P1). First, $A$ and $C$ are strictly on opposite sides of line $BK$ (direction $K-B$):
$$(K-B)\times(A-B)=-(A-B)\times(K-B),\qquad (A-B)\times(K-B)=(A-B)\times(K-A)=-(B-A)\times(K-A)=-\gamma_K\,\delta<0,$$
so $(K-B)\times(A-B)=\gamma_K\,\delta>0$; and by (2.2), $(K-B)\times(C-B)=-(C-B)\times(K-B)=-\alpha_K\,\delta<0$. (Here $(A-B)\times(K-B)=(A-B)\times(K-A)$ because $(A-B)\times(A-B)=0$.) Hence segment $AC$ meets line $BK$ in exactly one point $Y$, and $Y\ne A,C$ (strict signs), $Y\neq B$ (as $B\notin AC$, else $\delta=0$).

Next, $Y$ lies on the ray from $B$ through $K$. Write $Y=B+t(K-B)$, $t\neq0$. On one hand, $Y$ has barycentric coordinates $(1-s,0,s)$ with $s\in(0,1)$, so by (2.2) $(B-A)\times(Y-A)=s\,\delta>0$. On the other hand $Y-A=(B-A)+t(K-B)$ and $(B-A)\times(K-B)=(B-A)\times(K-A)=\gamma_K\,\delta$, so $(B-A)\times(Y-A)=t\,\gamma_K\,\delta$. Comparing, $t>0$.

*Proof for $X$.* Symmetric. Let $L$ have barycentric coordinates $(\alpha_L,\beta_L,\gamma_L)$, all positive. Then $(L-C)\times(A-C)=-(A-C)\times(L-C)=-\beta_L\,\delta<0$ by (2.2), while from $L-C=\alpha_L(A-C)+\beta_L(B-C)$ and (2.1), $(L-C)\times(B-C)=\alpha_L\,(A-C)\times(B-C)=\alpha_L\,\delta>0$. So $A,B$ are strictly on opposite sides of line $CL$, and segment $AB$ meets line $CL$ in a single point $X\ne A,B$. Writing $X=C+t(L-C)$, and noting that $X$ has barycentric coordinates $(1-s,s,0)$ with $s\in(0,1)$, (2.2) gives $(A-C)\times(X-C)=\beta_X\,\delta=s\,\delta>0$, while $(A-C)\times(X-C)=t\,(A-C)\times(L-C)=t\,\beta_L\,\delta$; hence $t>0$. $\square$

Introduce the signed coordinates along the two sides:
$$x:=AX\in(0,c),\qquad y:=AY\in(0,b),$$
so that on the line $AB$ (coordinatized from $A$ towards $B$) the points $A,X,M,B$ sit at $0,x,\tfrac{c}{2},c$, and on line $AC$ the points $A,Y,N,C$ sit at $0,y,\tfrac b2,b$.

Note for later use: since $Y$ lies on ray $BK$ and $Y\ne B$, **line $BY=$ line $BK$**; since $X$ lies on ray $CL$ and $X\ne C$, **line $CX=$ line $CL$**. Also $X\ne Y$ (lines $AB$ and $AC$ meet only at $A$, and $X\neq A$).

---

### 3. Translating the hypotheses into directed angles

By (P1)–(P2), $K$ and $L$ are interior to $ABC$; let their barycentric coordinates be positive. We use (2.2) and (0.1) repeatedly. Below, "$Z$ is on the $C$-side of $AB$" abbreviates "strictly on the same side of line $AB$ as $C$", etc.

**(S1)** If $Z$ is on the $C$-side of $AB$ (i.e. $\gamma_Z>0$), then $\measuredangle(BA\to BZ)=-\angle ABZ$ and $\measuredangle(MB\to MZ)=+\angle BMZ$.
*Proof.* $(A-B)\times(Z-B)=-(B-A)\times(Z-B)=-(B-A)\times(Z-A)=-\gamma_Z\,\delta<0$, so by (0.1) the signed angle $\measuredangle(BA\to BZ)$ is negative, of absolute value $\angle ABZ$. Also $B-M=\tfrac12(B-A)$ and $(B-A)\times(Z-M)=(B-A)\times(Z-A)-(B-A)\times(M-A)=\gamma_Z\,\delta-0>0$, so $\measuredangle(MB\to MZ)=+\angle BMZ$. $\square$

**(S2)** If $Z$ is on the $B$-side of $AC$ (i.e. $\beta_Z>0$), then $\measuredangle(CA\to CZ)=+\angle ACZ$ and $\measuredangle(NC\to NZ)=-\angle CNZ$.
*Proof.* By (2.2), $(A-C)\times(Z-C)=\beta_Z\,\delta>0$, so by (0.1) $\measuredangle(CA\to CZ)=+\angle ACZ$. For the second claim: $C-N=\tfrac12(C-A)$, and since $N-A$ is parallel to $C-A$,
$$(C-N)\times(Z-N)=\tfrac12\,(C-A)\times(Z-N)=\tfrac12\,(C-A)\times(Z-A)=-\tfrac12\,(A-C)\times(Z-A)=-\tfrac12\,\beta_Z\,\delta<0,$$
where $(A-C)\times(Z-A)=(A-C)\times(Z-C)+(A-C)\times(C-A)=\beta_Z\,\delta$. So $\measuredangle(NC\to NZ)=-\angle CNZ$. $\square$

Both $K$ and $L$ are on the $C$-side of $AB$ and on the $B$-side of $AC$ (interior points; (2.2)). Hence:

$$\measuredangle(BA\to BK)=-\angle ABK=-\theta,\qquad \measuredangle(BA\to BL)=-\angle ABL, \tag{3.1}$$
$$\measuredangle(CA\to CL)=+\angle ACL=+\theta,\qquad \measuredangle(CA\to CK)=+\angle ACK, \tag{3.2}$$
$$\measuredangle(MB\to MK)=+\angle BMK=+\psi, \tag{3.3}$$
$$\measuredangle(NC\to NL)=-\angle CNL=-\angle LNC=-\varphi. \tag{3.4}$$

**Use of "$K$ inside angle $LBA$".** Since $L$ is interior to $ABC$, $L$ is inside angle $ABC$ (same side of $AB$ as $C$ and of $BC$ as $A$, by (2.2)); by Lemma 5 applied to angle $ABC$ ($0^\circ<\angle ABC<180^\circ$ as $A,B,C$ form a triangle), $0^\circ<\angle LBA<\angle ABC<180^\circ$. Applying Lemma 5 to angle $LBA$ and the point $K$ inside it:
$$\angle ABL=\angle ABK+\angle KBL=\theta+\varphi' ,\qquad \varphi':=\angle LBK .$$
By hypothesis $\varphi'=\angle LNC=\varphi$. Hence, using (0.1) and (3.1),
$$\measuredangle(BK\to BL)\equiv\measuredangle(BA\to BL)-\measuredangle(BA\to BK)=-(\theta+\varphi)+\theta=-\varphi \pmod{360^\circ}. \tag{3.5}$$

**Use of "$L$ inside angle $ACK$".** $K$ is interior to $ABC$, hence inside angle $ACB$, so $0^\circ<\angle ACK<\angle ACB<180^\circ$ by Lemma 5. Applying Lemma 5 to angle $ACK$ and the point $L$ inside it: $\angle ACK=\angle ACL+\angle LCK=\theta+\psi'$ with $\psi':=\angle LCK=\angle BMK=\psi$ by hypothesis. Hence by (3.2),
$$\measuredangle(CL\to CK)\equiv\measuredangle(CA\to CK)-\measuredangle(CA\to CL)=(\theta+\psi)-\theta=+\psi \pmod{360^\circ}. \tag{3.6}$$

Two consequences ("nondegeneracy"): since $0<\varphi<180^\circ$ and $0<\psi<180^\circ$ by (2.3),
$$L\notin\text{line }BK \quad(\text{by }(3.5)),\qquad K\notin\text{line }CL\quad(\text{by }(3.6)), \tag{3.7}$$
because if $L$ lay on line $BK$ (note $L\ne B$: $L$ is interior to $ABC$), the ray $BL$ would coincide with ray $BK$ or its opposite, forcing $\measuredangle(BK\to BL)\in\{0^\circ,180^\circ\}$, contradicting (3.5) since $-\varphi\not\equiv0^\circ,180^\circ\pmod{360^\circ}$; likewise for $K$ and line $CL$ (note $K\ne C$), using (3.6).

---

### 4. The three circles

Recall line $BY=$ line $BK$ and line $CX=$ line $CL$.

**Claim 4.1 ($\omega_1$).** *The points $B,C,X,Y$ lie on one circle $\omega_1$.*

*Proof.* The points $X,Y,B$ are pairwise distinct and non-collinear: if $B$ were on line $XY$ then (as $X\ne B$) line $XY=$ line $XB=AB\ni Y$, contradicting $Y\notin AB$ (indeed $Y$ lies on segment $AC$ with $Y\ne A$, and $AB\cap AC=\{A\}$ because $A,B,C$ are not collinear). Also $C\notin\{X,Y\}$. Now compute directed line angles mod $180^\circ$:
$$\angle(BX,\,BY)\equiv\measuredangle(BA\to BK)\equiv-\theta \qquad(\text{line }BX=AB \text{ since } X\in AB,\ X\ne B;\ \text{line }BY=\text{line }BK),$$
$$\angle(CX,\,CY)\equiv-\angle(CY,\,CX)\equiv-\measuredangle(CA\to CL)\equiv-\theta \qquad(\text{line }CY=AC \text{ since } Y\in AC,\ Y\ne C;\ \text{line }CX=\text{line }CL).$$
So $\angle(CX,CY)\equiv\angle(BX,BY)\pmod{180^\circ}$. By Lemma 2 (with $P=X,\ Q=Y,\ R=B,\ S=C$), $C$ lies on the circle $\omega_1$ through $X,Y,B$. $\square$

Since $X,B\in\omega_1$ are distinct points of line $AB$, and $Y,C\in\omega_1$ are distinct points of line $AC$, Lemma 1(i),(iii) give
$$\operatorname{pow}(A,\omega_1)=x\,c=y\,b. \tag{4.1}$$
(Signed products: both $X$ and $B$ lie on the ray from $A$ towards $B$, etc.) Also
$$\operatorname{pow}(B,\omega_1)=0,\qquad \operatorname{pow}(C,\omega_1)=0, \tag{4.2}$$
and, since $B\ne Y$ are two points of $\omega_1$ on line $BK$ and $C\ne X$ are two points of $\omega_1$ on line $CL$,
$$\operatorname{pow}(K,\omega_1)=\langle B-K,\,Y-K\rangle,\qquad \operatorname{pow}(L,\omega_1)=\langle C-L,\,X-L\rangle. \tag{4.3}$$

**Claim 4.2 ($\omega_K$).** *Let $\omega_K$ be the circumcircle of $C,M,K$ (these are non-collinear: $K\notin$ line $CM$ and $K\notin AB\supseteq\{M\}$ by (P1)). Then line $AB$ meets $\omega_K$ exactly in the multiset $\{M,X\}$: if $X\ne M$ then $\omega_K\cap AB=\{M,X\}$; if $X=M$ then $AB$ is tangent to $\omega_K$ at $M$.*

*Proof.* By (3.3) and (3.6), mod $180^\circ$:
$$\angle(CL,\,CK)\equiv\psi\equiv\angle(MB,\,MK)\;=\;\angle(AB,\,MK). \tag{4.4}$$

*Case $X\ne M$.* The points $K,X,C$ are pairwise distinct ($K\notin AB\ni X$; $C\notin AB$; $K\ne C$) and non-collinear: line $XC=$ line $CL$ and $K\notin$ line $CL$ by (3.7). Also $M\notin\{K,X\}$ ($M\in AB$, $K\notin AB$; $X\ne M$ by assumption). Using line $CX=$ line $CL$ and line $MX=AB=$ line $MB$, (4.4) reads
$$\angle(CK,\,CX)\equiv-\psi\equiv\angle(MK,\,MX)\pmod{180^\circ}.$$
By Lemma 2 (with $P=K,\ Q=X,\ R=C,\ S=M$), $M$ lies on the circle through $K,X,C$; that circle passes through the non-collinear points $C,M,K$, hence equals $\omega_K$; thus $X\in\omega_K$. Since $M\ne X$ are two points of $\omega_K$ on $AB$, Lemma 1(i) gives $\omega_K\cap AB=\{M,X\}$.

*Case $X=M$.* Then $M\in$ line $CL$, so (as $C\ne M$) line $CL=$ line $CM$, and (4.4) becomes $\angle(AB,\,MK)\equiv\angle(CM,\,CK)\pmod{180^\circ}$. By Lemma 3(ii) (applied to $\omega_K\ni M,K,C$ and $\ell=AB$), $AB$ is tangent to $\omega_K$ at $M$. $\square$

By Lemma 1(iii) (line $AB$ through $A$ and through $B$, meeting $\omega_K$ at $M$ and $X$, coincident if $X=M$):
$$\operatorname{pow}(A,\omega_K)=\tfrac{c}{2}\,x,\qquad \operatorname{pow}(B,\omega_K)=\big(\tfrac{c}{2}-c\big)(x-c)=\tfrac{c}{2}\,(c-x), \tag{4.5}$$
$$\operatorname{pow}(K,\omega_K)=0, \tag{4.6}$$
and, since $C\ne X$ are two points of $\omega_K$ on line $CL$,
$$\operatorname{pow}(L,\omega_K)=\langle C-L,\,X-L\rangle. \tag{4.7}$$

**Claim 4.3 ($\omega_L$).** *Let $\omega_L$ be the circumcircle of $B,N,L$ (non-collinear: $L\notin$ line $BN$, $L\notin AC\supseteq\{N\}$ by (P2)). Then line $AC$ meets $\omega_L$ exactly in the multiset $\{N,Y\}$ (tangency at $N$ if $Y=N$).*

*Proof.* By (3.4) and (3.5), mod $180^\circ$:
$$\angle(BK,\,BL)\equiv-\varphi\equiv\angle(NC,\,NL)=\angle(AC,\,NL). \tag{4.8}$$

*Case $Y\ne N$.* The points $L,Y,B$ are pairwise distinct and non-collinear (line $BY=$ line $BK$ and $L\notin$ line $BK$ by (3.7); $L\notin AC\ni Y$). Also $N\notin\{L,Y,B\}$. Using line $BY=$ line $BK$ and line $NY=AC=$ line $NC$, (4.8) reads
$$\angle(BL,\,BY)\equiv\varphi\equiv\angle(NL,\,NY)\pmod{180^\circ}.$$
By Lemma 2 (with $P=L,\ Q=Y,\ R=B,\ S=N$), $N$ lies on the circle through $L,Y,B$, which then equals $\omega_L$; so $Y\in\omega_L$ and $\omega_L\cap AC=\{N,Y\}$.

*Case $Y=N$.* Then $N\in$ line $BK$, so line $BK=$ line $BN$, and (4.8) becomes $\angle(AC,\,NL)\equiv\angle(BN,\,BL)\pmod{180^\circ}$. By Lemma 3(ii) (with the circle $\omega_L\ni N,L,B$ and $\ell=AC$), $AC$ is tangent to $\omega_L$ at $N$. $\square$

Consequently
$$\operatorname{pow}(A,\omega_L)=\tfrac{b}{2}\,y,\qquad \operatorname{pow}(C,\omega_L)=\tfrac{b}{2}\,(b-y),\qquad \operatorname{pow}(L,\omega_L)=0,\qquad \operatorname{pow}(B,\omega_L)=0, \tag{4.9}$$
and, since $B\ne Y$ are two points of $\omega_L$ on line $BK$,
$$\operatorname{pow}(K,\omega_L)=\langle B-K,\,Y-K\rangle. \tag{4.10}$$

---

### 5. The affine power identity

Define $F:\mathbb{R}^2\to\mathbb{R}$ by
$$F(Z):=\operatorname{pow}(Z,\omega)-\operatorname{pow}(Z,\omega_K)-\operatorname{pow}(Z,\omega_L)+\operatorname{pow}(Z,\omega_1).$$

**$F$ is affine.** For any circle $\Gamma$ with centre $Z_\Gamma$ and radius $\rho_\Gamma$, $\operatorname{pow}(Z,\Gamma)=|Z|^2-2\langle Z_\Gamma,Z\rangle+|Z_\Gamma|^2-\rho_\Gamma^2$. In $F$ the $|Z|^2$-terms cancel ($+1-1-1+1=0$), so $F(Z)=\langle u,Z\rangle+v$ for a fixed vector $u$ and scalar $v$.

**$F(A)=0$:** by $\operatorname{pow}(A,\omega)=0$, (4.5), (4.9), (4.1):
$$F(A)=0-\tfrac{c}{2}x-\tfrac{b}{2}y+cx=\tfrac{cx}{2}-\tfrac{by}{2}=0 ,$$
using $cx=by$ from (4.1).

**$F(K)=0$:** $\operatorname{pow}(K,\omega)=0$ ($K\in\omega$), $\operatorname{pow}(K,\omega_K)=0$, and by (4.3), (4.10) $\operatorname{pow}(K,\omega_1)=\operatorname{pow}(K,\omega_L)=\langle B-K,Y-K\rangle$; the last two cancel.

**$F(L)=0$:** $\operatorname{pow}(L,\omega)=0$, $\operatorname{pow}(L,\omega_L)=0$, and by (4.3), (4.7) $\operatorname{pow}(L,\omega_1)=\operatorname{pow}(L,\omega_K)=\langle C-L,X-L\rangle$.

**Hence $F\equiv0$:** $A,K,L$ are not collinear, so $K-A$ and $L-A$ are linearly independent; from $F(A)=F(K)=F(L)=0$ we get $\langle u,K-A\rangle=\langle u,L-A\rangle=0$, so $u=0$, and then $v=F(A)=0$.

Evaluating $F$ at $B$ and $C$ and using (4.2), (4.5), (4.9):
$$\operatorname{pow}(B,\omega)=\operatorname{pow}(B,\omega_K)+\operatorname{pow}(B,\omega_L)-\operatorname{pow}(B,\omega_1)=\tfrac{c}{2}(c-x), \tag{5.1}$$
$$\operatorname{pow}(C,\omega)=\operatorname{pow}(C,\omega_K)+\operatorname{pow}(C,\omega_L)-\operatorname{pow}(C,\omega_1)=\tfrac{b}{2}(b-y). \tag{5.2}$$

---

### 6. Conclusion

$O$ is the centre of $\omega$ and $R_\omega=|OA|$ its radius, so $|OB|^2=\operatorname{pow}(B,\omega)+R_\omega^2$ and $|OC|^2=\operatorname{pow}(C,\omega)+R_\omega^2$. By Lemma 4 applied to the midpoints $M$ of $AB$ and $N$ of $AC$:
$$4\,OM^2=2\,OA^2+2\,OB^2-c^2,\qquad 4\,ON^2=2\,OA^2+2\,OC^2-b^2 .$$
Subtracting and using (5.1), (5.2) and $cx=by$ from (4.1):
$$4\,(OM^2-ON^2)=2\,(OB^2-OC^2)-c^2+b^2
=2\big[\operatorname{pow}(B,\omega)-\operatorname{pow}(C,\omega)\big]-c^2+b^2$$
$$=c(c-x)-b(b-y)-c^2+b^2=-cx+by=0 .$$
Therefore $OM=ON$. $\blacksquare$

---

### Remarks on hypothesis usage
- $\angle KBA=\angle ACL$ → Claim 4.1; $\angle LCK=\angle BMK$ together with "$L$ inside angle $ACK$" → Claim 4.2; $\angle LBK=\angle LNC$ together with "$K$ inside angle $LBA$" → Claim 4.3.
- "$K$ inside triangle $BMC$" is used exactly for: $K$ interior to $ABC$ (sign facts (S1)–(S2), crossbar (P3)) and $K\notin$ line $CM$ ($\omega_K$ nondegenerate). Similarly for $L$ and line $BN$.
- That $M,N$ are midpoints enters only through $AM=MB=\tfrac c2$, $AN=NC=\tfrac b2$ in (4.5), (4.9) and through Lemma 4.
- Numerical verification of every claim (generic and both tangency cases): `code/verify.py`, `code/check_signs.py`, `code/verify2.py`.
