# Analytic factorization lemma

## Statement
Let $p,q,s,t>0$. Put
\[
 K=\left(\frac{2p+s}{p+s},\frac{ps}{p+s}\right),\qquad
 L=(2-t(1-pq),t(p+q)),
\]
and let $\lambda=((2p+q)-ipq)/(p+q)$. Define $C=2N$ by the complex-vector relation $L=\lambda N$. If
\[
 (K-C)\times R_{x+z}N=0,
\]
where $p=\tan x,s=\tan z$ and $R_{x+z}$ denotes rotation by $x+z$, then $M=(1,0)$ and $N$ have equal powers with respect to the circle through $A=(0,0),K,L$.

## Proof status
Superseded by the fully proved, more general formulation in `lemmas/determinant-factorization.md`. In the notation below, the claim follows from that determinant factorization. Using the non-unit vector map
\[
T_{p,s}(u,v)=((1-ps)u-(p+s)v,(p+s)u+(1-ps)v),
\]
which is a positive scalar multiple of $R_{x+z}$, set
\[Q=(K-2N)\times T_{p,s}N.
\]
If
\[
D=\det\begin{pmatrix}
K_x&K_y&|K|^2\\
L_x&L_y&|L|^2\\
N_x-1&N_y&|N|^2-1
\end{pmatrix},
\]
a symbolic expansion and cancellation gives the compact identity
\[
D=\frac{p(pq^2t+pt+q)}{(p+q)(p+s)}Q.
\]
Thus $Q=0$ implies $D=0$. A complete human-verifiable derivation of this identity, organized by invariant quantities and coefficient comparison, is given in `lemmas/determinant-factorization.md` and reproduced in `current.md`.
