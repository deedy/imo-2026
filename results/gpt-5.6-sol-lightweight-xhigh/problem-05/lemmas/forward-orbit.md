# Forward-orbit lemma

## Statement
Suppose $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfies the inequalities in the problem. Then, for every $t>0$ and every integer $n\ge0$,
\[
f^{\,n}(t)=t+n(f(t)-t).
\]
In particular, $f(t)\ge t$, and the displacement $f(s)-s$ is constant along every forward orbit.

## Proof
Set $x=f(y)$ in the given chain. Its two outer quantities are both $f(y)$, so the middle quantity equals $f(y)$, giving
\[
f(f(y))=2f(y)-y. \tag{1}
\]
Let $t_0=t$ and $t_{n+1}=f(t_n)$. Equation (1) gives $t_{n+2}=2t_{n+1}-t_n$. Therefore this sequence has constant first difference, and induction yields
\[
t_n=t+n(t_1-t_0)=t+n(f(t)-t).
\]
If $f(t)-t<0$, this expression is nonpositive for sufficiently large $n$, contrary to $t_n\in\mathbb R_{>0}$. Thus $f(t)-t\ge0$. Finally,
\[
f(t+n(f(t)-t))=t+(n+1)(f(t)-t),
\]
which proves constancy of the displacement along the orbit. $\square$
