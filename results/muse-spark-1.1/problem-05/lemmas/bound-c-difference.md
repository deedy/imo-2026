# Lemma: Local bound for $c(x)-c(y)$

**Statement:** Let $c(x)=f(x)-x\ge0$, $P_y=f(y)=y+c(y)$. Then for all $x>0$,
$$2\sqrt{xP_y}-x-P_y\le c(x)-c(y)\le\sqrt{2x^2+2P_y^2}-x-P_y,$$
and in particular $|c(x)-c(y)|\le\frac{(x-P_y)^2}{P_y}$.

**Proof:** From squared inequalities,
$(x+y+c(x))^2\ge4x P_y$ and $(x+y+c(x))^2\le2x^2+2P_y^2$.
Positivity gives $2\sqrt{xP_y}\le x+y+c(x)\le\sqrt{2x^2+2P_y^2}$.
Subtract $x+y$ then subtract $c(y)=P_y-y$ to change to $c(x)-c(y)$.
For the absolute bound note
$2\sqrt{xP_y}-x-P_y=-(\sqrt x-\sqrt{P_y})^2=-(x-P_y)^2/(\sqrt x+\sqrt{P_y})^2$
and $\sqrt{2x^2+2P_y^2}-x-P_y=(x-P_y)^2/(\sqrt{2x^2+2P_y^2}+x+P_y)$.
Both denominators $\ge P_y$, giving estimate.
∎
