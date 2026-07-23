# Angle-parameter and polar-coordinate approach

## Idea
Set
\[
p=\angle KBA=\angle ACL,\quad q=\angle LBK=\angle LNC,\quad r=\angle LCK=\angle BMK.
\]
Let \(x=\angle BAK\) and \(y=\angle CAL\). Since \(M,N\) are midpoints, the sine rule in \(BMK,CNL\), followed by the sine rule in \(ABK,ACL\), gives
\[
\cot x=\cot p+2\cot r,\qquad \cot y=\cot p+2\cot q,
\]
and
\[
AK=cP_r,\quad AL=bP_q,\qquad P_r=\frac{\sin p}{\sin(p+x)},\quad P_q=\frac{\sin p}{\sin(p+y)},
\]
where \(c=AB,b=AC\). If \(\delta=\angle KAL=\alpha-x-y\), the two cross-angle hypotheses give
\[
\frac cbP_r=\frac{\sin(p+r)}{\sin(\delta+y+p+r)},\qquad
\frac bcP_q=\frac{\sin(p+q)}{\sin(\delta+x+p+q)}.
\]

If the circumcircle of \(AKL\) meets lines \(AB,AC\) again at \(D,E\), write directed \(AD=d,AE=e\). The desired assertion is equivalent to
\[
cd-be=\frac{c^2-b^2}{2}.
\]
Solving the circle equation in polar coordinates yields
\[
d=\frac{cP_r\sin(\alpha-y)-bP_q\sin x}{\sin\delta},\quad
e=\frac{-cP_r\sin y+bP_q\sin(\alpha-x)}{\sin\delta}.
\]
The midpoint construction also gives the very useful identity
\[
P_r\sin(\delta+x)-\frac12\sin\delta
=\frac{\sin p}{2\sin(p+r)}\sin(\delta+r),
\]
and its \((q,y)\)-analogue. Thus the target reduces to a trigonometric identity in \(p,q,r,x,y,\delta\), to be completed using the two cross-angle equations.

## Status
Promising and fully parameterizes the configuration. The final trigonometric identity remains to be organized/proved.
