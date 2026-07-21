import itertools

def clutters_ground(n, max_size=5):
    ground = list(range(n))
    all_sets = []
    for r in range(1, n+1):
        for comb in itertools.combinations(ground, r):
            all_sets.append(set(comb))
    # generate antichains? brute force enumeration of clutters (antichains) is huge; we can limit to small families
    # Instead enumerate intersecting families of sets where each set size <=3 maybe
    # We'll generate random intersecting antichains and test condition
    pass

def minimal_family(sets):
    # sets list of set, return antichain minimal
    uniq=[]
    seen=set()
    for s in sets:
        fs=frozenset(s)
        if fs not in seen:
            seen.add(fs)
            uniq.append(set(s))
    uniq.sort(key=lambda x: len(x))
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

def minimal_hitting_sets(F):
    if not F:
        return []
    primes = set().union(*F)
    primes = list(primes)
    n = len(primes)
    if n>12:
        return None
    prime_to_idx={p:i for i,p in enumerate(primes)}
    F_masks=[]
    for s in F:
        mask=0
        for p in s:
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
        is_min=True
        for m in minimal:
            if (m & hm)==m:
                is_min=False
                break
        if is_min:
            minimal.append(hm)
    res=[]
    for hm in minimal:
        s=set()
        for i in range(n):
            if hm>>i &1:
                s.add(primes[i])
        res.append(s)
    return res

def is_intersecting(F):
    for i in range(len(F)):
        for j in range(i+1, len(F)):
            if F[i].isdisjoint(F[j]):
                return False
    return True

def contains_some(T, M):
    # does T contain some member of M?
    for S in M:
        if S.issubset(T):
            return True
    return False

def test_random():
    import random
    # generate random intersecting clutters on ground 0..5
    ground = list(range(6))
    # generate all subsets size 2-3 maybe
    all_subsets=[]
    for r in [2,3]:
        for comb in itertools.combinations(ground, r):
            all_subsets.append(set(comb))
    # many random trials
    for trial in range(20000):
        # pick random size
        k=random.randint(1,8)
        chosen=random.sample(all_subsets, k)
        if not is_intersecting(chosen):
            continue
        M=minimal_family(chosen)
        if not M:
            continue
        # ensure intersecting
        if not is_intersecting(M):
            continue
        H=minimal_hitting_sets(M)
        if H is None:
            continue
        # check H intersecting?
        if not is_intersecting(H):
            continue
        # check if every H contains some M
        for h in H:
            if not contains_some(h, M):
                # found counterexample: H intersecting but some H not containing M
                print(f"Counterexample found M={M} H={H} bad h={h}")
                return True
    print("No counterexample in random trials")
    return False

test_random()

# exhaustive enumeration for ground 0..4 all antichains
ground = list(range(5))
all_subsets=[]
for r in range(1,4):
    for comb in itertools.combinations(ground, r):
        all_subsets.append(set(comb))
# enumerate all antichains of size up to 4? Number of antichains is huge (Dedekind), but ground 5 has 7581 antichains, manageable?
# We'll enumerate all antichains via brute force recursion
def all_antichains(ground_subsets):
    # use recursion over sorted subsets by size
    # For simplicity, generate all subsets of subsets collection and filter
    n=len(ground_subsets)
    # 2^... too large (C(5,2)+C(5,1)+... approx 15 inclusive). 2^15=32768 manageable
    all_subs = ground_subsets
    best=[]
    for mask in range(1<<len(all_subs)):
        chosen=[all_subs[i] for i in range(len(all_subs)) if mask>>i &1]
        # quick filter intersecting?
        # first check antichain
        ok=True
        for i in range(len(chosen)):
            for j in range(i+1, len(chosen)):
                if chosen[i].issubset(chosen[j]) or chosen[j].issubset(chosen[i]):
                    ok=False
                    break
            if not ok:
                break
        if not ok:
            continue
        if not is_intersecting(chosen):
            continue
        M=chosen
        H=minimal_hitting_sets(M)
        if H is None:
            continue
        if not is_intersecting(H):
            continue
        # check contains
        fail=False
        for h in H:
            if not contains_some(h, M):
                print(f"Counterexample exhaustive M={M} H={H}")
                fail=True
                break
        # if not fail and H intersecting, we have example where condition holds? Let's also record
        # We want cases where H intersecting but not maximal
        if fail:
            pass
    print("exhaustive for ground 0..4 up to size 3 subsets done")

all_antichains(all_subsets)

# Let's also search ground 6 with subsets size 2 and 3 for example where H intersecting but not super
ground=list(range(6))
all_subs=[]
for r in [2,3]:
    for comb in itertools.combinations(ground, r):
        all_subs.append(set(comb))
# attempt exhaustive over antichains of size up to 5: choose 5 out of maybe 35: huge. So random already done.

# But maybe we can directly search for M where H intersecting and some h not containing T, we already attempted random and found none, suggests equivalence might hold for clutters up to small size? Could be theorem?

# Let's attempt to prove: if M intersecting, then H intersecting implies every h contains some member of M.
# Suppose contrary there exists minimal hitting set h0 that does not contain any member of M.
# Then for each T in M, |T ∩ h0| ≥1, but T not subset of h0.
# Since h0 is minimal hitting, for each p in h0, there exists T_p in M such that T_p ∩ h0 = {p} (critical sets). This is property of minimal hitting sets: each element is essential.
# So we have for each p∈h0, a set T_p with intersection exactly {p}.
# Now consider two distinct p,q ∈ h0. T_p and T_q intersect somewhere (since M intersecting). Their intersection cannot be p or q unless... Let's analyze.
# T_p ∩ h0 = {p}, T_q ∩ h0 = {q}. So any element in T_p ∩ T_q cannot be in h0 except possibly if it equals p=q, which not. So T_p ∩ T_q is disjoint from h0.
# So there exists element x_{p,q} ∈ T_p ∩ T_q that is outside h0.
# This doesn't directly give disjointness of hitting sets, but maybe we can build two disjoint hitting sets from the T_p's ?
# Let's attempt to construct another hitting set disjoint from h0 ??? But h0 hits all T, so any hitting set disjoint from h0 would be disjoint from h0, contradicting intersecting property if it were minimal hitting. So we need to build a hitting set disjoint from h0 using the x's.
# Idea: Let H' be set of all those intersection points ??? Might yield a hitting set disjoint from h0.

# Attempt to formalize: Suppose h0 does not contain any T. Then for each p, T_p contains p plus other elements outside h0. Maybe we can combine?

# Let's brute search proof attempt via SAT for small sizes to see if counterexample exists for larger ground maybe >6. Our random didn't find.
# Let's increase random ground to 10 with larger sets size up to 4 random antichains intersecting.

def random_search2(trials=20000, ground_n=8):
    import random
    ground=list(range(ground_n))
    all_subsets=[]
    for r in range(2,5):
        for comb in itertools.combinations(ground, r):
            all_subsets.append(set(comb))
    for _ in range(trials):
        # generate random intersecting family by starting empty and adding random sets that keep intersecting
        M=[]
        attempts=20
        for __ in range(attempts):
            s=random.choice(all_subsets)
            # check if adding s keeps intersecting and antichain
            # check intersect with existing
            ok=True
            for t in M:
                if s.isdisjoint(t):
                    ok=False
                    break
            if not ok:
                continue
            # antichain condition: no subset
            for t in M:
                if t.issubset(s) or s.issubset(t):
                    ok=False
                    break
            if not ok:
                continue
            M.append(s)
        if len(M)==0:
            continue
        M=minimal_family(M)
        if not is_intersecting(M):
            continue
        # compute H
        H=minimal_hitting_sets(M)
        if H is None:
            continue
        if not is_intersecting(H):
            continue
        # check contains
        for h in H:
            if not contains_some(h, M):
                print(f"Counterexample2 M={M} H={H} bad {h}")
                return True
    print(f"No counterexample random2 ground {ground_n} trials {trials}")
    return False

random_search2(10000, 10)
