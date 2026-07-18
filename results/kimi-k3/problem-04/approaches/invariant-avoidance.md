# Approach: Shan-Yu's avoidance invariant for $\theta\ne180^\circ/m$ (status: proved, Theorem 2)

**Idea.** Shan-Yu maintains the invariant *"no angle of $\mathcal T$ is an
integer multiple of $\theta$"* (which is stronger than "no angle equal to
$\theta$"). Start: the equilateral triangle $(60^\circ,60^\circ,60^\circ)$ is
fine, because $60^\circ=k\theta$ would give $\theta=60^\circ/k=180^\circ/(3k)$,
of the excluded shape.

**Maintenance.** Given a clean triangle and any Mulan cut $(A,\alpha)$ with
halves $H_1=\{B,\alpha,180^\circ-B-\alpha\}$, $H_2=\{C,A-\alpha,B+\alpha\}$:

1. $\alpha=k\theta$ a multiple: then $H_2$ is clean ($A-\alpha=j\theta$ would
   give $A=(j+k)\theta$; $B+\alpha=j\theta$ would give $B=(j-k)\theta$).
2. $\alpha$ not a multiple and $180^\circ-B-\alpha$ not a multiple: $H_1$ clean.
3. $\alpha$ not a multiple but $180^\circ-B-\alpha=k\theta$: then in $H_2$,
   $A-\alpha=k\theta-C$ is not a multiple (else $C$ is), and
   $B+\alpha=180^\circ-k\theta$ — this is the *only* dangerous expression, and
   it is a multiple of $\theta$ iff $\theta=180^\circ/(j+k)$ for some $j\ge1$,
   i.e. iff $\theta=180^\circ/m$ for some integer $m\ge2$. Excluded by
   hypothesis. So $H_2$ is clean.

Case 3 is exactly where the argument fails for $\theta=180^\circ/n$ — matching
the fact that Mulan wins precisely those cases.

See `current.md` for the full rigorous proof.
