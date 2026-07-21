import random, math, itertools

def f_sorted(pieces):
    q=sorted(pieces, reverse=True)
    s=0.0
    for i in range(0,len(q),2):
        s+=q[i]
    return s, q

def best_Xiang(a, trials=20000, refine_iters=2000):
    n=2
    m=len(a)
    best=float('inf')
    best_cfg=None
    # enumerate t tuples
    def gen_tuples(idx, rem, cur):
        if idx==m:
            yield tuple(cur)
            return
        for ti in range(rem+1):
            cur.append(ti)
            yield from gen_tuples(idx+1, rem-ti, cur)
            cur.pop()
    for t in gen_tuples(0,n,[]):
        # for each t, we have sum_{ti} (ti+1) variables but simplex constraint per piece
        # total number of continuous variables = sum(t)
        # we can param by split ratios per piece: for ti=1, one variable r in (0,1)
        # ti=2, two variables: r1,r2 with r1>0,r2>0,r1+r2<1
        # We'll random sample many times
        for _ in range(trials):
            pieces=[]
            for ai,ti in zip(a,t):
                if ti==0:
                    pieces.append(ai)
                elif ti==1:
                    r=random.random()
                    # occasional bias to small
                    if random.random()<0.3:
                        r=random.random()*0.2
                    if random.random()<0.3:
                        r=1-random.random()*0.2
                    pieces.append(r*ai)
                    pieces.append((1-r)*ai)
                elif ti==2:
                    # split into 3
                    u1=random.random()
                    u2=random.random()
                    if u1>u2:
                        u1,u2=u2,u1
                    pieces.append(u1*ai)
                    pieces.append((u2-u1)*ai)
                    pieces.append((1-u2)*ai)
            fv,_=f_sorted(pieces)
            if fv<best:
                best=fv
                best_cfg=(t,list(pieces))
        # Try local refinement via hill climbing on best for this t (maybe later)
    # Additional refined search for top t candidates using simple hill climbing
    # We'll run extra refinement loops
    for _ in range(refine_iters):
        # perturb around current best_cfg if exists
        if best_cfg is None:
            break
        t_cur,_ = best_cfg
        # generate new random near? We'll just continue random but with best t
        # Actually we already sampled all t, but let's focus on best t overall?
        pass
    return best, best_cfg

def search_Liu_n2_fine():
    # use differential evolution like random search over a simplex
    best_L= -1
    best_a=None
    best_X=None
    for iter in range(5000):
        # sample a from Dirichlet uniform
        exps=[-math.log(random.random()+1e-12) for _ in range(3)]
        s=sum(exps)
        a=[e/s for e in exps]
        # optional: sort descending to avoid permutation? keep as list unsorted but pieces order doesn't matter for best_Xiang since t distribution cares which piece big, but a sorted descending will give same minimal because Xiang can choose which a to split.
        # So sort descending
        a_sorted=sorted(a, reverse=True)
        val,cfg = best_Xiang(a_sorted, trials=500, refine_iters=0)
        if val>best_L:
            best_L=val
            best_a=list(a_sorted)
            best_X=cfg
            print(f"iter {iter} new best Liu {best_L:.5f} a {best_a} Xiang best {val:.5f} t {cfg[0] if cfg else None}")
    return best_L,best_a,best_X

def coarse_grid():
    best=0
    best_a=None
    for a1 in [i/20 for i in range(1,20)]:
        for a2 in [j/20 for j in range(1,20)]:
            if a1 + a2 >=1: continue
            a3=1-a1-a2
            if a3<=0: continue
            a=sorted([a1,a2,a3], reverse=True)
            val,cfg=best_Xiang(a, trials=2000)
            if val>best:
                best=val
                best_a=a
                print(f"grid a {a} val {val:.4f} cfg {cfg[0]}")
    print("final best grid",best,best_a)

coarse_grid()
