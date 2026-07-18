import sys
from math import gcd, lcm
from itertools import combinations

def run(a1, limit):
    # sieve smallest prime factor
    spf = list(range(limit+1))
    i = 2
    while i*i <= limit:
        if spf[i] == i:
            for j in range(i*i, limit+1, i):
                if spf[j] == j: spf[j] = i
        i += 1
    def pset(n):
        s = set()
        while n > 1:
            p = spf[n]; s.add(p)
            while n % p == 0: n //= p
        return frozenset(s)
    seq = [a1]
    cons = [pset(a1)]   # inclusion-minimal constraint prime sets so far
    inS = {a1}
    for m in range(a1+1, limit+1):
        pm = pset(m)
        ok = True
        for c in cons:
            if not (pm & c): ok = False; break
        if ok:
            seq.append(m); inS.add(m)
            if not any(c <= pm for c in cons):
                cons = [c for c in cons if not (pm < c)]
                cons.append(pm)
    return seq, cons, inS, pset

def blocker(cons):
    ground = sorted(set().union(*cons))
    res = []
    if len(ground) > 22:
        return None, ground
    for size in range(1, len(ground)+1):
        for comb in combinations(ground, size):
            s = frozenset(comb)
            if any(q <= s for q in res): continue
            if all(s & c for c in cons): res.append(s)
    return res, ground

def prod(xs):
    r = 1
    for x in xs: r *= x
    return r

def check(a1, limit):
    seq, cons, inS, pset = run(a1, limit)
    B, ground = blocker(cons)
    if B is None:
        return dict(a1=a1, err="ground too big", ground=ground)
    ds = sorted(prod(Q) for Q in B)
    M = 1
    for d in ds: M = lcm(M, d)
    # check 1: member primes <= a1
    c1 = all(max(Q) <= a1 for Q in B)
    # check 1b: members pairwise intersect
    c1b = all(Q & Qp for Q in B for Qp in B)
    # check 2: membership formula on [a1, limit]
    c2 = True
    bad = None
    for m in range(a1, limit+1):
        mem = any(m % d == 0 for d in ds)
        if mem != (m in inS):
            c2 = False; bad = m; break
    # check 3: periodicity from n=1 with T = #S in [a1, a1+M), L = M
    c3 = None; T = None
    if a1 + 2*M <= limit:
        T = sum(1 for m in seq if a1 <= m < a1 + M)
        c3 = True
        for n in range(len(seq) - T):
            if seq[n+T] != seq[n] + M:
                c3 = False; break
    return dict(a1=a1, nterms=len(seq), cons=sorted(map(sorted, cons)),
                blocker=sorted(map(sorted, B)), ds=ds, M=M, T=T,
                c1_primes_le_a1=c1, c1b_pairwise=c1b, c2_membership=c2, bad=bad,
                c3_periodic=c3)

if __name__ == "__main__":
    vals = list(range(2, 61)) + [77, 91, 101, 105, 121, 125, 143, 169, 255, 385, 1001]
    for a1 in vals:
        r = check(a1, max(4000, 40*a1))
        if 'err' in r:
            print(a1, r); continue
        # if M too large relative to limit, rerun bigger
        if r['c3_periodic'] is None and a1 + 2*r['M'] <= 2_000_000:
            r = check(a1, min(2_000_000, a1 + 3*r['M'] + 1000))
        print(f"a1={r['a1']:5d} M={r['M']:8d} T={r['T']} blocker={r['blocker']} "
              f"c1={r['c1_primes_le_a1']} c1b={r['c1b_pairwise']} c2={r['c2_membership']} c3={r['c3_periodic']} bad={r['bad']}")
        sys.stdout.flush()
