# imo-2026-01 — tracking file
## Status
solved
## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- Translate operation into prime exponent map $(a,b)\mapsto(\min(a,b),|a-b|)$, i.e. Euclidean subtraction.
- Observe total product $P=\prod x_i$ satisfies $P_{\text{new}}=P_{\text{old}}/\gcd(m,n)$.
- Observe $k_t=\#\{i:x_i>1\}$ is nonincreasing, drops by 1 iff $\gcd=1$ or $m=n$, otherwise stays.
- Construct infinite-descent contradiction: if $k$ stabilizes at $\ge2$, $P$ strictly decreases forever.
- Per prime invariant $G_p=\gcd_i v_p(x_i)$ unchanged by operation, yielding final $M$ formula.

## Current best
For each prime $p$ write $v_p$. Then $(m,n)\to(\gcd,\mathrm{lcm}/\gcd)$ acts as $(a_p,b_p)\to(\min,|a-b|)$. Hence total product $P$ divides by $\gcd(m,n)$ each move and $k_t=\#\{>1\}$ never increases; if a sequence were infinite $k_t$ would stabilize at $\ge2$ after which $P$ would strictly decrease infinitely, impossible. Thus process always stops, and it can stop only when $k=1$, giving a single $M>1$. Moreover $G_p=\gcd_i v_p(x_i)$ is Euclidean-invariant, so in final state $v_p(M)=G_p$, i.e. $M=\prod p^{\gcd_i v_p(x_i^{(0)})}$, independent of choices.

## Full proof
Let $N=2026$; argument works for any $N\ge2$. Denote the multiset after $t$ moves by
$x^{(t)}_1,\dots ,x^{(t)}_N$, $x^{(0)}_i>1$.

### 1. The operation in prime exponents.

For $m,n>1$ write $m=\prod p^{a_p}$, $n=\prod p^{b_p}$ ($a_p,b_p\ge0$). Then
\[v_p(\gcd(m,n))=\min(a_p,b_p),\quad v_p(\operatorname{lcm}(m,n))=\max(a_p,b_p).\]
Hence
\begin{equation}\tag{1}
v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)=\max(a_p,b_p)-\min(a_p,b_p)=|a_p-b_p|.
\end{equation}
Also $\operatorname{lcm}(m,n)=mn/\gcd(m,n)$, so
\begin{equation}\tag{2}
\gcd(m,n)\cdot\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}=\operatorname{lcm}(m,n)=\frac{mn}{\gcd(m,n)}.
\end{equation}
Thus on exponents pair $(a_p,b_p)$ the move replaces (up to order) by
\begin{equation}\tag{3}
(\min(a_p,b_p),\;|a_p-b_p|),
\end{equation}
the subtractive Euclidean step.

Lemma: not both replacements are $1$. Indeed if $g=\gcd(m,n)=1$ then
$\ell/g=mn>1$. If $\ell/g=1$ then $\ell=g$; but $m\mid\ell$ and $n\mid\ell$,
so $m\le g$ and $n\le g$, while $g\le m,n$; thus $m=n=g>1$. So with
$m\neq n$ impossible to have $\ell/g=1$ when $g>1$; check: $\ell/g=1\Rightarrow\ell=g\Rightarrow m=n=g$ as above. Consequently:

- If $g=1$, new pair is $\{1,mn\}$, exactly one $>1$.
- If $g>1$ and $m=n$, then $\ell=m=n=g$, $\ell/g=1$, new pair $\{g,1\}$, exactly one $>1$.
- If $g>1$ and $m\neq n$, then both $g>1$ and $\ell/g>1$, new pair has two $>1$.

In particular at least one new number is $>1$.

### 2. Monotone quantities.

Product: $P_t=\prod_{i=1}^N x^{(t)}_i\in\mathbb N$. By (2), if move $t\to t+1$ uses $m,n$ with $g=\gcd(m,n)$,
\begin{equation}\tag{4}
P_{t+1}=P_t\cdot\frac{g\cdot\ell/g}{mn}=P_t\cdot\frac{\ell}{mn}=P_t/g.
\end{equation}
So $P_{t+1}\le P_t$, with equality iff $g=1$, strict iff $g>1$.

Count: $k_t=|\{i:x^{(t)}_i>1\}|$. From classification above, for a move on two $>1$ entries:
\[k_{t+1}=
\begin{cases}
k_t-1, & g=1,\\
k_t-1, & g>1,\,m=n,\\
k_t,   & g>1,\,m\neq n.
\end{cases}\]
Indeed we remove two $>1$ and insert $r\in\{1,2\}$ numbers $>1$.
Thus $k_{t+1}\le k_t$ and $k_{t+1}\ge k_t-1$.

Since initial $k_0=N\ge2$ and each move keeps at least one $>1$ among the replaced pair,
$k_t$ can never become $0$: if $k_t\ge2$, $k_{t+1}=k_t-2+r\ge k_t-1\ge1$.
If $k_t=1$ there is no legal move. Hence throughout defined process $k_t\ge1$,
nonincreasing.

### 3. Finiteness and form of terminal state — (a).

Assume an infinite sequence of moves existed. $k_t$ nonincreasing integer bounded below by $1$, so eventually constant: $\exists T$ with $k_t=k$ for all $t\ge T$.
If $k=1$, no two $>1$ entries exist, process would have stopped at $T$, contrary to infinitude.
Thus $k\ge2$ for $t\ge T$.

For $t\ge T$, $k_{t+1}=k_t$, so every move after $T$ is of the third type:
$m\neq n$, $g>1$, both replacements $>1$. Then by (4) $P_{t+1}=P_t/g<P_t$.
Thus $(P_t)_{t\ge T}$ is a strictly decreasing infinite sequence of positive integers, impossible.
Hence no infinite sequence exists; every choice sequence terminates after finitely many moves.

A terminal state means fewer than two entries $>1$. Since $k_t\ge1$ always, termination implies $k_t=1$. So exactly one integer $M>1$ remains, the other $N-1$ entries are $1$. This proves (a).

### 4. Invariant — (b).

Fix prime $p$. Let $a^{(t)}_i=v_p(x^{(t)}_i)\ge0$. Define
\[G^{(t)}_p=\gcd(a^{(t)}_1,\dots ,a^{(t)}_N),\]
with $\gcd(0,\dots,0)=0$.

Claim: $G^{(t)}_p$ is invariant.

Indeed (3) replaces $a_i,a_j$ by $a'_i=\min(a_i,a_j)$, $a'_j=|a_i-a_j|$.
For any $a,b\ge0$,
\[\gcd(a,b)=\gcd(\min(a,b),|a-b|),\]
since if $a\le b$, $\gcd(a,b)=\gcd(a,b-a)$ ($=\gcd(a,0)=a$ if $a=b$ or $b=0$), symmetrically.
Let $R$ be the other $N-2$ numbers. Then
\[\gcd(\text{all before})=\gcd(\gcd(a_i,a_j),R)=\gcd(\gcd(a'_i,a'_j),R)=\gcd(\text{all after}).\]
Thus $G^{(t+1)}_p=G^{(t)}_p$.

Let $G_p=G^{(0)}_p$ be initial.

Consider final state after termination: $y_k=M>1$ at some position $k$, $y_i=1$ for $i\neq k$.
Then $a^{(\text{final})}_i=0$ for $i\neq k$ and $a^{(\text{final})}_k=v_p(M)$. Hence
\[G^{(\text{final})}_p=\gcd(0,\dots,0,v_p(M),0,\dots,0)=v_p(M)\]
(with $v_p(M)=0$ allowed, giving $0$). By invariance,
\begin{equation}\tag{5}
v_p(M)=G_p=\gcd_{1\le i\le N} v_p(x^{(0)}_i)\quad\text{for every prime }p.
\end{equation}

Hence
\[M=\prod_{p} p^{\,\gcd_i v_p(x^{(0)}_i)},\]
where product over primes dividing some initial number (finite). This depends only on initial multiset, not on choices.

In particular existence of such $M>1$: if $p\mid x^{(0)}_{i_0}$ with $v_p>0$, then $\gcd_i v_p$ equals $\gcd$ of a collection containing $0$'s and a positive number, so it is $\gcd$ of the positive part, $\ge1$; indeed $\gcd(a,0)=a$. So any prime occurring in initial data contributes exponent $\ge1$; since at least one initial number $>1$ has a prime factor, the product above is $>1$, consistent with (a). The final $M>1$ is thus uniquely determined.

Therefore the value $M$ reached when the process stops does not depend on the sequence of choices of Confucius. This proves (b). $\blacksquare$
