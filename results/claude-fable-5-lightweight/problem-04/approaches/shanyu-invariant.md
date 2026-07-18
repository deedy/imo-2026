# Approach: Shan-Yu's invariant when $180^\circ$ is NOT an integer multiple of $\theta$

**Status: complete (this is the losing-side half of the final proof).**

Call a triangle **safe** if none of its three angles lies in
$\theta\mathbb N = \{\theta,2\theta,3\theta,\dots\}$.

Claim: if $180^\circ\notin\theta\mathbb N$ then from any safe triangle, after any Mulan cut, at
least one of the two children is safe. Indeed, cut at vertex $A$ with parameter
$\alpha\in(0,A)$; children $T_1=\{B,\alpha,180^\circ-B-\alpha\}$, $T_2=\{C,A-\alpha,B+\alpha\}$.
$B,C\notin\theta\mathbb N$ by safety, so if both children are unsafe then one of
$\{\alpha,180^\circ-B-\alpha\}$ and one of $\{A-\alpha,B+\alpha\}$ is a positive multiple of
$\theta$. All four combinations force a contradiction:
1. $\alpha=k\theta$, $A-\alpha=m\theta$ $\Rightarrow A=(k+m)\theta\in\theta\mathbb N$;
2. $\alpha=k\theta$, $B+\alpha=m\theta$ $\Rightarrow B=(m-k)\theta\in\theta\mathbb N$ (as $B>0$);
3. $180^\circ-B-\alpha=k\theta$, $A-\alpha=m\theta$ $\Rightarrow C=(k-m)\theta\in\theta\mathbb N$ (as $C>0$);
4. $180^\circ-B-\alpha=k\theta$, $B+\alpha=m\theta$ $\Rightarrow 180^\circ=(k+m)\theta$.

So Shan-Yu starts with a safe triangle (exists: only finitely many multiples of $\theta$ to avoid)
and always keeps a safe child; the triangle never has an angle $\theta$, so the game never ends.

This covers **all** $\theta$ with $180^\circ/\theta\notin\mathbb Z$, including every
$\theta\in(90^\circ,180^\circ)$ and e.g. $\theta=72^\circ$. Verified exactly for several such
$\theta$ in `code/verify.py` (`test_shanyu`), with Mulan trying all "threatening" cut values.

## Dead ends recorded along the way
- Tried invariant "all angles $<\theta$" for $\theta>90^\circ$ (works, via keeping the piece whose
  new angle at $P$ is $\le 90^\circ$), but the $\theta\mathbb N$-avoidance invariant subsumes it.
- Tried invariants "all angles $>\theta$" and "all angles in $(\theta,2\theta)$" for small
  $\theta$: not closed under Mulan's cuts. Abandoned in favor of the arithmetic invariant.
