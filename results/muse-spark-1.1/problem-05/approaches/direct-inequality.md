# Approach: direct AM-GM / RMS-AM comparison

Attempt: Try to apply AM>=GM and RMS>=AM directly to original form.

Observe that for any $u,v>0$, $\sqrt{(u^2+v^2)/2}\ge (u+v)/2\ge\sqrt{uv}$.
Thus if $f(x)=x+c$, then $f(x)+y = x+y+c$, $f(y)=y+c$, and inequalities become exactly RMS>=AM>=GM for pair $(x,y+c)$.

Goal to show $f(y)-y$ independent of $y$ and $\ge0$ via inequalities.

First, $P(x,y)$ gives $(f(x)+y)^2\ge4xf(y)$. Swapping? No swap symmetry.

Trying $x=y$ gives $(f(x)+x)^2\ge4x f(x)$ i.e. $(f(x)-x)^2\ge0$ trivial, and
$2x^2+2f(x)^2\ge(f(x)+x)^2$ i.e. same $(f(x)-x)^2\ge0$. So diagonal gives no info.

Need off-diagonal to link $c(x),c(y)$. Reformulation with $P=f(y)$ gave tight quadratic bound allowing $c$-difference estimate.

Status: merged into orbit-collapse approach.
