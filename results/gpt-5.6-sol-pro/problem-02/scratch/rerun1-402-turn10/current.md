# imo-2026-02 — tracking file

## Status
partial

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Directed-angle parameterization:** Set $\alpha=\angle KBA=\angle ACL$, $\beta=\angle LBK=\angle LNC$, and $\gamma=\angle LCK=\angle BMK$. The interior hypotheses imply $\alpha,\beta,\gamma>0$, $\alpha+\beta<\pi$, and $\alpha+\gamma<\pi$, and fix all ray orientations.
- **Complex coordinates (successful framework):** Put $A=0$, $B=1$, $C=w$. Straight ray intersections give
  \[
  k=1-\frac{\sin\gamma}{2\sin(\alpha+\gamma)}e^{-i\alpha},\qquad
  l=wg,\quad g=1-\frac{\sin\beta}{2\sin(\alpha+\beta)}e^{i\alpha}.
  \]
  Since the ray $BL$ has direction $\pi-(\alpha+\beta)$, write $l=1-te^{-i(\alpha+\beta)}$ with $t>0$, hence $w=l/g$.
- **Circle determinant (successful):** The circle through $0,k,l$ has equation $z\bar z+\bar qz+q\bar z=0$. Its centre is $-q$, and $OM=ON$ is equivalent to
  \[
  \frac{1-|w|^2}{4}+\frac{\bar q(1-w)+q(1-\bar w)}2=0.
  \]
  Eliminating $q$ using the equations at $k,l$ gives a $3\times3$ determinant.
- **Key factorization found:** For $s=\alpha+\beta$, $r=\alpha+\gamma$, the determinant $D$ satisfies the compact identity
  \[
  \frac Di=\frac{\sin\alpha(2t\sin\alpha+\sin\beta)}{4\sin s\sin r}\,
  \Im((w-k)\bar w e^{-ir}).
  \]
  The last given angle condition says precisely that the imaginary part is zero (with orientation supplied by the interior assumptions), so $D=0$. This identity has been tested numerically on 10,000 random inputs and symbolically in tangent variables. The remaining task is to replace the brute expansion with a readable hand-verifiable derivation and then finalize all orientation details.

## Current best
The proof is structurally complete modulo presentation of one elementary complex-number factorization. Normalize $A=0,B=1,C=w$ and parameterize the three common angles by $\alpha,\beta,\gamma$. The first and second ray intersections produce explicit $k$ and $g=l/w$; the incidence at $B$ gives $l=1-te^{-i(\alpha+\beta)}$. A determinant encoding the assertion that the circumcentre of $0,k,l$ lies on the perpendicular bisector of $1/2,w/2$ factors as a nonzero scalar times $\Im((w-k)\bar w e^{-i(\alpha+\gamma)})$, which vanishes exactly because $\angle LCK=\alpha+\gamma$. Thus only a transparent derivation of the determinant identity and careful signed-angle justification remain before the solution is fully rigorous.

## Full proof
Let
\[
\alpha=\angle KBA=\angle ACL,
\quad\beta=\angle LBK=\angle LNC,
\quad\gamma=\angle LCK=\angle BMK.
\]
Identify the plane with $\mathbb C$ and normalize $A=0$, $B=1$, $C=w$. Reflection of the diagram if necessary lets $\Im w>0$. Then the interior assumptions determine the directed ray angles used below.

Writing $k,l$ for the coordinates of $K,L$, the intersection of the ray from $B$ in direction $\pi-\alpha$ with the ray from $M=1/2$ in direction $\gamma$ gives
\[
k=1-\frac{\sin\gamma}{2\sin(\alpha+\gamma)}e^{-i\alpha}.
\]
Likewise, after scaling about $A$ by $1/w$, the intersection defining $L$ gives
\[
\frac lw=g=1-\frac{\sin\beta}{2\sin(\alpha+\beta)}e^{i\alpha}.
\]
Finally $\angle ABL=\alpha+\beta$, so for some $t>0$,
\[
l=1-te^{-i(\alpha+\beta)},\qquad w=\frac lg.
\]
Put $s=\alpha+\beta$, $r=\alpha+\gamma$. The third angle condition gives
\[
\Im((w-k)\bar w e^{-ir})=0,
\]
because $(k-w)/(-w)$ has argument $r$.

The circle through $0,k,l$ has an equation
\[
z\bar z+\bar qz+q\bar z=0,
\]
whose centre is $O=-q$. The assertion $|O-1/2|=|O-w/2|$ is, after expanding squares,
\[
E:=\frac{1-|w|^2}{4}+\frac{\bar q(1-w)+q(1-\bar w)}2=0.
\]
The equations at $k$ and $l$, together with $E=0$, are compatible exactly when
\[
D:=\det\begin{pmatrix}
 |k|^2&k&\bar k\\
 |l|^2&l&\bar l\\
 \dfrac{1-|w|^2}{4}&\dfrac{1-w}{2}&\dfrac{1-\bar w}{2}
\end{pmatrix}=0.
\]
The remaining algebraic lemma is
\[
\frac Di=\frac{\sin\alpha(2t\sin\alpha+\sin\beta)}{4\sin s\sin r}
\Im((w-k)\bar w e^{-ir}).
\]
Once this elementary identity is supplied with a readable derivation, the preceding vanishing proves $D=0$, hence $E=0$ (the first two rows are independent because the circumcircle exists), and therefore $OM=ON$.
