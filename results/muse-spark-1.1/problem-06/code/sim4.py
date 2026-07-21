import math
from collections import defaultdict

def prime_factors_set(n):
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
    # sets list of set
    # deduplicate
    uniq=[]
    seen=set()
    for s in sets:
        fs=frozenset(s)
        if fs not in seen:
            seen.add(fs)
            uniq.append(set(s))
    # keep inclusion minimal
    # sort by size
    uniq.sort(key=lambda x: len(x))
    mins=[]
    for s in uniq:
        # check if any already mins subset of s
        is_min=True
        for t in mins:
            if t.issubset(s):
                is_min=False
                break
        if is_min:
            # also need to remove any existing supersets? But because sorted by size, earlier are smaller, so no superset of current in mins yet? Could have equal size? No.
            # However there could be later superset that remains, but we iterate increasing so if we keep only minimal, we will not add superset.
            mins.append(s)
    # Actually this greedy works for inclusion minimal: smallest sets are minimal; any superset of them not minimal.
    return mins

def minimal_hitting_sets(F):
    # F list of sets (python set)
    if not F:
        return []
    # ground primes
    primes = set().union(*F) if F else set()
    primes = list(primes)
    # if empty ground?
    # brute force over subsets but may blow up; limit size?
    n=len(primes)
    if n>18:
        # heuristic: use recursive search for minimal hitting sets using backtracking
        # We'll implement typical algorithm
        # Use recursion to find all minimal hitting sets bounded?
        # For our tests n may be larger but we hope not.
        # We'll try iterative deepening limited to small size first
        # For analysis, we might need efficient
        # Use BFS
        from itertools import combinations
        # estimate: if n large, number of hitting sets may be huge; we can limit to small size maybe ≤5? But may miss larger
        # For now return None to indicate overflow
        return None
    prime_to_idx={p:i for i,p in enumerate(primes)}
    F_masks=[]
    for s in F:
        mask=0
        for p in s:
            if p in prime_to_idx:
                mask|=1<<prime_to_idx[p]
        F_masks.append(mask)
    hitting=[]
    for mask in range(1, 1<<n):
        ok=True
        for fm in F_masks:
            if mask & fm ==0:
                ok=False
                break
        if ok:
            hitting.append(mask)
    # minimal
    hitting.sort(key=lambda x: bin(x).count('1'))
    minimal=[]
    for hm in hitting:
        # check if any minimal subset already
        is_min=True
        for m in minimal:
            if (m & hm)==m:
                is_min=False
                break
        if is_min:
            # also remove any existing superset? But we process increasing size, so existing are smaller, can't be superset
            minimal.append(hm)
    # convert
    res=[]
    for hm in minimal:
        s=set()
        for i in range(n):
            if hm>>i &1:
                s.add(primes[i])
        res.append(s)
    return res

def is_intersecting_family(H):
    for i in range(len(H)):
        for j in range(i+1, len(H)):
            if H[i].isdisjoint(H[j]):
                return False
    return True

def simulate_until_stable(a1, max_steps=5000):
    S1=prime_factors_set(a1)
    F=[S1]
    a=a1
    seq=[a]
    steps=0
    while steps<max_steps:
        H=minimal_hitting_sets(F)
        if H is None:
            return seq, F, None, "H too large"
        if is_intersecting_family(H):
            # stable
            return seq, F, H, f"stable after {steps} steps"
        # compute next term: minimal multiple > a among p(h)
        best=None
        best_h=None
        best_prod=None
        for h in H:
            prod=1
            for p in h:
                prod*=p
            # next multiple > a
            nxt = (a//prod +1)*prod
            # if nxt==a? Actually > a, if a multiple, next = a+prod
            if nxt<=a:
                nxt+=prod
            if best is None or nxt<best:
                best=nxt
                best_h=h
                best_prod=prod
        # best is next a
        a=best
        seq.append(a)
        S=prime_factors_set(a)
        # check if S contains some set in F
        contains=False
        for t in F:
            if t.issubset(S):
                contains=True
                break
        if not contains:
            # add S to F and minimize
            newF=F+[S]
            F=minimal_family(newF)
        # else F unchanged -> but if F unchanged and H intersecting? Actually if contains, F unchanged, but H may still be non-intersecting? Wait if S contains member of F, F unchanged, but then H unchanged still non-intersecting, but we have found a good multiple (contains F). However existence of bad multiples still? But our next step picks minimal multiple which was this S (good). So we can continue without changing F. However earlier we argued that eventually a bad multiple will appear. So we may stay with same F for several steps (enumerating good multiples) before hitting bad one. Our loop currently updates only if contains False; otherwise we keep F same. That's correct, but we should continue looping: even if contains True, we remain at same F, but we have advanced a. Eventually we will get to a bad S where contains False, then F changes.
        steps+=1
    return seq, F, minimal_hitting_sets(F), "max steps reached"

# test various a1
for a1 in [6,10,15,21,33,35,77,105,221, 15*14, 2*3*5*7*11]:
    seq,F,H,msg = simulate_until_stable(a1, max_steps=2000)
    print(f"\na1={a1} {msg}")
    print(f"  steps (sequence len) {len(seq)} final F size {len(F)} : {F[:10]}")
    if H is not None:
        prods=[math.prod(list(h)) for h in H[:10]]
        print(f"  H size {len(H)} prods sample {prods[:10]} intersecting? {is_intersecting_family(H)}")
    else:
        print("  H overflow")
    # print tail of seq
    print(f"  tail seq {seq[-10:]}")

# try a1 = 35 deeper with overflow handling improved
print("\n--- deeper 35 with limited H size detection after many steps")
# Implement more efficient hitting set enumeration using recursion bounded
def minimal_hitting_sets_optimized(F):
    # Use recursive branching for hypergraph transversals (Berge)
    # We'll implement simple recursive algorithm for minimal hitting sets
    # Using standard algorithm: pick set S, branch on each element p in S: include p, remove sets containing p, recurse.
    # Keep minimal.
    # For large ground, may still blow up but we can prune and limit.
    # We'll use algorithm that returns all minimal hitting sets.
    # F is list of sets (python set)
    # Use frozenset representation maybe
    # Optimize with sorting sets by size.
    # We'll implement iterative recursion with memoization
    best = []
    # sort F by size ascending for faster pruning
    F_sorted = sorted(F, key=lambda x: len(x))
    # ground primes
    # recursive function: parameters: remaining sets (list of sets), current hitting set (set), index maybe
    # Use branching on smallest set
    from functools import lru_cache
    # To avoid huge blowup, we can maintain current best minimal size upper bound? Need all minimals, not just small.

    # Use typical algorithm for minimal hitting sets without pruning by superset? Might be exponential.

    # For our case, ground up to maybe 15-20, we can use bitmask method; earlier overflow at >18. But for 35 family size maybe grows beyond 18 primes -> impossible to brute force.
    # Let's try to use BFS limited to small hitting sets size up to say 4 or 5, because if minimal hitting sets size >5 products become huge, maybe not needed for next step? Actually we need all minimal to determine intersecting property and next multiple minimal.
    # However note that product of large hitting set is larger, so for determining next multiple, larger products tend to give larger next multiples? Not necessarily, but roughly larger product -> larger gap, but could still be minimal if residue close.
    # To check intersecting, we need to know existence of disjoint pair, which would involve relatively small sets? Might need large sets too.
    # For approximate, we can limit search to hitting sets of size up to maybe 4-5 to detect disjointness? Could be enough.

    # We'll implement generic recursion that enumerates all minimal hitting sets but with pruning by subsumption using bitmasks if n <= 22 else limited.

    # Count distinct primes
    primes = set().union(*F) if F else set()
    primes = list(primes)
    n = len(primes)
    if n <= 20:
        return minimal_hitting_sets(F)
    # else use heuristic sampling to find a disjoint pair if any
    # For intersecting check, we can try to find two disjoint minimal hitting sets via SAT style.
    # This is NP-hard; but we can attempt to find disjoint pair by brute force search for small sizes.

    # To test intersecting, we need to know if there exist two minimal hitting sets disjoint.
    # Equivalent to exists partition of ... Could search via brute force for small sizes.

    # For now return None
    return None

# For large families, we will just simulate sequence using direct gcd rule for many steps to see if pattern emerges eventually periodic with period maybe large.
# Let's brute force gcd sequence for a1=35 for many steps (5000) using efficient gcd checking
def gen_gcd(a1, N):
    seq=[a1]
    # keep list of prime factor sets? but gcd check with all previous numbers is expensive O(N^2). However we can use condition that checking gcd with minimal family only? Since gcd>1 with all previous is equivalent to hitting minimal family. So we can maintain minimal family and just check if S contains member -> actually to test if number m is allowed we need to check if its prime set hits all F (which is equivalent to checking if it contains F member if H intersecting? No earlier).
    # For generation, we can use family F approach: number m is allowed iff its prime set hits F (i.e., contains some hitting set). Which is equivalent to m divisible by some p(h) for h in H.
    # So to generate next term, we need H, but H may be large to compute.
    # Alternative: direct gcd checking with previous numbers but using prime sets of previous numbers? Still need to check against all previous terms, but number of terms large (5000) and numbers up to maybe 20000, gcd checking O(N^2) may be okay for 5000 (25M gcd ops) maybe heavy but okay in Python with optimization maybe not.
    # We can maintain for each previous term its prime set? Actually gcd>1 with each previous term equivalent to for each previous term share at least one prime, which is equivalent to hitting minimal family only? Wait need to check: Condition "for all i ≤ n, gcd(a_{n+1}, a_i)>1" is equivalent to S_{n+1} intersects S_i for each i, not just minimal ones? But if S_i is superset of some minimal set, intersecting S_i's superset implies intersecting the minimal? Actually if S_i ⊇ T, then if S_{n+1} intersects T, it automatically intersects S_i? No, intersection with T ⊂ S_i implies intersection with S_i (since T subset). So it suffices to intersect minimal sets. So we only need to check hitting minimal family.
    # So number of checks is |F| not n.
    seq=[a1]
    S1=prime_factors_set(a1)
    F=[S1]
    a=a1
    for _ in range(N-1):
        # compute H for current F
        H=minimal_hitting_sets(F)
        if H is None:
            print("H too large at step", len(seq), "F size", len(F))
            # fallback to direct gcd checking using family F (|F| maybe smaller than n)
            # To find next number, we can iterate m = a+1 upwards and test if prime set hits F
            # Test hitting F directly: for each set T in F, need intersection non-empty
            # That is cheaper than computing H if F size small but H huge.
            # We'll find next m by scanning
            m=a+1
            while True:
                Sm=prime_factors_set(m)
                ok=True
                for Tf in F:
                    if Sm.isdisjoint(Tf):
                        ok=False
                        break
                if ok:
                    break
                m+=1
            a=m
            seq.append(a)
            # update F
            # check if Sm contains some T in F
            contains=False
            for Tf in F:
                if Tf.issubset(Sm):
                    contains=True
                    break
            if not contains:
                F=minimal_family(F+[Sm])
            continue
        # using H to find next multiple quickly
        best=None
        best_h=None
        for h in H:
            prod=math.prod(list(h))
            nxt=(a//prod+1)*prod
            if nxt<=a:
                nxt+=prod
            if best is None or nxt<best:
                best=nxt
                best_h=h
        a=best
        seq.append(a)
        S=prime_factors_set(a)
        # update
        contains=False
        for Tf in F:
            if Tf.issubset(S):
                contains=True
                break
        if not contains:
            F=minimal_family(F+[S])
    return seq,F

seq,F = gen_gcd(35, 3000)
print(f"seq len {len(seq)} F size {len(F)} F {F[:20]} tail {seq[-20:]}")
# check gaps
diffs=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
print("max gap", max(diffs[500:]), "min gap", min(diffs[500:]))
# attempt to detect ultimate period if H intersecting
H=minimal_hitting_sets(F)
if H is not None:
    print("H size", len(H), "intersecting?", is_intersecting_family(H), "prods sample", [math.prod(list(h)) for h in H[:10]])
else:
    print("H too large to compute")

# also run for 105
seq,F = gen_gcd(105, 3000)
print(f"\n105 seq len {len(seq)} F size {len(F)} tail {seq[-20:]}")
H=minimal_hitting_sets(F)
if H is not None:
    print("H size", len(H), "intersecting?", is_intersecting_family(H))
else:
    print("H too large")
