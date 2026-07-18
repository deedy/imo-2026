# imo-2026-01 — tracking file

## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- **Per-prime exponent dynamics + monovariant + gcd invariant** (see `approaches/potential-and-invariant.md`) — **successful, used in the final proof.** A move sends the exponent pair $(a,b)=(v_p(m),v_p(n))$ to $(\min(a,b),\max(a,b)-\min(a,b))$. Termination via the strictly decreasing potential $T+N$ ($T=\sum_i\Omega(x_i)$, $N=$ number of entries $>1$); part (b) via the invariance of $g_p=\gcd_i v_p(x_i)$ for each prime $p$.
- Computational verification (`code/check.py`): exhaustive BFS over the whole game tree for all multisets $\{a,b,c\}\subseteq[2,14]$, 300 random 4-tuples in $[2,30]$, 60 random 5-tuples in $[2,12]$. Confirmed: every terminal state has exactly one entry $>1$, the surviving value is identical across all terminal states, and it equals $\prod_p p^{\gcd_i v_p(a_i)}$; also verified $T+N$ strictly decreases along every edge. All checks passed.

## Current best
Complete proof of both parts. Explicit formula: if the initial numbers are $a_1,\dots,a_{2026}$, then the process always terminates and the unique surviving integer greater than $1$ is
$$M=\prod_{p\ \mathrm{prime}} p^{\,\gcd\left(v_p(a_1),\dots,v_p(a_{2026})\right)},$$
which depends only on the initial numbers — proving (b). Part (a) follows from the strictly decreasing potential $T+N$ (termination) plus the fact that each move outputs at least one integer $>1$ (so the count of entries $>1$ never drops below $1$).

## Full proof

Throughout, the **state** of the blackboard is the tuple $(x_1,\dots,x_{2026})$ of the written numbers. For a prime $p$ and a positive integer $x$, $v_p(x)$ denotes the exponent of $p$ in $x$, and $\Omega(x)=\sum_p v_p(x)$ is the number of prime factors of $x$ counted with multiplicity (so $\Omega(1)=0$, and $\Omega(x)\ge 1$ for $x>1$). We use the standard facts
$$v_p(\gcd(m,n))=\min(v_p(m),v_p(n)),\qquad v_p(\operatorname{lcm}(m,n))=\max(v_p(m),v_p(n)).$$

### Lemma 1 (effect of a move on exponents)
Let a move replace $m,n>1$ by $g=\gcd(m,n)$ and $h=\operatorname{lcm}(m,n)/\gcd(m,n)$. Then $g,h$ are positive integers, and for every prime $p$, writing $a=v_p(m)$, $b=v_p(n)$,
$$v_p(g)=\min(a,b),\qquad v_p(h)=\max(a,b)-\min(a,b).$$

*Proof.* For every prime $p$ we have $v_p(\gcd(m,n))=\min(a,b)\le\max(a,b)=v_p(\operatorname{lcm}(m,n))$; hence $\gcd(m,n)\mid\operatorname{lcm}(m,n)$, so $h$ is a positive integer and $v_p(h)=\max(a,b)-\min(a,b)$. $\blacksquare$

All other entries are unchanged by the move, and every entry always remains a positive integer.

### Lemma 2 (a move produces at least one entry $>1$)
With the notation of Lemma 1, $\max(g,h)>1$.

*Proof.* Suppose $h=1$. Then $\operatorname{lcm}(m,n)=\gcd(m,n)$. Since $\gcd(m,n)\mid m\mid \operatorname{lcm}(m,n)$, this forces $g=\gcd(m,n)=m=\operatorname{lcm}(m,n)$, and $m>1$, so $g>1$. Hence $h=1$ implies $g>1$; in all cases at least one of $g,h$ exceeds $1$. $\blacksquare$

### Lemma 3 (monovariant)
For a state $S=(x_1,\dots,x_{2026})$ define
$$T(S)=\sum_{i=1}^{2026}\Omega(x_i),\qquad N(S)=\#\{i:\ x_i>1\},\qquad \Phi(S)=T(S)+N(S).$$
Then every move strictly decreases $\Phi$, i.e. $\Phi(S')\le\Phi(S)-1$ for the state $S'$ after the move.

*Proof.* Let the move replace $m,n$ by $g,h$ as above. Fix a prime $p$ and let $a=v_p(m),b=v_p(n)$. By Lemma 1,
$$v_p(g)+v_p(h)=\min(a,b)+\big(\max(a,b)-\min(a,b)\big)=\max(a,b)=a+b-\min(a,b)=v_p(m)+v_p(n)-v_p(g).$$
Summing over all primes $p$ gives $\Omega(g)+\Omega(h)=\Omega(m)+\Omega(n)-\Omega(g)$, hence
$$T(S')=T(S)-\Omega(g).$$
For $N$: the two chosen positions contribute $2$ to $N(S)$ (both $m,n>1$) and at most $2$ to $N(S')$; all other positions are unchanged. Hence $N(S')\le N(S)$ always. We distinguish two cases.

*Case $g=1$.* Then $h=\operatorname{lcm}(m,n)=mn/\gcd(m,n)=mn>1$, so the two positions contribute exactly $1$ to $N(S')$, giving $N(S')=N(S)-1$; and $T(S')=T(S)-\Omega(1)=T(S)$. Thus $\Phi(S')=\Phi(S)-1$.

*Case $g>1$.* Then $\Omega(g)\ge1$, so $T(S')\le T(S)-1$, and $N(S')\le N(S)$. Thus $\Phi(S')\le\Phi(S)-1$.

In both cases $\Phi$ decreases by at least $1$. $\blacksquare$

### Part (a)

**Termination.** $\Phi$ is a nonnegative integer for every state (each $x_i\ge 1$), and by Lemma 3 it strictly decreases with every move. Hence at most $\Phi(S_0)$ moves can be made from the initial state $S_0$: after finitely many moves the process stops.

**The process stops exactly when $N\le 1$.** A move requires two entries $>1$ in different places, and any two entries $>1$ can be chosen; thus a move is possible if and only if $N\ge2$. So the final state satisfies $N\le 1$.

**$N\ge1$ at all times.** Initially $N=2026\ge1$. Consider any move, performed from a state with $N\ge 2$. The two chosen positions held two entries $>1$ and, by Lemma 2, hold at least one entry $>1$ afterwards; all other positions are unchanged. Hence $N$ decreases by at most $1$ per move, so after the move $N\ge 2-1=1$. By induction, $N\ge1$ in every state ever reached.

Combining: the process terminates after finitely many moves, and in the final state $1\le N\le1$, i.e. **exactly one integer on the blackboard is greater than $1$**. Call it $M$. This proves (a). $\blacksquare$

### Part (b)

For a state $S=(x_1,\dots,x_{2026})$ and a prime $p$ define
$$g_p(S)=\gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big)\in\mathbb{Z}_{\ge0},$$
with the standard conventions $\gcd(t,0)=t$ and $\gcd(0,0,\dots,0)=0$ (so $g_p(S)=0$ exactly when $p$ divides no entry).

### Lemma 4 (invariance of $g_p$)
For every prime $p$ and every move $S\to S'$ we have $g_p(S')=g_p(S)$.

*Proof.* First, for all integers $a,b\ge0$,
$$\gcd\big(\min(a,b),\ \max(a,b)-\min(a,b)\big)=\gcd(a,b).\tag{$\ast$}$$
Indeed, WLOG $a\le b$; an integer $d$ divides both $a$ and $b-a$ if and only if it divides both $a$ and $b$, so the pairs $(a,b-a)$ and $(a,b)$ have the same common divisors and hence the same gcd. (If $a=b=0$, both sides are $0$.)

Now let the move act on entries $m,n$ with $a=v_p(m)$, $b=v_p(n)$, and let $r$ denote the gcd of the values $v_p(x_i)$ over all the *other* $2024$ positions. By Lemma 1 and the associativity of gcd,
$$g_p(S')=\gcd\Big(r,\ \gcd\big(\min(a,b),\,\max(a,b)-\min(a,b)\big)\Big)\stackrel{(\ast)}{=}\gcd\big(r,\ \gcd(a,b)\big)=g_p(S). \qquad\blacksquare$$

**Conclusion of (b).** Let $S_0=(a_1,\dots,a_{2026})$ be the initial state and let $S_f$ be any final state reached by any sequence of choices. By part (a), $S_f$ consists of one integer $M>1$ and $2025$ ones. Hence for every prime $p$,
$$g_p(S_f)=\gcd\big(v_p(M),0,\dots,0\big)=v_p(M).$$
By Lemma 4, $g_p(S_f)=g_p(S_0)$ for every prime $p$. Therefore
$$v_p(M)=g_p(S_0)=\gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big)\qquad\text{for every prime }p,$$
and since only the finitely many primes dividing $a_1\cdots a_{2026}$ give a nonzero exponent,
$$M=\prod_{p\ \mathrm{prime}} p^{\,\gcd\left(v_p(a_1),\dots,v_p(a_{2026})\right)}.$$
This expression depends only on the initial numbers $a_1,\dots,a_{2026}$ and not on any of Confucius's choices. Hence the value of $M$ is the same for every legal sequence of moves. $\blacksquare$

*(Consistency check: since $a_1>1$, some prime $p$ satisfies $v_p(a_1)\ge1$, whence $g_p(S_0)\ge1$ and indeed $M>1$, matching part (a).)*
