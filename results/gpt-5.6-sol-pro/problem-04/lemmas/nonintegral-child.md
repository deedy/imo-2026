# Lemma: one child preserves nonintegrality

## Statement
Fix a nonintegral real number $s$. Suppose a triangle has normalized angle triple $(a,b,c)$, where $a,b,c$ are all nonintegral and $a+b+c=s$. After any legal cevian cut, at least one of the two resulting triangles has all three angles nonintegral.

## Proof
Relabel so that the cut is from the vertex of angle $a$ and splits that angle into $x$ and $a-x$. The child triples are
\[
(b,x,s-b-x),\qquad(c,a-x,b+x).
\]
Assume neither child has all its angles nonintegral. Since $b$ and $c$ are nonintegral, this means
\[
x\in\mathbb Z\ \text{or}\ s-b-x\in\mathbb Z,
\]
and
\[
a-x\in\mathbb Z\ \text{or}\ b+x\in\mathbb Z.
\]
Pairing the two choices gives four cases. Respectively, the sums or differences of the asserted integers show that
\[
a=x+(a-x),\quad b=(b+x)-x,
\]
\[
c=(s-b-x)-(a-x),\quad\text{or}\quad s=(s-b-x)+(b+x)
\]
is an integer. These contradict, respectively, the nonintegrality of $a,b,c,s$. Hence one child has three nonintegral angles. $\square$
