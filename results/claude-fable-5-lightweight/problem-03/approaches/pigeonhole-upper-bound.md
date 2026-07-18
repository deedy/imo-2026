# Approach: subset-sum pigeonhole + cross-pairing (upper bound) — SUCCESSFUL

Goal: whatever ≤ n+1 pieces L creates, Y forces D ≤ u = 1/(2^{n+1}-1) with ≤ n cuts.

- If L made m ≤ n pieces: halve each (m cuts): all parts in equal pairs ⇒ D = 0.
- If m = n+1: the 2^m subset sums lie in [0,1]; 2^m - 1 consecutive gaps sum to 1,
  so two subsets S ≠ S′ have |σ(S′) − σ(S)| ≤ 1/(2^m −1) = u. Set A = S′\S, B = S\S′
  (disjoint, not both empty), Δ = σ(A) − σ(B) ∈ [0,u] (wlog).
- B = ∅: halve all pieces outside A (≤ m−1 = n cuts); final = pairs ⊎ A-pieces;
  D = D(A-pieces) ≤ σ(A) = Δ ≤ u.
- A,B ≠ ∅: concatenate A-pieces as [0,σA), B-pieces as [0,σB). Cut the A-row at all
  B-boundaries and at σB (when interior and not already boundaries), the B-row at all
  A-boundaries (when interior, < σB). Then the common-refinement intervals of [0,σB)
  occur once on each row: equal pairs; leftover = A-material in [σB, σA), total Δ.
  Halve all remaining pieces. Cut count ≤ q + (p−1) + (m−p−q) = m−1 = n.
  Final D = D(leftover) ≤ Δ ≤ u (pairs cancel).

Verified with exact rational arithmetic on 4000 random configs (verify_lemmaD.py):
cut counts ≤ n, D ≤ u always.
