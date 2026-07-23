# Lemma: reduction of an integral multiple of the target

## Statement
Normalize a straight angle to have measure $1$, and let $t=1/n$ for an integer $n\ge2$. If the current triangle has an angle $kt$ for some integer $k$ with $1\le k\le n-1$, then Mulan can force a win after at most $k-1$ further cuts.

## Proof
We use induction on $k$. If $k=1$, the triangle already has an angle $t$, so Mulan has won without another cut.

Now let $k\ge2$. From the vertex whose angle is $kt$, Mulan draws the unique interior ray which splits this angle into portions $t$ and $(k-1)t$. This ray meets the opposite side at a nonvertex point, so it is a legal cut. One child contains the angle $t$, while the other contains the angle $(k-1)t$. If Shan-Yu keeps the former, Mulan wins. If he keeps the latter, the induction hypothesis gives a win after at most $k-2$ additional cuts. In either case, at most $k-1$ cuts are required. $\square$
