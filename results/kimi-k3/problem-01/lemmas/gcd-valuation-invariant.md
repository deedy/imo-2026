# Lemma: invariance of the gcd of the $p$-adic valuations

**Statement.** Let $a_1,\dots,a_N$ be the entries on the board ($N \ge 2$). For every prime
$p$ define
$$G_p \;=\; \gcd\big(v_p(a_1),\,v_p(a_2),\,\dots,\,v_p(a_N)\big) \;\in\; \mathbb{Z}_{\ge 0},$$
where $v_p(x)$ is the exponent of $p$ in $x$ (with $v_p(1) = 0$) and we use the convention
$\gcd(0,\dots,0) = 0$. Then $G_p$ does not change under any legal move.

**Proof.** A move replaces two entries $m, n > 1$ by $g = \gcd(m,n)$ and
$\ell = \operatorname{lcm}(m,n)/g$, and leaves all other entries fixed. So among the $N$
numbers $v_p(a_1), \dots, v_p(a_N)$ only two change, namely
$$\alpha = v_p(m), \quad \beta = v_p(n) \quad\longrightarrow\quad
\alpha' = v_p(g) = \min(\alpha,\beta), \quad
\beta' = v_p(\ell) = \max(\alpha,\beta) - \min(\alpha,\beta) = |\alpha - \beta|.$$

**Claim.** For every positive integer $t$:
$$t \mid \alpha \ \text{and}\ t \mid \beta
\quad\Longleftrightarrow\quad
t \mid \alpha' \ \text{and}\ t \mid \beta'.$$

*Proof of claim.* We may assume $\alpha \le \beta$, so $\alpha' = \alpha$ and
$\beta' = \beta - \alpha$.
($\Rightarrow$) If $t \mid \alpha$ and $t \mid \beta$ then $t \mid \beta - \alpha = \beta'$.
($\Leftarrow$) If $t \mid \alpha' = \alpha$ and $t \mid \beta' = \beta - \alpha$ then
$t \mid \alpha + (\beta - \alpha) = \beta$. $\square$

Hence the set of positive common divisors of the whole $N$-tuple of valuations is unchanged
by the move. If the $N$-tuple is not the all-zero tuple, its gcd is the largest element of
this set, so it is unchanged; if it is the all-zero tuple, then in particular
$\alpha = \beta = 0$, whence $\alpha' = \beta' = 0$ and the tuple stays all-zero, and the gcd
equals $0$ before and after. In all cases $G_p$ is invariant. $\blacksquare$

**Corollary (value of the final number).** If the process ends at $(1,\dots,1,M)$, then the
valuation tuple at $p$ is $(0,\dots,0,v_p(M))$ with gcd $v_p(M)$ (as $\gcd(x,0) = x$).
Invariance gives, with the $a_i$ denoting the **initial** numbers,
$$v_p(M) = \gcd\big(v_p(a_1),\dots,v_p(a_N)\big)\quad\text{for every prime } p,
\qquad\text{i.e.}\qquad
M = \prod_{p\ \mathrm{prime}} p^{\gcd(v_p(a_1),\dots,v_p(a_N))}.$$
The product is finite: only primes dividing some initial $a_i$ contribute a nontrivial factor.
