# Lemma: the increment $f(t)-t$ is constant

## Statement
Let $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfy the original two mean inequalities. Then $p(t)=f(t)-t$ is constant on $\mathbb R_{>0}$.

## Proof
By the key mean estimate, the iterate lemma, and the descent lemma, we know: $p(t)\ge0$; forward iterates satisfy $f^{[n]}(t)=t+n p(t)$; and if $p(t)=c>0$, then after descending if necessary there is $r\in(0,c]$ with $p(r)=c$, so the points
\[
x_n=r+nc\qquad(n\ge0)
\]
all satisfy $f(x_n)=x_n+c$.

Suppose $p$ is not constant. Then it takes two values $c>d\ge0$. Choose $r$ and $(x_n)$ as above for the larger value $c$. Choose $y$ with $p(y)=d$. If $d>0$, replace $y$ by a sufficiently large forward iterate $f^{[m]}(y)=y+md$, which still has increment $d$; hence we may assume that
\[
2s>c,\qquad s:=\sqrt{2(c-d)(c+d+2y)}. \tag{1}
\]
If $d=0$, no replacement is needed: $s^2=2c(c+2y)>2c^2$, so $2s>c$ already.

For this fixed $y$, we have $f(y)=y+d$. The left original inequality with $x=x_n$ gives, after squaring,
\[
2(x_n^2+(y+d)^2)\ge (x_n+c+y)^2. \tag{2}
\]
Define
\[
Q(X)=2(X^2+(y+d)^2)-(X+c+y)^2.
\]
With $A=c+y$, direct expansion gives
\[
Q(X)=(X-A)^2-s^2,
\]
since
\[
s^2=2((c+y)^2-(y+d)^2)=2(c-d)(c+d+2y).
\]
Therefore (2) says that no $x_n$ may lie in the open interval
\[
I=(A-s,A+s).
\]
But $A+s=c+y+s>c\ge r=x_0$. If $x_0>A-s$, then $x_0\in I$, contradicting (2). If $x_0\le A-s$, then because $x_n\to\infty$ with step $c<2s$ by (1), the sequence $(x_n)$ cannot jump over $I$: for the first $n$ with $x_n>A-s$, we have $n\ge1$, $x_{n-1}\le A-s$, and hence
\[
x_n=x_{n-1}+c\le A-s+c<A-s+2s=A+s,
\]
so $x_n\in I$, again contradicting (2). Thus the assumption that $p$ takes two different values is impossible, so $p$ is constant.
