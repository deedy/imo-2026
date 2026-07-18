# Lemma 3 — directed tangent–chord (statement + proof)

**Lemma.** Let $\Gamma$ be a circle through pairwise distinct points $M,K,C$, and let $t$ be the tangent to $\Gamma$ at $M$ (the unique line through $M$ meeting $\Gamma$ only at $M$; it has direction $i(M-Z_0)$ where $Z_0$ is the centre — see Lemma 1(ii) in `power-and-median.md`). Then:

(i) $\angle(t,MK)\equiv\angle(CM,CK)\pmod{180^\circ}$;

(ii) if a line $\ell$ through $M$ satisfies $\angle(\ell,MK)\equiv\angle(CM,CK)\pmod{180^\circ}$, then $\ell=t$; in particular $\ell\cap\Gamma=\{M\}$.

**Proof.** (i) Maps $Z\mapsto aZ+\beta$ ($a\in\mathbb C^*$) preserve directed line angles (all direction vectors are multiplied by $a$), and being bijections that map circles to circles, they map tangent lines to tangent lines. So assume $\Gamma$ is the unit circle centred at $0$; write $m,k,c$ for the three points, $|m|=|k|=|c|=1$, so $\bar m=1/m$, etc. The tangent $t$ at $m$ has direction $im$. Let
$$z:=\frac{(k-m)(m-c)}{m\,(k-c)}\ne0 .$$
Then
$$\bar z=\frac{\frac{m-k}{km}\cdot\frac{c-m}{mc}}{\frac1m\cdot\frac{c-k}{kc}}
=\frac{(m-k)(c-m)}{m(c-k)}=-z,$$
so $z$ is purely imaginary and $z/i\in\mathbb R\setminus\{0\}$. Hence
$$\angle(t,MK)-\angle(CM,CK)\equiv\arg\frac{k-m}{im}-\arg\frac{k-c}{m-c}
=\arg\frac{(k-m)(m-c)}{im(k-c)}=\arg\frac zi\equiv0\pmod{180^\circ}.$$

(ii) By (i), $\angle(\ell,MK)\equiv\angle(t,MK)$, so $\angle(\ell,t)\equiv0$, i.e. $\ell\parallel t$; both pass through $M$, hence $\ell=t$. $\blacksquare$

Numerically sanity-checked in `code/verify2.py` (2000 random instances, no mismatch).
