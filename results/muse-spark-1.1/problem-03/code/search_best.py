import random, math, itertools, sys
import time

def f_val(pieces):
    # pieces list
    q = sorted(pieces, reverse=True)
    s=0.0
    for i in range(0,len(q),2):
        s+=q[i]
    return s

def best_Xiang_random(a, n, trials=20000):
    m=len(a)
    best=1.0
    best_cfg=None
    # precompute for speed
    for _ in range(trials):
        # sample t distribution: n balls into m bins via random multinomial
        t=[0]*m
        # use random allocation: for each of n cuts, choose bin uniformly
        for __ in range(n):
            idx=random.randrange(m)
            t[idx]+=1
        pieces=[]
        for ai,ti in zip(a,t):
            if ti==0:
                pieces.append(ai)
            else:
                # split ai into ti+1 random pieces: use uniform Dirichlet via sorted uniform cuts
                # generate ti random numbers in (0,1) sorted
                cuts=[random.random() for __ in range(ti)]
                cuts.sort()
                prev=0.0
                for c in cuts:
                    pieces.append((c-prev)*ai)
                    prev=c
                pieces.append((1-prev)*ai)
        fv=f_val(pieces)
        if fv<best:
            best=fv
            best_cfg=(tuple(t), pieces[:])
    # extra refinement: try to improve best via local perturbations of best_cfg's splits
    # We'll attempt hill climbing from best
    if best_cfg is not None:
        t_best,_ = best_cfg
        # do extra local search around best t
        for _ in range(trials//2):
            # use t_best
            pieces=[]
            for ai,ti in zip(a,t_best):
                if ti==0:
                    pieces.append(ai)
                else:
                    cuts=[random.random() for __ in range(ti)]
                    cuts.sort()
                    prev=0.0
                    for c in cuts:
                        pieces.append((c-prev)*ai)
                        prev=c
                    pieces.append((1-prev)*ai)
            fv=f_val(pieces)
            if fv<best:
                best=fv
                best_cfg=(t_best, pieces[:])
    return best,best_cfg

def best_Xiang_exact_n2(a):
    # exact via grid for n=2
    m=len(a)
    n=2
    best=1.0
    # generate t tuples sum <=n
    def gen(idx,rem,cur):
        if idx==m:
            yield tuple(cur)
            return
        for ti in range(rem+1):
            cur.append(ti)
            yield from gen(idx+1, rem-ti, cur)
            cur.pop()
    for t in gen(0,n,[]):
        # For each t, we can do dense grid search over split params
        # t = (t0,t1,t2) sum <=2
        # Cases:
        if sum(t)==0:
            fv=f_val(a)
            if fv<best:
                best=fv
        elif sum(t)==1:
            # single split
            idx=[i for i,ti in enumerate(t) if ti==1][0]
            ai=a[idx]
            others=[a[j] for j in range(m) if j!=idx]
            # evaluate at many r
            for k in range(1,1000):
                r=k/1000
                pieces=[r*ai,(1-r)*ai]+others
                fv=f_val(pieces)
                if fv<best:
                    best=fv
        elif sum(t)==2:
            if 2 in t:
                idx=[i for i,ti in enumerate(t) if ti==2][0]
                ai=a[idx]
                others=[a[j] for j in range(m) if j!=idx]
                # grid over 2 cuts
                for k in range(1,100):
                    for l in range(k+1,100):
                        c1=k/100
                        c2=l/100
                        pieces=[c1*ai,(c2-c1)*ai,(1-c2)*ai]+others
                        fv=f_val(pieces)
                        if fv<best:
                            best=fv
                # random extra
                for _ in range(5000):
                    c1=random.random()
                    c2=random.random()
                    if c1>c2:
                        c1,c2=c2,c1
                    pieces=[c1*ai,(c2-c1)*ai,(1-c2)*ai]+others
                    fv=f_val(pieces)
                    if fv<best:
                        best=fv
            else:
                # 1+1
                idxs=[i for i,ti in enumerate(t) if ti==1]
                i,j=idxs
                ai=a[i]; aj=a[j]
                ak=[a[k] for k in range(m) if k not in idxs][0]
                for ri in range(1,100):
                    for rj in range(1,100):
                        r_i=ri/100
                        r_j=rj/100
                        pieces=[r_i*ai,(1-r_i)*ai, r_j*aj,(1-r_j)*aj, ak]
                        fv=f_val(pieces)
                        if fv<best:
                            best=fv
                for _ in range(5000):
                    r_i=random.random()
                    r_j=random.random()
                    pieces=[r_i*ai,(1-r_i)*ai, r_j*aj,(1-r_j)*aj, ak]
                    fv=f_val(pieces)
                    if fv<best:
                        best=fv
    return best

def search_Liu_n(n, outer_trials=2000, inner_trials=5000):
    best_L=-1
    best_a=None
    for it in range(outer_trials):
        # sample a Dirichlet
        exps=[-math.log(random.random()+1e-12) for _ in range(n+1)]
        s=sum(exps)
        a=[e/s for e in exps]
        if n==2:
            val=best_Xiang_exact_n2(a)
        else:
            val,_=best_Xiang_random(a,n,trials=inner_trials)
        if val>best_L:
            best_L=val
            best_a=a[:]
            print(f"[n={n} outer={it}] new best {best_L:.6f} a {[f'{x:.4f}' for x in a]}")
    return best_L,best_a

# Test n=2 with exact
print("=== n=2 exact search ===")
best_L,best_a=search_Liu_n(2, outer_trials=2000, inner_trials=0)
print(f"final n=2 best {best_L:.6f} a {best_a}")

print("\n=== n=3 random search ===")
best_L,best_a=search_Liu_n(3, outer_trials=500, inner_trials=5000)
print(f"final n=3 best {best_L:.6f} a {best_a} target {8/15:.6f}")

