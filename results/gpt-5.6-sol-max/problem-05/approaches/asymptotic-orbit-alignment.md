# Asymptotic alignment of forward orbits

## Idea
Compare points far along two arithmetic forward orbits. Align one orbit point $x$ with the successor $f(y)$ of a point on the other orbit. The RMS--AM gap then tends to zero, forcing an ordering between the two orbit step sizes.

## Status
Successful.

## Details
Suppose $d(a)=p>0$ and $d(b)=q>0$. Orbit points have the form
\[
x=a+mp,\qquad y=b+nq,
\]
with $d(x)=p$ and $d(y)=q$. Put $v=f(y)=b+(n+1)q$. The upper inequality yields
\[
p-q\le \Phi(x,v),
\qquad
\Phi(u,v)=\sqrt{2(u^2+v^2)}-u-v
=\frac{(u-v)^2}{\sqrt{2(u^2+v^2)}+u+v}.
\]
For each sufficiently large $m$, take
\[
n=\left\lfloor\frac{a+mp-(b+q)}q\right\rfloor.
\]
Then $0\le x-v<q$, while $x,v\to\infty$. Consequently
\[
0\le\Phi(x,v)\le \frac{q^2}{x+v}\to0,
\]
so $p\le q$. Reversing the roles of the two orbits gives $q\le p$. Thus all positive values of $d$ are equal.

No density or rationality property of $p/q$ is needed: a bounded alignment error suffices because the denominator in the rationalized RMS gap tends to infinity.
