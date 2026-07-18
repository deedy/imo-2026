# imo-2026-01 — tracking file

## Status
solved

## Problem
There are $2026$ integers greater than $1$ written on a blackboard, not necessarily different. In a move, Confucius chooses two integers $m>1$ and $n>1$ from different places on the blackboard and replaces these two integers with $\gcd(m,n)$ and $\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. He continues to make moves while it is possible to do so. (a) Prove that, regardless of the choices of Confucius, after finitely many moves, exactly one integer $M$ on the blackboard is greater than $1$. (b) Prove that the value of $M$ does not depend on the choices of Confucius.

## Approaches tried
- **Lexicographic potential (product, #ones) + prime-wise gcd-of-valuations invariant** — successful; this is the proof below. See `approaches/invariant-valuations.md`.
- **Prime-wise reduction to a subtractive Euclidean game on exponents** — equivalent viewpoint, useful for discovering the invariant; see `approaches/prime-wise-euclidean.md`.
- **Dead ends** (recorded in `approaches/dead-ends.md`): the sum of the entries is *not* monotone (e.g. $(6,10)\mapsto(2,15)$, $16\to17$); the ordinary gcd of all entries is *not* the answer (e.g. $(4,6)\mapsto\dots\mapsto M=6\neq 2$); an associative "star product" reformulation and induction on $N$ were considered but not needed.

## Current best
Complete solution. (a) Every play terminates: with $P$ = product of all entries and $z$ = number of entries equal to $1$, a move with $g=\gcd(m,n)$ sends $P\mapsto P/g$; if $g\ge2$ the product at least halves, if $g=1$ the product is kept but $z$ increases by $1$ (and $z$ never decreases), so there are at most $\lfloor\log_2 P_0\rfloor + 2026$ moves. Moreover no move can produce two $1$'s, so some entry $>1$ always survives, and the terminal position has **exactly one** entry $M>1$. (b) For every prime $p$ the quantity $G_p=\gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big)$ is invariant, since a move changes the pair of valuations by $(\alpha,\beta)\mapsto(\min(\alpha,\beta),|\alpha-\beta|)$, which preserves gcd's. In the terminal position $G_p=v_p(M)$, whence the explicit choice-independent answer
$$M=\prod_{p\ \text{prime}} p^{\gcd\big(v_p(a_1),\ldots,v_p(a_{2026})\big)}$$
(the greatest common *exponential* divisor of the initial numbers). Verified exhaustively by computer for all small boards (`code/verify.py`).

## Full proof

Let $N = 2026$ and let $a_1,\dots,a_N$ denote the integers on the board (so initially
$a_i \ge 2$). A *move* chooses indices $i \ne j$ with $a_i, a_j > 1$ and replaces the pair
$(a_i, a_j) = (m,n)$ by
$$g = \gcd(m,n) \qquad\text{and}\qquad \ell = \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.$$
Both $g$ and $\ell$ are positive integers, because $g \mid \operatorname{lcm}(m,n)$. Note also
$$g\cdot \ell \;=\; \operatorname{lcm}(m,n) \;=\; \frac{mn}{g}. \tag{1}$$

### Part (a): the process terminates with exactly one integer greater than $1$

**Step 1: every sequence of moves is finite.**
Let $P = a_1 a_2 \cdots a_N \in \mathbb{Z}_{>0}$ be the product of all entries and let
$z = \#\{i : a_i = 1\}$. Consider a move on $(m,n)$ and put $g = \gcd(m,n)$.

*Effect on $P$.* By (1), the product of the two affected entries changes from $mn$ to
$mn/g$; all other entries are unchanged. Hence $P$ becomes $P/g$.

*Monotonicity of $z$.* A move never destroys an entry equal to $1$: only entries $>1$ may be
chosen, so the two replaced entries exceed $1$, and the two new entries are $\ge 1$. Hence
$z$ is non-decreasing throughout the process; also $0 \le z \le N$.

*Type A: $g \ge 2$.* Then $P$ is multiplied by $1/g \le \tfrac12$.

*Type B: $g = 1$.* Then $\ell = mn \ge 2\cdot 2 = 4 > 1$, so the pair $(m,n)$ is replaced by
$(1, mn)$: the product $P$ is unchanged and $z$ increases by exactly $1$.

Now bound the number of moves of each type. Since $z$ is non-decreasing, takes values in
$\{0,1,\dots,N\}$, and increases by $1$ at every type B move, the whole play contains **at
most $N$ type B moves**. Since $P$ is always a positive integer and each type A move at
least halves it, if the play contained $t$ type A moves then
$1 \le P_{\mathrm{final}} \le P_0 / 2^{t}$, so $t \le \lfloor \log_2 P_0 \rfloor$, where
$P_0$ is the initial product. Therefore every play has at most
$\lfloor \log_2 P_0 \rfloor + N$ moves; in particular every play is finite, regardless of
Confucius's choices. $\blacksquare$

**Step 2: at least one entry greater than $1$ always remains.**
We prove by induction on the number of moves that after any number of moves, some entry
exceeds $1$. This holds initially since all $N$ entries exceed $1$. Suppose it holds before
a move on $(m,n)$. If $g = \gcd(m,n) \ge 2$, then the new entry $g$ itself exceeds $1$. If
$g = 1$, then the new entry $\ell = mn \ge 4$ exceeds $1$. All entries not involved in the
move are unchanged, so after the move some entry still exceeds $1$. $\blacksquare$

**Conclusion of (a).** Confucius continues while a move is possible, i.e. while there are
two entries $>1$ at different places. By Step 1 he stops after finitely many moves; in the
final position **at most one** entry exceeds $1$, and by Step 2 **at least one** entry
exceeds $1$. Hence exactly one entry $M > 1$ remains, and the other $N-1$ entries all
equal $1$. $\blacksquare$

### Part (b): the final value $M$ is independent of the choices

For a prime $p$ and an integer $x \ge 1$, write $v_p(x)$ for the exponent of $p$ in the
factorisation of $x$ (so $v_p(1) = 0$). For each prime $p$ define
$$G_p \;=\; \gcd\big(v_p(a_1),\, v_p(a_2),\, \dots,\, v_p(a_N)\big) \;\in\; \mathbb{Z}_{\ge 0},$$
the greatest common divisor of a tuple of nonnegative integers, with the convention
$\gcd(0,\dots,0) = 0$.

**Step 3: $G_p$ is invariant under moves.**
A move changes only two of the $N$ entries, hence only two of the $N$ valuations, namely
$$\alpha = v_p(m), \quad \beta = v_p(n)
\;\longrightarrow\;
\alpha' = v_p(g) = \min(\alpha,\beta), \quad
\beta' = v_p(\ell) = \max(\alpha,\beta) - \min(\alpha,\beta) = |\alpha - \beta|.$$
*Claim:* for every positive integer $t$,
$$t \mid \alpha \ \text{and}\ t \mid \beta
\quad\Longleftrightarrow\quad
t \mid \alpha' \ \text{and}\ t \mid \beta'.$$
Indeed, we may assume $\alpha \le \beta$, so $\alpha' = \alpha$ and $\beta' = \beta - \alpha$.
If $t \mid \alpha$ and $t \mid \beta$, then $t \mid \beta - \alpha$. Conversely, if
$t \mid \alpha$ and $t \mid \beta - \alpha$, then $t \mid \alpha + (\beta - \alpha) = \beta$.
This proves the claim.

Consequently the set of positive common divisors of the whole $N$-tuple of valuations is
unchanged by the move. If the tuple is not identically zero, its gcd is the largest element
of this set, hence unchanged. If the tuple is identically zero, then in particular
$\alpha = \beta = 0$, so $\alpha' = \beta' = 0$ and the tuple remains identically zero; the
gcd equals $0$ before and after. In all cases $G_p$ is invariant. $\blacksquare$

**Step 4: computing $M$.**
By part (a), every play ends in the position $(1, 1, \dots, 1, M)$ (up to the order of the
places). In this position the tuple of $p$-adic valuations is $(0, \dots, 0, v_p(M))$, whose
greatest common divisor equals $v_p(M)$, since $\gcd(x, 0) = x$. By the invariance of Step 3
applied to the initial numbers $a_1, \dots, a_N$,
$$v_p(M) \;=\; \gcd\big(v_p(a_1),\, v_p(a_2),\, \dots,\, v_p(a_N)\big)
\qquad\text{for every prime } p.$$
A positive integer is uniquely determined by its exponents $v_p(\cdot)$, and only primes
dividing some initial $a_i$ contribute; hence
$$\boxed{\,M \;=\; \prod_{p\ \mathrm{prime}} p^{\,\gcd\big(v_p(a_1),\, v_p(a_2),\, \dots,\, v_p(a_N)\big)}\,}$$
which depends only on the initial integers, not on Confucius's choices. $\blacksquare$

**Remarks (consistency checks).**
- If all initial numbers are equal to $c$, then $M = c$: each move is $(c,c)\mapsto(c,1)$.
- If the initial numbers are pairwise coprime, each valuation tuple contains at most one
  nonzero entry, and $\gcd(0,\dots,0,e) = e$, so $M = a_1 a_2 \cdots a_N$: coprime moves
  $(m,n)\mapsto(1,mn)$ merely merge everything into one product.
- For two initial numbers $(x,y)$ one gets $M = \prod_p p^{\gcd(v_p(x),v_p(y))}$; e.g.
  $(4,6)\mapsto(2,6)\mapsto(2,3)\mapsto(1,6)$ gives $M = 6 = 2^{\gcd(2,1)} 3^{\gcd(0,1)}$.
- In the language of exponential divisibility, $M$ is the greatest common exponential
  divisor of the initial numbers: the unique maximal $d$ with $v_p(d) \mid v_p(a_i)$ for
  all $p$ and all $i$.

*Computer verification* (`code/verify.py`): exhaustive search over all plays for all
multisets of lengths $2$–$6$ with small values confirms that every play ends with exactly
one entry $>1$ and that the terminal value coincides with the boxed formula; 500 random
playouts with $N \le 12$ and 2000 single-move invariant checks confirm the same. All tests
passed.
