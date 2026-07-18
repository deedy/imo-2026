# Lemma 2 — directed inscribed-angle criterion (statement + proof)

**Conventions.** Plane $=\mathbb C$. Directed angle between lines $\ell_1,\ell_2$ with direction vectors $d_1,d_2\ne0$: $\angle(\ell_1,\ell_2):=\arg(d_2/d_1)\bmod 180^\circ$ (well defined and additive mod $180^\circ$).

**Lemma.** Let $P,Q,R$ be pairwise distinct, non-collinear points and $\Gamma$ the unique circle through them. For every point $S\notin\{P,Q\}$:
$$S\in\Gamma\iff \angle(SP,SQ)\equiv\angle(RP,RQ)\pmod{180^\circ}.$$

**Proof.** Uniqueness of $\Gamma$: its centre is the intersection of the perpendicular bisectors of $PQ$ and $PR$ (not parallel since $P,Q,R$ are not collinear), and the radius is then determined.

Put $w:=(Q-R)\overline{(P-R)}\ne0$. Since $\frac{Q-R}{P-R}=\frac{w}{|P-R|^2}$ and $P,Q,R$ are not collinear, $\arg\frac{Q-R}{P-R}\not\equiv0\pmod{180^\circ}$, hence $\operatorname{Im}w\ne0$.

Define $g(Z):=\operatorname{Im}\big[w\,(P-Z)\overline{(Q-Z)}\big]$, a real-valued function on $\mathbb C$. Expanding $(P-Z)\overline{(Q-Z)}=P\bar Q-P\bar Z-\bar QZ+|Z|^2$ shows $g(Z)=(\operatorname{Im}w)|Z|^2+\lambda(Z)$ with $\lambda$ real affine in $Z\in\mathbb R^2$. Dividing by $\operatorname{Im}w\ne0$, the set $\{g=0\}$ is $\{|Z-Z_1|^2=\rho_1\}$ for some $Z_1\in\mathbb C$, $\rho_1\in\mathbb R$: it is empty, a point, or a circle. But
$$g(P)=0,\quad g(Q)=0,\quad g(R)=\operatorname{Im}\big[|P-R|^2|Q-R|^2\big]=0,$$
three distinct points, so $\{g=0\}$ is a circle through $P,Q,R$, hence $\{g=0\}=\Gamma$.

Now fix $S\notin\{P,Q\}$. Then
$$\angle(SP,SQ)\equiv\angle(RP,RQ)
\iff \arg\tfrac{Q-S}{P-S}\equiv\arg\tfrac{Q-R}{P-R}\ (180^\circ)
\iff \tfrac{Q-S}{P-S}\overline{\Big(\tfrac{Q-R}{P-R}\Big)}\in\mathbb R\setminus\{0\}.$$
Multiplying by the positive real $|P-S|^2|P-R|^2$, this is equivalent to $(Q-S)\overline{(P-S)}\,\overline{(Q-R)}(P-R)\in\mathbb R$, i.e. (conjugating) to $w(P-S)\overline{(Q-S)}\in\mathbb R$, i.e. to $g(S)=0$, i.e. to $S\in\Gamma$. (The quantity is automatically nonzero as $S\ne P,Q$ and $w\ne0$.) $\blacksquare$

Numerically sanity-checked in `code/verify2.py` (2000 random instances, no mismatch).
