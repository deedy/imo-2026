# Lemma: equal pairs cancel in the alternating sum

For a finite multiset X of nonnegative reals let D(X) = Σ (−1)^{i−1} x_i over the
(unique) non-increasing value sequence x_1 ≥ x_2 ≥ ....

**Claim.** D(X ⊎ {y,y}) = D(X) for any y ≥ 0.

**Proof.** Let p = #{i : x_i ≥ y}. The sorted sequence of X ⊎ {y,y} is
x_1,...,x_p, y, y, x_{p+1},...,x_r. Alternating sum:
Σ_{i≤p} (−1)^{i−1}x_i + (−1)^p y + (−1)^{p+1} y + Σ_{i>p} (−1)^{(i+2)−1} x_i = D(X). ∎

**Corollary.** If a multiset is a disjoint union of equal pairs and a sub-multiset L,
its alternating sum equals D(L), and 0 ≤ D(L) ≤ Σ(L).

(0 ≤ D and D ≤ Σ follow from grouping consecutive terms.)
