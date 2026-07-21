import math

def prime_factors_set(n):
    s=set()
    d=2
    while d*d<=n:
        if n%d==0:
            s.add(d)
            while n%d==0:
                n//=d
        d+=1 if d==2 else 2
    if n>1:
        s.add(n)
    return s

def minimal_family(sets):
    # sets list of set
    # remove duplicates via frozenset
    uniq=[]
    seen=set()
    for s in sets:
        f=frozenset(s)
        if f not in seen:
            seen.add(f)
            uniq.append(s)
    # minimal inclusion
    mins=[]
    for i, s in enumerate(uniq):
        is_min=True
        for j, t in enumerate(uniq):
            if i!=j and t.issubset(s) and t!=s:
                is_min=False
                break
        if is_min:
            mins.append(s)
    return mins

def minimal_hitting_sets(F):
    # F list of sets over ground
    if not F:
        return []
    primes = set().union(*F)
    primes = list(primes)
    # we search for inclusion-minimal hitting sets
    # brute force by increasing size up to maybe 6
    # but we can prune
    # For ground up to maybe 10 primes, powerset is up to 1024 feasible
    # For larger ground, but our examples small
    # We'll enumerate all subsets sorted by size
    from itertools import combinations
    # generate all hitting superset minimal
    n = len(primes)
    # convert F to list of bit masks
    prime_to_idx = {p:i for i,p in enumerate(primes)}
    F_masks=[]
    for s in F:
        mask=0
        for p in s:
            mask|=1<<prime_to_idx[p]
        F_masks.append(mask)
    # for each subset mask, check if hitting: mask intersects each F_mask !=0
    hitting_masks=[]
    for mask in range(1, 1<<n):
        ok=True
        for fm in F_masks:
            if mask & fm ==0:
                ok=False
                break
        if ok:
            hitting_masks.append(mask)
    # minimal among hitting_masks by inclusion
    minimal=[]
    for hm in hitting_masks:
        is_min=True
        for other in hitting_masks:
            if other!=hm and (other & hm)==other: # other subset hm
                is_min=False
                break
        if is_min:
            minimal.append(hm)
    # convert back to set of primes
    res=[]
    for hm in minimal:
        s=set()
        for i in range(n):
            if hm>>i &1:
                s.add(primes[i])
        res.append(s)
    return res

def simulate(a1, steps):
    S1 = prime_factors_set(a1)
    F = [S1]
    a=a1
    seq=[a]
    for _ in range(steps-1):
        F_min = minimal_family(F)
        H = minimal_hitting_sets(F_min)
        # compute next term
        best = None
        best_H = None
        for h in H:
            prod=1
            for p in h:
                prod*=p
            # next multiple >a
            nxt = (a//prod+1)*prod
            if best is None or nxt<best:
                best=nxt
                best_H=h
        # best is a_{next}
        a=best
        seq.append(a)
        S = prime_factors_set(a)
        # update F list
        # if any existing minimal set already subset of S, we can ignore? But for F we keep all? For minimal we need check
        # To keep overall family size limited, we can keep only minimal family + new set? Actually F for minimal purposes only need minimal family. Because if S already contains some minimal set, F_min unchanged.
        # If S is superset of some minimal set, we don't add
        # Otherwise we add S and recompute minimal
        # So:
        contains=False
        for t in F_min:
            if t.issubset(S):
                contains=True
                break
        if not contains:
            # need to add
            F.append(S)
            # optional prune: keep only minimal family for next iteration to keep smaller? But for correctness of future minimal we only need minimal family, but we keep all minimal as F = F_min ∪ {S} minimal version.
            F = minimal_family(F)
        # else F unchanged (F = F_min)
        else:
            F = F_min
    return seq, F

for a1 in [35, 105, 77, 15]:
    seq, F_final = simulate(a1, 500)
    print(f"\na1={a1} len seq {len(seq)} final F size {len(F_final)} sets: {F_final}")
    # compute H final
    H_final = minimal_hitting_sets(F_final)
    print(f"H final size {len(H_final)} {H_final} products {[math.prod(list(h)) for h in H_final]}")
    # detect periodicity tail
    # compute products
    M = [math.prod(list(h)) for h in H_final]
    L = 1
    # lcm
    import math as m
    l=1
    for mi in M:
        l= l*mi // math.gcd(l,mi)
    print(f"lcm {l}")
    # verify next terms would follow this H for some tail region: simulate generating numbers as sorted multiples of M > current
    # generate tail of multiples
    # To check if seq tail equals multiples of M
    # Generate sorted set of multiples of M up to max seq
    max_n = seq[-1]
    mult_set = set()
    for mi in M:
        for multiple in range((seq[0]//mi)*mi, max_n+1, mi):
            if multiple>=seq[0] and multiple%mi==0:
                # but will include numbers < seq? We'll filter later
                pass
        # actual up to max
        start = (seq[0] + mi -1)//mi * mi
        # but seq[0] itself may not be multiple? Actually seq0 is multiple of some Mi? For our F, maybe yes
        for k in range(start, max_n+1, mi):
            mult_set.add(k)
    sorted_mult = sorted(mult_set)
    # Compare sorted_mult with seq
    # print first 100 vs
    # Check equality after some index
    # Let's find first index where they diverge
    mismatch=None
    for i, (a,b) in enumerate(zip(seq, sorted_mult)):
        if a!=b:
            mismatch=i
            break
    if mismatch is None:
        if len(seq)!=len(sorted_mult):
            mismatch=min(len(seq), len(sorted_mult))
    print(f"mismatch index {mismatch}")
    if mismatch is not None:
        print("seq[mismatch:mismatch+20]", seq[mismatch:mismatch+20])
        print("mult[mismatch:mismatch+20]", sorted_mult[mismatch:mismatch+20] if mismatch<len(sorted_mult) else [])
        # also compare tail
    else:
        print("perfect match!")

# More detailed for 35 with longer steps 2000
print("\n--- long 35 2000")
seq, F_final = simulate(35, 2000)
print(f"final F size {len(F_final)} {F_final}")
H_final = minimal_hitting_sets(F_final)
prods=[math.prod(list(h)) for h in H_final]
print(f"H size {len(H_final)} prods {prods}")
l=1
for mi in prods:
    l=l*mi//math.gcd(l,mi)
print("lcm", l)
# detect eventual period via diff pattern on last 500
diffs=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
# try to find T,L from tail
# assume eventual moduli stable for last maybe 500 steps, T should equal number of residues
# residues = prods hitting count
# compute set of residues modulo l that are divisible by any prod
residues=set()
for r in range(l):
    for mi in prods:
        if r%mi==0:
            residues.add(r)
            break
# number of residues
T_expected = len(residues)
print("expected T", T_expected)
# check if tail differences repeat with period T
tail_start=1500
# check sequence modulo l
# For periodic set, seq[n+T]=seq[n]+l
# test for last maybe 400
ok=True
for i in range(tail_start, len(seq)-T_expected-1):
    if seq[i+T_expected]!=seq[i]+l:
        ok=False
        print("fail at", i, seq[i], seq[i+T_expected])
        break
print("tail periodic?", ok)
# print early check global periodic?
# check if whole sequence follows multiples of prods
max_n=seq[-1]
mult_set=set()
for mi in prods:
    start = (seq[0] + mi -1)//mi * mi
    # ensure first term included
    # but want all multiples from seq[0] onward
    for k in range(start, max_n+1, mi):
        mult_set.add(k)
sorted_mult=sorted(mult_set)
print("len seq vs mult", len(seq), len(sorted_mult))
# find first mismatch
for i in range(len(seq)):
    if i>=len(sorted_mult) or seq[i]!=sorted_mult[i]:
        print(f"first mismatch at {i} seq {seq[i]} vs mult {sorted_mult[i] if i<len(sorted_mult) else None}")
        # print some surrounding
        print(seq[i-5:i+10])
        print(sorted_mult[i-5:i+10])
        break
else:
    print("full match up to max")

