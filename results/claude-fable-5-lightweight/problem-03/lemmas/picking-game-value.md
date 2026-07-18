# Lemma: value of the alternating picking game

Let A be a finite multiset of nonnegative reals, sorted a_1 ≥ a_2 ≥ ... ≥ a_M.
O(A) = Σ_{i odd} a_i, E(A) = Σ_{i even} a_i.

**Claim.**
(1) The player to move first can guarantee ≥ O(A) against arbitrary opposition.
(2) The player moving second can guarantee ≥ E(A) against arbitrary opposition.
Hence with total 1, the first player's securable amount is exactly O(A) = (1+D)/2,
D = O − E the alternating sum.

**Proof.**
Two removal inequalities (index computations on the sorted list):

(2.1) For j ≥ 2: O(A∖{a_1,a_j}) − (O(A) − a_1)
      = (a_2−a_3)+(a_4−a_5)+... (ending at (a_{j−2}−a_{j−1}) if j even,
        at (a_{j−1}−a_j) if j odd) ≥ 0.
   [After removing a_1, a_j: rank of a_i is i−1 for i<j and i−2 for i>j, so
    O(A∖{a_1,a_j}) = Σ_{2≤i≤j−1 even} a_i + Σ_{i>j odd} a_i.]

(2.2) For any j: O(A∖{a_j}) − E(A)
      = (a_1−a_2)+(a_3−a_4)+... (ending at (a_{j−2}−a_{j−1}) if j odd,
        at (a_{j−1}−a_j) if j even) ≥ 0.
   [Rank of a_i is i for i<j, i−1 for i>j, so
    O(A∖{a_j}) = Σ_{i<j odd} a_i + Σ_{i>j even} a_i.]

(1) Greedy ("always take a largest remaining"), strong induction on |B| for the
statement "if it is your move at multiset B, greedy nets ≥ O(B)": take b_1; if the
opponent then takes b_j, induction on C = B∖{b_1,b_j} gives ≥ O(C) ≥ O(B) − b_1 by
(2.1); total ≥ O(B). Bases |B| ≤ 1 trivial.

(2) After the opponent's first move a_j, apply (1) to A∖{a_j}: get ≥ O(A∖{a_j})
≥ E(A) by (2.2). ∎

Verified by exhaustive minimax on 300 random multisets (code/verify_lemmaA.py).
