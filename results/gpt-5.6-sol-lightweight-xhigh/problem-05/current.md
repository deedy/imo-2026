# imo-2026-05 — tracking file
## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- **Direct equality and orbit analysis (successful):** Substituting $x=f(y)$ makes the two outer expressions equal, hence forces $f(f(y))=2f(y)-y$. Forward iteration then shows that $f(y)-y$ is nonnegative and remains constant along the whole forward orbit.
- **Asymptotic comparison of two orbits (successful):** If two points have positive displacements $a=f(u)-u$ and $b=f(v)-v$, their forward orbits are arithmetic progressions. Choosing far-out terms of the two progressions that remain a bounded distance apart makes the RMS--AM gap tend to zero, forcing $a=b$.
- **Topological elimination of mixed behavior (successful):** Once every displacement is either $0$ or one common $c>0$, the first inequality shows that the zero-displacement and $c$-displacement sets are both open. Connectedness of $\mathbb R_{>0}$ rules out a mixture.
- **Ratio/asymptotic-bound exploration (abandoned):** Writing $f(t)=t\,r(t)$ gives pairwise quadratic constraints and rough bounds, but these do not by themselves expose the exact solutions as efficiently as the equality substitution $x=f(y)$.

## Current best
All solutions are
\[
\boxed{f(x)=x+c\quad\text{for every }x>0,\qquad c\ge 0.}
\]
The proof below derives an arithmetic-progression structure for every forward orbit, proves that all positive orbit increments coincide, and then excludes coexistence of zero and positive increments.

## Full proof
Put
\[
d(t)=f(t)-t\qquad(t>0).
\]
We first determine the forward orbits of $f$. In the given inequalities, fix $y>0$ and set $x=f(y)$. Both outer expressions then equal $f(y)$:
\[
\sqrt{\frac{f(y)^2+f(y)^2}{2}}=f(y)
\quad\text{and}\quad
\sqrt{f(y)f(y)}=f(y).
\]
Consequently the middle expression must also equal $f(y)$, so
\[
\frac{f(f(y))+y}{2}=f(y),
\qquad\text{or equivalently}\qquad
f(f(y))=2f(y)-y. \tag{1}
\]
For any fixed $t>0$, define $t_0=t$ and $t_{n+1}=f(t_n)$ for $n\ge0$. Applying (1) to $t_n$ gives
\[
t_{n+2}=2t_{n+1}-t_n.
\]
Thus, by induction,
\[
t_n=t+n\bigl(f(t)-t\bigr)=t+n d(t) \qquad(n\ge0). \tag{2}
\]
Every $t_n$ belongs to $\mathbb R_{>0}$. If $d(t)<0$, the right-hand side of (2) is nonpositive for all sufficiently large integers $n$, a contradiction. Hence
\[
d(t)\ge0\qquad\text{for every }t>0. \tag{3}
\]
Moreover, (2) shows that along this orbit
\[
f(t+n d(t))=t+(n+1)d(t), \tag{4}
\]
so its displacement remains equal to $d(t)$.

We next prove that any two positive displacements are equal. Let $u,v>0$, and write
\[
a=d(u)>0,\qquad b=d(v)>0.
\]
Suppose, without loss of generality, that $a>b$. By (4), for all nonnegative integers $n,m$,
\[
f(u+na)=u+(n+1)a,
\qquad
f(v+mb)=v+(m+1)b. \tag{5}
\]
Choose integers $n\to\infty$ and
\[
m_n=\left\lfloor\frac{u+na-v-b}{b}\right\rfloor.
\]
For all sufficiently large $n$, $m_n\ge0$. Set
\[
p_n=u+na,
\qquad
q_n=v+(m_n+1)b.
\]
The definition of $m_n$ gives
\[
0\le p_n-q_n<b, \tag{6}
\]
and both $p_n$ and $q_n$ tend to infinity.

Apply the first given inequality with $x=p_n$ and $y=v+m_n b$. By (5), $f(x)=p_n+a$ and $f(y)=q_n$, and hence
\[
p_n+q_n+(a-b)
=f(x)+y
\le \sqrt{2(p_n^2+q_n^2)}.
\]
It follows that
\[
0<a-b
\le \sqrt{2(p_n^2+q_n^2)}-p_n-q_n
=\frac{(p_n-q_n)^2}{\sqrt{2(p_n^2+q_n^2)}+p_n+q_n}. \tag{7}
\]
By (6), the numerator on the right is less than $b^2$, whereas its denominator tends to infinity. The right-hand side of (7) therefore tends to $0$, contradicting $a-b>0$. Interchanging $u$ and $v$ similarly rules out $b>a$. Thus
\[
d(u)=d(v)\quad\text{whenever }d(u)>0\text{ and }d(v)>0. \tag{8}
\]

If $d$ is identically zero, then $f(t)=t$, which is one of the claimed functions. Otherwise, by (8), there is a constant $c>0$ such that
\[
d(t)\in\{0,c\}\qquad\text{for every }t>0. \tag{9}
\]
Define
\[
A=\{t>0:d(t)=0\},
\qquad
B=\{t>0:d(t)=c\}.
\]
We show that both $A$ and $B$ are open in $\mathbb R_{>0}$. If this were false at some point of either set, there would be sequences $r_k\in B$ and $s_k\in A$ with $r_k-s_k\to0$ and with both sequences converging to the same positive limit $L$ (one can keep whichever of the two points is fixed and choose points of the other set approaching it). Apply the first inequality with $x=r_k$ and $y=s_k$. Since $f(r_k)=r_k+c$ and $f(s_k)=s_k$, it yields
\[
r_k+s_k+c=f(r_k)+s_k
\le \sqrt{2(r_k^2+s_k^2)}. \tag{10}
\]
Taking $k\to\infty$ in (10) gives $2L+c\le2L$, impossible. Therefore every point of either $A$ or $B$ has a neighborhood containing no point of the other set; both sets are open.

The disjoint open sets $A$ and $B$ have union $\mathbb R_{>0}$. Since $\mathbb R_{>0}$ is connected and $B$ is nonempty, we must have $A=\varnothing$. Hence $d(t)=c$ for every $t>0$. Together with the identically-zero case, this proves that every possible function has the form
\[
f(t)=t+c
\]
for some constant $c\ge0$.

Finally, every such function does satisfy the inequalities. Indeed, if $f(t)=t+c$ with $c\ge0$, then for all $x,y>0$,
\[
\sqrt{\frac{x^2+f(y)^2}{2}}
=\sqrt{\frac{x^2+(y+c)^2}{2}}
\ge\frac{x+(y+c)}2
=\frac{f(x)+y}{2}
\ge\sqrt{x(y+c)}
=\sqrt{xf(y)},
\]
where the two inequalities are respectively the root-mean-square--arithmetic-mean and arithmetic-mean--geometric-mean inequalities for the positive numbers $x$ and $y+c$. This completes the characterization.
