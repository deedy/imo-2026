import math

def prime_factors_set(n):
    s=set()
    nn=n
    d=2
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
    # sets list of set
    uniq=[]
    seen=set()
    for s in sets:
        fs=frozenset(s)
        if fs not in seen:
            seen.add(fs)
            uniq.append(set(s))
    uniq.sort(key=lambda x: (len(x), sorted(x)))
    mins=[]
    for s in uniq:
        is_min=True
        for t in mins:
            if t.issubset(s):
                is_min=False
                break
        if is_min:
            # also need to ensure no existing mins superset? Since sorted by size, earlier are smaller, so if s contains earlier t, we already flagged not minimal. If s is smaller than some existing mins, that cannot happen because sorted by size ascending, but could have same size incomparable.
            mins.append(s)
    return mins

def simulate(a1, N):
    seq=[a1]
    S1=prime_factors_set(a1)
    M=[S1]
    a=a1
    for idx in range(1,N):
        # find next m > a that hits all sets in M
        m=a+1
        while True:
            # quick check: need to share prime with each set in M
            # we can compute prime factors set of m, but we can early exit by checking divisibility by primes in each set
            # Instead of factoring m fully, we can check if for each T in M, gcd(m, product(T))? Actually need existence of p in T dividing m.
            # Equivalent to for each T, exists p in T with p|m i.e., m mod p ==0 for some p in T.
            # So we can test divisibility without factoring: for each T, check if any p in T divides m. That's sufficient! Because if m shares prime with T, that prime must be in T and divide m. So we don't need full factorization of m, just test divisibility by primes in each T.
            # However to know primes in T, we have them.
            # So condition: for all T in M, exists p in T with m % p ==0.
            ok=True
            for T in M:
                hit=False
                for p in T:
                    if m % p ==0:
                        hit=True
                        break
                if not hit:
                    ok=False
                    break
            if ok:
                break
            m+=1
        a=m
        seq.append(a)
        # compute its prime factor set for M update (need full factor set to know minimal sets, but note only primes that are in current ground plus maybe new primes matter? Actually S_a may contain primes outside ground of M; those primes are not needed to hit M (since hitting condition already satisfied using primes within ground). But for future M, its full prime set matters because it may contain new primes that become part of ground. However for checking if S contains some T in M, we only need to know if T subset of S. If S contains new prime outside, it still may contain T if T subset of S's intersection with ground. So we need full factor set, but we can compute prime factors set of a (factorization).
        S=prime_factors_set(a)
        # check if S contains some T in M
        contains=False
        for T in M:
            if T.issubset(S):
                contains=True
                break
        if not contains:
            # add S as new minimal
            M=minimal_family(M+[S])
        # else unchanged
        if idx%1000==0:
            ground=set().union(*M) if M else set()
            print(f"step {idx} a={a} |M|={len(M)} ground size {len(ground)} ground {sorted(ground)[:20]} max prime {max(ground) if ground else None}")
    return seq, M

for a1 in [35, 77, 105, 3*5*7*11*13, 2*3*5*7*11, 11*13, 17*19, 2*3*5*7*11*13]:
    print(f"\n=== a1={a1} S1={prime_factors_set(a1)}")
    seq, M = simulate(a1, 5000)
    ground=set().union(*M)
    print(f"final |M|={len(M)} ground {sorted(ground)}")
    print(f"tail seq {seq[-20:]}")
    # compute gaps
    diffs=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
    print(f"gap max {max(diffs[1000:])} min {min(diffs[1000:])} avg {sum(diffs[1000:])/len(diffs[1000:])}")
    # check if M appears stable for last 1000 steps (no change)
    # We printed only final, but we can track stability by checking if M changed in last 1000
    # For now approximate by checking last M vs earlier: we would need to recompute with tracking changes
    # Let's do second pass tracking change times
    seq2, M2 = simulate(a1, 2000) # dummy to get change times? We'll modify simulate to return change log
