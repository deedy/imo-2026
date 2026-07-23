"""Exact-rational sanity checks for the two algebraic claims in the proof."""
from fractions import Fraction


def is_int(q: Fraction) -> bool:
    return q.denominator == 1


# Necessity lemma: exhaustive small positive rational data.
checked_cuts = 0
for den in range(2, 10):
    vals = [Fraction(n, den) for n in range(1, 6 * den) if n % den]
    for a in vals:
        for b in vals:
            for c in vals:
                s = a + b + c
                if is_int(s):
                    continue
                # Enumerate rational interior split parameters on same grid.
                for xn in range(1, int(a * den) + 1):
                    x = Fraction(xn, den)
                    if not (0 < x < a):
                        continue
                    left = (b, x, s - b - x)
                    right = (c, a - x, b + x)
                    assert all(q > 0 for q in left + right)
                    assert (all(not is_int(q) for q in left)
                            or all(not is_int(q) for q in right))
                    checked_cuts += 1

# Sufficiency interval claim for rational triangles of integral total N.
checked_triangles = 0
for N in range(2, 9):
    den = 12
    for an in range(1, N * den):
        for bn in range(1, N * den - an):
            cn = N * den - an - bn
            a, b, c = (Fraction(an, den), Fraction(bn, den), Fraction(cn, den))
            if any(is_int(q) for q in (a, b, c)):
                continue
            found = False
            # Search all ordered choices (a0,b0) of distinct angles.
            angles = (a, b, c)
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    a0, b0 = angles[i], angles[j]
                    for k in range(1, N):
                        if b0 < k < a0 + b0:
                            found = True
            assert found, (N, a, b, c)
            checked_triangles += 1

print(f"checked {checked_cuts} cuts and {checked_triangles} integral-sum triangles")
