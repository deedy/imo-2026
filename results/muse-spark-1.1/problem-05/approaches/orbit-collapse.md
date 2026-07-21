# Approach: orbit collapse at $x=f(y)$

Idea: Square the two inequalities to remove roots. Define
$\alpha(x,y)=(f(x)+y)^2-4xf(y)\ge0$ and $\beta(x,y)=2x^2+2f(y)^2-(f(x)+y)^2\ge0$.
Then $\alpha+\beta=2(x-f(y))^2$.

For any $y$, choosing $x=f(y)$ forces $\alpha+\beta=0$, hence $\alpha=\beta=0$.
This yields $f(f(y))=2f(y)-y$ and equality case in original.

Let $c(y)=f(y)-y$. Then $c(f(y))=c(y)$ and iteration gives
$f^{n}(y)=y+n c(y)$. Positivity of iterates forces $c(y)\ge0$.

Consequence: images satisfy $f(y)=P$, $c(y)=P-y$.
Rewrite conditions as bounds for $c(x)$ in terms of $P$:
$2\sqrt{xP}-x-y\le c(x)\le\sqrt{2x^2+2P^2}-x-y$.
Subtract $c(y)$ to bound $|c(x)-c(y)|\le (x-P)^2/P$.

If $c(a)>0$, $c(b)>0$, consider arithmetic progressions $a+n c(a)$ and $b+m c(b)$.
For large $n$, $A_n$ is $P=f(A_{n-1})$ and close to some $B_m$ within half step.
The bound then forces $c(a)=c(b)$. Hence all positive values equal $p$.

If $Z=\{c=0\}$ and $Q=\{c>0\}$ both non-empty, separation $|a-b|\ge p$ for
$a\in Q,b\in Z$ follows from the upper bound inequality. This makes $Z,Q$ both
open in $(0,\infty)$, contradicting connectedness. Hence constant $c\ge0$.

Status: succeeds, gives full classification.
