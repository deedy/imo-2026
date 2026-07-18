# Lemma (halving lemma): triangles containing a multiple of $\theta$ are winning

**Statement.** Fix any $\theta\in(0^\circ,180^\circ)$. Let $k\ge 1$ be an
integer with $k\theta<180^\circ$. If the current triangle $\mathcal T$ has an
angle equal to $k\theta$, then Mulan can force victory from $\mathcal T$ in at
most $k-1$ further moves (for $k=1$ the game is already over).

**Proof.** Induction on $k$.

*Base $k=1$.* $\mathcal T$ has an angle exactly $\theta$, so the game stops
immediately: Mulan has won, $0$ moves.

*Step.* Let $k\ge 2$ and suppose $\mathcal T$ has angles $A=k\theta$, $B$, $C$.
Mulan cuts at the vertex with angle $A$ with parameter $\alpha=\theta$
(legitimate since $0<\theta<k\theta=A$). By the cut-geometry lemma the two
halves are
$$H_1=\{B,\ \theta,\ 180^\circ-B-\theta\},\qquad
  H_2=\{C,\ (k-1)\theta,\ B+\theta\}.$$
Both are genuine triangles: $180^\circ-B-\theta>0$ because
$B<180^\circ-A=180^\circ-k\theta\le 180^\circ-2\theta$.

If Shan-Yu keeps $H_1$, the new triangle has an angle $\theta$ and the game
stops: Mulan wins after this one move. If Shan-Yu keeps $H_2$, the new triangle
has an angle $(k-1)\theta$; if $k-1=1$ the game stops, otherwise by induction
Mulan wins from $H_2$ within $(k-1)-1=k-2$ further moves. In all cases Mulan
wins within $1+(k-2)=k-1$ moves. $\blacksquare$

**Remark.** No hypothesis on $\theta$ is needed here; the divisibility question
only enters in whether Mulan can *force* a multiple of $\theta$ to appear.
