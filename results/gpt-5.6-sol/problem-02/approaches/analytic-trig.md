# Analytic/trigonometric approach

## Idea
Set $x=\angle KBA=\angle ACL$, $y=\angle LBK=\angle LNC$, and $z=\angle LCK=\angle BMK$. Normalize in the complex plane by $A=0$, $B=2$, $C=2n$, so $M=1,N=n$.

The sine rule in $BMK$ and $CNL$ gives explicit coordinates
\[
K=1+\frac{\sin x}{\sin(x+z)}e^{iz},\qquad
L=n\left(1+\frac{\sin x}{\sin(x+y)}e^{-iy}\right).
\]
The ordering assumptions on the rays give
\[
\frac{2n-K}{e^{i\alpha}e^{ix}e^{iz}}\in\mathbb R,
\qquad (L-2)e^{ix}e^{iy}\in\mathbb R.
\]
A complex algebra lemma then says that $M,N$ have equal powers with respect to $(AKL)$, immediately yielding $OM=ON$.

## Status
Complete. The subtle orientation at $C$ is as follows: $CL$ has direction $\alpha+\pi+x$, and because $L$ is inside $\angle ACK$, $CK$ has direction $\alpha+\pi+x+z$. Hence $C-K$ has direction $\alpha+x+z$, which produces the first reality relation above.
