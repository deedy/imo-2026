# Approach: lexicographic potential + gcd-of-valuations invariant (SUCCESSFUL)

**Idea.**
- (a) Track the product $P$ of all entries and the number $z$ of entries equal to $1$.
  A move with $g = \gcd(m,n)$ sends $P \mapsto P/g$; if $g \ge 2$ the product at least halves;
  if $g = 1$ the product is preserved but $z$ increases by $1$ (and $z$ never decreases).
  So $(P, N - z)$ decreases lexicographically $\Rightarrow$ termination.
  Separately, a move can never produce two $1$'s, so some entry $>1$ always survives;
  hence the terminal position has exactly one entry $M > 1$.
- (b) For each prime $p$, the move acts on the pair of valuations as
  $(\alpha,\beta) \mapsto (\min(\alpha,\beta), |\alpha-\beta|)$, and
  $\gcd(\min(\alpha,\beta), |\alpha-\beta|) = \gcd(\alpha,\beta)$; hence
  $G_p = \gcd_i v_p(a_i)$ is an invariant. In the terminal position $G_p = v_p(M)$, giving
  the explicit formula
  $$M = \prod_{p} p^{\gcd(v_p(a_1),\dots,v_p(a_N))},$$
  manifestly independent of the choices.

**Status.** Complete proof; written up in `current.md`, with standalone lemmas in
`lemmas/termination.md`, `lemmas/one-survives.md`, `lemmas/gcd-valuation-invariant.md`.

**Verification.** `code/verify.py`:
- exhaustive game-tree search for all multisets of lengths 2 (values 2..24), 3 (2..10),
  4 (2..6), 5 (2..4), 6 (2..3): every play ends with exactly one entry $>1$, the terminal
  value is unique and equals the formula;
- 500 random playouts with $N \le 12$, values $\le 200$: final $M$ matches the formula and
  the move bound $N + \lfloor\log_2 P_0\rfloor$ holds;
- 2000 single-move invariant checks: $G_p$ unchanged for every prime $p$.
All passed.
