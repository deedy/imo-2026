# Scratch notes (chronological)

- Examples: a1=2 -> evens; a1=15 -> {15,18,20,24,30,36,40,42,45,48,50,54,60,...} = numbers hitting each of {2,3},{2,5},{3,5}; period 30, 8 residues {0,6,10,12,15,18,20,24}.
- Gcd condition is symmetric across the whole sequence => S pairwise non-coprime; greedy minimality => completeness: S = all m>=a1 compatible with S.
- Membership predicate = "P(m) is a transversal of {P(s)}" = "P(m) contains a minimal transversal (member)". So S = [a1,oo) ∩ ⋃_Q d_Q Z. Crux: #members finite.
- Members pairwise intersect (realize supersets Q∪{fresh prime} as elements of S).
- Self-blocking clutter axioms (b(M)=M) are NOT enough: infinite example U_k(u)={u_1..u_k,x_{k+1},y_{k+1}}. So greediness needed quantitatively.
- Greedy => downward witness (Lemma 3) => cheap witness: for member Q, t∈Q, exists member Q' with Q'∩Q={t}, d_{Q'} < a1·d_Q/t. KEY: test integer m = π(Q\{t})^e, least power > a1, so m ≤ a1·π(Q\{t}); its witness s < m carries a member disjoint from Q\{t}.
- Descent at a prime q > a1: products of members containing q shrink by factor a1/q < 1 each step but stay ≥ q. Contradiction. Singleton-member case separate (then M={{p}}, p|a1).
- Hence all member primes ≤ a1, M finite, S = finite union of APs from a1 onwards exactly; take L = primorial(a1), T = #good residues. Periodicity holds from n=1 because the AP description is exact from a1 (no eventual qualifier needed).
- Numerics (code/verify.py): all 2..60 plus 77,91,101,105,121,125,143,169,255,385,663,1001,1155 pass all checks (member primes ≤ a1, membership formula, pairwise intersection, periodicity from n=1). Interesting blockers: a1=385: {2,7},{2,3,5},{2,3,11},{2,11,19},{3,7,11},{3,7,19},{5,7,11} (prime 19 ≤ 385 appears); a1=143: {2,11},{3,11},{11,13},{2,3,13}.
