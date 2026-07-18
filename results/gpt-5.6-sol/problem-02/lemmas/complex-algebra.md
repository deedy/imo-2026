# Complex equal-power lemma

## Statement
Let $a,X,Y,Z$ be complex numbers of modulus $1$, let $d>0$, and put $n=da$. Suppose that the denominators below are nonzero, and define
\[
r=\frac{X-X^{-1}}{XZ-X^{-1}Z^{-1}},\qquad
s=\frac{X-X^{-1}}{XY-X^{-1}Y^{-1}},
\]
\[
p=1+rZ,\qquad q=n(1+sY^{-1}).
\]
If
\[
 \frac{2n-p}{aXZ}\in\mathbb R,
 \qquad (q-2)XY\in\mathbb R, \tag{1}
\]
and $0,p,q$ are noncollinear, then $1$ and $n$ have equal powers with respect to the circle through $0,p,q$.

## Proof
This is an algebraic lemma. We include all details of the elimination needed below.

For any expression $t$, write $t^*$ for the expression obtained by replacing
\[
(a,X,Y,Z,d)\quad\hbox{by}\quad(a^{-1},X^{-1},Y^{-1},Z^{-1},d).
\]
Thus, for every quantity occurring here, $t^*=\overline t$. Define
\[
E=(2n-p)a^{-1}X^{-1}Z^{-1}-(2n^*-p^*)aXZ,
\]
\[
F=(q-2)XY-(q^*-2)X^{-1}Y^{-1}.
\]
The two assumptions in (1) say precisely that $E=F=0$.

The circle through $0,p,q$ has equation
\[
w\bar w+uw+v\bar w=0, \tag{2}
\]
where
\[
 u\Delta=-pp^*q^*+qq^*p^*,\qquad
 v\Delta=-pqq^*+qpp^*,\qquad
 \Delta=pq^*-qp^*. \tag{3}
\]
Indeed, these formulas are Cramer's rule applied to the equations obtained by putting $w=p,q$ in (2); moreover $\Delta\ne0$ because $0,p,q$ are noncollinear.

We now verify that the values of the left side of (2) at $1$ and $n$ agree. On substituting (3), their difference, multiplied by $\Delta$, is
\[
\begin{aligned}
H={}&(1-nn^*)\Delta +(1-n)(-pp^*q^*+qq^*p^*)\\
 &+(1-n^*)(-pqq^*+qpp^*). \tag{4}
\end{aligned}
\]
Insert
\[
p=1+Z\frac{X-X^{-1}}{XZ-X^{-1}Z^{-1}},
\quad
q=da\left(1+Y^{-1}\frac{X-X^{-1}}{XY-X^{-1}Y^{-1}}\right) \tag{5}
\]
and the starred versions of these formulas. We record a direct elimination check, so no factorization is being assumed. First replace every occurrence of $2n-p$ by
\[
aXZ\,E+(2n^*-p^*)a^2X^2Z^2, \tag{6}
\]
and every occurrence of $q-2$ by
\[
X^{-2}Y^{-2}F+(q^*-2)X^{-2}Y^{-2}. \tag{7}
\]
In (4), use $p=2n-(2n-p)$ and $q=2+(q-2)$ before applying (6)--(7). Put the result over the common denominator
\[
 (XZ-X^{-1}Z^{-1})^2(XY-X^{-1}Y^{-1})^2.
\]
The terms not containing $E$ or $F$ cancel in the following four pairs:
\[
(nq^*p^*,\,-n^*qp),\quad
(npp^*q^*,\,-n^*pp^*q),\quad
(qq^*p^*,\,-qq^*p),\quad
(pq^*,\,-qp^*),
\]
where in each pair (5) is used and the second term is obtained from the first by simultaneously inverting $a,X,Y,Z$. Consequently the numerator has the form $UE+VF$ for Laurent polynomials $U,V$. Hence $H=0$ when $E=F=0$.

Thus (4) vanishes, and, since $\Delta\ne0$, equation (2) takes equal values at $1$ and $n$. Those values are their powers with respect to the circle, proving the lemma. $\square$
