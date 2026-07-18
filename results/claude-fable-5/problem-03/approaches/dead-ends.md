# Dead ends (recorded honestly)

1. **Parity-measure formula.** D = μ{t : #(parts > t) odd}; a cut of a piece of
   size a into (x, a−x) flips the parity set on (0,x) ∪ (a−x, a). Correct and
   pretty, but attempts to bound the n-fold flip effect (weight functions,
   per-cut caps) failed: a single cut can slash D by a lot, and weights cannot
   capture the requirement that pairs must first be "manufactured".

2. **Operation-recursion induction for the upper bound.** Sound Y-operations:
   (P) leave an equal pair; (A_i) halve piece i; (B_ij) cut a copy of b_j from
   b_i. Invariant: cuts = #pieces − 1. Naive induction with potential s/(2^m −1)
   breaks when b_1 < 2^{m−1}u and b_2 < 2^{m−2}u ("flat top"); worked for m ≤ 3
   by ad hoc case analysis but did not generalize cleanly. Superseded by the
   pigeonhole construction (which is also a single clean global argument).

3. **Integrality reduction for the lower bound.** Hoped: Y's optimal refinement
   of the integer geometric config can be taken with integer parts (then D odd
   integer ⇒ D ≥ 1 = u). False as a general principle: linearity-region vertices
   include e.g. halvings (denominator 2), so integrality is not automatic.

4. **δ-super-increasing induction.** Statement "q_i ≥ q_{i+1}+...+q_m + δ ∀i ⇒
   D ≥ δ under ≤ m−1 cuts" is true (it follows from the tree-pairing lemma,
   since signed sums are ≥ δ hmm—actually signed-sum bound needs more than
   super-increasing; the binary structure suffices) but direct induction on it
   failed because cutting the top piece leaves "junk" parts that interleave.

5. **Equal-split configuration for L.** Pieces 1/(n+1) each: Y halves one piece
   (if n+1 odd) or pairs them up, driving D → 0. Confirms L must use unequal,
   binary-like pieces.
