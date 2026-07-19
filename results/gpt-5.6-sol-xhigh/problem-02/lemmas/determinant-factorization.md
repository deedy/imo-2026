# Determinant factorization

## Statement
Let $x,y,z,t$ be real numbers satisfying $0<x<\pi/2$, $0<x+y<\pi$, and $0<x+z<\pi$. Define
\[
 k=1+\frac{\sin x}{\sin(x+z)}e^{iz},\qquad
 l=2-te^{-i(x+y)},\qquad l=\lambda n,
\]
where
\[
 \lambda=1+\frac{\sin x}{\sin(x+y)}e^{-iy}.
\]
For complex $u,v$, write $[u,v]=\operatorname{Im}(\bar u v)$. Then, with
\[
 D=[k,l](|n|^2-1)-[k,n-1]|l|^2+[l,n-1]|k|^2,
\]
one has
\[
D=\frac{\sin x(t\sin x+\sin y)}{\sin(x+y)\sin(x+z)}
[k-2n,e^{i(x+z)}n].
\]

## Proof
The displayed definitions above are the formulas referred to below as (2)--(4). First suppose that $\cos y\cos z\ne0$. Put
\[
 p=\tan x,\qquad q=\tan y,\qquad s=\tan z,
 \qquad r=t\cos x\cos y. \tag{15}
\]
The signs of $q,s,r$ will not matter. The assumptions $0<x+y<\pi$ and $0<x+z<\pi$ imply that $p+q$ and $p+s$ are nonzero. Dividing the coordinate formulas (2)--(4) by the appropriate products of cosines gives
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
To verify (31)--(32) without any concealed division, multiply each $R_i$ first by $d$ and insert
\[
 v=p(2-u),\quad U=1+\frac pd,\quad V=-\frac{pq}{d},\quad
 W=1+\frac{2p}{d}+\frac{p^2(1+q^2)}{d^2},
\]
together with (22)--(28); collecting the coefficients of $u$ gives exactly the displayed products. This is ordinary distributive expansion, and the formulas (31)--(32) record the full remainders after collection. The second relation in (21) makes every one of them zero, proving (30), hence (29).

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

Finally, both sides of the asserted identity are continuous in $(x,y,z,t)$ on its stated domain. Indeed, $\lambda\ne0$: if $\sin y\ne0$, this follows from $\operatorname{Im}\lambda=-\sin x\sin y/\sin(x+y)\ne0$, while if $\sin y=0$, the inequalities force $y=0$ and then $\lambda=2$. The subset where $\cos y\cos z\ne0$ is dense in the domain, so the identity also holds when $\cos y\cos z=0$, by continuity. This completes the proof.
