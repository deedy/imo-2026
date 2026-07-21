import random, math

def f(pieces):
    q=sorted(pieces, reverse=True)
    return sum(q[i] for i in range(0,len(q),2))

def best_Xiang_response(a, n_cut, trials=8000):
    m=len(a)
    # allocations of cuts: composition of up to n_cut into m bins
    # We'll sample allocations randomly proportional to search
    best_val = 1.0
    best_cfg = None
    # Enumerate t tuples for small n,m maybe all
    # For n=2,m=3, enumerates 6 combos of sum=2 plus sums <2 also allowed (since at most n). Include <=n.
    # Let's generate all tuples summing <= n with stars bars
    def gen_tuples(idx, remaining, cur):
        if idx==m:
            # any remaining unused cuts is allowed, so we yield cur padded? Actually we need sum <= n, so cur sum <=n already.
            yield tuple(cur)
            return
        for ti in range(remaining+1):
            cur.append(ti)
            yield from gen_tuples(idx+1, remaining-ti, cur)
            cur.pop()
    t_list = list(gen_tuples(0,n_cut,[]))
    # For each t, we need to minimize f over splits of each a_i into ti+1 parts
    # This is an optimization problem inner. For small m and tiny ti, we can brute via random + local.
    # For ti=0, no split
    # For ti=1, split ratio r in (0,1)
    # For ti=2, split ratios for 3 parts
    # We'll do random search per t.
    for t in t_list:
        # quick upper bound: if best already high?
        for _ in range(trials//max(1,len(t_list))):
            pieces=[]
            for ai,ti in zip(a,t):
                if ti==0:
                    pieces.append(ai)
                elif ti==1:
                    r=random.random()
                    # maybe bias towards extreme to reduce f for Xiang? We'll sample with beta
                    # Let's mix uniform and extreme
                    if random.random()<0.5:
                        r = random.random()*0.2  # close to 0
                    pieces.append(r*ai)
                    pieces.append((1-r)*ai)
                elif ti==2:
                    # 3 parts: sample dirichlet with random concentration
                    # Use uniform dirichlet sometimes and extreme sometimes
                    exps=[-math.log(random.random()+1e-12) for __ in range(3)]
                    s=sum(exps)
                    # also try extreme where one middle piece large
                    if random.random()<0.3:
                        # make one piece large ~0.5, others small
                        # contrive
                        r = random.random()
                        # produce parts: make middle large
                        # just keep dirichlet but it's okay
                        pass
                    for e in exps:
                        pieces.append(e/s*ai)
                else:
                    # ti>2, larger
                    exps=[-math.log(random.random()+1e-12) for __ in range(ti+1)]
                    s=sum(exps)
                    for e in exps:
                        pieces.append(e/s*ai)
            val=f(pieces)
            if val<best_val:
                best_val=val
                best_cfg=(t,pieces)
    return best_val, best_cfg


def optimize_Liu(n, outer_iters=2000, inner_trials=4000):
    best_Liu_val=-1
    best_a=None
    best_X=None
    for it in range(outer_iters):
        # sample a Dirichlet uniform on simplex of dimension n (n+1 parts)
        exps=[-math.log(random.random()+1e-12) for _ in range(n+1)]
        s=sum(exps)
        a=[e/s for e in exps]
        val,cfg = best_Xiang_response(a, n, trials=inner_trials)
        if val>best_Liu_val:
            best_Liu_val=val
            best_a=a.copy()
            best_X=cfg
            print(f"new best outer {it} val {val:.5f} a {['%.3f'%x for x in a]} cfg {cfg[0]}")
    return best_Liu_val,best_a,best_X

for n in [1,2,3,4]:
    print(f"\n=== Optimizing n={n} ===")
    best_val,a,cfg = optimize_Liu(n, outer_iters=500, inner_trials=2000)
    print(f"Result n={n} best ~{best_val:.4f} a {a}")

