# Safe-child invariant

## Statement
Fix $0^\circ<\theta<180^\circ$ such that $180^\circ/\theta$ is not an integer. Call a triangle **safe** if none of its angles is a positive integral multiple of $\theta$. After any legal cut of a safe triangle, at least one of the two child triangles is safe.

## Proof
Let the angles of the safe parent triangle be $A,B,C$, and suppose the cut is drawn from the $A$-vertex to the opposite side. Put $x=\angle BAP$, so the two children have angle triples
\[
(B,x,180^\circ-B-x),\qquad (C,A-x,B+x).
\]
Assume for contradiction that both children are not safe. Since the inherited angles $B$ and $C$ are safe, there are positive integers $p,q$ for which one equality from each of the following two rows holds:
\[
 x=p\theta\quad\text{or}\quad 180^\circ-B-x=p\theta,
\]
\[
 A-x=q\theta\quad\text{or}\quad B+x=q\theta.
\]
There are four combinations.

1. If $x=p\theta$ and $A-x=q\theta$, then $A=(p+q)\theta$.
2. If $x=p\theta$ and $B+x=q\theta$, then $B=(q-p)\theta$; positivity of $B$ makes $q-p$ a positive integer.
3. If $180^\circ-B-x=p\theta$ and $A-x=q\theta$, then, using $180^\circ-B=A+C$, subtraction gives $C=(p-q)\theta$; positivity of $C$ makes $p-q$ a positive integer.
4. If $180^\circ-B-x=p\theta$ and $B+x=q\theta$, then $180^\circ=(p+q)\theta$.

The first three alternatives contradict the safety of the parent. The fourth says that $180^\circ/\theta=p+q$ is an integer, contrary to the hypothesis. Thus both children cannot be unsafe. $\square$
