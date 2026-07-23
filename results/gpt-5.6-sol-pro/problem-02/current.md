# imo-2026-02 — tracking file
## Status
solved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Angle parameters and polar coordinates.** The midpoint conditions and sine rule reduce the problem to a trigonometric factorization.
- **Circle intersections with $AB,AC$.** If the circumcircle of $AKL$ meets the oriented lines $AB,AC$ again at $D,E$, then $OM=ON$ is exactly $AB\cdot AD-AC\cdot AE=(AB^2-AC^2)/2$.
- **Numerical/symbolic checking.** `code/explore_trig.py` checked compatible samples; `code/symbolic_poly.py` exposed the exact harmonic factorization and its factor $\sin(x-y)$.
- **Harmonic factorization (successful).** The target residual is exactly $\sin(x-y)$ times the compatibility residual. A complete proof is in `lemmas/trigonometric-factorization.md`.

## Current best
The problem is solved. With suitable angle parameters, the two midpoint conditions determine $AK/AB$ and $AL/AC$. The two remaining angle conditions yield a compatibility equation. An oriented-circle calculation turns $OM=ON$ into a trigonometric target, and the factorization lemma shows that its residual is $\sin(x-y)$ times the already-zero compatibility residual.

## Full proof
Let
\[
p=\angle KBA=\angle ACL,\quad q=\angle LBK=\angle LNC,\quad r=\angle LCK=\angle BMK,
\]
and put
\[
x=\angle BAK,\qquad y=\angle CAL,\qquad \delta=\angle KAL.
\]
Because $K$ lies inside $\angle LBA$, the ray $BK$ lies between $BA$ and $BL$; because $L$ lies inside $\angle ACK$, the ray $CL$ lies between $CA$ and $CK$. We first justify the resulting order of the rays at $A$. Write the positive normalized affine coordinates of $K,L$ relative to $A,B,C$ as
\[
K=(k_A,k_B,k_C),\qquad L=(l_A,l_B,l_C).
\]
At $B$, the first betweenness says
$k_C/k_A<l_C/l_A$; at $C$, the second says
$l_B/l_A<k_B/k_A$. Therefore
\[
\frac{k_B}{l_B}>\frac{k_A}{l_A}>\frac{k_C}{l_C}.
\]
Thus $k_C/k_B<l_C/l_B$. Indeed, a ray from $A$ through a point with affine coordinates $(u_A,u_B,u_C)$ has direction $u_B\overrightarrow{AB}+u_C\overrightarrow{AC}$; consequently this last inequality says precisely that the ray $AK$ lies between $AB$ and $AL$. Since both points are inside $ABC$, the ray order is consequently
$AB,AK,AL,AC$. Hence
\[
\angle BAC=x+\delta+y. \tag{0}
\]
Put $c=AB$ and $b=AC$.

Applying the sine rule in $ABK$ and $BMK$, and using $BM=c/2$, gives
\[
BK=\frac{c\sin x}{\sin(p+x)}=\frac{c\sin r}{2\sin(p+r)}.
\]
Consequently
\[
\cot x=\cot p+2\cot r,
\qquad AK=cP,\qquad P:=\frac{\sin p}{\sin(p+x)}. \tag{1}
\]
Similarly, the sine rule in $ACL$ and $CNL$, using $CN=b/2$, gives
\[
\cot y=\cot p+2\cot q,
\qquad AL=bQ,\qquad Q:=\frac{\sin p}{\sin(p+y)}. \tag{2}
\]

Now apply the sine rule in $ACK$ and $ABL$. From (0),
\[
\angle CAK=\delta+y, \qquad \angle BAL=x+\delta.
\]
Also, the angle assumptions give
\[
\angle ACK=p+r, \qquad \angle ABL=p+q.
\]
Thus, on setting
\[
U=p+r+\delta+y, \qquad V=p+q+\delta+x,
\]
we obtain
\[
\frac cbP=\frac{\sin(p+r)}{\sin U},
\qquad
\frac bcQ=\frac{\sin(p+q)}{\sin V}. \tag{3}
\]
Multiplying these equalities yields
\[
PQ\sin U\sin V=\sin(p+r)\sin(p+q). \tag{4}
\]

Let the circle through $A,K,L$ meet the oriented lines $AB,AC$ again at $D,E$, respectively, and write $AD=d$, $AE=e$ as directed lengths. Take $A$ as origin, and let $\mathbf e_B,\mathbf e_C$ be the unit vectors along $AB,AC$. If
$\mathbf w=2\overrightarrow{AO}$, the circle has equation
\[
|\mathbf z|^2=\mathbf w\cdot\mathbf z.
\]
It follows that
\[
d=\mathbf w\cdot\mathbf e_B,
\qquad e=\mathbf w\cdot\mathbf e_C. \tag{5}
\]
Since $\overrightarrow{AM}=(c/2)\mathbf e_B$ and
$\overrightarrow{AN}=(b/2)\mathbf e_C$, we have
\[
OM^2-ON^2
=\frac{c^2-b^2}{4}-\frac{cd-be}{2}.
\]
Therefore $OM=ON$ is equivalent to
\[
cd-be=\frac{c^2-b^2}{2}. \tag{6}
\]

Let $\mathbf u_K,\mathbf u_L$ be the unit vectors along $AK,AL$. The circle equation at $K,L$ says
\[
\mathbf w\cdot\mathbf u_K=cP,\qquad
\mathbf w\cdot\mathbf u_L=bQ.
\]
The angles from $AB$ to $AK$, from $AK$ to $AL$, and from $AL$ to $AC$ are $x,\delta,y$, respectively. Solving these two linear equations and then taking the projections of $\mathbf w$ on $AB,AC$ gives
\[
d=\frac{cP\sin(\delta+x)-bQ\sin x}{\sin\delta},
\qquad
e=\frac{-cP\sin y+bQ\sin(\delta+y)}{\sin\delta}. \tag{7}
\]

From the first relation in (1), a direct sine expansion gives
\[
P\sin(\delta+x)-\frac12\sin\delta
=\frac{\sin p}{2\sin(p+r)}\sin(\delta+r). \tag{8}
\]
Analogously, (2) gives
\[
Q\sin(\delta+y)-\frac12\sin\delta
=\frac{\sin p}{2\sin(p+q)}\sin(\delta+q). \tag{9}
\]
Substitution of (7)--(9) shows that (6) is equivalent to
\[
\frac cb\frac{\sin p\sin(\delta+r)}{2\sin(p+r)}
-\frac bc\frac{\sin p\sin(\delta+q)}{2\sin(p+q)}
+P\sin y-Q\sin x=0. \tag{10}
\]
Using (3), equation (10) is equivalent to $T=0$, where
\[
\begin{aligned}
T={}&Q\sin p\sin(\delta+r)\sin V
-P\sin p\sin(\delta+q)\sin U\\
&+2(P\sin y-Q\sin x)\sin(p+r)\sin(p+q). \tag{11}
\end{aligned}
\]

We use the following trigonometric identity, proved below:
\[
T=\sin(x-y)\bigl(PQ\sin U\sin V- \sin(p+r)\sin(p+q) \bigr). \tag{12}
\]
Indeed, the relations $\cot x=\cot p+2\cot r$ and
$\cot y=\cot p+2\cot q$ imply
\[
P=\frac{\sin r}{2\sin(r-x)}, \qquad
Q=\frac{\sin q}{2\sin(q-y)}, \tag{13}
\]
and
\[
\frac{\sin(p+r)}{\sin p}=\frac{\sin(r-x)}{\sin x}, \qquad
\frac{\sin(p+q)}{\sin p}=\frac{\sin(q-y)}{\sin y}. \tag{14}
\]
From (13), putting the expression in brackets below over a common denominator, and using the sine subtraction formula, we obtain
\[
\begin{aligned}
&[2(P\sin y-Q\sin x)+\sin(x-y)]\sin(p+r)\sin(p+q)\\
&\qquad=\sin^2p\sin(q+x-r-y). \tag{15}
\end{aligned}
\]
For completeness, the numerator used here is
\[
\begin{aligned}
&\sin r\sin y\sin(q-y)-\sin q\sin x\sin(r-x)\\
&\quad+\sin(x-y)\sin(r-x)\sin(q-y)\\
&=\sin x\sin y\sin(q+x-r-y),
\end{aligned}
\]
and (14) then gives (15).

It remains to verify (12). Put
\[
W=2\delta+p+q+r,\qquad D=q+x-r-y.
\]
After applying $2\sin s\sin t=\cos(s-t)-\cos(s+t)$, the part of twice the difference between the two sides of (12) that depends on $\delta$ is
\[
-Q\sin p\cos(W+x)+P\sin p\cos(W+y)
 +\sin(x-y)PQ\cos(W+p+x+y). \tag{16}
\]
Divide (16) by $PQ$ and use
$\sin p/P=\sin(p+x)$ and $\sin p/Q=\sin(p+y)$. The result is
\[
-\sin(p+x)\cos(W+x)+\sin(p+y)\cos(W+y)
 +\sin(x-y)\cos(W+p+x+y),
\]
which is zero: applying $2\sin a\cos b=\sin(a+b)+\sin(a-b)$ makes its six terms cancel in pairs.

It remains to compare the constant parts. We first prove
\[
\begin{aligned}
&Q\sin p\cos(r-p-q-x)-P\sin p\cos(q-p-r-y)\\
&\quad-\sin(x-y)PQ\cos D=-2\sin^2p\sin D. \tag{17}
\end{aligned}
\]
After division by $PQ$, this is equivalent to
\[
\begin{aligned}
&\sin(p+x)\cos(p+y+D)-\sin(p+y)\cos(D-p-x)\\
&\quad-\sin(x-y)\cos D
=-2\sin(p+x)\sin(p+y)\sin D. \tag{18}
\end{aligned}
\]
Here we used
$r-p-q-x=-(p+y+D)$ and $q-p-r-y=D-(p+x)$.
To prove (18), expand the two cosines of sums and also
$\sin(x-y)=\sin((p+x)-(p+y))$. All terms containing $\cos D$ cancel, while the two remaining terms are both
$-\sin(p+x)\sin(p+y)\sin D$.

In twice the difference between the sides of (12), the complete constant part is the left side of (17) plus
\[
[4(P\sin y-Q\sin x)+2\sin(x-y)]\sin(p+r)\sin(p+q).
\]
By (15), this latter expression is $2\sin^2p\sin D$, which cancels the right side of (17). Thus both the variable and constant parts vanish, proving (12).

By (4), the right-hand side of (12) is zero. Hence $T=0$, so (10), (6), and therefore $OM=ON$ follow.
