# Backward forcing from target multiples

## Idea
Enlarge the immediately terminal set (triangles containing $\theta$) to a class from which victory can be forced recursively.

## Status
Successful, used for sufficiency.

## Details
Any triangle containing $m\theta$ for a positive integer $m$ is winning. For $m\ge2$, cut from that vertex and divide the angle as
\[
m\theta=\theta+(m-1)\theta.
\]
Whichever child Shan-Yu retains, it either contains the target immediately or contains the lower multiple $(m-1)\theta$. Induction gives a bound of $m-1$ further cuts.

When $180^\circ=n\theta$, it therefore suffices to make one cut whose two possible children each contain some positive integral multiple of $\theta$. The cut-point angles are supplementary, so forcing them to be $k\theta$ and $(n-k)\theta$ does exactly this.
