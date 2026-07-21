import math

def prime_factors_set(n):
    # return set of prime divisors
    s=set()
    d=2
    nn=n
    while d*d<=nn:
        if nn%d==0:
            s.add(d)
            while nn%d==0:
                nn//=d
        d+=1 if d==2 else 2
    if nn>1:
        s.add(nn)
    return s

def minimal_family(sets):
    # sets list of sets, return minimal inclusion antichain
    # deduplicate
    uniq=[]
    seen=set()
    for s in sets:
        fs=frozenset(s)
        if fs not in seen:
            seen.add(fs)
            uniq.append(set(s))
    # sort by size ascending
    uniq.sort(key=lambda x: (len(x), sorted(x)))
    mins=[]
    for s in uniq:
        is_min=True
        for t in mins:
            if t.issubset(s):
                is_min=False
                break
        if is_min:
            mins.append(s)
    return mins

def simulate_gen(a1, N):
    # generate sequence using direct hitting condition (check against minimal family M)
    seq=[a1]
    S1=prime_factors_set(a1)
    M=[S1]  # minimal family
    a=a1
    for idx in range(1,N):
        # find next m > a such that for all T in M, gcd with T non-empty intersection
        m=a+1
        # naive scan, but with early exit
        while True:
            Sm=prime_factors_set(m)
            ok=True
            for T in M:
                # check intersection
                # since sets small, check any common
                inter=False
                # faster: if any p in T divides m, then intersection
                # Instead of set disjoint, check divisibility via? Use Sm set already
                if Sm.isdisjoint(T):
                    ok=False
                    break
            if ok:
                break
            m+=1
        a=m
        seq.append(a)
        Sm=prime_factors_set(a)
        # check if Sm contains some T in M
        contains=False
        for T in M:
            if T.issubset(Sm):
                contains=True
                break
        if not contains:
            # new minimal set
            # also need to check if Sm is superset of existing? Already not contains, but could be subset of existing
            # Update M to minimal family of M ∪ {Sm}
            M=minimal_family(M+[Sm])
        # else M unchanged
        if idx%1000==0:
            print(f"step {idx} a={a} |M|={len(M)} max prime in M {max(max(s) for s in M)} ")
    return seq, M

for a1 in [35, 77, 105, 15*7, 3*5*7*11, 3*7*11, 2*3*5*7]:
    print(f"\n=== a1={a1}")
    seq, M = simulate_gen(a1, 5000)
    print(f"final |M|={len(M)} M sample {M[:20]}")
    print(f"tail seq {seq[-20:]}")
    diffs=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
    print(f"gap stats max {max(diffs[1000:])} min {min(diffs[1000:])}")

