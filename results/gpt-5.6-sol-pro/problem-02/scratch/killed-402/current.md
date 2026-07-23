# imo-2026-02 — tracking file
## Status
partial

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Analytic/trigonometric coordinates (promising).** Introduced the three common/local angles $x=\angle KBA=\angle ACL$, $y=\angle LBK=\angle LNC$, $z=\angle LCK=\angle BMK$, together with $\kappa=\angle BAK$, $\lambda=\angle LAC$, $\alpha=\angle BAC$, normalized $AB=1$, and wrote $AC=v$. All point positions and the remaining compatibility condition have now been reduced to explicit trigonometric equations. Numerical testing on several random parameter choices confirms that these equations imply the desired power identity to machine precision.
- **Circle/power reformulation (promising).** Since $M\in AB$ and $N\in AC$, if the circumcircle $(AKL)$ meets $AB,AC$ again at $P,Q$, then $OM=ON$ is equivalent to $\operatorname{Pow}(M)=\operatorname{Pow}(N)$, namely $\frac12(\frac12-AP)=\frac v2(\frac v2-AQ)$. Explicit formulas for $AP,AQ$ have been obtained.
- **Synthetic angle chase.** Looked for direct spiral similarities involving the midpoint homothety, but no complete synthetic route has yet emerged.

## Current best
After scaling $AB=1$ and putting $AC=v$, let $x,y,z,\kappa,\lambda,\alpha$ be as above. Sine-law computations give $AK=g=\sin x/\sin(x+\kappa)$, $AL=vh$ where $h=\sin x/\sin(x+\lambda)$, and $\cot\kappa=\cot x+2\cot z$, $\cot\lambda=\cot x+2\cot y$. The two cross-incidences ($L$ lying on its prescribed ray from $B$, $K$ on its prescribed ray from $C$) give $vh=\sin(x+y)/\sin(\alpha-\lambda+x+y)$ and $v=g\sin(\alpha-\kappa+x+z)/\sin(x+z)$, hence the single compatibility equation
$$gh\sin(\alpha-\lambda+x+y)\sin(\alpha-\kappa+x+z)=\sin(x+y)\sin(x+z).$$
For the circle $(AKL)$, its second radial intersections with $AB,AC$ have signed distances
$$AP=\frac{g\sin(\alpha-\lambda)-vh\sin\kappa}{\sin(\alpha-\lambda-\kappa)},\qquad AQ=\frac{-g\sin\lambda+vh\sin(\alpha-\kappa)}{\sin(\alpha-\lambda-\kappa)}.$$
It remains to prove rigorously that the compatibility equation and the two cotangent relations force $1-2AP=v^2-2v\,AQ$. This is now a concrete trigonometric lemma; numerical verification is complete, but the symbolic proof and all angle-range bookkeeping remain open.

## Full proof
A complete proof is not yet available. The established reduction is as follows.

Scale so that $AB=1$ and write $AC=v$. Put
$$x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,\quad z=\angle LCK=\angle BMK,$$
$$\kappa=\angle BAK,\quad \lambda=\angle LAC,\quad \alpha=\angle BAC.$$
Because $K,L$ lie in the indicated interior triangles, their relevant rays have the natural order encoded by these angles. Applying the sine rule in $ABK$ and $ACL$ yields
$$AK=\frac{\sin x}{\sin(x+\kappa)}=:g,\qquad AL=v\frac{\sin x}{\sin(x+\lambda)}=:vh.$$
Comparing these with the sine rule in $BMK$ (where $BM=1/2$) and $CNL$ (where $CN=v/2$), respectively, gives
$$\cot\kappa=\cot x+2\cot z,\qquad \cot\lambda=\cot x+2\cot y.$$
The sine rule in $ABL$ and $ACK$ gives
$$vh=\frac{\sin(x+y)}{\sin(\alpha-\lambda+x+y)},\qquad
v=g\frac{\sin(\alpha-\kappa+x+z)}{\sin(x+z)}.$$
These imply the compatibility equation displayed in `Current best`.

Let the circle $(AKL)$ meet the oriented rays $AB,AC$ for the second time at signed radial distances $p=AP,q=AQ$. The equation of any circle through $A$, restricted to a ray from $A$, immediately gives
$$p=\frac{g\sin(\alpha-\lambda)-vh\sin\kappa}{\sin(\alpha-\lambda-\kappa)},\qquad
q=\frac{-g\sin\lambda+vh\sin(\alpha-\kappa)}{\sin(\alpha-\lambda-\kappa)}.$$
Finally,
$$\operatorname{Pow}_{(AKL)}(M)=\frac12\left(\frac12-p\right),\qquad
\operatorname{Pow}_{(AKL)}(N)=\frac v2\left(\frac v2-q\right).$$
Thus it suffices to complete the trigonometric implication $1-2p=v^2-2vq$.
