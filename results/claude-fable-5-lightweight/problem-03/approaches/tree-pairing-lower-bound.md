# Approach: tree-pairing / signed subset sums (lower bound) — SUCCESSFUL

Goal: any refinement of the geometric config (2^n,...,2,1)u with ≤ n cuts has
alternating sum D ≥ u.

Mechanism:
- D = Σ (a_{2i-1} - a_{2i}) + [M odd]·a_M over consecutive sorted pairs; so if D is
  small, the sorted parts form near-equal consecutive pairs with small total slack.
- Each pair gives an edge between the two original pieces containing its parts
  (multigraph on the n+1 pieces; loops allowed). #edges = ⌊M/2⌋ ≤ n < n+1 = #vertices,
  so some connected component is a simple tree T.
- 2-color T; the signed sum Ξ = Σ_{j∈T} ±(piece_j length) then satisfies
  |Ξ| ≤ Σ slacks + [M odd]a_M ≤ D (each cross pair contributes ±(difference)),
  because parts of T-pieces only pair inside T (component) and never with the same
  piece (no loops).
- For geometric pieces, Ξ/u is a ±-signed sum of distinct powers of 2 over a nonempty
  set — a nonzero integer — so |Ξ| ≥ u. Hence D ≥ u.

Key discovery that led to this: attempting a "perfect pairing" impossibility proof:
if all parts paired exactly, a tree component would give a vanishing signed sum of
distinct powers of 2 — impossible. The quantitative version replaces "vanishing"
with "≤ D".

This argument in fact shows: for ANY configuration q_1..q_m whose nonzero signed
subset sums are all ≥ δ in absolute value, every refinement with ≤ m-1 cuts has
D ≥ δ. Pigeonhole (see upper bound) shows δ ≤ s/(2^m -1) always, so geometric is optimal.
