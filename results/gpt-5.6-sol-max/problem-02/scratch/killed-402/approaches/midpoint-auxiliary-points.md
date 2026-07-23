# Auxiliary points beyond the midpoints

## Idea
Define $P$ on line $BK$ by requiring $K$ to be the midpoint of $BP$, and define $Q$ on line $CL$ by requiring $L$ to be the midpoint of $CQ$. Since $M,K$ are midpoints of $AB,BP$ in triangle $ABP$, we have $MK\parallel AP$; similarly $NL\parallel AQ$. Thus, writing
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,\quad z=\angle LCK=\angle BMK,
\]
the hypotheses become
\[
\angle PBA=x,\quad \angle BAP=z,\qquad
\angle ACQ=x,\quad \angle QAC=y,
\]
with $L$ the midpoint of $CQ$, $K$ the midpoint of $BP$, and additionally $\angle LBP=y$, $\angle QCK=z$.

## Current status
Promising. This turns every given angle into ordinary angle data in two triangles $ABP$ and $ACQ$, and makes a trigonometric parametrization possible.

Put $\alpha=\angle BAC$, $AB=c$, $AC=b$. Orient $AB$ at argument $0$ and $AC$ at argument $\alpha$. By the sine rule,
\[
 AP=c\frac{\sin x}{\sin(x+z)},\qquad AQ=b\frac{\sin x}{\sin(x+y)}.
\]
Consequently
\[
 K=\frac c2\left(1+\frac{\sin x}{\sin(x+z)}e^{iz}\right),
\quad
 L=\frac b2e^{i\alpha}\left(1+\frac{\sin x}{\sin(x+y)}e^{-iy}\right).
\]
The direction conditions $\arg(BL)=\pi-x-y$ and $\arg(CK)=\alpha+\pi+x+z$ give
\[
2c\sin(x+y)=b\left(\sin(\alpha+x+y)+\frac{\sin x\sin(\alpha+x)}{\sin(x+y)}\right),
\]
\[
2b\sin(x+z)=c\left(\sin(\alpha+x+z)+\frac{\sin x\sin(\alpha+x)}{\sin(x+z)}\right).
\]
The next step is to factor the compatibility condition and then prove the circumcircle/power identity.
