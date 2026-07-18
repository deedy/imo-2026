# Lemma: modular survival under a cut

## Statement
Fix \(\theta>0\), and suppose \(180^\circ\notin\theta\mathbb Z\). If no angle of a triangle belongs to \(\theta\mathbb Z\), then after any legal cut, at least one of the two resulting triangles has no angle in \(\theta\mathbb Z\).

## Proof
Take classes in the additive quotient group \(\mathbb R/(\theta\mathbb Z)\). Denote the parent angles by \(a,b,c\), so \(a,b,c\ne0\) and
\[
a+b+c=t:=[180^\circ]\ne0.
\]
Suppose the cut splits the angle with class \(a\) into classes \(u,v\), where \(u+v=a\). The class triples of the two children are
\[
(u,b,c+v)\quad\text{and}\quad(v,c,b+u).
\]
(The third angles are obtained by adding to each original endpoint angle the unused part of the split angle.)

Assume both children contain a zero class. Since \(b,c\ne0\), this requires one condition from each of
\[
u=0\ \text{or}\ c+v=0,
\qquad
v=0\ \text{or}\ b+u=0.
\]
The pairing \(u=v=0\) gives \(a=0\); the pairing \(u=0=b+u\) gives \(b=0\); and the pairing \(c+v=0=v\) gives \(c=0\). All are impossible. The only remaining pairing is
\[
c+v=0,\qquad b+u=0,
\]
which yields \(t=a+b+c=(u+v)+b+c=0\), also impossible. Therefore at least one child contains no zero class. \(\square\)
