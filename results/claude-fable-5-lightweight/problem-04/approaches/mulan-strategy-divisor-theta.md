# Approach: Mulan's strategy when $n\theta = 180^\circ$ ($n\ge 2$ integer)

**Status: complete (this is the winning-side half of the final proof).**

Idea: the set $\theta\mathbb N=\{\theta,2\theta,\dots,(n-1)\theta\}$ (multiples below $180^\circ$)
is a "ratchet": by the chain lemma any triangle containing such an angle is already won for Mulan.
So it suffices to reach, from an arbitrary triangle, a position where **both** children of some cut
contain an angle in $\theta\mathbb N$; then whichever piece Shan-Yu keeps is won.

The double threat: cut through the vertex of a **largest** angle $A$, and choose $\alpha$ so that
the angle at $P$ in $T_1$ equals $k\theta$, i.e. $\alpha = 180^\circ-B-k\theta$. Then
$T_1\ni k\theta$ and $T_2$'s angle at $P$ is $B+\alpha = 180^\circ-k\theta=(n-k)\theta$.
This is where $n\theta=180^\circ$ is used: the two angles at $P$ sum to $180^\circ$, so both can be
multiples of $\theta$ **only if** $180^\circ$ is a multiple of $\theta$.

Feasibility of $k$: need a multiple $k\theta$ in the open interval $(C,180^\circ-B)$, whose length
is $A$ (largest angle, so $A\ge 60^\circ$). Two cases:
- $n\ge3$: then $\theta\le 60^\circ\le A$ and $A\notin\theta\mathbb N$ forces $A>\theta$; an open
  interval of length $>\theta$ whose left endpoint is not a multiple of $\theta$ contains a
  multiple of $\theta$.
- $n=2$ ($\theta=90^\circ$): $B,C<90^\circ$ (if $A>90^\circ$ then $B+C<90^\circ$; if $A<90^\circ$
  all angles $<90^\circ$; $A=90^\circ$ is impossible since the game would have stopped), so
  $90^\circ\in(C,180^\circ-B)$, take $k=1$. (Geometrically: the altitude from $A$.)

Total: at most $n-1$ cuts. Verified exactly for $n=2,\dots,8$ against random Shan-Yu play in
`code/verify.py` (`test_mulan`).
