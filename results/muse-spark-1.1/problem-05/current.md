# imo-2026-05 — tracking file
## Status
solved

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- Reformulated as two squared inequalities and introduced $\alpha,\beta$ with sum $2(x-f(y))^2$.
- Obtained $x=f(y)$ collapse giving $f(f(y))=2f(y)-y$.
- Showed $c(x)=f(x)-x\ge0$ by iterating and positivity.
- Showed $c(f(x))=c(x)$ and orbit is arithmetic: $f^n(y)=y+n c(y)$.
- Derived bounds for $c_x$ around image points: $|c_x-c_y|\le (x-f(y))^2 / f(y)$.
- Used density/separation argument to prove all positive $c$ equal and mixed zero/positive impossible.
- Concluded $f(x)=x+c$, $c\ge0$.

## Current best
The only solutions are $f_c(x)=x+c$ for $c\ge0$. Verification: $(f_c(x)+y)/2=(x+y+c)/2$, $x f_c(y)=x(y+c)$, $x^2+f_c(y)^2=x^2+(y+c)^2$, and both AM-GM and RMS-AM give $(x-(y+c))^2\ge0$.

## Full proof
Let $P(x,y)$ be the statement
$$ \sqrt{\frac{x^2+f(y)^2}{2}}\ge\frac{f(x)+y}{2}\ge\sqrt{x f(y)}\qquad x,y>0. \tag{0}$$
Both sides $\ge0$. Squaring,
\begin{align}
A(x,y):&\;(f(x)+y)^2\ge 4x f(y), \tag{1}\\
B(x,y):&\;2x^2+2f(y)^2\ge (f(x)+y)^2. \tag{2}
\end{align}
Indeed $(0)$ is equivalent to (1) and (2). Set
$$\alpha(x,y)=(f(x)+y)^2-4xf(y)\ge0,\qquad \beta(x,y)=2x^2+2f(y)^2-(f(x)+y)^2\ge0.$$
Then
$$\alpha+\beta =2x^2+2f(y)^2-4xf(y)=2(x-f(y))^2\ge0. \tag{3}$$

Put $c(x)=f(x)-x$, so $f(x)=x+c(x)$ and $f(x)>0\Rightarrow c(x)>-x$.

1. **The image point gives equality.** Fix $y>0$ and take $x_0=f(y)>0$. Then $x_0-f(y)=0$, so by (3) $\alpha(x_0,y)+\beta(x_0,y)=0$. Since both $\ge0$, $\alpha=\beta=0$. Hence
$$(f(f(y))+y)^2=4f(y)^2.$$
Both sides $>0$, so $f(f(y))+y=2f(y)$ and
$$f(f(y))=2f(y)-y\quad\forall y>0, \tag{4}$$
in particular $2f(y)>y$, i.e. $f(y)>y/2$, and
$$c(f(y))=f(f(y))-f(y)=f(y)-y=c(y). \tag{5}$$

2. **Nonnegativity of $c$.** Iterate (4). Define $a_0=y$, $a_{n+1}=f(a_n)$. By (5), $c(a_{n+1})=c(a_n)$. Induction gives $c(a_n)=c(y)$ and
$$a_{n+1}=a_n+c(y),\qquad a_n=y+n\,c(y)\quad n\ge0. \tag{6}$$
All $a_n>0$ because $f$ maps to $>0$. If $c(y)<0$ then $a_n\to-\infty$, and for $n>y/|c(y)|$ we have $a_n\le0$, impossible. Hence
$$c(y)\ge0\quad\forall y,\qquad f(y)\ge y. \tag{7}$$
Moreover (5)–(6) hold.

Denote $p_y=c(y)\ge0$, $P_y=f(y)=y+p_y$. Then $f(y)=P_y$.

3. **Local confinement of $c$.** From (1)(2) with $f=x+c$ notation,
$$(x+y+c(x))^2\ge4x(y+c(y)),\qquad (x+y+c(x))^2\le2x^2+2(y+c(y))^2. \tag{8}$$
Fix $y$ and put $P=P_y=y+c(y)$. Then $y+c(y)=P$. (8) becomes
$$2\sqrt{xP}-x-y\le c(x)\le\sqrt{2x^2+2P^2}-x-y, \tag{9}$$
where the lower bound is effective only when it is $>0$ (otherwise $c(x)\ge0$ already). Rewrite using $y=P-c(y)$:
$$c(x)-c(y)\in[I_L(x,P),\,I_U(x,P)], \tag{10}$$
$$I_L(x,P)=2\sqrt{xP}-x-P=-(\sqrt{x}-\sqrt{P})^2=-\frac{(x-P)^2}{(\sqrt{x}+\sqrt{P})^2},$$
$$I_U(x,P)=\sqrt{2x^2+2P^2}-x-P=\frac{(x-P)^2}{\sqrt{2x^2+2P^2}+x+P}.$$
Thus $I_L\le0\le I_U$ and
$$I_L(x,P)=-(x+P-2\sqrt{xP}),\quad |I_L|=( \sqrt{x}-\sqrt{P})^2,\quad I_U\ge0.$$
Hence
$$|c(x)-c(y)|\le\max(|I_L|,I_U).$$
But
$$|I_L|=\frac{(x-P)^2}{(\sqrt{x}+\sqrt{P})^2}\le\frac{(x-P)^2}{P},\qquad I_U=\frac{(x-P)^2}{\sqrt{2x^2+2P^2}+x+P}\le\frac{(x-P)^2}{P}. \tag{11}$$
Therefore for every $y>0$ with $P=f(y)$,
$$|c(x)-c(y)|\le\frac{(x-P)^2}{P}\quad\forall x>0. \tag{12}$$
In particular if $x=P$, $c(x)=c(y)$, consistent with (5).

4. **All positive values of $c$ coincide.** Let
$$Z=\{x:c(x)=0\},\qquad Q=\{x:c(x)>0\}.$$
Assume $a,b\in Q$, $p=c(a)>0$, $q=c(b)>0$. By (6), forward orbits
$$A_n=a+n p\;(n\ge0),\quad B_m=b+m q\;(m\ge0)$$
satisfy $c(A_n)=p$, $c(B_m)=q$, and for $n\ge1$, $A_n=f(A_{n-1})\in\operatorname{Im}f$, similarly $B_m\in\operatorname{Im}f$ for $m\ge1$.

Fix $n\ge1$, $P_n=A_n$. For any $X>0$ there is $m$ with $|X-B_m|\le q/2$ (nearest point of the arithmetic progression, at least for $X\ge b$). Choose $X=P_n$ with $P_n\ge b$ (eventually true since $P_n\to\infty$). Pick $m_n$ minimizing $|P_n-B_{m_n}|$; then $h_n:=B_{m_n}-P_n$, $|h_n|\le q/2$.

Apply (12) with $y=A_{n-1}$ so $P=f(y)=P_n$ and $x=B_{m_n}$:
$$|c(B_{m_n})-c(y)|=|q-p|\le\frac{h_n^2}{P_n}\le\frac{(q/2)^2}{P_n}.$$
Since $P_n=a+n p\to\infty$, the right side $\to0$. Hence $p=q$. So any two points with positive $c$ have same value. Denote this common value by $p>0$ if $Q\neq\varnothing$.

5. **Zero and positive cannot coexist.** Suppose $Z\neq\varnothing$ and $Q\neq\varnothing$, so $p>0$ is the unique positive value. Take $b\in Z$, $a\in Q$. For pair $(x=a,y=b)$, condition $B$ gives
$$(a+b+p)^2\le2a^2+2b^2\iff (a-b)^2\ge p^2+2p(a+b)\ge p^2. \tag{13}$$
Thus $|a-b|\ge p$ for every $a\in Q,b\in Z$. Indeed (13) is exactly the $B$-inequality. Consequently
$$\inf\{|a-b|:a\in Q,b\in Z\}\ge p>0. \tag{14}$$

If $\inf$ is $\ge d>0$, then $Z$ and $Q$ are both open in $(0,\infty)$: If $z\in Z$ and $|x-z|<d$, $x$ cannot belong to $Q$ (otherwise distance $<d$), so the $d$-ball around $z$ stays in $Z$; similarly for $Q$. Thus $(0,\infty)=Z\sqcup Q$ would be a separation into two disjoint non-empty open sets, contradicting connectedness of $(0,\infty)$. Detailed: Suppose $d=\operatorname{dist}(Z,Q)>0$. For $z\in Z$, $(z-d/2,z+d/2)\cap(0,\infty)$ meets $Q$ would give points at distance $<d$; hence the interval lies in $Z$. So $Z$ open, similarly $Q$ open.

Therefore one of $Z,Q$ is empty.

If $Q=\varnothing$, then $c\equiv0$.

If $Z=\varnothing$, then $c(x)=p>0$ for all $x$, constant.

6. **Form of $f$.** In either case $c$ is constant: $c(x)=c_0\ge0$ for all $x$. Hence
$$f(x)=x+c_0,\quad c_0\ge0.$$
Positivity $f:(0,\infty)\to(0,\infty)$ exactly requires $c_0\ge0$ (if $c_0<0$, choose $x<|c_0|$ giving $f(x)\le0$).

7. **Verification.** Let $f_c(x)=x+c$, $c\ge0$. Then for any $x,y>0$,
$$\frac{f_c(x)+y}{2}=\frac{x+y+c}{2},$$
$$\sqrt{xf_c(y)}=\sqrt{x(y+c)},\quad \sqrt{\frac{x^2+f_c(y)^2}{2}}=\sqrt{\frac{x^2+(y+c)^2}{2}}.$$
By AM$\ge$GM, $\frac{x+(y+c)}{2}\ge\sqrt{x(y+c)}$, i.e.
$$(x+y+c)^2-4x(y+c)=(x-y-c)^2\ge0.$$
By RMS$\ge$AM, $\sqrt{\frac{x^2+(y+c)^2}{2}}\ge\frac{x+y+c}{2}$, i.e.
$$2x^2+2(y+c)^2-(x+y+c)^2=(x-y-c)^2\ge0.$$
Thus both inequalities hold, with equalities exactly when $x=y+c=f_c(y)$.

Hence all functions $f(x)=x+c$, $c\ge0$, and only they, satisfy the requirement.

∎
