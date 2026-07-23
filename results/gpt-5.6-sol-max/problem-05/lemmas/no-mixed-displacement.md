# Lemma: zero and positive displacement cannot coexist

## Statement
Suppose a function satisfying the problem has displacement $d(t)=f(t)-t$ taking only the values $0$ and $c$, where $c>0$. If $c$ occurs, then $d(t)=c$ for every $t>0$.

## Proof
Define
\[
A=\{t>0:d(t)=0\},\qquad B=\{t>0:d(t)=c\}.
\]
For $x\in B$ and $y\in A$, the upper inequality reads
\[
\sqrt{\frac{x^2+y^2}{2}}\ge\frac{x+c+y}{2},
\]
and hence
\[
c\le\Phi(x,y),\qquad
\Phi(x,y)=\sqrt{2(x^2+y^2)}-x-y.
\]
The function $\Phi$ is continuous and $\Phi(t,t)=0$. If $b\in B$, every point sufficiently close to $b$ has $\Phi(b,y)<c$ and therefore cannot lie in $A$; so $B$ is open. If $a\in A$, every point sufficiently close to $a$ has $\Phi(x,a)<c$ and therefore cannot lie in $B$; so $A$ is open. The disjoint sets $A,B$ cover the connected interval $\mathbb R_{>0}$. Since $B$ is nonempty, $A$ must be empty. $\square$
