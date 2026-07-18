# Verify the constructive XY strategy (Lemma D) with exact rational arithmetic:
# For random configs b_1>=...>=b_{n+1}>0 summing to 1, construct XY's cuts per the
# pigeonhole + cross-pairing recipe; check #cuts <= n and final D <= u = 1/(2^{n+1}-1).
from fractions import Fraction
import random, itertools

def D(parts):
    s = sorted(parts, reverse=True)
    d = Fraction(0); sg = 1
    for x in s: d += sg*x; sg = -sg
    return d

def xy_strategy(b):
    # b: list of piece lengths (Fractions), m pieces, XY budget m-1 cuts.
    # Returns final multiset of parts and number of cuts used.
    m = len(b)
    u = Fraction(1, 2**m - 1) * sum(b)
    # find two subsets with close sums
    idx = range(m)
    sums = []
    for mask in range(2**m):
        s = sum(b[i] for i in range(m) if mask >> i & 1)
        sums.append((s, mask))
    sums.sort()
    best = None
    for (s1, m1), (s2, m2) in zip(sums, sums[1:]):
        gap = s2 - s1
        if best is None or gap < best[0]:
            best = (gap, m2, m1)  # sigma(m2) - sigma(m1) = gap >= 0
    gap, mA, mB = best
    common = mA & mB
    mA ^= common; mB ^= common
    A = [i for i in range(m) if mA >> i & 1]
    B = [i for i in range(m) if mB >> i & 1]
    assert gap <= u and (A or B)
    sA = sum(b[i] for i in A); sB = sum(b[i] for i in B)
    assert sA - sB == gap
    parts = []
    cuts = 0
    others = [i for i in range(m) if i not in A and i not in B]
    for i in others:
        parts += [b[i]/2, b[i]/2]; cuts += 1
    if not B:
        for i in A: parts.append(b[i])
    else:
        # boundaries
        sbA = [Fraction(0)]
        for i in A: sbA.append(sbA[-1] + b[i])
        sbB = [Fraction(0)]
        for i in B: sbB.append(sbB[-1] + b[i])
        # cut points on A-row: B-interior boundaries < sB, plus sB itself
        cutsA = sorted(set(x for x in sbB[1:-1] if 0 < x < sA) | ({sB} if sB < sA else set()))
        cutsB = sorted(set(x for x in sbA[1:-1] if 0 < x < sB))
        # count actual cuts (exclude coincidences with own boundaries)
        realA = [x for x in cutsA if x not in sbA]
        realB = [x for x in cutsB if x not in sbB]
        cuts += len(realA) + len(realB)
        gridA = sorted(set(sbA) | set(realA))
        gridB = sorted(set(sbB) | set(realB))
        parts += [gridA[j+1]-gridA[j] for j in range(len(gridA)-1)]
        parts += [gridB[j+1]-gridB[j] for j in range(len(gridB)-1)]
    return parts, cuts, u

random.seed(3)
for trial in range(4000):
    n = random.randint(1, 6)
    m = n + 1
    raw = sorted([Fraction(random.randint(1, 300), 1) for _ in range(m)], reverse=True)
    tot = sum(raw)
    b = [x / tot for x in raw]
    parts, cuts, u = xy_strategy(b)
    assert cuts <= n, (b, cuts, n)
    assert sum(parts) == 1
    d = D(parts)
    assert d <= u, (b, parts, d, u)
print("Lemma D constructive strategy verified on 4000 random configs (exact arithmetic)")
