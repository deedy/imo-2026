# imo-2026-05 — tracking file

## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- **Forward-orbit displacement (successful):** substituting $x=f(y)$ forces $f(f(y))=2f(y)-y$. Thus, for $d(t)=f(t)-t$, the displacement is constant along every forward orbit, whose terms are $t+nd(t)$. Positivity of all those terms gives $d(t)\ge 0$.
- **Asymptotic alignment of arithmetic orbits (successful):** for two points with positive displacements $p,q$, their forward orbits are arithmetic progressions. Terms of the first orbit can be aligned within a bounded distance of shifted terms of the second. The upper inequality then forces $p\le q$; reversing the points forces $q\le p$.
- **Connectedness after displacement quantization (successful):** once every positive displacement has one common value $c$, the sets where $d=0$ and $d=c$ would both be open if both occurred. This contradicts connectedness of $\mathbb R_{>0}$.
- **Direct expansion of the squared inequalities (not used):** expanding produces polynomial bounds involving $d(x)$ and $d(y)$, but these are less transparent than rewriting the upper bound in terms of $x$, $f(y)$, and $d(x)-d(y)$.
- **Linear/translation ansatz (sanity check):** $f(x)=x+c$ works for every $c\ge 0$ by the AM--GM and RMS--AM inequalities; a homogeneous linear trial $f(x)=ax$ is consistent only for $a=1$.
- **Numerical checks:** `code/sanity_check.py` tests the candidate family on random inputs across twelve orders of magnitude and checks the orbit-alignment estimate. Standalone write-ups of the three proof lemmas are in `lemmas/`.

## Current best
The complete characterization is
\[
\boxed{f(x)=x+c\quad\text{for every }x>0,\qquad c\ge 0.}
\]
The proof first obtains nonnegative, forward-orbit-invariant displacement $d=f-\operatorname{id}$; asymptotic alignment of two arithmetic forward orbits shows that all positive values of $d$ coincide; finally, continuity of the numerical RMS--AM gap and connectedness of $\mathbb R_{>0}$ rule out coexistence of displacement $0$ with a positive displacement.

## Full proof
Put
\[
d(t)=f(t)-t\qquad(t>0).
\]

### 1. Forward orbits and nonnegative displacement
(Standalone version: [orbit-structure lemma](lemmas/orbit-structure.md).)
Fix $y>0$ and substitute $x=f(y)$. The two outer expressions in the given chain are then both $f(y)$, since
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y)
\quad\text{and}\quad
\sqrt{f(y)f(y)}=f(y).
\]
Consequently equality holds throughout, and hence
\[
f(f(y))=2f(y)-y. \tag{1}
\]
It follows that
\[
d(f(y))=f(f(y))-f(y)=f(y)-y=d(y). \tag{2}
\]
For $n\ge 0$, let $f^n$ denote the $n$-fold iterate (with $f^0$ the identity). Equations (1)--(2), followed by induction, give
\[
d(f^n(y))=d(y),
\qquad
f^n(y)=y+n d(y) \quad(n\ge 0). \tag{3}
\]
Every $f^n(y)$ is positive. If $d(y)<0$, however, then the second formula in (3) is negative for every sufficiently large integer $n$, a contradiction. Therefore
\[
d(y)\ge 0\qquad\text{for all }y>0. \tag{4}
\]

### 2. All positive displacements are equal
(Standalone version: [positive-displacements-equal lemma](lemmas/positive-displacements-equal.md).)
Let $a,b>0$ have positive displacements
\[
p=d(a)>0,\qquad q=d(b)>0.
\]
By (3), for all nonnegative integers $m,n$,
\[
x:=f^m(a)=a+mp,
\qquad
y:=f^n(b)=b+nq,
\]
and $d(x)=p$, $d(y)=q$. Write
\[
v=f(y)=b+(n+1)q.
\]
The left-hand inequality of the problem (that is, the upper bound on the middle expression) becomes
\[
\sqrt{\frac{x^2+v^2}{2}}
 \ge \frac{f(x)+y}{2}
 =\frac{(x+p)+(v-q)}2.
\]
After multiplication by $2$, this yields
\[
p-q\le \Phi(x,v),
\qquad
\Phi(u,v):=\sqrt{2(u^2+v^2)}-u-v. \tag{5}
\]
For every sufficiently large $m$, choose
\[
n=n_m:=\left\lfloor\frac{a+mp-(b+q)}q\right\rfloor.
\]
Then $n_m\ge0$, and with $x_m=a+mp$ and
$v_m=b+(n_m+1)q$ we have
\[
0\le x_m-v_m<q. \tag{6}
\]
Moreover, $x_m,v_m\to\infty$. Rationalizing gives, for all positive $u,v$,
\[
\Phi(u,v)
=\frac{(u-v)^2}{\sqrt{2(u^2+v^2)}+u+v}. \tag{7}
\]
Thus (6)--(7) imply
\[
0\le \Phi(x_m,v_m)
\le \frac{q^2}{x_m+v_m}\longrightarrow 0.
\]
Applying (5) along this sequence gives $p-q\le0$. Interchanging $a$ and $b$ and repeating the same argument gives $q-p\le0$. Hence
\[
p=q. \tag{8}
\]
Therefore, either $d$ vanishes identically, or there is a number $c>0$ such that
\[
d(t)\in\{0,c\}\qquad(t>0). \tag{9}
\]

### 3. The two displacement values cannot coexist
(Standalone version: [no-mixed-displacement lemma](lemmas/no-mixed-displacement.md).)
Suppose now that $c>0$ occurs, and define
\[
A=\{t>0:d(t)=0\},
\qquad
B=\{t>0:d(t)=c\}.
\]
By (9), these sets are disjoint and cover $\mathbb R_{>0}$, and $B$ is nonempty.

If $x\in B$ and $y\in A$, then $f(x)=x+c$ and $f(y)=y$. The left-hand inequality in the problem gives
\[
\sqrt{\frac{x^2+y^2}{2}}\ge\frac{x+c+y}{2},
\]
or equivalently
\[
c\le \Phi(x,y), \tag{10}
\]
where $\Phi$ is as in (5). The function $\Phi$ is continuous on $\mathbb R_{>0}^2$ and satisfies
\[
\Phi(t,t)=0\qquad(t>0). \tag{11}
\]

Fix $b\in B$. By (11) and continuity, all $y$ sufficiently close to $b$ satisfy $\Phi(b,y)<c$. Such a $y$ cannot belong to $A$, by (10), so it belongs to $B$. Hence $B$ is open in $\mathbb R_{>0}$. Similarly, if $a\in A$, then all $x$ sufficiently close to $a$ satisfy $\Phi(x,a)<c$; (10) shows that such an $x$ cannot belong to $B$. Hence $A$ is also open in $\mathbb R_{>0}$.

The interval $\mathbb R_{>0}$ is connected, so it cannot be the union of two disjoint nonempty open subsets. Since $B$ is nonempty, we conclude that $A$ is empty. Thus $d(t)=c$ for every $t>0$. Together with the case $d\equiv0$, this proves that every solution must have the form
\[
f(t)=t+c\qquad(t>0)
\]
for some $c\ge0$.

### 4. Verification
Conversely, fix $c\ge0$ and let $f(t)=t+c$. For all $x,y>0$, set $z=y+c>0$. Then
\[
\frac{f(x)+y}{2}=\frac{x+z}{2}.
\]
The RMS--AM and AM--GM inequalities applied to the positive numbers $x,z$ give
\[
\sqrt{\frac{x^2+z^2}{2}}
\ge \frac{x+z}{2}
\ge \sqrt{xz}.
\]
Since $z=f(y)$, this is precisely the required chain. Hence every $c\ge0$ indeed gives a solution, completing the characterization.
