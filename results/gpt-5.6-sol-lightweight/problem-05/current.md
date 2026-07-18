# imo-2026-05 — tracking file

## Status

solved

## Problem

Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried

- **Iteration and rigidity (successful):** Substituting $x=f(y)$ forces an affine relation along every forward orbit. A symmetrized substitution then gives a quadratic modulus estimate for the displacement $g=f-\mathrm{id}$, from which monotonicity, continuity, and finally constancy follow.
- **Direct inequality reformulation (exploratory):** Rewriting both inequalities in terms of $g(x)-g(y)$ reveals error terms vanishing when $x=f(y)$, but the raw asymmetric bounds do not by themselves immediately compare all displacement classes. The iterate identity supplies the needed symmetry.
- **Sanity checking:** Random numerical tests verify both inequalities for translations $f(x)=x+c$ over many orders of magnitude; this is only a check, not part of the proof.

## Current best

The complete set of solutions is
\[
\boxed{f(x)=x+c\quad\text{for all }x>0,\qquad c\ge0.}
\]
The proof first derives $f(f(t))=2f(t)-t$. For $g(t)=f(t)-t$, forward iteration gives $f^n(t)=t+ng(t)$ and hence $g\ge0$. Comparing the original inequality at $(x,y)=(f(u),v)$ and $(f(v),u)$ gives a quadratic estimate on $|g(u)-g(v)|$. This forces $f$ to be increasing, then $g$ to be nondecreasing and continuous, and a partition argument forces $g$ to be constant.

## Full proof

Define
\[
g(t)=f(t)-t\qquad(t>0).
\]

### 1. The iterate identity

In the given chain, set $x=f(y)$. Its two outer terms are both $f(y)$, since
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y)
\quad\text{and}\quad
\sqrt{f(y)f(y)}=f(y).
\]
Thus equality holds throughout, and
\[
\frac{f(f(y))+y}{2}=f(y).
\]
Therefore
\[
f(f(y))=2f(y)-y. \tag{1}
\]
In terms of $g$, equation (1) says
\[
g(f(y))=f(f(y))-f(y)=f(y)-y=g(y). \tag{2}
\]
It follows by induction from (2) that, for every integer $n\ge0$,
\[
f^n(y)=y+ng(y). \tag{3}
\]
Every forward iterate belongs to $\mathbb R_{>0}$. If $g(y)<0$, the right side of (3) is nonpositive for all sufficiently large $n$, a contradiction. Hence
\[
g(y)\ge0\qquad\text{for all }y>0. \tag{4}
\]

### 2. A quadratic comparison estimate

Fix $u,v>0$. Apply the original chain with $x=f(u)$ and $y=v$. By (1), and by $v=f(v)-g(v)$, its middle numerator is
\[
f(f(u))+v=f(u)+g(u)+f(v)-g(v).
\]
Writing $X=f(u)$, $Z=f(v)$, and $d=g(u)-g(v)$, we obtain
\[
\sqrt{\frac{X^2+Z^2}{2}}\ge \frac{X+Z+d}{2}\ge\sqrt{XZ}. \tag{5}
\]
The right-hand inequality in (5) gives
\[
d\ge 2\sqrt{XZ}-X-Z=-(\sqrt X-\sqrt Z)^2. \tag{6}
\]
Interchanging $u$ and $v$ in the same argument replaces $d$ by $-d$, so (6) also gives
\[
-d\ge-(\sqrt X-\sqrt Z)^2.
\]
Consequently
\[
|g(u)-g(v)|\le\bigl(\sqrt{f(u)}-\sqrt{f(v)}\bigr)^2. \tag{7}
\]

### 3. Monotonicity

We first prove that $f$ is strictly increasing. Let $u>v$, and set
\[
h=u-v>0,\qquad d=g(u)-g(v),\qquad \Delta=f(u)-f(v)=h+d.
\]
If $\Delta=0$, (7) gives $d=0$, contrary to $\Delta=h+d$ and $h>0$.

Suppose instead that $\Delta<0$. Then $d<-h$, while (7) yields
\[
|d|\le \bigl(\sqrt{f(u)}-\sqrt{f(v)}\bigr)^2
=|\Delta|\frac{|\sqrt{f(u)}-\sqrt{f(v)}|}{\sqrt{f(u)}+\sqrt{f(v)}}
<|\Delta|.
\]
On the other hand, since $\Delta=h+d<0$,
\[
|\Delta|=|d|-h<|d|,
\]
a contradiction. Thus $\Delta>0$, proving that $f$ is strictly increasing.

Every iterate $f^n$ is consequently strictly increasing. From (3), for $u>v$ and every positive integer $n$,
\[
u+ng(u)=f^n(u)>f^n(v)=v+ng(v).
\]
Hence
\[
g(u)-g(v)>-\frac{u-v}{n}.
\]
Letting $n\to\infty$ gives $g(u)\ge g(v)$. Therefore $g$ is nondecreasing. \(\tag{8}\)

### 4. Continuity

Fix $t>0$. Since $g$ is nondecreasing, its right limit
\[
L=\lim_{s\downarrow t}g(s)
\]
exists and is finite (for example, $g(t)\le g(s)\le g(t+1)$ when $t<s<t+1$). Put $J=L-g(t)\ge0$ and $A=f(t)>0$. As $s\downarrow t$, we have
\[
f(s)=s+g(s)\longrightarrow t+L=A+J.
\]
Passing to the limit in (7) gives
\[
J\le(\sqrt{A+J}-\sqrt A)^2. \tag{9}
\]
If $J>0$, then
\[
(\sqrt{A+J}-\sqrt A)^2
=J\frac{\sqrt{A+J}-\sqrt A}{\sqrt{A+J}+\sqrt A}<J,
\]
contradicting (9). Hence $J=0$, so $g$ is right-continuous at $t$.

The left limit exists as well (when approaching within $\mathbb R_{>0}$). If
\[
J=g(t)-\lim_{s\uparrow t}g(s)>0,
\]
then passing to the limit in (7) gives
\[
J\le(\sqrt{f(t)}-\sqrt{f(t)-J})^2<J,
\]
again a contradiction. Thus $g$ is also left-continuous. Therefore $g$, and hence $f(t)=t+g(t)$, is continuous on $\mathbb R_{>0}$. \(\tag{10}\)

### 5. The displacement is constant

Fix $0<a<b$. For a positive integer $N$, partition $[a,b]$ into $N$ equal subintervals, with endpoints
\[
x_i=a+\frac{i(b-a)}N\qquad(0\le i\le N).
\]
Because $f$ is strictly increasing and $g$ is nondecreasing, the quantities
\[
\Delta_i=f(x_i)-f(x_{i-1})>0,
\qquad
d_i=g(x_i)-g(x_{i-1})\ge0
\]
are nonnegative as indicated. By (7),
\[
\begin{aligned}
d_i
&\le \bigl(\sqrt{f(x_i)}-\sqrt{f(x_{i-1})}\bigr)^2\\
&=\frac{\Delta_i^2}{\bigl(\sqrt{f(x_i)}+\sqrt{f(x_{i-1})}\bigr)^2}
\le\frac{\Delta_i^2}{4f(a)}.
\end{aligned}
\]
Summing and using telescoping gives
\[
\begin{aligned}
0\le g(b)-g(a)
&\le \frac1{4f(a)}\sum_{i=1}^N\Delta_i^2\\
&\le \frac{\max_i\Delta_i}{4f(a)}\sum_{i=1}^N\Delta_i\\
&=\frac{\max_i\Delta_i}{4f(a)}\bigl(f(b)-f(a)\bigr). \tag{11}
\end{aligned}
\]
By (10), $f$ is uniformly continuous on the compact interval $[a,b]$. The partition mesh tends to zero, so $\max_i\Delta_i\to0$ as $N\to\infty$. Equation (11) therefore gives $g(b)=g(a)$. Since $a<b$ were arbitrary, $g$ is constant on $\mathbb R_{>0}$.

Thus there is a constant $c$ such that
\[
f(x)=x+c.
\]
By (4), $c\ge0$.

### 6. Verification

Conversely, let $c\ge0$ and define $f(x)=x+c$. Then $f$ maps positive reals to positive reals, and
\[
\frac{f(x)+y}{2}=\frac{x+(y+c)}2=\frac{x+f(y)}2.
\]
For the two positive numbers $x$ and $f(y)$, the root-mean-square/arithmetic-mean inequality and the arithmetic-mean/geometric-mean inequality give
\[
\sqrt{\frac{x^2+f(y)^2}{2}}
\ge \frac{x+f(y)}2
\ge\sqrt{xf(y)}.
\]
Hence every such function works, completing the characterization.
