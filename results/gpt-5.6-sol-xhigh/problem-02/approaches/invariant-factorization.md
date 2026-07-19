# Invariant determinant factorization

## Idea
Normalize $A=0$, $B=2$, $M=1$ and use
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,\quad z=\angle LCK=\angle BMK.
\]
The local triangles give
\[
k=1+\frac{\sin x}{\sin(x+z)}e^{iz},\quad
l=2-te^{-i(x+y)},\quad
l=\left(1+\frac{\sin x}{\sin(x+y)}e^{-iy}\right)n.
\]
The last incidence condition becomes
\[
[k-2n,e^{i(x+z)}n]=0.
\]
The desired equality of powers of $M$ and $N$ with respect to $(AKL)$ is represented by a $3\times3$ determinant $D$. Instead of expanding $N$, write $L=\lambda N$ and reduce $D$ and the incidence determinant to the four invariants $K\cdot L,[K,L],|K|^2,|L|^2$.

## Status
Completed. In tangent variables $p=\tan x,q=\tan y,s=\tan z$ and $r=t\cos x\cos y$, the invariant formulas yield
\[
(p+q)(p+s)D=p\{q+p(1+q^2)r\}[K-2N,TN],
\]
where $T=(1-ps)+i(p+s)=e^{i(x+z)}/(\cos x\cos z)$. The coefficient comparison, including an explicit difference table, is written in `current.md` and in `lemmas/determinant-factorization.md`. Conversion back to sines gives the exact factorization needed in the proof.