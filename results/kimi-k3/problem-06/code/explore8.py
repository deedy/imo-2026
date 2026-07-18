"""Deep look at a1=9690 = 2*3*5*17*19."""
from math import gcd
from sympy import factorint
from explore1 import rad_primes, prod

def run(a1, N):
    b_list = [rad_primes(a1)]
    H = {frozenset([p]) for p in b_list[0]}
    seq = [a1]
    shrinks = []
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
        b_list.append(b)
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
        H = Hnew
    return seq, shrinks, H, b_list

seq, shrinks, H, b_list = run(9690, 30000)
print(f"#shrinks = {len(shrinks)}, last shrink = {shrinks[-1] if shrinks else None}")
print(f"shrinks[-15:] = {shrinks[-15:]}")
Hl = list(H)
pw = all((Hl[i] & Hl[j]) for i in range(len(Hl)) for j in range(i+1, len(Hl)))
print(f"final |H| = {len(H)}, pairwise intersecting: {pw}")
print(f"final H = {sorted(sorted(h) for h in H)}")
print(f"M = {min(prod(h) for h in H)}")
# check gaps periodicity on tail
gaps = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
print("gaps[-30:]", gaps[-30:])
