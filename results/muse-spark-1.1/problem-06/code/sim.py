import math
from sympy import primerange, factorint

def next_term(a_seq):
    # a_seq list
    # find smallest m > last such that gcd(m, each earlier) >1
    last = a_seq[-1]
    # prime sets
    prime_sets = []
    for x in a_seq:
        # factor
        f = set(factorint(x).keys())
        prime_sets.append(f)
    m = last+1
    while True:
        fm = set(factorint(m).keys())
        ok = True
        for ps in prime_sets:
            if fm.isdisjoint(ps):
                ok = False
                break
        if ok:
            return m
        m+=1

def gen(a1, N):
    seq = [a1]
    for _ in range(N-1):
        nxt = next_term(seq)
        seq.append(nxt)
    return seq

for a1 in range(2, 50):
    seq = gen(a1, 200)
    # print last 50
    # try to detect periodicity: look for T
    # compute differences
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    # Try to find T, L such that seq[n+T]-seq[n] constant = L for all n up to len-T-20? Check eventual?
    # But problem claims global T,L. Try to search small T up to 20, L compute from end
    found = None
    for T in range(1, 21):
        # for n large, say second half, check if seq[n+T]-seq[n] is constant
        vals = []
        for n in range(100, 200-T):
            vals.append(seq[n+T]-seq[n])
        if len(set(vals))==1:
            L = vals[0]
            # check if holds from start?
            ok_all = True
            for n in range(0, len(seq)-T):
                if seq[n+T]-seq[n]!=L:
                    ok_all=False
                    break
            if ok_all:
                found = (T,L)
                break
            else:
                # eventual only?
                pass
    if found:
        print(f"a1={a1} global period {found} seq start {seq[:20]}")
    else:
        # try eventual
        for T in range(1,21):
            vals = []
            for n in range(100, 200-T):
                vals.append(seq[n+T]-seq[n])
            if len(set(vals))==1:
                print(f"a1={a1} eventual period T={T} L={vals[0]} tail diffs {diffs[90:110]} seq tail {seq[90:110]}")
                break
        else:
            print(f"a1={a1} no small eventual period found diffs tail {diffs[90:120]}")
