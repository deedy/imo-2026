# Angle-parameter analytic approach

## Idea
Let
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,\quad z=\angle LCK=\angle BMK.
\]
Place $A=0$, $B=1$, $C=\rho e^{i\alpha}$, so $M=1/2$ and $N=(\rho/2)e^{i\alpha}$. The local triangles $BMK$ and $CNL$ give explicit complex coordinates
\[
k=\frac12+\frac{\sin x}{2\sin(x+z)}e^{iz},\qquad
l=\rho e^{i\alpha}\left(\frac12+\frac{\sin x}{2\sin(x+y)}e^{-iy}\right).
\]
The remaining incidences $C,K$ and $B,L$ yield two formulas for $\rho$:
\[
2\rho\sin^2(x+z)=\sin(x+z)\sin(\alpha+x+z)+\sin x\sin(\alpha+x),
\]
\[
\rho\{\sin(x+y)\sin(\alpha+x+y)+\sin x\sin(\alpha+x)\}=2\sin^2(x+y).
\]
The plan is to express equality of the powers of $M,N$ to $(AKL)$ in these variables and show it is a consequence of these two incidence equations.

## Status
Superseded. The parametrization is valid, but direct elimination in $(\rho,\alpha)$ is unnecessarily long. The completed invariant reorganization is recorded in `approaches/invariant-factorization.md` and the master proof.
