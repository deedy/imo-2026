import random, itertools, math

def f_value(pieces):
    # pieces list of floats
    q = sorted(pieces, reverse=True)
    s=0.0
    for i in range(0,len(q),2):
        s+=q[i]
    return s

def random_split(total, k):
    # split total into k parts (k = t+1) sum to total, each >0 allowed tiny
    # sample k-1 cut points uniform sorted
    # Dirichlet uniform
    if k==1:
        return [total]
    cuts = sorted([random.random() for _ in range(k-1)])
    # map to simplex via order stats of uniform
    # Actually Dirichlet with uniform order stats: we need spacings
    # Use random points in simplex via exponential or uniform
    # Simpler: generate k-1 uniform, sort, take differences multiplied by total
    prev=0.0
    parts=[]
    for c in cuts:
        parts.append((c-prev)*total)
        prev=c
    parts.append((1-prev)*total)
    return parts

def random_split_with_dust_bias(total, k, dust_prob=0.3):
    # occasionally produce dust pieces
    # produce parts with one tiny epsilon
    if random.random()<dust_prob and k>1:
        # make one piece = total - eps, rest eps/(k-1) tiny
        eps = random.random()* total * 0.01  # tiny
        # Actually make k-1 tiny pieces sum to eps
        if k-1==1:
            return [total-eps, eps]
        # split eps into k-1 parts
        cuts = sorted([random.random() for _ in range(k-2)]) if k-1>1 else []
        prev=0.0
        tiny=[]
        for c in cuts:
            tiny.append((c-prev)*eps)
            prev=c
        tiny.append((1-prev)*eps)
        # choose position of big piece randomly? but sorted later
        parts = [total-eps] + tiny
        # shuffle? but not needed
        return parts
    else:
        # uniform simplex
        # use Dirichlet via exponentials
        exps = [random.random() for _ in range(k)] # not exp but uniform -> not uniform but okay
        # Actually use random exponentials for uniform simplex
        # Using -log(U)
        exps = [-math.log(random.random()+1e-12) for _ in range(k)]
        s=sum(exps)
        return [e/s*total for e in exps]

def best_Xiang_for_a(a, n_trials_per_dist=20000):
    # a list len m0
    m0=len(a)
    best = f_value(a) # no cuts
    best_detail=None

    # generate all distributions of t_i sum <= n (n = max cuts = len(a?) actually original n)
    # But for evaluating for n=2, total cuts allowed up to n
    # Here we need to consider general n as global; pass as parameter? Use len? We'll assume n = len(a)-1? Actually n = initial max points; a length = n+1 if Liu uses max.
    # For n=2 case, n=2.
    # We'll assume n = m0-1 (if Liu uses all)
    n = m0-1 # for initial full use
    # but we also want generic, we will later handle.

    # enumerate tuples t_i >=0 sum <= n
    # for small n we can brute force loops.
    # For each tuple, we know k_i = t_i+1 parts per interval.

    # Use recursion to generate
    def gen_tuples(idx, remaining, cur):
        if idx==m0:
            yield tuple(cur)
            return
        for ti in range(remaining+1):
            cur.append(ti)
            yield from gen_tuples(idx+1, remaining-ti, cur)
            cur.pop()
    for t_tuple in gen_tuples(0,n,[]):
        ks = [t+1 for t in t_tuple]
        # skip all zero? include
        # Now do random search over splits
        for _ in range(n_trials_per_dist):
            pieces=[]
            for total,k in zip(a,ks):
                if k==1:
                    pieces.append(total)
                else:
                    parts = random_split_with_dust_bias(total,k)
                    pieces.extend(parts)
            val = f_value(pieces)
            if val < best - 1e-12:
                best=val
                best_detail=(t_tuple, pieces)
    return best, best_detail

def evaluate_many_a_random(n, n_a_samples=2000, inner_trials=5000):
    best_for_Liu = -1
    best_a=None
    best_detail=None
    for _ in range(n_a_samples):
        # sample a Dirichlet
        exps = [-math.log(random.random()+1e-12) for _ in range(n+1)]
        s=sum(exps)
        a=[e/s for e in exps]
        # a may be small random, but also include structured candidates later
        val,detail = best_Xiang_for_a(a, n_trials_per_dist=inner_trials)
        if val> best_for_Liu:
            best_for_Liu=val
            best_a=a
            best_detail=detail
    return best_for_Liu, best_a, best_detail

# Test n=1
def test_n1():
    print("=== n=1 ===")
    # a has 2 pieces
    # brute over a
    best=0
    best_a=None
    for a1 in [i/100 for i in range(1,100)]:
        a=[a1,1-a1]
        val,_ = best_Xiang_for_a(a, n_trials_per_dist=2000)
        if val>best:
            best=val
            best_a=a
    print("best",best,best_a)

# test_n1()

def approx_n(n):
    print(f"=== Approx n={n} ===")
    # sample a with optimization using larger inner trials for top candidates
    # start random search
    best_val=-1
    best_a=None
    for iter in range(5):
        v,a,d = evaluate_many_a_random(n, n_a_samples=2000, inner_trials=2000)
        print(f"iter sample best {v} a {a}")
        if v>best_val:
            best_val=v
            best_a=a
    # refine around best_a
    if best_a is not None:
        # local search
        for _ in range(2000):
            # perturb
            new_a = [max(1e-6, x+random.gauss(0,0.02)) for x in best_a]
            s=sum(new_a)
            new_a=[x/s for x in new_a]
            v,d = best_Xiang_for_a(new_a, n_trials_per_dist=5000)
            # Actually function returns tuple
            # best_Xiang returns (best, detail)
            if v>best_val:
                best_val=v
                best_a=new_a
                print("improved local",best_val,best_a)
    # final evaluation with high trials
    final_val,detail = best_Xiang_for_a(best_a, n_trials_per_dist=20000)
    print(f"FINAL n={n} best val approx {final_val} a {best_a} detail {detail}")

# Try n=2 quick
approx_n(2)

# Also try n=3
approx_n(3)

