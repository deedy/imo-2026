"""Exact verification of the two claims with Fraction arithmetic.

Claim 1: theta = 180/n  =>  Mulan's explicit strategy wins in <= n-1 moves
         (verified by exhaustively branching over Shan-Yu's binary choices).
Claim 2: theta != 180/m for all m  =>  Shan-Yu's "M-free" invariant is maintainable
         (checked against random Mulan cuts).
"""
from fractions import Fraction
import random
import sys

D180 = Fraction(180)


def halves(A, B, C, alpha):
    """Cut at vertex A, alpha = angle adjacent to B."""
    h1 = (B, alpha, D180 - B - alpha)
    h2 = (C, A - alpha, B + alpha)
    return h1, h2


def valid(tri):
    return all(x > 0 for x in tri) and sum(tri) == D180


# ---------------- Claim 1 ----------------

def test_mulan(n, trials, seed=0):
    theta = Fraction(180, n)
    rng = random.Random(seed)

    def is_mult(x):
        return (x / theta).denominator == 1  # integer multiple of theta in (0,180)

    def mulan_move(tri):
        # returns (A,B,C,alpha); must be a valid cut with both halves winning
        # case 1: some marked angle k*theta, k>=2 -> halve it
        for i, x in enumerate(tri):
            if is_mult(x):
                k = x / theta
                assert k >= 2, f"k=1 should have ended game: {tri}"
                A = x
                B = tri[(i + 1) % 3]
                C = tri[(i + 2) % 3]
                return A, B, C, theta
        # case 2: find u != v with dist_up(u) < v
        for i, u in enumerate(tri):
            assert not is_mult(u)
            k = u // theta  # floor, since u/theta not integral
            du = (k + 1) * theta - u
            assert 0 < du < theta
            for j, v in enumerate(tri):
                if i != j and du < v:
                    w = tri[6 - i - j - (i + j)] if False else None
                    others = [t for t in range(3) if t != i and t != j]
                    A = v
                    B = u
                    C = tri[others[0]]
                    return A, B, C, du
        raise AssertionError(f"no dist_up pair found for {tri}, theta={theta}")

    def play(tri, depth=0):
        """max number of further moves until theta appears, over Shan-Yu choices."""
        assert valid(tri), tri
        if any(x == theta for x in tri):
            return 0
        A, B, C, alpha = mulan_move(tri)
        assert 0 < alpha < A, (tri, alpha)
        h1, h2 = halves(A, B, C, alpha)
        for h in (h1, h2):
            assert valid(h), (tri, alpha, h)
        return 1 + max(play(h1, depth + 1), play(h2, depth + 1))

    worst = 0
    for t in range(trials):
        # random rational triangle
        x = Fraction(rng.randrange(1, 10**6), rng.randrange(1, 10**6))
        y = Fraction(rng.randrange(1, 10**6), rng.randrange(1, 10**6))
        z = Fraction(rng.randrange(1, 10**6), rng.randrange(1, 10**6))
        s = x + y + z
        x = x * D180 / s
        y = y * D180 / s
        z = D180 - x - y
        tri = (x, y, z)
        if any(v == theta for v in tri):
            continue
        # also mix in triangles that contain a multiple of theta
        if t % 3 == 0:
            k = rng.randrange(1, n)
            rest = D180 - k * theta
            u = Fraction(rng.randrange(1, 10**5), rng.randrange(1, 10**5))
            v = rest * u / (u + 1)
            tri = (k * theta, v, rest - v)
        m = play(tri)
        worst = max(worst, m)
        assert m <= n - 1, (n, tri, m)
    print(f"Claim1 n={n:3d} theta={str(theta):>6}: OK, worst #moves = {worst} (bound {n-1})")


# ---------------- Claim 2 ----------------

def test_shanyu(theta, trials=200, rounds=300, seed=1):
    rng = random.Random(seed)

    def is_mult(x):
        return (x / theta).denominator == 1

    def mfree(tri):
        return not any(is_mult(x) for x in tri)

    ok = True
    for t in range(trials):
        tri = (Fraction(60), Fraction(60), Fraction(60))
        assert mfree(tri)
        for r in range(rounds):
            # Mulan picks random vertex and random rational alpha
            i = rng.randrange(3)
            A = tri[i]
            B = tri[(i + 1) % 3]
            C = tri[(i + 2) % 3]
            u = Fraction(rng.randrange(1, 10**7), rng.randrange(1, 10**7))
            alpha = A * u / (u + 1)  # in (0,A)
            h1, h2 = halves(A, B, C, alpha)
            f1, f2 = mfree(h1), mfree(h2)
            if not (f1 or f2):
                print(f"INVARIANT BROKEN: theta={theta}, tri={tri}, A={A},alpha={alpha}, h1={h1}, h2={h2}")
                return False
            tri = h1 if f1 else h2
            assert valid(tri)
    print(f"Claim2 theta={str(theta):>8}: OK ({trials}x{rounds} random cuts, invariant held)")
    return ok


if __name__ == "__main__":
    random.seed(0)
    for n in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20, 25, 30, 45, 60, 90]:
        test_mulan(n, trials=120, seed=n)
    print()
    for theta in [Fraction(360, 7), Fraction(180, 2) + Fraction(1, 3),
                  Fraction(207, 10), Fraction(179, 2),
                  Fraction(540, 7), Fraction(60, 1) + Fraction(1, 2),
                  Fraction(123456, 789)]:
        # sanity: theta must NOT be of the form 180/m
        assert (Fraction(180) / theta).denominator != 1, theta
        test_shanyu(theta)
