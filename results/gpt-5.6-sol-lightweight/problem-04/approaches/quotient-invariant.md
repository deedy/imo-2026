# Quotient-group obstruction

**Idea.** Work modulo the additive subgroup \(\theta\mathbb Z\). If \(180^\circ\notin\theta\mathbb Z\), Shan-Yu starts with a triangle none of whose angles is \(0\) modulo \(\theta\), and always retains a child with the same property.

Write the parent classes as \(a,b,c\), their sum as \(t=[180^\circ]\ne0\), and split \(a=u+v\). The child class triples are
\[
(u,b,c+v),\qquad (v,c,b+u).
\]
Because \(b,c\ne0\), for the first child to acquire a zero one needs \(u=0\) or \(c+v=0\); for the second, one needs \(v=0\) or \(b+u=0\). Every pairing except \(c+v=0=b+u\) contradicts \(a,b,c\ne0\); the last pairing implies \(t=0\). Hence the two children cannot both contain a multiple of \(\theta\).

This property excludes an angle exactly \(\theta\), so Mulan can never win.

**Status:** Complete; proves necessity.