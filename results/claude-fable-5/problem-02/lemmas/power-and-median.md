# Lemma 1 (power of a point along a line) and Lemma 4 (median length)

**Lemma 1.** Let $\Gamma$ be a circle with centre $Z_0$ and radius $\rho>0$, and $\ell$ a line.
(i) $\ell\cap\Gamma$ has at most two points.
(ii) If $M\in\Gamma$, there is exactly one line through $M$ meeting $\Gamma$ only at $M$ (the tangent at $M$); its direction is $i(M-Z_0)$.
(iii) If $Z\in\ell$ and $\ell$ meets $\Gamma$ at $U,V$ (with $U=V$ in the tangent case), then $\operatorname{pow}(Z,\Gamma):=|Z-Z_0|^2-\rho^2=\langle U-Z,V-Z\rangle$ (product of signed lengths along $\ell$).

**Proof.** Parametrize $\ell=\{Z+td\}$, $|d|=1$. Then
$$|Z+td-Z_0|^2-\rho^2=t^2+2t\langle d,Z-Z_0\rangle+\operatorname{pow}(Z,\Gamma),$$
a monic quadratic in $t$: at most two roots — (i). For (ii) take $Z=M\in\Gamma$: roots $0$ and $-2\langle d,M-Z_0\rangle$, coincident iff $d\perp(M-Z_0)$, which determines a unique line through $M$. For (iii): with $U=Z+t_1d$, $V=Z+t_2d$, Vieta gives $t_1t_2=\operatorname{pow}(Z,\Gamma)$, and $\langle U-Z,V-Z\rangle=t_1t_2$. $\blacksquare$

**Lemma 4.** For any points $O,P,Q$ and $W=\tfrac12(P+Q)$:
$$4|OW|^2=2|OP|^2+2|OQ|^2-|PQ|^2 .$$

**Proof.** $4|W-O|^2=|(P-O)+(Q-O)|^2=|P-O|^2+2\langle P-O,Q-O\rangle+|Q-O|^2$ and $|PQ|^2=|P-O|^2-2\langle P-O,Q-O\rangle+|Q-O|^2$; add. $\blacksquare$
