# Lemma: f(f(y)) = 2 f(y) − y, and f(y) ≥ y

**Setting.** $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ satisfies, for all $x,y>0$:
(1) $2x^2+2f(y)^2\ge (f(x)+y)^2$ and (2) $(f(x)+y)^2\ge 4xf(y)$.

**Statement.**
(a) $f(f(y)) = 2f(y)-y$ for all $y>0$.
(b) $f(y)\ge y$ for all $y>0$; moreover with $g(y)=f(y)-y$ one has
$f\bigl(y+n\,g(y)\bigr)=y+(n+1)g(y)$ for all integers $n\ge 0$.

**Proof.**
(a) Put $x=f(y)$ in (1): $4f(y)^2\ge (f(f(y))+y)^2$; both sides of the underlying
quantities are positive, so $2f(y)\ge f(f(y))+y$. Put $x=f(y)$ in (2):
$(f(f(y))+y)^2\ge 4f(y)^2$, so $f(f(y))+y\ge 2f(y)$. Combine.

(b) Fix $y>0$, set $y_0=y$, $y_{n+1}=f(y_n)>0$. By (a) applied at $y_n$:
$y_{n+2}=2y_{n+1}-y_n$, so $y_n=y+n(f(y)-y)$ for all $n\ge0$ (arithmetic progression).
If $f(y)<y$, then $y_n<0$ for large $n$, contradicting $y_n>0$. Hence $f(y)\ge y$.
The displayed orbit formula is just $f(y_n)=y_{n+1}$. $\blacksquare$
