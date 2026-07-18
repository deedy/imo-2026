# imo-2026-05 — tracking file

## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- Tried the first guesses $f\equiv c$ and power functions $f(x)=x^a$. Constants fail immediately by letting $y\to0^+$ in the right-hand inequality; non-identity powers fail by homogeneity. This was a dead end for the full classification, but it suggested looking for functions making $f(x)+y$ equal to $x+f(y)$.
- Checked $f(x)=x+c$. It works because then $f(x)+y=x+f(y)$, so the middle term is exactly the arithmetic mean of the two numbers $x$ and $f(y)$ occurring in the quadratic and geometric means. This gave the candidate family and shifted the problem to proving that $f(x)-x$ is constant.
- Developed the successful "mean interval" approach (see `approaches/mean-interval.md`): for fixed $x,y$, the two given inequalities say that $(f(x)+y)^2$ lies in the interval $[(x+f(y))^2-(x-f(y))^2,\ (x+f(y))^2+(x-f(y))^2]$. Substituting $x=f(y)$ forces $f(f(y))=2f(y)-y$.
- Developed the successful "orbit/forbidden interval" argument (see `approaches/orbit-forbidden-interval.md`): the relation $f(f(t))=2f(t)-t$ makes forward iterates arithmetic progressions and positivity forces $f(t)\ge t$. If the increment $f(t)-t$ took two values $c>d$, then the $c$-orbit eventually falls inside an interval where the left-hand mean inequality with a $d$-increment point is impossible.

## Current best
The complete set of solutions is
\[
\boxed{f(x)=x+c\quad(x>0)}
\]
for an arbitrary constant $c\ge0$. The proof is complete below: setting $M=f(x)+y$, $N=x+f(y)$ rewrites the hypothesis as $|M^2-N^2|\le (x-f(y))^2$; taking $x=f(y)$ gives $f(f(y))=2f(y)-y$, whose iterates are arithmetic and positivity gives $p(x):=f(x)-x\ge0$. A descent argument shows that if $p(x)=c>0$, then the orbit of $x$ under $f$ starts at some $r\in(0,c]$ and is $r+nc$. If $p$ took two values $c>d$, the left-hand inequality would fail on a forbidden interval whose length can be made larger than the spacing $c$ of the $c$-orbit, forcing a point of that orbit into the forbidden interval. Hence $p$ is constant.

## Full proof
We will prove that the solutions are exactly
\[
f(x)=x+c\qquad(x>0)
\]
for constants $c\ge0$.

For fixed $x,y>0$, put
\[
v=f(y),\qquad M=f(x)+y,\qquad N=x+v=x+f(y).
\]
Since all quantities are positive, the right-hand given inequality is equivalent to
\[
M^2\ge 4xv.
\]
But
\[
4xv=(x+v)^2-(x-v)^2=N^2-(x-f(y))^2.
\]
Similarly, the left-hand given inequality is equivalent to
\[
M^2\le 2(x^2+v^2)=(x+v)^2+(x-v)^2=N^2+(x-f(y))^2.
\]
Thus the whole hypothesis is equivalent to
\[
\boxed{\big|(f(x)+y)^2-(x+f(y))^2\big|\le (x-f(y))^2}\tag{1}
\]
for all $x,y>0$. This is the key mean estimate recorded in `lemmas/key-mean-estimate.md`.

Now substitute $x=f(y)$ in (1). The right side is $0$, so
\[
(f(f(y))+y)^2=(2f(y))^2.
\]
Both sides are positive, hence
\[
\boxed{f(f(y))=2f(y)-y}\tag{2}
\]
for every $y>0$.

Let $f^{[0]}(t)=t$ and $f^{[n+1]}(t)=f(f^{[n]}(t))$. Fix $t$ and write
\[
p(t)=f(t)-t.
\]
Applying (2) repeatedly gives, with $a_n=f^{[n]}(t)$,
\[
a_{n+2}=f(f(a_n))=2f(a_n)-a_n=2a_{n+1}-a_n.
\]
Since $a_0=t$ and $a_1=t+p(t)$, induction yields
\[
\boxed{f^{[n]}(t)=t+n p(t)}\qquad(n\ge0).\tag{3}
\]
Every $f^{[n]}(t)$ is positive. If $p(t)<0$, then $t+n p(t)<0$ for all sufficiently large $n$, contradicting (3). Therefore
\[
\boxed{p(t)=f(t)-t\ge0}\qquad(t>0).\tag{4}
\]
Also (3) shows that $p$ is constant on each forward orbit of $f$; this is `lemmas/iterate-positivity.md`.

We next need a descent statement. Suppose $p(t)=c$ and $t>c>0$. Put $z=t-c>0$ and write $e=p(z)\ge0$. Then
\[
f(t)=t+c,\qquad f(z)=z+e=t-c+e.
\]
Apply (1) to the pair $(t,z)$. We have
\[
f(t)+z=(t+c)+(t-c)=2t,
\]
and
\[
t+f(z)=t+(t-c+e)=2t-c+e,
\]
while
\[
t-f(z)=t-(t-c+e)=c-e.
\]
Hence (1) gives
\[
|c-e|\,(4t-c+e)\le (c-e)^2.\tag{5}
\]
If $c\ne e$, dividing (5) by $|c-e|$ gives
\[
4t-c+e\le |c-e|.
\]
But $t>c$, so
\[
4t-c+e>3c+e>|c-e|,
\]
where the last inequality is immediate both when $e\ge c$ and when $e<c$. This contradiction proves $e=c$. Consequently
\[
f(z)=z+c=t.
\]
So, whenever $p(t)=c$ and $t>c$, the point $t-c$ is still positive, has the same increment $c$, and maps to $t$; this is `lemmas/descent.md`.

It follows that for any $t$ with $p(t)=c>0$, repeatedly subtracting $c$ while the current point remains $>c$ is legitimate and preserves the increment $c$. After finitely many subtractions we reach a number
\[
r\in(0,c]
\]
with $p(r)=c$. Therefore, by (3),
\[
\boxed{f^{[n]}(r)=r+nc\quad(n\ge0),\qquad p(r+nc)=c.}\tag{6}
\]

We now prove that $p$ is constant on all of $\mathbb R_{>0}$; this is the constancy argument in `lemmas/constancy.md`. Suppose not. Then there exist points whose increments are
\[
c>d\ge0.
\]
By the previous paragraph, choose $r\in(0,c]$ with $p(r)=c$, and define
\[
x_n=r+nc\qquad(n\ge0),
\]
so that $f(x_n)=x_n+c$ by (6).

Choose a point $y$ with $p(y)=d$. If $d>0$, replace $y$ by a suitable forward iterate $f^{[m]}(y)=y+md$; by (3) this keeps $p(y)=d$ and makes $y$ arbitrarily large. Hence in all cases we may assume that
\[
\boxed{2s>c,\qquad\text{where } s:=\sqrt{2(c-d)(c+d+2y)}.}\tag{7}
\]
Indeed, if $d>0$ this is achieved by taking the above iterate large enough; if $d=0$, then already
\[
s^2=2c(c+2y)>2c^2,
\]
so $s>\sqrt2\,c$ and certainly $2s>c$.

For this fixed $y$, we have $f(y)=y+d$. Apply the left-hand part of the original inequality with $x=x_n$:
\[
\sqrt{\frac{x_n^2+(y+d)^2}{2}}\ge \frac{f(x_n)+y}{2}
=\frac{x_n+c+y}{2}.
\]
Squaring gives
\[
2(x_n^2+(y+d)^2)\ge (x_n+c+y)^2.\tag{8}
\]
Consider the quadratic
\[
Q(X)=2(X^2+(y+d)^2)-(X+c+y)^2.
\]
With $A=c+y$, a direct expansion gives
\[
Q(X)=(X-A)^2-s^2,
\]
because
\[
s^2=2\big((c+y)^2-(y+d)^2\big)=2(c-d)(c+d+2y).
\]
Thus (8) says exactly that $x_n$ must not lie in the open interval
\[
I=(A-s,A+s).
\]
But $A+s=c+y+s>c\ge r=x_0$, so $x_0<A+s$. If $x_0>A-s$, then already $x_0\in I$, contradicting (8) for $n=0$. Otherwise $x_0\le A-s$. Since $x_n\to\infty$ and the step of the sequence $(x_n)$ is $c<2s$ by (7), the sequence cannot jump over the interval $I$: if $n$ is the first index with $x_n>A-s$, then $n\ge1$, $x_{n-1}\le A-s$, and
\[
x_n=x_{n-1}+c\le A-s+c<A-s+2s=A+s.
\]
Hence $x_n\in I$, again contradicting (8). Therefore the assumed two increments $c>d$ cannot occur.

So $p(t)$ is a constant $c\ge0$, i.e.
\[
f(t)=t+c\qquad(t>0).
\]

It remains to verify that every such function works. Let $c\ge0$ and $f(t)=t+c$. For $x,y>0$, set
\[
a=x,\qquad b=f(y)=y+c.
\]
Then
\[
f(x)+y=x+c+y=a+b.
\]
Consequently the required inequalities become
\[
\sqrt{\frac{a^2+b^2}{2}}\ge \frac{a+b}{2}\ge \sqrt{ab}.
\]
The right inequality is $(a+b)^2\ge4ab$, and the left inequality is $2(a^2+b^2)\ge(a+b)^2$; both follow from $(a-b)^2\ge0$. Hence all functions $f(x)=x+c$ with $c\ge0$ satisfy the condition, and no other functions do.

Therefore the answer is
\[
\boxed{f(x)=x+c\ (x>0)\text{ for some constant }c\ge0.}
\]
