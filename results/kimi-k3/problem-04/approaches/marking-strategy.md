# Approach: Mulan's winning strategy for $\theta=180^\circ/n$ (status: proved, Theorem 1)

**Idea.** Measure angles in units of $\theta$; the triangle sums to $n$
(an integer). "Marked" angles are the integer multiples of $\theta$ in
$(0^\circ,180^\circ)$; by the halving lemma any triangle containing a marked
angle $k\theta$ is won within $k-1$ moves.

**The one-move reduction.** If no angle is marked, Mulan wants a single cut
making *both* halves marked. Cut at vertex $A=v$ with $\alpha$: the halves are
$\{u,\alpha,180^\circ-u-\alpha\}$ and $\{w,v-\alpha,u+\alpha\}$. Choose
$\alpha=d(u)$, the distance from $u$ up to the next multiple of $\theta$. Then
$u+\alpha$ is a multiple of $\theta$ — and, crucially, so is its supplement
$180^\circ-(u+\alpha)$, **because $180^\circ=n\theta$ is itself a multiple of
$\theta$**. This is the only place the hypothesis $\theta=180^\circ/n$ is used
on Mulan's side. The move is legal iff $d(u)<v$.

**The pairing lemma.** Among the three (unmarked) angles there is always an
ordered pair $u\ne v$ with $d(u)<v$: the numbers $d(\cdot)\in(0,\theta)$ sum to
a multiple of $\theta$ in $\{\theta,2\theta\}$ (since $u+d(u)$ are multiples of
$\theta$ summing to $180^\circ+\sum d$), while failure of all pairs gives
$\sum d\ge \sum u = n\theta$, forcing $n=2$ and equalities $d(A)=B$, $d(B)=C$,
$d(C)=A$, whence $A+d(A)=A+B$ a multiple of $\theta$ forces
$C=\theta$ — contradiction.

**Bound.** $1$ move to make both halves marked, then $\le n-2$ halving moves:
total $\le n-1$ (computations show this is exactly the worst case).

See `current.md` for the full rigorous proof.
