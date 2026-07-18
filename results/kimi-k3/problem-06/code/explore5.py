"""Hunt for dangerous configurations: disjoint transversals of size >= 2 (could
lead to perpetual shrinkage), and record stable H structures."""
from math import gcd
from sympy import factorint
from explore1 import rad_primes, prod

def run(a1, N):
    b = rad_primes(a1)
    H = {frozenset([p]) for p in b}
    seq = [a1]
    shrinks = []
    dangerous = []
    for n in range(1, N):
        an = seq[-1]
        best = None
        for h in H:
            hv = prod(h)
            m = (an // hv + 1) * hv
            if best is None or m < best:
                best = m
        seq.append(best)
        b = rad_primes(best)
        cand = set()
        for h in H:
            if h & b:
                cand.add(h)
            else:
                for q in b:
                    cand.add(h | {q})
        cand = list(cand)
        Hnew = set()
        for t in cand:
            if not any(u < t for u in cand):
                Hnew.add(t)
        if Hnew != H:
            shrinks.append(n)
        # check for dangerous pair: disjoint, both size >= 2
        Hl = list(Hnew)
        for i in range(len(Hl)):
            for j in range(i+1, len(Hl)):
                if not (Hl[i] & Hl[j]) and len(Hl[i]) >= 2 and len(Hl[j]) >= 2:
                    dangerous.append((n, sorted(Hl[i]), sorted(Hl[j])))
        H = Hnew
    return seq, shrinks, H, dangerous

if __name__ == "__main__":
    # 1) Inspect stable H for interesting odd a1
    for a1 in [105, 1155, 1001, 385, 165, 195, 255, 455, 595, 665, 935, 1105, 1309, 1495, 1729, 1995]:
        seq, shrinks, H, dang = run(a1, 4000)
        print(f"a1={a1:5d}: #shrinks={len(shrinks):4d} last={shrinks[-1] if shrinks else None} "
              f"stableH={[sorted(h) for h in H]} dangerous_pairs={len(dang)}")
        if dang:
            print(f"    first dangerous: {dang[0]}")
