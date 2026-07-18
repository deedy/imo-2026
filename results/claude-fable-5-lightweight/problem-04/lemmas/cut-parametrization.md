# Lemma (Cut parametrization)

**Statement.** Let $\mathcal T$ be a triangle whose angles are $A, B, C$ (at vertices which we
also call $A,B,C$). A legal cut of Mulan through vertex $A$ goes to a point $P$ in the interior of
side $BC$. Writing $\alpha=\angle BAP$, the cut is legal iff $\alpha\in(0,A)$, every such $\alpha$
is realizable by exactly one $P$, and the two resulting triangles have angle multisets
$$T_1=\{B,\ \alpha,\ 180^\circ-B-\alpha\},\qquad T_2=\{C,\ A-\alpha,\ B+\alpha\}.$$

**Proof.** As $P$ moves along the open segment $BC$, the ray $AP$ sweeps the open angular region
between rays $AB$ and $AC$, so $\alpha=\angle BAP$ ranges bijectively and continuously over
$(0^\circ,A)$; $P$ interior to $BC$ corresponds exactly to $0<\alpha<A$.

Triangle $ABP$ has angle $B$ at $B$ and angle $\alpha$ at $A$; hence its angle at $P$ is
$\angle APB=180^\circ-B-\alpha$. Triangle $APC$ has angle $C$ at $C$ and angle $A-\alpha$ at $A$;
hence its angle at $P$ is $180^\circ-C-(A-\alpha)=(180^\circ-A-B-C)+B+\alpha=B+\alpha$.
(Equivalently, $\angle APC=180^\circ-\angle APB$.) $\blacksquare$

*Sanity check:* verified numerically with random coordinates in `code/verify.py` (`geo_check`).
