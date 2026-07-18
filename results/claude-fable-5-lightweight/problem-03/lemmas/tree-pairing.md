# Lemma (lower bound): refinements of the geometric configuration

u = 1/(2^{n+1}−1); pieces q_j = 2^j u (j = 0..n). Suppose the pieces are refined by
K ≤ n cuts into M = n+1+K parts. Then the alternating sum D of the parts is ≥ u.

**Proof.**
1. Fix a non-increasing enumeration a_1 ≥ ... ≥ a_M of the parts (physical objects).
   Pair P_i = {a_{2i−1}, a_{2i}}, slack ε_i = a_{2i−1} − a_{2i} ≥ 0; if M is odd a_M
   is unpaired. Then D = Σ ε_i + [M odd] a_M.
2. Multigraph G: vertices = the n+1 original pieces; each pair P_i is an edge joining
   the pieces containing its two parts (loop if equal). |E| = ⌊M/2⌋ ≤ n < n+1 = |V|.
3. A connected multigraph on v vertices has ≥ v−1 edges, equality only for a simple
   tree. If every component had a cycle/loop then |E| ≥ |V| — contradiction. So some
   component T is a simple tree (possibly one vertex).
4. Properly 2-color T with signs s(j) = ±1. Let Ξ = Σ_{j∈T} s(j) 2^j u. Since T ≠ ∅
   and the exponents are distinct, Ξ/u is a nonzero integer: |Ξ| ≥ u
   (top power exceeds the sum of all smaller ones).
5. Expand Ξ over parts. Every part inside a T-piece is either the lone a_M or lies in
   a pair which is an edge of T (components absorb incident edges; no loops in T means
   the two parts of such a pair lie in DISTINCT T-pieces, which carry opposite signs).
   Each edge of T therefore contributes ±ε_i to Ξ; the lone part contributes ±a_M
   (if its piece is in T). Hence |Ξ| ≤ Σ_{E_T} ε_i + [M odd] a_M ≤ D.
6. Combining: D ≥ |Ξ| ≥ u. ∎

Remark: the only property of the lengths used is: every nonempty ±1-signed subset sum
of the piece lengths has absolute value ≥ u. For 2^j u this holds by binary rigidity.

Monte Carlo verification: code/verify_lemmaC.py (n ≤ 7, 40000 random refinements each,
including snapped/structured cut positions): min D found = u exactly for n ≤ 4 and
> u for larger n (random search weaker there), never below u.
