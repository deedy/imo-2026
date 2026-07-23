# Connectedness after displacement quantization

## Idea
Once the displacement is known to take only the values $0$ and one fixed $c>0$, show that both level sets would be open. Connectedness then excludes their coexistence.

## Status
Successful.

## Details
Let
\[
A=\{t:d(t)=0\},\qquad B=\{t:d(t)=c\}.
\]
For $x\in B$ and $y\in A$, the upper inequality implies
\[
c\le \Phi(x,y),
\qquad
\Phi(x,y)=\sqrt{2(x^2+y^2)}-x-y.
\]
But $\Phi$ is continuous and $\Phi(t,t)=0$. Around a point $b\in B$, all nearby $y$ satisfy $\Phi(b,y)<c$, so none can lie in $A$; thus $B$ is open. Around a point $a\in A$, all nearby $x$ satisfy $\Phi(x,a)<c$, so none can lie in $B$; thus $A$ is open. As $A,B$ partition the connected interval $\mathbb R_{>0}$, one is empty. If $c$ occurs, then $B$ is nonempty and hence $A$ is empty.

This argument obtains the needed regularity from the inequality itself; no prior continuity or monotonicity of $f$ is assumed.
