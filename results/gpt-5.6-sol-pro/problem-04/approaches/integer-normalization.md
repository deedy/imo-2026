# Integer normalization and forcing strategy

## Idea
Normalize all angles by dividing by the target angle $\theta$, and write
\[
s=\frac{180^\circ}{\theta}.
\]
The target is then the normalized angle $1$, while every triangle has angle sum $s$.

If $s=N$ is an integer, any positive integral angle $m$ is winning: split it into $1$ and $m-1$, so either Shan-Yu leaves an immediate target or leaves a smaller positive integral angle. This is induction on $m$.

To create integral angles in both children at once, write the current angles as $a,b,c$. Cutting from the vertex of angle $a$ and taking the split parameter $x$ gives children
\[
(b,x,N-b-x),\qquad(c,a-x,b+x).
\]
If an integer $k$ lies in $(b,a+b)$, choose $x=k-b$. The first child then has angle $k$ and the second has angle $N-k$.

Such a labeling always exists when none of $a,b,c$ is integral:
- if some angle $a>1$, the interval $(b,a+b)$ has length greater than $1$;
- if all angles are less than $1$, then the integral sum must be $N=2$, and $b<1<a+b=2-c$.

## Status
Successful. This proves sufficiency for every $\theta=180^\circ/N$, $N\ge2$.
