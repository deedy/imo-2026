# Lemma: all positive displacements are equal

## Statement
Under the hypotheses of the problem, let $d(t)=f(t)-t$. If $d(a)>0$ and $d(b)>0$, then $d(a)=d(b)$.

## Proof
Write $p=d(a)>0$ and $q=d(b)>0$. By the forward-orbit structure, for nonnegative integers $m,n$ the points
\[
x=a+mp,\qquad y=b+nq
\]
have displacements $p,q$, respectively. Put $v=f(y)=b+(n+1)q$. The upper inequality gives
\[
\sqrt{2(x^2+v^2)}\ge f(x)+y=x+v+p-q,
\]
so
\[
p-q\le \Phi(x,v),\qquad
\Phi(u,v)=\sqrt{2(u^2+v^2)}-u-v.
\]
For all sufficiently large $m$, choose
\[
n=\left\lfloor\frac{a+mp-(b+q)}q\right\rfloor\ge0.
\]
Then $0\le x-v<q$ and $x,v\to\infty$. Since
\[
\Phi(x,v)=\frac{(x-v)^2}{\sqrt{2(x^2+v^2)}+x+v},
\]
we obtain $0\le\Phi(x,v)\le q^2/(x+v)\to0$. Thus $p\le q$. Reversing $a,b$ yields $q\le p$, and hence $p=q$. $\square$
