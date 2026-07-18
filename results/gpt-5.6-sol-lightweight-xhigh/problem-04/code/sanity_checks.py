#!/usr/bin/env python3
"""Exact small-grid checks of the two combinatorial angle claims.

Angles are normalized so a straight angle is 1.
"""
from fractions import Fraction


def is_multiple(x: Fraction, t: Fraction) -> bool:
    q = x / t
    return q.denominator == 1 and q.numerator >= 1


def check_safe_invariant() -> int:
    checked = 0
    # Targets t for which 1/t is not an integer.
    targets = [Fraction(p, q) for q in range(3, 16) for p in range(1, q)
               if (Fraction(1, 1) / Fraction(p, q)).denominator != 1]
    for t in targets:
        den = 24
        for ai in range(1, den - 1):
            for bi in range(1, den - ai):
                ci = den - ai - bi
                A, B, C = (Fraction(v, den) for v in (ai, bi, ci))
                if any(is_multiple(z, t) for z in (A, B, C)):
                    continue
                for xi in range(1, ai):
                    x = Fraction(xi, den)
                    child1 = (B, x, 1 - B - x)
                    child2 = (C, A - x, B + x)
                    safe1 = not any(is_multiple(z, t) for z in child1)
                    safe2 = not any(is_multiple(z, t) for z in child2)
                    assert safe1 or safe2, (t, (A, B, C), x, child1, child2)
                    checked += 1
    return checked


def check_integer_interval_lemma() -> int:
    checked = 0
    for n in range(2, 10):
        den = 13
        total = n * den
        for ai in range(1, total - 1):
            for bi in range(1, total - ai):
                ci = total - ai - bi
                vals = [Fraction(ai, den), Fraction(bi, den), Fraction(ci, den)]
                if any(v.denominator == 1 for v in vals):
                    continue
                found = False
                # Test all ordered choices of a,b among the three.
                for i in range(3):
                    for j in range(3):
                        if i == j:
                            continue
                        a, b = vals[i], vals[j]
                        if any(b < k < a + b for k in range(1, n)):
                            found = True
                assert found, (n, vals)
                checked += 1
    return checked


if __name__ == "__main__":
    print("safe cut configurations checked:", check_safe_invariant())
    print("integer-interval triples checked:", check_integer_interval_lemma())
