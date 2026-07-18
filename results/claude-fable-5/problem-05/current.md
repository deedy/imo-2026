# imo-2026-05 — tracking file

## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that
$$\sqrt{\frac{x^2 + f(y)^2}{2}}\ \ge\ \frac{f(x) + y}{2}\ \ge\ \sqrt{xf(y)}$$
for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- **Squared reformulation + substitution $x=f(y)$** (successful): squaring both inequalities gives $2x^2+2f(y)^2 \ge (f(x)+y)^2 \ge 4xf(y)$. Plugging $x=f(y)$ makes the two bounds collide and forces the exact identity $f(f(y)) = 2f(y)-y$. Orbits of $f$ are then arithmetic progressions; positivity forces $f(y)\ge y$.
- **Testing candidates**: $f(x)=kx$ works only for $k=1$; but $f(x)=x+c$ works for every constant $c\ge 0$ (QM–AM–GM applied to the pair $x$, $y+c$). Numerically verified in `code/verify.py`; random perturbations of $x+c$ violate one of the two inequalities.
- **Orbit rigidity / asymptotic sandwich** (successful): a point $a$ with gap $d=f(a)-a>0$ generates the orbit $a+nd$ on which $f(t)=t+d$. Using orbit points as $y$ in both squared inequalities and choosing the orbit point nearest to $x$ gives the two-sided bound $d-\frac{d^2}{4x}\le f(x)-x\le d+\frac{d^2}{16x-4d}$ for $x\ge a+d$. Hence all positive gaps are equal and all large enough $x$ have gap exactly $d$.
- **Downward bootstrap** (successful): if $f(t)=t+d$ for all $t\ge T$, then taking $x=y+d$ in both squared inequalities pins $f(y)=y+d$ for all $y\ge T-d$; induction covers all of $\mathbb{R}_{>0}$.

## Current best
**Answer: the solutions are exactly the functions $f(x) = x + c$ for a constant $c \ge 0$.** Complete proof below: sufficiency is QM–AM–GM applied to the numbers $x$ and $y+c$; necessity follows from the forced identity $f(f(y))=2f(y)-y$ (equality at $x=f(y)$), which makes orbits arithmetic progressions, whence $f(y)\ge y$, then an asymptotic sandwich shows the gap $g=f-\mathrm{id}$ is a constant $d$ on $[a+d,\infty)$ for any $a$ with $g(a)=d>0$, and a downward bootstrap propagates $f=\mathrm{id}+d$ to all of $\mathbb{R}_{>0}$; if $g\equiv 0$ then $f=\mathrm{id}$ (the case $c=0$).

## Full proof

**Answer.** The functions satisfying the condition are exactly
$$f(x) = x + c \qquad (x>0),$$
where $c \ge 0$ is an arbitrary nonnegative real constant.

Throughout, since all quantities appearing under square roots and on both sides are positive, the given condition is equivalent to the pair of squared inequalities
$$\textbf{(1)}\quad 2x^2 + 2f(y)^2 \ \ge\ \bigl(f(x)+y\bigr)^2, \qquad\qquad
\textbf{(2)}\quad \bigl(f(x)+y\bigr)^2 \ \ge\ 4x\,f(y),$$
required for all $x,y>0$.

---

### Part I: every $f(x)=x+c$ with $c\ge 0$ is a solution

Fix $c\ge 0$ and let $f(x)=x+c$; note $f$ maps $\mathbb{R}_{>0}$ to $\mathbb{R}_{>0}$. For $x,y>0$ put $u=x>0$ and $v=y+c>0$. Then
$$\frac{x^2+f(y)^2}{2}=\frac{u^2+v^2}{2},\qquad \frac{f(x)+y}{2}=\frac{x+c+y}{2}=\frac{u+v}{2},\qquad xf(y)=uv,$$
so the required chain is exactly the QM–AM–GM inequality for the two positive numbers $u,v$:
$$\sqrt{\tfrac{u^2+v^2}{2}}\ \ge\ \tfrac{u+v}{2}\ \ge\ \sqrt{uv},$$
which holds because $2(u^2+v^2)-(u+v)^2=(u-v)^2\ge0$ and $(u+v)^2-4uv=(u-v)^2\ge0$. $\blacksquare$

---

### Part II: every solution is of this form

Let $f$ satisfy (1) and (2) for all $x,y>0$.

#### Step 1: $f(f(y)) = 2f(y) - y$ for all $y>0$.

Substitute $x = f(y)$ (a legitimate positive value) into (1):
$$2f(y)^2 + 2f(y)^2 \ \ge\ \bigl(f(f(y)) + y\bigr)^2 \ \Longrightarrow\ 2f(y) \ \ge\ f(f(y)) + y ,$$
using that both sides are positive. Substitute $x = f(y)$ into (2):
$$\bigl(f(f(y)) + y\bigr)^2 \ \ge\ 4f(y)\cdot f(y) \ \Longrightarrow\ f(f(y)) + y \ \ge\ 2f(y).$$
Combining, $f(f(y)) + y = 2f(y)$, i.e.
$$\textbf{(3)}\qquad f(f(y)) = 2f(y) - y \qquad\text{for all } y>0.$$

#### Step 2: $f(y)\ge y$; orbits are arithmetic progressions.

Fix $y>0$ and define $y_0=y$, $y_{n+1}=f(y_n)$ ($n\ge0$); all $y_n>0$. Applying (3) at the point $y_n$ gives $y_{n+2} = 2y_{n+1}-y_n$, so $(y_n)$ is an arithmetic progression:
$$y_n = y + n\,g(y), \qquad\text{where } g(y):=f(y)-y .$$
If $g(y)<0$ then $y_n<0$ for large $n$, contradicting $y_n>0$. Hence
$$\textbf{(4)}\qquad f(y)\ \ge\ y \quad\text{for all } y>0,$$
and moreover, since $y_{n+1}=f(y_n)$,
$$\textbf{(5)}\qquad f\bigl(y + n\,g(y)\bigr) = y + (n+1)\,g(y)\qquad (n=0,1,2,\dots).$$

#### Two elementary square-root estimates.

**(E1)** For all real $u$ with $-1\le u\le 3$: $\;\sqrt{1+u} \ \ge\ 1 + \tfrac{u}{2} - \tfrac{u^2}{2}$.

*Proof.* If the right side is negative, this is trivial. Otherwise both sides are nonnegative and squaring is equivalent; expanding,
$$(1+u) - \Bigl(1+\tfrac{u}{2}-\tfrac{u^2}{2}\Bigr)^2 = \tfrac34 u^2 + \tfrac12 u^3 - \tfrac14 u^4 = -\tfrac{u^2}{4}(u-3)(u+1)\ \ge\ 0$$
for $-1\le u\le 3$. $\square$

**(E2)** For $A>0$, $B\ge 0$: $\;\sqrt{A^2+B}\ \le\ A + \tfrac{B}{2A}$.

*Proof.* $\bigl(A+\tfrac{B}{2A}\bigr)^2 = A^2 + B + \tfrac{B^2}{4A^2} \ge A^2+B$, and both sides are positive. $\square$

#### Step 3: a point with gap $d>0$ pins down all gaps at large arguments.

Suppose $g(a) = d > 0$ for some $a>0$. By (5),
$$f(a+nd) = a+(n+1)d \qquad (n\ge 0). \tag{6}$$

**Claim.** For every $x \ge a+d$,
$$d - \frac{d^2}{4x}\ \le\ g(x)\ \le\ d + \frac{d^2}{16x - 4d}. \tag{7}$$

*Proof.* The set $\{a+(n+1)d : n\ge 0\} = \{a+d,\,a+2d,\,\dots\}$ is an arithmetic progression with step $d$ whose least element is $a+d\le x$. Let $m=\lfloor (x-a)/d\rfloor$; then $m\ge 1$ and $a+md\le x< a+(m+1)d$, and $x$ lies within $d/2$ of one of the two endpoints $a+md,\ a+(m+1)d$, both of which belong to the set. Hence there is an index $n\ge0$ with
$$\bigl|\,a+(n+1)d - x\,\bigr| \ \le\ \frac d2 .$$
Write $y := a+nd$ and $\varepsilon := (y+d) - x$, so $f(y) = y+d = x+\varepsilon$ by (6) and $|\varepsilon|\le d/2$. Note $x \ge a+d > d$, hence $|\varepsilon|/x < \tfrac12$.

*Lower bound.* By (2), $\bigl(f(x)+y\bigr)^2 \ge 4x f(y) = 4x(x+\varepsilon)$; since $f(x)+y>0$,
$$f(x)\ \ge\ 2\sqrt{x(x+\varepsilon)} - y \ =\ 2x\sqrt{1+\tfrac{\varepsilon}{x}} - (x+\varepsilon-d).$$
By (E1) with $u=\varepsilon/x\in(-\tfrac12,\tfrac12)$,
$$2x\sqrt{1+\tfrac{\varepsilon}{x}} \ \ge\ 2x\Bigl(1+\tfrac{\varepsilon}{2x}-\tfrac{\varepsilon^2}{2x^2}\Bigr) = 2x + \varepsilon - \tfrac{\varepsilon^2}{x},$$
so
$$f(x) \ \ge\ 2x+\varepsilon-\tfrac{\varepsilon^2}{x} - x - \varepsilon + d \ =\ x + d - \frac{\varepsilon^2}{x}\ \ge\ x + d - \frac{d^2}{4x},$$
using $\varepsilon^2\le d^2/4$. This is the left inequality of (7).

*Upper bound.* By (1), $\bigl(f(x)+y\bigr)^2 \le 2x^2 + 2f(y)^2 = 2x^2 + 2(x+\varepsilon)^2$. A direct expansion gives the identity
$$2x^2 + 2(x+\varepsilon)^2 = (2x+\varepsilon)^2 + \varepsilon^2 .$$
Since $2x+\varepsilon \ge 2x - \tfrac d2 > 0$, (E2) with $A = 2x+\varepsilon$, $B=\varepsilon^2$ yields
$$f(x) \ \le\ \sqrt{(2x+\varepsilon)^2+\varepsilon^2} - y \ \le\ 2x+\varepsilon + \frac{\varepsilon^2}{2(2x+\varepsilon)} - (x+\varepsilon-d) \ =\ x + d + \frac{\varepsilon^2}{2(2x+\varepsilon)} .$$
Finally $\varepsilon^2\le d^2/4$ and $2(2x+\varepsilon)\ge 2(2x-\tfrac d2)=4x-d>0$, so
$$f(x)\ \le\ x+d+\frac{d^2/4}{4x-d}\ =\ x + d + \frac{d^2}{16x-4d},$$
the right inequality of (7). $\square$

#### Step 4: all positive gaps are equal.

Suppose $g(a)=d>0$ and $g(a')=d'>0$. For every $x\ge\max(a+d,\,a'+d')$, (7) applied to both points gives
$$d - \frac{d^2}{4x} \ \le\ g(x) \ \le\ d' + \frac{d'^2}{16x-4d'} ,$$
so that $d-d'\le \frac{d^2}{4x}+\frac{d'^2}{16x-4d'}$ for all such $x$. The right-hand side tends to $0$ as $x\to\infty$, whence $d\le d'$; by symmetry $d'\le d$. Hence $d=d'$:
$$\textbf{(8)}\qquad \text{all positive values of } g \text{ are equal.}$$

#### Step 5: if some gap is positive, then $g\equiv d$ on a half-line.

Assume $g(a)=d>0$. For every $x\ge a+d$ we have $x> d > \tfrac d4$, so the lower bound in (7) gives
$$g(x)\ \ge\ d - \frac{d^2}{4x}\ >\ 0 .$$
By (8), a positive gap must equal $d$; hence
$$f(x) = x + d \qquad\text{for all } x \ge T:=a+d. \tag{9}$$

#### Step 6: downward bootstrap — $f(x)=x+d$ on all of $\mathbb{R}_{>0}$.

**Claim.** If $f(t)=t+d$ for all $t\ge T$ (some $T>0$, $d>0$), then $f(y)=y+d$ for every $y>0$ with $y\ge T-d$.

*Proof.* Let $y>0$ with $y+d\ge T$, and put $x:=y+d\ \ge T$, so $f(x)=x+d=y+2d$.
- Inequality (1) with this pair: $2(y+d)^2 + 2f(y)^2 \ \ge\ (y+2d+y)^2 = 4(y+d)^2$, hence $f(y)^2\ge (y+d)^2$, i.e. $f(y)\ge y+d$.
- Inequality (2) with this pair: $(y+2d+y)^2 \ \ge\ 4(y+d)f(y)$, i.e. $4(y+d)^2 \ge 4(y+d)f(y)$, hence $f(y)\le y+d$.

Therefore $f(y)=y+d$. $\square$

Starting from (9) and applying the Claim repeatedly, we get by induction on $k\ge0$: $f(y)=y+d$ for all $y>0$ with $y\ge T-kd$. Indeed, the base case $k=0$ is (9); for the inductive step, if $f(t)=t+d$ holds for all $t>0$ with $t\ge T-kd$, then for any $y>0$ with $y\ge T-(k+1)d$ the point $x=y+d$ satisfies $x>0$ and $x\ge T-kd$, so $f(x)=x+d$ and the two displayed computations above give $f(y)=y+d$. Since $T-kd\to-\infty$, every $y>0$ is covered:
$$f(y) = y + d \qquad\text{for all } y>0.$$

#### Step 7: conclusion.

Either $g(y)=f(y)-y$ is identically $0$, in which case $f(y)=y=y+0$; or some gap is positive, in which case Steps 3–6 give $f(y)=y+d$ for all $y>0$ with the constant $d>0$. In both cases
$$f(x) = x + c \quad\text{for all }x>0, \text{ for some constant } c\ge 0 .$$
Together with Part I, the set of solutions is exactly $\{\,x\mapsto x+c \ :\ c\ge 0\,\}$. $\blacksquare$
