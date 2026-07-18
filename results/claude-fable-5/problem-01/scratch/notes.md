# Scratch notes imo-2026-01

Move: (m,n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)), allowed iff m,n>1.

Per prime p with exponents (a,b) = (v_p(m), v_p(n)):
  gcd gets min(a,b), lcm/gcd gets max(a,b)-min(a,b).

Key observations:
- Sum of exponents of p drops from a+b to max(a,b): total Omega decreases by Omega(gcd).
- gcd(min, max-min) = gcd(a,b): per-prime gcd of the whole exponent multiset is INVARIANT.
- Terminal: exactly one entry > 1 (call it M); then v_p(M) = gcd of initial exponents g_p.
- So M = prod_p p^{g_p}. That's (b).
- Termination: T + N strictly decreases where T = sum Omega(x_i), N = #entries > 1.
  * gcd=1 move: T unchanged, N drops by exactly 1 (outputs 1 and mn>1).
  * gcd>1 move: T drops by Omega(gcd)>=1, N non-increasing (outputs at most 2 entries >1).
- N >= 1 always: outputs of a move include at least one entry >1
  (lcm/gcd=1 => m=n => gcd=m>1). Move needs N>=2, drops N by at most 1.

Plan: verify by exhaustive BFS on small multisets.
