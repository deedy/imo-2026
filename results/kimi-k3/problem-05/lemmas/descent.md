# Lemma: descent along an orbit of positive increment

## Statement
Assume the key estimate
\[
\big|(f(x)+y)^2-(x+f(y))^2\big|\le (x-f(y))^2 \tag{1}
\]
holds and that $p(u):=f(u)-u\ge0$ for all $u>0$. If $p(t)=c$ and $t>c>0$, then $z=t-c$ is positive, $p(z)=c$, and $f(z)=t$. Consequently, every $t$ with $p(t)=c>0$ can be reduced by repeatedly subtracting $c$ to some $r\in(0,c]$ with $p(r)=c$.

## Proof
Let $z=t-c>0$ and write $e=p(z)\ge0$. Then
\[
f(t)=t+c,\qquad f(z)=z+e=t-c+e.
\]
Apply (1) with $(x,y)=(t,z)$. We compute
\[
f(t)+z=(t+c)+(t-c)=2t,
\]
\[
t+f(z)=t+(t-c+e)=2t-c+e,
\]
and
\[
t-f(z)=t-(t-c+e)=c-e.
\]
Thus (1) gives
\[
|c-e|(4t-c+e)\le (c-e)^2. \tag{*}
\]
If $c\ne e$, divide (*) by $|c-e|$ to get $4t-c+e\le |c-e|$. But $t>c$, so
\[
4t-c+e>3c+e>|c-e|,
\]
where the final inequality holds both for $e\ge c$ and for $e<c$. Contradiction. Hence $e=c$, and therefore
\[
f(z)=z+c=(t-c)+c=t.
\]

For the last statement, start from $t$ with $p(t)=c>0$. While the current point is $>c$, subtract $c$; by the part just proved this stays in $\mathbb R_{>0}$ and preserves the increment $c$. After finitely many subtractions the process stops at $r$ with $0<r\le c$, and $p(r)=c$.
