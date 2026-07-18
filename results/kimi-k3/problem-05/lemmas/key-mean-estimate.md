# Lemma: key mean estimate

## Statement
For a function $f:\mathbb R_{>0}\to\mathbb R_{>0}$, the two inequalities
\[
\sqrt{\frac{x^2+f(y)^2}{2}}\ge \frac{f(x)+y}{2}\ge \sqrt{x f(y)}
\]
are equivalent to
\[
\big|(f(x)+y)^2-(x+f(y))^2\big|\le (x-f(y))^2. \tag{1}
\]
Moreover, (1) implies
\[
f(f(t))=2f(t)-t\qquad(t>0). \tag{2}
\]

## Proof
Let $v=f(y)$, $M=f(x)+y$, and $N=x+v$. All are positive. The right-hand inequality is $M/2\ge\sqrt{xv}$, equivalently
\[
M^2\ge4xv=(x+v)^2-(x-v)^2=N^2-(x-f(y))^2.
\]
The left-hand inequality is, after squaring,
\[
M^2\le2(x^2+v^2)=(x+v)^2+(x-v)^2=N^2+(x-f(y))^2.
\]
Together these two displays are exactly (1).

Now put $x=f(t)$ and $y=t$ in (1). The right side becomes $(f(t)-f(t))^2=0$. Hence
\[
(f(f(t))+t)^2=(2f(t))^2.
\]
Since both quantities inside the squares are positive, $f(f(t))+t=2f(t)$, which is (2).
