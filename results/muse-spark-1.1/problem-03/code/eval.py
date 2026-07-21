import random, itertools, math

def f_val(pieces):
    q = sorted(pieces, reverse=True)
    s=0
    for i in range(0,len(q),2):
        s+=q[i]
    return s

def best_Xiang(a, n_cut, grid_res=41, random_extra=5000):
    """
    a: list of lengths summing to 1
    n_cut: max cuts Xiang can use
    Compute minimal achievable f via enumeration over t allocations and grid search.
    Returns minimal f.
    """
    m=len(a)
    # generate t tuples sum <= n_cut
    def gen(idx, rem, cur):
        if idx==m:
            yield tuple(cur)
            return
        for ti in range(rem+1):
            cur.append(ti)
            yield from gen(idx+1, rem-ti, cur)
            cur.pop()
    t_list=list(gen(0,n_cut,[]))
    best=1.0
    best_cfg=None

    for t in t_list:
        # total continuous variables = sum(t)
        # if sum=0 -> evaluate directly
        if sum(t)==0:
            fv=f_val(a)
            if fv<best:
                best=fv
                best_cfg=(t,a)
            continue
        # We'll perform grid search + random
        # For each ti, we need ti cut positions inside interval ai
        # Represent as sorted uniform cuts in [0,ai]
        # For ti=1, single parameter r = cut position fraction
        # For ti=2, two parameters c1<c2 in (0,1)
        # For ti=3, three parameters etc.
        # For grid, we'll use discretization of cut positions at multiples of 1/grid_res

        # Build per-interval grid options
        # For each i, generate list of possible fragment lists for that interval
        # For ti=1: options = [[r,1-r]*ai for r in grid]
        # For ti=2: options for (c1,c2) grid
        # For larger ti, combinatorial explosion, use random only
        # We'll produce product across intervals via nested loops if total combos manageable
        # For n<=3, max ti <=3 and m<=4, total combos may be moderate if we limit per interval options to ~40
        # Instead of product, we will do random search plus some systematic when ti small

        # Precompute per i options for grid
        per_i_options=[]
        for ai,ti in zip(a,t):
            if ti==0:
                per_i_options.append([[ai]])
            elif ti==1:
                opts=[]
                for k in range(1,grid_res):
                    r=k/grid_res
                    opts.append([r*ai,(1-r)*ai])
                per_i_options.append(opts)
            elif ti==2:
                opts=[]
                # grid for c1<c2
                for k in range(1,grid_res):
                    for l in range(k+1,grid_res):
                        c1=k/grid_res
                        c2=l/grid_res
                        opts.append([c1*ai,(c2-c1)*ai,(1-c2)*ai])
                per_i_options.append(opts)
            elif ti==3:
                opts=[]
                # choose 3 cuts: for grid_res ~21 to keep size manageable
                # We'll sample limited
                for _ in range(2000):
                    c=sorted([random.random() for __ in range(3)])
                    opts.append([c[0]*ai,(c[1]-c[0])*ai,(c[2]-c[1])*ai,(1-c[2])*ai])
                per_i_options.append(opts)
            else:
                # ti>3 use random options
                opts=[]
                for _ in range(2000):
                    c=sorted([random.random() for __ in range(ti)])
                    frags=[]
                    prev=0
                    for cc in c:
                        frags.append((cc-prev)*ai)
                        prev=cc
                    frags.append((1-prev)*ai)
                    opts.append(frags)
                per_i_options.append(opts)

        # Now total combinations product
        # If product too large, use random sampling across product
        # Compute product size estimate
        prod_size=1
        for opts in per_i_options:
            prod_size*=len(opts)
            if prod_size>200000:
                break
        if prod_size<=200000:
            # enumerate product via iterative
            # Use recursion/generation
            # Python loop over product via itertools.product
            for combo in itertools.product(*per_i_options):
                # combo is per interval fragments list
                pieces=[]
                for frags in combo:
                    pieces.extend(frags)
                fv=f_val(pieces)
                if fv<best:
                    best=fv
                    best_cfg=(t,pieces)
        else:
            # random sampling across product
            for _ in range(random_extra*2):
                pieces=[]
                for opts in per_i_options:
                    frags=random.choice(opts)
                    pieces.extend(frags)
                fv=f_val(pieces)
                if fv<best:
                    best=fv
                    best_cfg=(t,pieces)
            # additional pure random
            for _ in range(random_extra):
                pieces=[]
                for ai,ti in zip(a,t):
                    if ti==0:
                        pieces.append(ai)
                    else:
                        cuts=sorted([random.random() for __ in range(ti)])
                        prev=0
                        for c in cuts:
                            pieces.append((c-prev)*ai)
                            prev=c
                        pieces.append((1-prev)*ai)
                fv=f_val(pieces)
                if fv<best:
                    best=fv
                    best_cfg=(t,pieces)

    return best,best_cfg

def test_geometric():
    for n in [1,2,3,4,5]:
        S=2**(n+1)-1
        a=[2**k / S for k in range(n+1)]
        best,cfg=best_Xiang(a,n,grid_res=21, random_extra=5000)
        print(f"n={n} geom best approx {best:.6f} = {best*S:.4f}/{S} target {2**n}/{S}={2**n/S:.6f} cfg t={cfg[0]}")

test_geometric()

def search_Liu_n(n, outer_iters=200):
    best_L=-1
    best_a=None
    best_X=None
    for it in range(outer_iters):
        # random a Dirichlet
        exps=[-math.log(random.random()+1e-12) for _ in range(n+1)]
        s=sum(exps)
        a=[e/s for e in exps]
        # evaluate
        val,_=best_Xiang(a,n,grid_res=15, random_extra=2000)  # coarse for speed
        if val>best_L:
            best_L=val
            best_a=a[:]
            print(f" n={n} outer {it} new best coarse {best_L:.6f} a {[f'{x:.3f}' for x in a]}")
            # refine precise for this a
            val2,_=best_Xiang(a,n,grid_res=41, random_extra=8000)
            if val2>best_L:
                best_L=val2
            # keep maybe?
    # final refinement
    print(f"\n=== Final refinement for n={n} best {best_L:.6f} a {best_a}")
    if best_a:
        val_precise,cfg=best_Xiang(best_a,n,grid_res=51, random_extra=20000)
        print(f"Precise refinement: {val_precise:.6f} cfg {cfg[0]}")
        # local search around best_a
        cur_a=best_a[:]
        cur_best=val_precise
        for step in range(200):
            sigma=0.05
            new_a=[max(1e-6, x+random.gauss(0,sigma)) for x in cur_a]
            s=sum(new_a)
            new_a=[x/s for x in new_a]
            val,_=best_Xiang(new_a,n,grid_res=21, random_extra=5000)
            if val>cur_best:
                cur_best=val
                cur_a=new_a
                print(f" local {step} improved to {cur_best:.6f} a {[f'{x:.4f}' for x in cur_a]}")
        # final
        final_val,cfg=best_Xiang(cur_a,n,grid_res=61, random_extra=20000)
        print(f" FINAL n={n} {final_val:.6f} a {cur_a}")
        return final_val,cur_a
    return best_L,best_a

for n in [2,3,4]:
    search_Liu_n(n, outer_iters=200)

