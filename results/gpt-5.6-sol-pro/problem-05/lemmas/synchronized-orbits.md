# Synchronized-orbits lemma

## Statement
Suppose $d:\mathbb R_{>0}\to\mathbb R_{\ge0}$ has the following properties:

1. If $d(u)=a>0$, then $d(u+ma)=a$ for every integer $m\ge0$.
2. For all $x,y>0$, setting $a=d(x)$ and $b=d(y)$ gives
   \[
   (x-y)^2+4yb+2b^2\ge2a(x+y)+a^2. \tag{1}
   \]

Then all positive values of $d$ are equal.

## Proof
Let $d(u)=a>0$ and $d(v)=b>0$. Put $X_m=u+ma$. For all sufficiently large $m$, define
\[
n_m=\left\lfloor\frac{X_m-v}{b}\right\rfloor\ge0,
\qquad Y_m=v+n_m b.
\]
Then $0\le X_m-Y_m<b$. Hence $X_m,Y_m\to\infty$ and $X_m/Y_m\to1$. Property 1 gives $d(X_m)=a$ and $d(Y_m)=b$.

Use (1) with $(x,y)=(X_m,Y_m)$ and divide by $Y_m$. Passing to the limit yields $4b\ge4a$. Use (1) with $(x,y)=(Y_m,X_m)$ and divide by $X_m$; passing to the limit yields $4a\ge4b$. Thus $a=b$.
