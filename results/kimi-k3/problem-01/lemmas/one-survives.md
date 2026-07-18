# Lemma: at least one entry greater than $1$ always survives

**Statement.** Starting from $N \ge 2$ integers, all $>1$, after any number of legal moves at
least one entry on the board is still $> 1$.

**Proof.** Induction on the number of moves. Base case: initially all entries exceed $1$.
Inductive step: suppose the claim holds before a move on $(m,n)$ with $m,n > 1$. Write
$g = \gcd(m,n)$ and $\ell = \operatorname{lcm}(m,n)/g$ for the two new entries.

- If $g \ge 2$, then the new entry $g$ itself exceeds $1$.
- If $g = 1$, then $\ell = mn \ge 2\cdot 2 = 4 > 1$.

All entries not involved in the move are unchanged, so in either case some entry exceeds $1$
after the move. $\blacksquare$

**Corollary (terminal positions).** A position admits no legal move iff at most one entry
exceeds $1$. Combined with the lemma, in every terminal position **exactly one** entry $M$
exceeds $1$ (and the other $N-1$ entries equal $1$).
