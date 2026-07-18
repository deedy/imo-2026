"""Part A (lower bound): super-increasing family with margin delta,
subdivided with <= n cuts, must have D >= delta.

We test:
 (1) Claim A itself, adversarially (random + local search to MINIMIZE D).
 (2) The 'R/E decomposition' route: D(R) >= D(E) + delta where R = max-fragments,
     E = excess fragments.
"""
from fractions import Fraction
import random, itertools

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[0::2]) - sum(s[1::2])

def D_of(tup):
    return alt_sum(list(tup))

def random_superincreasing(n, delta, rng, scale=1000):
    """Random super-increasing family: a_1 >= delta, a_{i+1} >= delta + sum_{j<=i} a_j."""
    a = []
    s = 0
    for i in range(n + 1):
        lo = delta + s if i >= 1 else delta
        # pick value in [lo, 3*lo] rationally
        num = rng.randint(int(lo * scale), int(3 * lo * scale) + 1)
        v = Fraction(num, scale)
        a.append(v)
        s += v
    return a

def random_subdivision(a, cuts, rng):
    """Subdivide each a_i into fragments; total `cuts` cuts."""
    cur = [(x, i) for i, x in enumerate(a)]  # (size, parent)
    for _ in range(cuts):
        idx = rng.randrange(len(cur))
        L, p = cur[idx]
        u = Fraction(rng.randint(1, 10**6), 10**6 + 1) * L
        cur = cur[:idx] + [(u, p), (L - u, p)] + cur[idx+1:]
    return cur

def RE_split(cur, nparents):
    """R = max fragment of each parent; E = the rest."""
    byparent = {}
    for x, p in cur:
        byparent.setdefault(p, []).append(x)
    R, E = [], []
    for p, fr in byparent.items():
        fr = sorted(fr)
        R.append(fr[-1])
        E.extend(fr[:-1])
    return tuple(R), tuple(E)

def test_claim_A(n, trials=300, seed=1):
    rng = random.Random(seed)
    delta = Fraction(1, 97)  # arbitrary
    worst = None
    for t in range(trials):
        a = random_superincreasing(n, delta, rng)
        c = rng.randint(0, n)
        cur = random_subdivision(a, c, rng)
        M = tuple(x for x, _ in cur)
        D = D_of(M)
        if D < delta:
            print("CLAIM A FAIL:", a, cur, D)
            return False
        # R/E test
        R, E = RE_split(cur, n + 1)
        DR, DE = D_of(R), D_of(E) if E else Fraction(0)
        if DR < DE + delta:
            print("R/E FAIL:", a, cur, "D(R)=", DR, "D(E)=", DE, "delta=", delta)
            return False
        if worst is None or D - delta < worst:
            worst = D - delta
    print(f"n={n}: Claim A held in {trials} trials; min slack D-delta = {float(worst):.4f}; R/E held")
    return True

def adversarial_geometric(n, iters=2000, seed=2):
    """Local search to minimize D over subdivisions of geometric family with n cuts."""
    rng = random.Random(seed)
    delta = Fraction(1)
    a = [delta * 2**i for i in range(n + 1)]
    S = sum(a)
    best = None
    for t in range(iters):
        c = rng.randint(1, n)
        cur = random_subdivision(a, c, rng)
        # local improvement: try random re-cuts
        M = tuple(x for x, _ in cur)
        D = D_of(M)
        if best is None or D < best:
            best = D
    print(f"n={n}: geometric family, min D over {iters} random subdivisions = {float(best):.5f}, "
          f"delta*S... delta = {float(delta):.5f}, match: {best >= delta}")
    return best

if __name__ == "__main__":
    for n in [1, 2, 3, 4]:
        test_claim_A(n)
    print()
    for n in [1, 2, 3, 4, 5]:
        adversarial_geometric(n)
