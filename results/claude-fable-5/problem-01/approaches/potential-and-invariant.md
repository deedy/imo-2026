# Approach: monovariant for (a), per-prime gcd invariant for (b)

**Status: successful — this is the approach used in the final proof.**

## Idea

Work prime by prime. If $a=v_p(m)$, $b=v_p(n)$, a move sends the exponent pair $(a,b)$ to
$(\min(a,b),\,\max(a,b)-\min(a,b))$ — a subtractive-Euclid step.

### Part (a): termination + exactly one survivor
- Potential $\Phi = T + N$ where $T=\sum_i \Omega(x_i)$ ($\Omega$ = number of prime factors with
  multiplicity, $\Omega(1)=0$) and $N=\#\{i: x_i>1\}$.
- A move replaces $m,n$ by $g=\gcd$, $h=\operatorname{lcm}/\gcd$; since per prime
  $\min + (\max-\min) = \max \le a+b$ with deficit $\min$, we get
  $\Omega(g)+\Omega(h) = \Omega(m)+\Omega(n)-\Omega(g)$, so $T$ drops by $\Omega(g)$.
- $N$ never increases (2 inputs $>1$, at most 2 outputs $>1$); if $g=1$ then outputs are $1$ and $mn>1$,
  so $N$ drops by exactly $1$. Hence $\Phi$ drops by $\ge 1$ every move $\Rightarrow$ termination.
- At least one output is $>1$: $h=1 \Rightarrow \operatorname{lcm}=\gcd \Rightarrow m=n \Rightarrow g=m>1$.
  So $N$ drops by at most 1 per move; a move requires $N\ge2$, hence $N\ge1$ forever.
  Terminal $\iff N\le 1$; combined with $N \ge 1$: terminal $N=1$.

### Part (b): invariant
- For each prime $p$, the gcd $g_p$ of all the exponents $v_p(x_i)$ (convention: gcd of all zeros is 0)
  is invariant, because $\gcd(\min(a,b), \max(a,b)-\min(a,b)) = \gcd(a,b)$.
- Terminal state is $(M,1,\dots,1)$, so $v_p(M) = g_p(\text{terminal}) = g_p(\text{initial})$ for every $p$.
- Hence $M = \prod_p p^{\,g_p(\text{initial})}$, independent of all choices.

## Verification
`code/check.py`: exhaustive BFS over the full game tree for all triples in $[2,14]^3$,
300 random 4-tuples in $[2,30]$, 60 random 5-tuples in $[2,12]$. Every terminal state has exactly
one entry $>1$; the surviving value is the same at all terminals and equals the predicted formula.
The potential $T+N$ was verified to strictly decrease along every edge of the game graph.
All checks passed.
