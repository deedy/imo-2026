# Lemma (Chain lemma)

Fix $\theta\in(0^\circ,180^\circ)$.

**Statement.** If at the start of a round the triangle $\mathcal T$ has an angle equal to
$k\theta$ for some integer $k\ge 1$ (necessarily $k\theta<180^\circ$), then Mulan can win within
at most $k-1$ further cuts, no matter how Shan-Yu plays.

**Proof.** Induction on $k$.

*Base $k=1$:* $\mathcal T$ has an angle $\theta$, so the game stops at once and Mulan wins (0 cuts).

*Step $k\ge 2$:* Let $A=k\theta$ be that angle and $B,C$ the other two angles. Since
$0<\theta<k\theta=A$, by the cut parametrization lemma Mulan may cut through vertex $A$ with
$\alpha=\theta$. The children are
$$T_1=\{B,\ \theta,\ 180^\circ-B-\theta\},\qquad T_2=\{C,\ (k-1)\theta,\ B+\theta\}.$$
If Shan-Yu keeps $T_1$, the next round starts with a triangle having an angle exactly $\theta$,
so the game stops and Mulan wins (1 cut total). If Shan-Yu keeps $T_2$, it has an angle
$(k-1)\theta$, and by the induction hypothesis Mulan wins within $k-2$ further cuts, i.e. $k-1$
cuts in total. $\blacksquare$
