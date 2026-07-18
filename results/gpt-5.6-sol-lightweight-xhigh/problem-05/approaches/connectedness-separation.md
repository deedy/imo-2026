# Separation and connectedness

## Idea
Once every displacement is either $0$ or a fixed $c>0$, show that points of the two types cannot approach each other. The two types would therefore form a separation of the connected interval $\mathbb R_{>0}$.

## Status
Successful; eliminates mixtures of fixed points and points translated by $c$.

## Details
Let
\[
A=\{t:f(t)=t\},\qquad B=\{t:f(t)=t+c\}.
\]
If $r\in B$ and $s\in A$, the first functional inequality gives
\[
r+s+c\le\sqrt{2(r^2+s^2)}.
\]
Thus there cannot be sequences $r_k\in B$ and $s_k\in A$ converging to the same positive limit $L$, since passage to the limit would give $2L+c\le2L$.

It follows that every point of $A$ has a relative neighborhood in $\mathbb R_{>0}$ disjoint from $B$, and conversely; hence both $A$ and $B$ are open. Since they are disjoint and cover the connected set $\mathbb R_{>0}$, one is empty. If $B$ was defined using a displacement known to occur, then $B\ne\varnothing$, so $A=\varnothing$.
