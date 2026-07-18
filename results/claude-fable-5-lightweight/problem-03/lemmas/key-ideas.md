# Key proof ideas (to be validated & written up)

Notation: after all cuts, final pieces sorted a_1 >= a_2 >= ... >= a_M.
D = a_1 - a_2 + a_3 - ... (alternating sum). LB's optimal-play value = (1+D)/2.
u = 1/(2^{n+1}-1). Geometric config: b_i = 2^{n+1-i} u, i=1..n+1.

## Lemma A (picking game value)
Value to first player = odd-rank sum O(A); second player can guarantee even-rank
sum E(A). Both by greedy + exchange induction. So LB's value = O = (1+D)/2.

## Lemma C (lower bound: refinement of geometric with <= n cuts has D >= u)
TREE-PAIRING ARGUMENT:
- Pair consecutive sorted parts (a_1,a_2), (a_3,a_4), ...; slacks eps_i sum
  (plus lone a_M if M odd) to exactly D.
- Build multigraph: vertices = the n+1 original pieces; each pair = edge between
  the origin pieces of its two parts (loop if same piece).
- M <= 2n+1 so #edges <= n < n+1 = #vertices => some connected component T is a
  tree (no loops, no cycles).
- 2-color T (bipartition s_j = ±1). Consider Xi = sum_{j in T} s_j * (size of
  piece j). Every part of a T-piece lies in a cross pair inside T (edge) or is
  the lone a_M. Each edge contributes ±(difference) = ±eps; so |Xi| <= D.
- But Xi = u * (± sum of DISTINCT powers of 2, nonempty) => |Xi| >= u.
  Hence D >= u.

## Lemma D (upper bound: vs ANY config of m <= n+1 pieces, XY forces D <= u)
- If m <= n: halve every piece (m cuts <= n): all parts in equal pairs, D = 0.
- If m = n+1: subset-sum pigeonhole: the 2^{n+1} subset sums of the pieces lie
  in [0,1]; two consecutive sorted sums differ by <= 1/(2^{n+1}-1) = u. Take
  S != S', let A = S\S', B = S'\S (disjoint), wlog Delta = sigma(A)-sigma(B) in [0,u].
- If B = empty (A nonempty): halve all m-|A| pieces not in A (uses <= m-1 = n cuts),
  leave A uncut. Final: equal pairs + A; D = D(A) <= sigma(A) = Delta <= u.
- If A,B nonempty: lay A's pieces along [0,sigma(A)), B's along [0,sigma(B)).
  Cut A-pieces at all B-boundaries in (0,sigma(B)) and at sigma(B); cut B-pieces at
  all A-boundaries in (0,sigma(B)). Common-refinement intervals of [0,sigma(B))
  appear once on each side: equal pairs. Leftover: A-material in (sigma(B),sigma(A)),
  total Delta (possibly several parts). Halve all other pieces.
  Cuts: <= (q-1)+1 on A-side + (p-1) on B-side + (m-p-q) halvings = m-1 = n. OK.
  Final D = D(leftovers) <= Delta <= u.
- Pairs-cancel lemma: D(X ⊎ {y,y}) = D(X). So D(final) <= Delta <= u.
- Then LB's value = (1+D)/2 <= (1+u)/2 = 2^n/(2^{n+1}-1).

## Auxiliary facts
- (1+u)/2 = 2^n/(2^{n+1}-1).
- D(multiset) <= sum(multiset); D >= 0.
- Pigeonhole gap bound: 2^m reals in [0,1] have two within 1/(2^m-1)... (2^m
  values => 2^m - 1 consecutive gaps summing to <= 1). Need 2^{n+1}-1 gaps: ok
  with m = n+1: 2^{n+1} sums, gaps 2^{n+1}-1, min gap <= u. ✔
