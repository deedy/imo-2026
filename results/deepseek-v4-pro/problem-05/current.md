# imo-2026-05 — tracking file

## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that

\[
\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}
\]

for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
1. Numerical brute-force — only $f(x)=x+c$ ($c\ge 0$) survives.
2. Substituting $x=f(y)$ forces the functional equation $f(f(x))=2f(x)-x$.
3. Reformulating with $g(x)=f(x)-x$ yields two algebraic identities for the squared‑inequality remainders $A,B$.
4. From $|A-B|\le A+B$ we obtain a universal inequality (7).
5. The functional equation implies forward orbits are arithmetic progressions with common difference $g(x)$.  If $g(x)<0$ the orbit leaves $\mathbb{R}_{>0}$ – contradiction.  Hence $g\ge 0$.
6. Using arithmetic progressions together with (7) shows that $g$ attains at most one positive value.
7. A backward‑induction lemma gives a point $u\in(0,c]$ with $g(u)=c$ (if $c>0$ is a value).
8. A covering argument (intervals around the forward orbit) forces the zero‑set $S_0=\emptyset$, hence $g$ is constant $c$.
9. Verification that $f(x)=x+c$ works for any $c\ge 0$.

## Current best
**Answer:** $f(x) = x + c$ for a constant $c \ge 0$.

## Full proof

Let $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ satisfy

\[
\sqrt{\frac{x^2 + f(y)^2}{2}} \ge \frac{f(x) + y}{2} \ge \sqrt{x f(y)} \qquad \forall x,y>0. \tag{1}
\]

All quantities are positive, so squaring preserves the inequalities:

\[
2x^2 + 2f(y)^2 \ge (f(x)+y)^2 \ge 4x f(y) \qquad \forall x,y>0. \tag{2}
\]

---

### 1.  A functional equation

Put $x = f(y)$ (which is $>0$) in (2).  The leftmost term becomes $2f(y)^2+2f(y)^2 = 4f(y)^2$ and the rightmost becomes $4f(y)f(y) = 4f(y)^2$.  Hence the chain collapses to equality:

\[
\bigl(f(f(y)) + y\bigr)^2 = 4f(y)^2 .
\]

Taking square roots (all terms are positive) yields  

\[
f(f(y)) + y = 2f(y) \qquad\Longrightarrow\qquad 
\boxed{f(f(x)) = 2f(x) - x \qquad \forall x>0.} \tag{3}
\]

Define  

\[
g(x) = f(x) - x \qquad (x>0).
\]

Then $g(x) > -x$ and (3) rewrites as  

\[
x+g(x) + g(x+g(x)) = 2x+2g(x) - x \;\Longrightarrow\;
\boxed{g(x+g(x)) = g(x) \qquad \forall x>0.} \tag{4}
\]

---

### 2.  Positivity of $g$

**Lemma 0.** $g(x) \ge 0$ for all $x>0$.

*Proof.* Fix $x>0$ and define the forward orbit $x_0 = x$, $x_{n+1} = f(x_n)$ for $n\ge 0$.  Using (3),

\[
x_{n+2} = f(x_{n+1}) = 2f(x_n) - x_n = 2x_{n+1} - x_n .
\]

The recurrence $x_{n+2} - 2x_{n+1} + x_n = 0$ has the unique solution $x_n = A + Bn$ with $A,B$ determined by the initial conditions: $x_0 = x$, $x_1 = f(x) = x + g(x)$.  Hence $A = x$, $B = g(x)$, and

\[
x_n = x + n g(x) \qquad (n\ge 0).
\]

From (4) we have $g(x_n) = g(x)$ for all $n\ge 0$.  Now, if $g(x) < 0$, then $x_n$ becomes non‑positive for sufficiently large $n$, contradicting that every $x_n$ is in the domain $\mathbb{R}_{>0}$ (because $f: \mathbb{R}_{>0}\to\mathbb{R}_{>0}$).  Therefore $g(x) \ge 0$. ∎

Thus $g$ takes only non‑negative values.

---

### 3.  Algebraic reformulation

Write $a = g(x)$, $b = g(y)$; then $f(x)=x+a$, $f(y)=y+b$.  The two inequalities in (2) are  

\[
\begin{aligned}
A(x,y) &:= 2x^2 + 2(y+b)^2 - (x+y+a)^2 \ge 0,\\
B(x,y) &:= (x+y+a)^2 - 4x(y+b) \ge 0 .
\end{aligned}
\]

Expanding:

\[
\begin{aligned}
A(x,y) &= (x-y)^2 - a^2 - 2a(x+y) + 4by + 2b^2,\\
B(x,y) &= (x-y)^2 + a^2 + 2a(x+y) - 4bx .
\end{aligned}
\]

Adding and subtracting gives two fundamental identities  

\[
\begin{aligned}
A(x,y) + B(x,y) &= 2\bigl(x - y - b\bigr)^2 = 2\bigl(x - f(y)\bigr)^2, \tag{5}\\
A(x,y) - B(x,y) &= -2(a-b)(a+b+2x+2y). \tag{6}
\end{aligned}
\]

Because $A,B \ge 0$, we have $|A-B| \le A+B$ (the absolute difference of two non‑negative numbers never exceeds their sum).  Substituting (5) and (6) and cancelling a factor $2$ yields  

\[
\boxed{|g(x)-g(y)|\,\bigl(g(x)+g(y)+2x+2y\bigr) \le \bigl(x - y - g(y)\bigr)^2 \qquad \forall x,y>0.} \tag{7}
\]

Swapping $x$ and $y$ gives the symmetric inequality  

\[
|g(x)-g(y)|\,\bigl(g(x)+g(y)+2x+2y\bigr) \le \bigl(y - x - g(x)\bigr)^2 \qquad \forall x,y>0. \tag{8}
\]

---

### 4.  At most one positive value of $g$

Let $V = \{g(x) : x>0\}$.  Suppose $V$ contains two distinct positive numbers $c_1 > c_2 > 0$.  Choose $u,v>0$ with $g(u)=c_1$, $g(v)=c_2$.  From the functional equation (4) we obtain  

\[
g(u + n c_1) = c_1,\qquad g(v + m c_2) = c_2 \qquad \forall\, n,m\in\mathbb{N}_0 .
\]

Insert $x = u + n c_1$, $y = v + m c_2$ into (7).  With $a=c_1$, $b=c_2$,

\[
(c_1-c_2)\bigl(c_1+c_2 + 2u + 2v + 2n c_1 + 2m c_2\bigr) 
\le \bigl(u - v - c_2 + n c_1 - m c_2\bigr)^2 . \tag{9}
\]

We show that for suitably chosen $n,m\to\infty$ the inequality fails.

*Rational ratio.*  If $c_1/c_2 \in \mathbb{Q}$, write $c_1/c_2 = p/q$ with $p,q\in\mathbb{N}$ coprime.  Then $p c_2 = q c_1$.  Take $n = q t$, $m = p t$ for $t\in\mathbb{N}$.  Then $n c_1 - m c_2 = 0$, so the right‑hand side of (9) is the constant $(u-v-c_2)^2$, while the left‑hand side grows linearly with $t$ (coefficient $2(c_1-c_2)(q c_1 + p c_2) > 0$).  For large $t$ the inequality is violated – contradiction.

*Irrational ratio.*  If $c_1/c_2 \notin \mathbb{Q}$, the fractional parts $\{n(c_1/c_2)\}$ are dense in $[0,1]$ (a classical fact: for irrational $\alpha$, the sequence $n\alpha \bmod 1$ is dense).  Consequently the set $\{n c_1 - m c_2 : n,m\in\mathbb{N}_0\}$ is dense in $\mathbb{R}$.  Hence we can choose sequences $(n_k,m_k)\to(\infty,\infty)$ with $n_k c_1 - m_k c_2 \to -(u - v - c_2)$.  Then the right‑hand side of (9) tends to $0$ while the left‑hand side tends to $+\infty$, again a contradiction.

Thus $V$ contains **at most one** positive number.  Because $g\ge 0$, the only possible values are $0$ and at most one $c>0$.  Consequently, either  

* (i) $g\equiv 0$ (constant), which gives $f(x)=x$, a solution; or  
* (ii) there is $c>0$ such that $V \subseteq \{0, c\}$ with both values attainable.

We now exclude case (ii).  Assume $c>0$ and both $0$ and $c$ occur.  Set  

\[
S_0 = \{x>0 : g(x)=0\},\qquad S_c = \{x>0 : g(x)=c\},
\]

both non‑empty.  (Because $V\subseteq\{0,c\}$, every $x>0$ belongs to $S_0\cup S_c$.)

---

### 5.  Inequalities between the two level sets

Take $x\in S_0$, $y\in S_c$ ($a=0$, $b=c$).  The formulas for $A$ and $B$ become  

\[
\begin{aligned}
A(x,y) &= (x-y)^2 + 4cx + 2c^2 \ge 0 \quad\text{(always true)},\\
B(x,y) &= (x-y)^2 - 4cx \ge 0 \;\Longrightarrow\; (x-y)^2 \ge 4cx , \tag{10}\\
A(y,x) &= (x-y)^2 - c^2 - 2c(x+y) \ge 0 \;\Longrightarrow\; (x-y)^2 \ge c^2 + 2c(x+y). \tag{11}
\end{aligned}
\]

From (11) and $x,y>0$ we obtain $(x-y)^2 > c^2$, hence  

\[
|x-y| > c \qquad \forall\,x\in S_0,\;y\in S_c . \tag{12}
\]

---

### 6.  Existence of a small element in $S_c$

**Lemma 1.** There exists $u \in (0, c]$ with $g(u) = c$.

*Proof.* Pick any $y_0 \in S_c$.  If $y_0 \le c$ we are done.  Suppose $y_0 > c$ and set $z = y_0 - c > 0$.  Apply inequality (7) with $x = y_0$, $y = z$.  We have $a = g(y_0)=c$, and $b = g(z)$ belongs to $\{0,c\}$ (all values are in $V\subseteq\{0,c\}$).

Compute:
\[
\begin{aligned}
\text{LHS} &= |c-b|\bigl(c + b + 2y_0 + 2z\bigr)
            = |c-b|\bigl(c + b + 2y_0 + 2(y_0-c)\bigr)
            = |c-b|\bigl(b - c + 4y_0\bigr),\\
\text{RHS} &= \bigl(y_0 - z - b\bigr)^2 = \bigl(y_0 - (y_0-c) - b\bigr)^2 = (c - b)^2 .
\end{aligned}
\]

Let $d = b - c$.  Then $\text{LHS}=|d|(d+4y_0)$, $\text{RHS}=d^2$.

* If $d > 0$: $d(d+4y_0)\le d^2 \;\Longrightarrow\; 4y_0 d \le 0$, impossible.
* If $d = 0$: inequality holds as $0\le 0$.
* If $d < 0$: $|d|=-d$, giving $(-d)(d+4y_0)\le d^2 \;\Longrightarrow\; -d^2 -4y_0 d \le d^2 \;\Longrightarrow\; -4y_0 d \le 2d^2$.  Since $d<0$, divide by $-2d>0$: $2y_0 \le -d = |d|$.

Thus $|d| \ge 2y_0$.  But $b=g(z)\in\{0,c\}$, so $|d|=|b-c|$ is either $0$ (if $b=c$) or $c$ (if $b=0$).  

If $b=0$, then $|d|=c$, giving $c \ge 2y_0$, i.e. $y_0 \le c/2$, contradicting $y_0 > c$.  Therefore $b \neq 0$, so $b = c$; hence $g(z)=c$.

Thus $z = y_0 - c \in S_c$.  If $z > c$, repeat the argument with $y_0$ replaced by $z$.  After $\lfloor y_0/c\rfloor$ steps we reach an element $u \in (0, c]$ belonging to $S_c$. ∎

---

### 7.  The forward orbit and a covering argument

From Lemma 1 we have $u \in (0, c]$ with $g(u) = c$.  By (4),

\[
g(u + n c) = c \qquad \forall\, n \in \mathbb{N}_0 .
\]

Thus the arithmetic progression  

\[
P = \{u + n c : n \ge 0\} \subseteq S_c .
\]

Consider the closed intervals  

\[
I_n = [\,u + n c - c,\; u + n c + c\,] \qquad (n \ge 0).
\]

Their union covers all positive real numbers.  Indeed,
* $I_0 = [u-c,\; u+c]$; because $0 < u \le c$, the left endpoint is $\le 0$, so $I_0$ contains $(0,\; u+c]$.
* $I_1 = [u,\; u+2c]$, $I_2 = [u+c,\; u+3c]$, …
Since $I_n$ and $I_{n+1}$ overlap (their intersection is $[u+nc,\; u+(n+1)c]$), we have  

\[
\bigcup_{n\ge 0} I_n = (0,\infty).
\]

Now take any $x > 0$.  There exists $n \ge 0$ such that $x \in I_n$, i.e.  

\[
|x - (u + n c)| \le c .
\]

If $x \in S_0$, then by (12) we must have $|x - (u + n c)| > c$ (because $u+nc \in S_c$).  This is impossible.  Hence $S_0 = \emptyset$.

---

### 8.  Conclusion

Since $S_0 = \emptyset$, the function $g$ never takes the value $0$.  Together with §4 this forces $g(x) \equiv c$ for the positive constant $c$.  Thus  

\[
f(x) = x + c \qquad (c > 0).
\]

The earlier case $g\equiv 0$ gives $f(x)=x$, which corresponds to $c=0$.  Both are covered by the single formula  

\[
\boxed{f(x) = x + c \quad\text{for some constant } c \ge 0.}
\]

**Verification.**  For $f(x)=x+c$ ($c\ge 0$) the original inequalities become  

\[
\sqrt{\frac{x^2 + (y+c)^2}{2}} \ge \frac{x+y+c}{2} \ge \sqrt{x(y+c)} ,
\]

which are exactly the Quadratic‑Mean–Arithmetic‑Mean inequality and the Arithmetic‑Mean–Geometric‑Mean inequality applied to the two positive numbers $x$ and $y+c$.  Both inequalities are true for all $x,y>0$.

Therefore the set of all solutions is $\{x \mapsto x + c \mid c \ge 0\}$.
