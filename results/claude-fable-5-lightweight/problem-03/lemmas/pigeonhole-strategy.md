# Lemma (upper bound): Xiang Yu forces D ≤ u against any configuration

Pieces q_1,...,q_m > 0 (m ≤ n+1), Σ = 1, Y has ≤ n cuts. Then Y can cut so that the
final multiset A has D(A) ≤ u = 1/(2^{n+1}−1).

**Proof.**
- m ≤ n: halve every piece: A = equal pairs, D = 0.
- m = n+1: the 2^m subset sums lie in [0,1]; sorted, their 2^m − 1 consecutive gaps
  sum to 1, so some gap ≤ 1/(2^m−1) = u: sets S ≠ S′ with 0 ≤ σ(S′) − σ(S) ≤ u.
  A* = S′\S, B* = S\S′ disjoint, not both empty, Δ = σ(A*) − σ(B*) ∈ [0,u]; A* ≠ ∅.
  - If B* = ∅: halve the m − |A*| ≤ n pieces outside A*; final = pairs ⊎ {q_i : i∈A*};
    D = D(A*-pieces) ≤ σ(A*) = Δ ≤ u.
  - Else: concatenate A*-pieces as [0, σA) with partial sums α_0=0<...<α_p=σA;
    B*-pieces as [0, σB), partial sums β_0=0<...<β_q=σB = σA − Δ. Marks:
    (i) midpoint of each piece outside A*∪B* (m−p−q marks);
    (ii) in the A*-row: all points of {β_1,...,β_q} ∩ (0, σA) not equal to some α_k
        (≤ q marks);
    (iii) in the B*-row: all points of {α_1,...,α_{p−1}} ∩ (0, σB) not equal to some
        β_k (≤ p−1 marks).
    Total ≤ (m−p−q) + q + (p−1) = m−1 = n. All marks interior to pieces, distinct.
    Let Γ = sorted distinct values of ({α_k} ∪ {β_k}) ∩ [0, σB]. Both rows' cut grids
    restricted to [0, σB] equal Γ, so each interval of Γ contributes one equal pair
    (one part from each row). No A*-part straddles σB. Leftover: A*-parts filling
    [σB, σA), total Δ. Final A = (equal pairs) ⊎ leftover, so
    D(A) = D(leftover) ≤ Δ ≤ u. ∎

Consequence with the picking lemma: Y also plays greedily in the claiming phase and
secures (1 − D)/2 ≥ (1 − u)/2, capping Liu Bang at (1 + u)/2 = 2^n/(2^{n+1} − 1).

Verified with exact rationals on 4000 random configurations (code/verify_lemmaD.py):
cut count ≤ n and D ≤ u always.
