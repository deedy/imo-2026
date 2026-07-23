# imo-2026-05 — tracking file
## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- Tested affine and multiplicative candidates. This identified the family $f(x)=x+c$ with $c\ge 0$; direct substitution turns both squared inequality gaps into $(x-y-c)^2$.
- Used the equality-producing substitution $x=f(y)$. It gives the exact second-iterate relation $f(f(y))=2f(y)-y$.
- Iterated the second-iterate relation. Every forward orbit is the arithmetic progression $f^n(x)=x+n(f(x)-x)$, so positivity of the codomain forces $f(x)\ge x$.
- Rewrote the upper inequality in terms of the displacement $d(x)=f(x)-x$. For two strictly positive displacements, synchronized their arithmetic orbits to remain a bounded distance apart while tending to infinity. Applying the upper inequality in both orders forces the two displacements to be equal.
- Ruled out coexistence of zero displacement and a common positive displacement. The upper inequality separates points of the two types by more than the positive displacement, while a finite chain in an interval with shorter steps must contain two adjacent points of different types.
- Also examined pointwise bounds obtained from $x=y$ and the lower inequality; these give rough growth restrictions but do not by themselves compare displacements at different points, so they were not used in the final proof.

## Current best
All solutions are exactly $\boxed{f(x)=x+c\quad(x>0)}$, where $c$ is an arbitrary real constant with $c\ge 0$.

## Full proof
Define the displacement
\[
d(t):=f(t)-t\qquad(t>0).
\]
We first obtain an exact relation. In the given chain put $x=f(y)$. Its leftmost term is then
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y),
\]
and its rightmost term is
\[
\sqrt{f(y)f(y)}=f(y).
\]
Consequently the middle term is equal to $f(y)$, and hence
\[
f(f(y))=2f(y)-y. \tag{1}
\]
It follows that
\[
d(f(y))=f(f(y))-f(y)=f(y)-y=d(y). \tag{2}
\]
By induction, (2) gives, for every integer $n\ge 0$,
\[
f^n(y)=y+n d(y). \tag{3}
\]
If $d(y)<0$, then the right-hand side of (3) is nonpositive for every sufficiently large $n$, contrary to the fact that every iterate of $f$ lies in $\mathbb R_{>0}$. Thus
\[
d(y)\ge 0\qquad\text{for every }y>0. \tag{4}
\]

We next prove that any two positive values of $d$ are equal. Squaring the first inequality in the given chain is legitimate because both sides are positive. On writing
\[
a=d(x),\qquad b=d(y),
\]
we obtain
\[
2x^2+2(y+b)^2\ge (x+a+y)^2,
\]
or equivalently
\[
(x-y)^2+4yb+2b^2\ge 2a(x+y)+a^2. \tag{5}
\]

Let $u,v>0$ satisfy
\[
d(u)=a>0,\qquad d(v)=b>0.
\]
By (2)--(3),
\[
d(u+ma)=a,\qquad d(v+nb)=b \tag{6}
\]
for all integers $m,n\ge 0$. For every sufficiently large integer $m$, put
\[
X_m=u+ma,
\qquad
n_m=\left\lfloor\frac{X_m-v}{b}\right\rfloor,
\qquad
Y_m=v+n_m b.
\]
Then $n_m\ge 0$ and
\[
0\le X_m-Y_m<b. \tag{7}
\]
In particular, $X_m,Y_m\to\infty$ and $X_m/Y_m\to1$. By (6), their displacements are respectively $a,b$. Apply (5) with $(x,y)=(X_m,Y_m)$ and divide by $Y_m$:
\[
\frac{(X_m-Y_m)^2}{Y_m}+4b+\frac{2b^2}{Y_m}
\ge
2a\left(\frac{X_m}{Y_m}+1\right)+\frac{a^2}{Y_m}.
\]
Letting $m\to\infty$ and using (7) yields $4b\ge4a$, so $b\ge a$. Applying (5) instead with $(x,y)=(Y_m,X_m)$ and dividing by $X_m$ gives, in the same way, $4a\ge4b$. Therefore $a=b$.

It follows that either $d$ is identically zero, or there is a number $c>0$ such that
\[
d(t)\in\{0,c\}\qquad(t>0). \tag{8}
\]
We show that in the latter case the value $0$ cannot occur. Suppose that $d(p)=c$ and $d(q)=0$. Substitution of $x=p$, $y=q$, $a=c$, and $b=0$ into (5) gives
\[
(p-q)^2\ge 2c(p+q)+c^2>c^2,
\]
so every point with displacement $c$ is at distance greater than $c$ from every point with displacement $0$:
\[
|p-q|>c. \tag{9}
\]
If both types in (8) occurred, choose one point $p$ of the first type and one point $q$ of the second type. Choose an integer $N>|p-q|/c$ and divide the interval from $p$ to $q$ into the points
\[
t_i=p+\frac{i}{N}(q-p),\qquad i=0,1,\ldots,N.
\]
All these points are positive, and consecutive ones are at distance $|p-q|/N<c$. Since $t_0$ and $t_N$ have different displacement types, some consecutive pair must have different types. This contradicts (9). Hence no mixing is possible. Together with (4), we have proved that for some constant $c\ge0$,
\[
d(t)=c\qquad(t>0),
\]
and therefore
\[
f(t)=t+c. \tag{10}
\]

It remains to verify these functions. Let $c\ge0$ and $f(t)=t+c$. For every $x,y>0$, the arithmetic mean of the two positive numbers $x$ and $y+c$ is
\[
\frac{x+y+c}{2}=\frac{f(x)+y}{2}.
\]
The root-mean-square--arithmetic-mean and arithmetic-mean--geometric-mean inequalities give
\[
\sqrt{\frac{x^2+(y+c)^2}{2}}
\ge \frac{x+y+c}{2}
\ge \sqrt{x(y+c)},
\]
which is exactly the required chain. Thus all and only the functions in (10), with $c\ge0$, are solutions.
