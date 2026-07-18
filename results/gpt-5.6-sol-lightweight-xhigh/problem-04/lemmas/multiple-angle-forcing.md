# Forcing from an integral multiple of the target

## Statement
Fix $0^\circ<\theta<180^\circ$. If a current triangle has an angle $m\theta$, where $m$ is a positive integer, then Mulan can force a win after finitely many further cuts. More precisely, she needs at most $m-1$ cuts.

## Proof
We induct on $m$. For $m=1$, the current triangle already has an angle $\theta$, so the game stops before another cut.

Let $m\ge2$ and suppose the result holds for $m-1$. From the vertex whose angle is $m\theta$, Mulan draws the unique cevian which divides that angle into angles $\theta$ and $(m-1)\theta$. This is a legal cut because both parts are positive. One child has an angle $\theta$; if Shan-Yu retains it, Mulan wins at the next stopping check. The other child has an angle $(m-1)\theta$; if Shan-Yu retains that one, the induction hypothesis applies. Thus at most one cut followed by at most $m-2$ further cuts is enough. $\square$
