# imo-2026-02 — tracking file

## Status
solved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Numerical exploration** (`code/explore.py`): confirmed $OM=ON$ across many triangles and parameter choices; confirmed the configuration exists and is (generically) unique for each $\varphi$.
- **Power-of-a-point reformulation**: $OM=ON\iff\operatorname{pow}(M)=\operatorname{pow}(N)\iff\operatorname{pow}(B)-\operatorname{pow}(C)=\dfrac{c^2-b^2}{2}$ (median/Apollonius identity). This is the route that worked.
- **Angle chasing**: found $\cot\angle BAK=\cot\varphi+2\cot\gamma$, $\cot\angle CAL=\cot\varphi+2\cot\beta$; found $\angle MKC=\angle NLB=180^\circ-A-\varphi$ (automatic, not the crux).
- **Law of sines in four triangles** ($BMK$, $CNL$, $BKC$, $BCL$) → two quadratic constraints ConsP, ConsQ on $p=BK$, $q=CL$. **This is the key structural fact.**
- **Coordinate computation of powers** with $A$ at origin (complex notation $K=c-pe^{-i\varphi}$, $L=e^{iA}(b-qe^{i\varphi})$) → explicit formulas for $\operatorname{pow}(B),\operatorname{pow}(C)$; discovered they simplify to closed forms using ConsP, ConsQ.
- **Symbolic verification** (`code/verify_identity.py`, `code/verify_power_formulas.py`): the two crucial polynomial identities are exactly true (difference simplifies to $0$); the elimination R1∧R3⇒ConsP verified exactly.

## Current best
Complete rigorous proof. The crux: the given angle conditions force $p=BK$ and $q=CL$ to satisfy the quadratics
$2\sin(A+\varphi)p^2-(2\sin A+\sin(A+2\varphi))cp+c^2\sin(A+\varphi)-bc\sin\varphi=0$ (and the analogous one for $q$ with $b$),
which in turn force $\operatorname{pow}(B)=\dfrac{c^2\sin(A+\varphi)-bc\sin\varphi}{2\sin(A+\varphi)}$ and $\operatorname{pow}(C)=\dfrac{b^2\sin(A+\varphi)-bc\sin\varphi}{2\sin(A+\varphi)}$, so $\operatorname{pow}(B)-\operatorname{pow}(C)=\frac{c^2-b^2}{2}$, equivalent to $OM=ON$.

## Full proof

### Notation
Let $A,B,C$ also denote the angles of $\triangle ABC$, and $a=BC$, $b=CA$, $c=AB$. Put
$$\varphi:=\angle KBA=\angle ACL,\qquad \beta:=\angle LBK=\angle LNC,\qquad \gamma:=\angle LCK=\angle BMK,$$
and $p:=BK$, $q:=CL$. Since $K$ lies inside $\angle LBA$, $\angle ABL=\beta+\varphi$; since $L$ lies inside $\angle ACK$, $\angle ACK=\gamma+\varphi$. All angles appearing below are positive because $K\in\triangle BMC$ and $L\in\triangle BNC$ are interior points (so rays $BK,BL$ lie inside $\angle ABC$ and rays $CK,CL$ inside $\angle ACB$); in particular $0<\varphi<B$, $\beta+\varphi<B$, $\gamma+\varphi<C$, whence $A+\varphi<A+B<\pi$ and $\sin(A+\varphi)>0$.

### Step 1: Reduction to powers of $B$ and $C$
Let $R$ be the radius of the circumcircle $\omega=(AKL)$ and write $\operatorname{pow}(\cdot)$ for power w.r.t. $\omega$. Since $M$ is the midpoint of $AB$, Apollonius's median formula in $\triangle OAB$ gives
$$OM^2=\frac{2OA^2+2OB^2-AB^2}{4}=\frac{2R^2+2OB^2-c^2}{4},$$
so $\operatorname{pow}(M)=OM^2-R^2=\dfrac{\operatorname{pow}(B)}{2}-\dfrac{c^2}{4}$. Similarly $\operatorname{pow}(N)=\dfrac{\operatorname{pow}(C)}{2}-\dfrac{b^2}{4}$. Therefore
$$OM=ON\iff\operatorname{pow}(M)=\operatorname{pow}(N)\iff\operatorname{pow}(B)-\operatorname{pow}(C)=\frac{c^2-b^2}{2}.\tag{1}$$

### Step 2: Four law-of-sines relations
*Triangle $BMK$:* angles $\varphi$ at $B$ (as $M\in BA$), $\gamma$ at $M$, $\pi-\varphi-\gamma$ at $K$; with $BM=c/2$:
$$p=BK=\frac{c\sin\gamma}{2\sin(\varphi+\gamma)}.\tag{R1}$$
*Triangle $CNL$:* angles $\varphi$ at $C$ (as $N\in CA$), $\beta$ at $N$, $\pi-\varphi-\beta$ at $L$; with $CN=b/2$:
$$q=CL=\frac{b\sin\beta}{2\sin(\varphi+\beta)}.\tag{R2}$$
*Triangle $BKC$:* $\angle KBC=B-\varphi$, $\angle KCB=C-(\gamma+\varphi)$ (using $\angle ACK=\gamma+\varphi$), $\angle BKC=A+\gamma+2\varphi$:
$$p=BK=\frac{a\sin(C-\varphi-\gamma)}{\sin(A+\gamma+2\varphi)}.\tag{R3}$$
*Triangle $BCL$:* $\angle LBC=B-(\beta+\varphi)$ (using $\angle ABL=\beta+\varphi$), $\angle BCL=C-\varphi$, $\angle BLC=A+\beta+2\varphi$:
$$q=CL=\frac{a\sin(B-\varphi-\beta)}{\sin(A+\beta+2\varphi)}.\tag{R4}$$

### Step 3: The quadratic constraints (elimination of $\beta,\gamma$)
**Auxiliary identity:** for any $x$,
$c\sin(A+x)=b\sin x+a\sin(C-x)$. Indeed with $a=2R'\sin A$, $b=2R'\sin B$, $c=2R'\sin C$ this is equivalent to $\sin C\sin(A+x)=\sin B\sin x+\sin A\sin(C-x)$, and using $\sin B=\sin(A+C)$ the RHS equals $\sin C(\sin x\cos A+\sin A\cos x)=\sin C\sin(A+x)$.

Combining (R3) with the identity at $x=\gamma+\varphi$:
$$p\sin(A+\gamma+2\varphi)=c\sin(A+\gamma+\varphi)-b\sin(\gamma+\varphi).\tag{EqC}$$
Expanding (R1) and (EqC) with the addition formulas:
$$2p\sin\varphi\cos\gamma=(c-2p\cos\varphi)\sin\gamma,\tag{i}$$
$$\big[c\cos(A+\varphi)-p\cos(A+2\varphi)-b\cos\varphi\big]\sin\gamma=\big[p\sin(A+2\varphi)-c\sin(A+\varphi)+b\sin\varphi\big]\cos\gamma.\tag{ii}$$
Eliminating $\sin\gamma,\cos\gamma$ from (i),(ii) (multiply (i) by the bracket in (ii)'s LHS and (ii) by $2p\sin\varphi$, subtract — legitimate since the resulting identity $(c-2p\cos\varphi)(\cdots)-(2p\sin\varphi)(\cdots)=0$ follows from (i)∧(ii)):
$$(c-2p\cos\varphi)\big[p\sin(A+2\varphi)-c\sin(A+\varphi)+b\sin\varphi\big]=2p\sin\varphi\big[c\cos(A+\varphi)-p\cos(A+2\varphi)-b\cos\varphi\big].$$
Expand. The terms $-2pb\sin\varphi\cos\varphi$ cancel on both sides. Using $2\sin\varphi\cos(A+\varphi)=\sin(A+2\varphi)-\sin A$, $2\cos\varphi\sin(A+\varphi)=\sin(A+2\varphi)+\sin A$, and $\cos\varphi\sin(A+2\varphi)-\sin\varphi\cos(A+2\varphi)=\sin(A+\varphi)$, everything simplifies to:
$$\boxed{2\sin(A+\varphi)\,p^2-\big(2\sin A+\sin(A+2\varphi)\big)cp+c^2\sin(A+\varphi)-bc\sin\varphi=0}\quad(\mathrm{ConsP})$$
The symmetric computation with (R2),(R4) (swap $b\leftrightarrow c$, $p\leftrightarrow q$, $\gamma\leftrightarrow\beta$) gives:
$$\boxed{2\sin(A+\varphi)\,q^2-\big(2\sin A+\sin(A+2\varphi)\big)bq+b^2\sin(A+\varphi)-bc\sin\varphi=0}\quad(\mathrm{ConsQ})$$

### Step 4: Powers of $B$ and $C$ in coordinates
Place $A=(0,0)$, $B=(c,0)$, $C=(b\cos A,b\sin A)$. From $\angle KBA=\varphi$, $BK=p$ and from $\angle ACL=\varphi$, $CL=q$:
$$K=(c-p\cos\varphi,\;p\sin\varphi),\qquad L=\big(b\cos A-q\cos(A+\varphi),\;b\sin A-q\sin(A+\varphi)\big).$$
The circle $\omega$ passes through the origin, so it has equation $x^2+y^2+ux+vy=0$; the power of a point $P$ equals $g(P)=x_P^2+y_P^2+ux_P+vy_P$. The conditions $g(K)=g(L)=0$ form a $2\times2$ linear system in $u,v$ with determinant
$$\Delta=K_xL_y-K_yL_x=bc\sin A-(bp+cq)\sin(A+\varphi)+pq\sin(A+2\varphi)=2[AKL]\neq0$$
($A,K,L$ are not collinear since $\omega$ is the circumcircle of a genuine triangle). Solving:
$$u=\frac{|L|^2K_y-|K|^2L_y}{\Delta},\qquad v=\frac{|K|^2L_x-|L|^2K_x}{\Delta},$$
where $|K|^2=c^2-2cp\cos\varphi+p^2$ and $|L|^2=b^2-2bq\cos\varphi+q^2$. Therefore
$$\operatorname{pow}(B)=c^2+cu=c^2+\frac{c\big[|L|^2p\sin\varphi-|K|^2\big(b\sin A-q\sin(A+\varphi)\big)\big]}{\Delta},\tag{2}$$
and, using $L_x\sin A-L_y\cos A=q\sin\varphi$ and $K_y\cos A-K_x\sin A=p\sin(A+\varphi)-c\sin A$,
$$\operatorname{pow}(C)=b^2+ub\cos A+vb\sin A=b^2+\frac{b\big[|K|^2q\sin\varphi+|L|^2\big(p\sin(A+\varphi)-c\sin A\big)\big]}{\Delta}.\tag{3}$$

### Step 5: Key algebraic identities
Write $s_1=\sin(A+\varphi)$, $s_\varphi=\sin\varphi$, $s_A=\sin A$. The following two identities hold, where each side is a polynomial in $p,q$ whose coefficients are trigonometric polynomials in $A,\varphi$:
$$2s_1\Delta\left(\operatorname{pow}(B)-\frac{c^2s_1-bcs_\varphi}{2s_1}\right)=c\big(s_1q-bs_A\big)\cdot\mathrm{ConsP}+c s_\varphi\, p\cdot\mathrm{ConsQ},\tag{4}$$
$$2s_1\Delta\left(\operatorname{pow}(C)-\frac{b^2s_1-bcs_\varphi}{2s_1}\right)=b s_\varphi\, q\cdot\mathrm{ConsP}+b\big(s_1p-cs_A\big)\cdot\mathrm{ConsQ},\tag{5}$$
where $\operatorname{pow}(B),\operatorname{pow}(C)$ are substituted from (2),(3) and $\mathrm{ConsP},\mathrm{ConsQ}$ from Step 3.

*Verification of (4).* Multiplying (2) out, the LHS of (4) equals
$$\Delta\big(c^2s_1+bcs_\varphi\big)+2s_1c\Big[|L|^2ps_\varphi-|K|^2\big(bs_A-qs_1\big)\Big].$$
Both this and the RHS of (4) are polynomials in $p,q$ involving only the monomials $p^2q,\,pq^2,\,p^2,\,q^2,\,pq,\,p,\,q,\,1$. Comparing coefficients monomial by monomial, the two sides agree immediately in every monomial except possibly $pq$; the difference of the two $pq$-coefficients is $c\cdot E(A,\varphi)$ with
$$E=b\big[3s_As_\varphi+4s_\varphi^2\cos(A+\varphi)-\cos A\cos\varphi+\cos(A+3\varphi)\big]+4c\big[s_As_1+\cos A\cos(A+\varphi)-\cos\varphi\big].$$
The second bracket is $\cos\big((A+\varphi)-A\big)-\cos\varphi=0$. For the first, write $\cos(A+3\varphi)=\cos(A+\varphi)\cos2\varphi-\sin(A+\varphi)\sin2\varphi$; then
$$\begin{aligned}
&s_\varphi^{-1}\cdot(\text{first bracket})=3s_As_\varphi+4s_\varphi^2\cos(A+\varphi)-\cos A\cos\varphi+\cos(A+\varphi)(1-2s_\varphi^2)-2s_1s_\varphi\cos\varphi\\
&=3s_As_\varphi-\cos A\cos\varphi+\cos(A+\varphi)+2s_\varphi\big[s_\varphi\cos(A+\varphi)-s_1\cos\varphi\big]\\
&=3s_As_\varphi-\cos A\cos\varphi+\cos(A+\varphi)+2s_\varphi\sin\big(\varphi-(A+\varphi)\big)\\
&=s_As_\varphi-\cos A\cos\varphi+\cos(A+\varphi)=-\cos(A+\varphi)+\cos(A+\varphi)=0 .
\end{aligned}$$
Hence $E=0$ and (4) holds. (All steps are direct expansions using only the addition formulas; the computation was also verified symbolically in `code/verify_power_formulas.py`.) Identity (5) is the same computation with the roles $b\leftrightarrow c$, $p\leftrightarrow q$ interchanged.

### Step 6: Conclusion
Since $\mathrm{ConsP}=\mathrm{ConsQ}=0$ (Step 3) and $s_1\Delta\neq0$, identities (4),(5) give
$$\operatorname{pow}(B)=\frac{c^2\sin(A+\varphi)-bc\sin\varphi}{2\sin(A+\varphi)},\qquad \operatorname{pow}(C)=\frac{b^2\sin(A+\varphi)-bc\sin\varphi}{2\sin(A+\varphi)}.$$
Subtracting:
$$\operatorname{pow}(B)-\operatorname{pow}(C)=\frac{(c^2-b^2)\sin(A+\varphi)}{2\sin(A+\varphi)}=\frac{c^2-b^2}{2}.$$
By (1) this is equivalent to $OM=ON$. $\blacksquare$
