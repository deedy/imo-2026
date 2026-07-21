# Lemma: $c(x)=f(x)-x\ge0$

**Statement:** Let $f:R_{>0}\to R_{>0}$ satisfy conditions, define $c(x)=f(x)-x$.
Then $c(f(y))=c(y)$ and $c(y)\ge0$ for all $y$, and $f(f(y))=2f(y)-y$.

**Proof:** Square as in full proof. For $y>0$, set $x=f(y)$. Then
$\alpha(x,y)\ge0,\beta(x,y)\ge0$ and $\alpha+\beta=2(x-f(y))^2=0$.
Hence $\alpha=\beta=0$, giving $(f(f(y))+y)^2=4f(y)^2$, so $f(f(y))=2f(y)-y$
(since positive). Thus $c(f(y))=f(f(y))-f(y)=f(y)-y=c(y)$.
Iterate: $a_0=y$, $a_{n+1}=f(a_n)$. By induction $a_n=y+n c(y)$ and
$c(a_n)=c(y)$. Since $f$ maps to $>0$, all $a_n>0$. If $c(y)<0$, picking
$n> y/|c(y)|$ makes $a_n\le0$ contradiction. Hence $c(y)\ge0$.
∎
