# Lemma 5 — angle addition inside an angle

**Definition.** For $0^\circ<\angle QVR<180^\circ$, "$P$ lies inside angle $QVR$" means: $P$ is strictly on the same side of line $VQ$ as $R$, and strictly on the same side of line $VR$ as $Q$.

**Lemma.** If $P$ lies inside angle $QVR$ then $\angle QVP+\angle PVR=\angle QVR$ and $0^\circ<\angle QVP<\angle QVR$.

**Proof.** Unsigned angles and sides of lines are invariant under translations, rotations, reflections; place $V=0$ with unit vector along $VQ$ equal to $q=(1,0)$ and, reflecting in the $x$-axis if necessary, unit vector along $VR$ equal to $r=(\cos\gamma,\sin\gamma)$ with $\gamma:=\angle QVR\in(0^\circ,180^\circ)$. Let $p=(\cos\sigma,\sin\sigma)$, $\sigma\in(-180^\circ,180^\circ]$, be the unit vector along $VP$.

Same side of line $VQ$ (the $x$-axis) as $R$: $\sin\sigma>0$, i.e. $\sigma\in(0^\circ,180^\circ)$.
Same side of line $VR$ as $Q$: $r\times p$ has the sign of $r\times q=-\sin\gamma<0$; and $r\times p=\sin(\sigma-\gamma)$ with $\sigma-\gamma\in(-180^\circ,180^\circ)$, so this says $\sigma<\gamma$.

Hence $0<\sigma<\gamma$, and $\angle QVP=\sigma$, $\angle PVR=\gamma-\sigma$, $\angle QVR=\gamma$. $\blacksquare$
