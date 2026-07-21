# Lemma: All positive $c$-values coincide

**Statement:** Assume $f$ satisfies conditions, $c\ge0$. Let $Q=\{x:c(x)>0\}$.
If $a,b\in Q$, then $c(a)=c(b)$.

**Proof:** Let $p=c(a)>0$, $q=c(b)>0$. Orbits $A_n=a+n p$, $B_m=b+m q$ satisfy
$c(A_n)=p$, $c(B_m)=q$, and for $n\ge1$, $A_n=f(A_{n-1})$. By previous lemma
with $y=A_{n-1}$, $P=f(y)=A_n$, for any $x$, $|c(x)-p|\le (x-A_n)^2/A_n$.
Take $x=B_{m_n}$ where $m_n$ minimizes $|B_m-A_n|$. For $A_n\ge b$, the spacing
of $B_m$ is $q$, so $|B_{m_n}-A_n|\le q/2$. Then $|q-p|\le (q/2)^2/A_n$.
Letting $n\to\infty$, $A_n\to\infty$, so $|q-p|=0$.
∎
