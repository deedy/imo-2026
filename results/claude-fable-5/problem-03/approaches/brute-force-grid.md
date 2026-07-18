# Approach: exhaustive grid search (code/brute.c)

**Idea.** Reduce the game to: L picks piece multiset (≤ n+1 positive lengths, sum 1),
Y refines with ≤ n cuts, payoff to L is (1+D)/2 with D = alternating sum of sorted
final parts. Discretize to integers summing to N; enumerate all L configs (allowing
zero parts to emulate fewer marks) and all Y refinements (allowing zero parts to
emulate unused cuts / limit positions); compute max over L of min over Y of D.

**Status: successful (as evidence).** Results:
- n=1, N=12: max-min D = 4/12 = 1/3 → V = 2/3; optimizers include (8,4).
- n=2, N=42: 6/42 = 1/7 → V = 4/7; optimizers include geometric (24,12,6); tie polytope.
- n=3, N=30: 2/30 = 1/15 → V = 8/15; N=45: 3/45 = 1/15.
- n=4, N=62: 2/62 = 1/31 → V = 16/31.
- n=5, N=126, single config (64,32,16,8,4,2): min D = 2/126 = 1/63 → V = 32/63.

All consistent with c = 2^n/(2^{n+1}-1), achieved by geometric config
(2^n, ..., 2, 1)·u, u = 1/(2^{n+1}-1).

Caveat: grid search cannot by itself certify the real-valued optimum; used only to
locate the answer. Rigorous proofs are Lemmas 4 and 5 in current.md; additionally
Monte Carlo over real-valued refinements (verify_lemmaC.py) and exact rational
verification of Y's constructive strategy (verify_lemmaD.py) passed.
