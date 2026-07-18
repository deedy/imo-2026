# Safe-triangle invariant

## Idea
For the negative direction, strengthen “does not contain the target” to “does not contain any positive integral multiple of the target.”

## Status
Successful, proves necessity.

## Details
Call a triangle safe if no angle is in $\{\theta,2\theta,3\theta,\ldots\}$. If a cut from angle $A$ uses parameter $x$, the children are
\[
(B,x,180^\circ-B-x),\qquad(C,A-x,B+x).
\]
If both are unsafe, select a target multiple from each. Pairing the two possible new angles in each child gives four cases. Three cases force one of $A,B,C$ to have already been a multiple of $\theta$; the fourth forces $180^\circ$ to be a multiple of $\theta$. Thus, when $180^\circ/\theta$ is nonintegral, every cut of a safe triangle has a safe child.

The equilateral triangle is safe in that situation: $60^\circ=m\theta$ would imply $180^\circ/\theta=3m$. Shan-Yu can start with it and always retain a safe child, preventing victory forever.
