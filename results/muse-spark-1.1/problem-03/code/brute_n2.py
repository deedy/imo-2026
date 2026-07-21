import random, math, itertools

def f_val(pieces):
    q=sorted(pieces, reverse=True)
    return sum(q[i] for i in range(0,len(q),2)), q

def best_Xiang_for_a(a, inner_samples=5000):
    """
    a list of piece sizes (sum 1)
    Xiang has up to n=2 cuts
    Compute minimal achievable f via search over split parameters.
    We'll enumerate t distributions and for each do random search + also evaluation of special points where split sizes equal other pieces etc.
    Return min f.
    """
    n=2 # total cuts Xiang
    m=len(a)
    best=float('inf')
    best_cfg=None
    # generate all t tuples sum <=n
    def gen_tuples(idx, rem, cur):
        if idx==m:
            yield tuple(cur)
            return
        for ti in range(rem+1):
            cur.append(ti)
            yield from gen_tuples(idx+1, rem-ti, cur)
            cur.pop()
    for t in gen_tuples(0,n,[]):
        # if sum(t) < n, we allow unused cuts, but essentially that's covered by allowing some t small, but we also have case of using less cuts -> still t sum <n.
        # So keep all.
        # For each t, we need to minimize over splits.
        # We'll perform random search with many samples
        # Additionally, for low-dimensional splits we can also try grid search over split ratios.
        for _ in range(inner_samples):
            pieces=[]
            for ai, ti in zip(a,t):
                if ti==0:
                    pieces.append(ai)
                elif ti==1:
                    r = random.random()
                    # bias towards equal split sometimes to reduce f
                    # but keep uniform
                    pieces.append(r*ai)
                    pieces.append((1-r)*ai)
                elif ti==2:
                    # split into 3: generate 3 random positive summing to ai
                    # Dirichlet random
                    e = [random.random() for __ in range(3)]
                    # Actually use uniform simplex: generate 2 random sorted cuts
                    u1, u2 = random.random(), random.random()
                    if u1>u2:
                        u1,u2 = u2,u1
                    pieces.append(u1*ai)
                    pieces.append((u2-u1)*ai)
                    pieces.append((1-u2)*ai)
            fv,_ = f_val(pieces)
            if fv<best:
                best=fv
                best_cfg=(t,pieces)
        # additionally for t with single cut on one piece, we can attempt to find optimal r exactly by evaluating critical thresholds
        # For t=(1,0,0) etc where only one piece splitted into two, the function f(r) is piecewise linear? Actually sorted order changes at values where r*a = some other piece b or c.
        # We can evaluate r at values b/a, c/a etc plus around etc.
        # Let's handle case of exactly one split overall (total pieces 4)
        if sum(t)==1:
            # find index j where tj=1
            for j in range(m):
                if t[j]==1:
                    aj=a[j]
                    others=[a[k] for k in range(m) if k!=j]
                    # candidate r values where split pieces equal others
                    # split pieces are r*aj and (1-r)*aj
                    # For sorted order, the values that matter are when r*aj = other or (1-r)*aj = other
                    cand=set()
                    for b in others:
                        if b<aj:
                            cand.add(b/aj)
                            cand.add(1-b/aj)
                    # also r=0.5
                    cand.add(0.5)
                    # evaluate near those
                    for rc in cand:
                        for delta in [-1e-6,0,1e-6]:
                            r=rc+delta
                            if 0<r<1:
                                pieces=[]
                                for k in range(m):
                                    if k==j:
                                        pieces.append(r*aj)
                                        pieces.append((1-r)*aj)
                                    else:
                                        pieces.append(a[k])
                                fv,_ = f_val(pieces)
                                if fv<best:
                                    best=fv
                                    best_cfg=(t,pieces)
        # for t sum=2 but distribution (2,0,0) splitting one piece into 3
        # similarly we could grid search but random might be enough
        # for (1,1,0) two pieces each split into 2: we have two parameters r1,r2. Critical values where pieces equal each other or other piece.
        # Could do more exhaustive grid for n=2 with resolution 100x100
        if t in [(1,1,0),(1,0,1),(0,1,1)]:
            # indices of split pieces
            idxs=[i for i,ti in enumerate(t) if ti==1]
            if len(idxs)==2:
                i1,i2=idxs
                a1,a2 = a[i1],a[i2]
                other_idx = 3 - i1 - i2 if m==3 else None
                # grid
                for r1 in [k/50 for k in range(1,50)]:
                    # quick?
                    pass
    return best, best_cfg

def search_Liu_n2(grid_step=0.05, inner=3000):
    best_for_Liu=-1
    best_a=None
    # iterate over a1,a2,a3 summing to 1 with step
    n_steps=int(1/grid_step)
    for i in range(n_steps+1):
        a1=i*grid_step
        for j in range(n_steps+1 - i):
            a2=j*grid_step
            a3=1-a1-a2
            if a3< -1e-9:
                continue
            if a3<0:
                a3=0
            # sorting? Liu's pieces order doesn't matter, but we have list
            a=[a1,a2,a3]
            # skip if any zero? but allow maybe? at most n cuts gives up to 3 pieces, but zero pieces correspond to fewer cuts (collocated cuts). Let's require each >0.
            if min(a)<=1e-9:
                continue
            val,_ = best_Xiang_for_a(a, inner_samples=inner)
            if val>best_for_Liu:
                best_for_Liu=val
                best_a=a.copy()
                print(f"grid new best {best_for_Liu:.4f} a {best_a}")
    return best_for_Liu,best_a

# First quick test for specific a's
def test_specific():
    examples=[
        [0.4,0.4,0.2],
        [1/3,1/3,1/3],
        [0.5,0.25,0.25],
        [0.6,0.2,0.2],
        [0.45,0.35,0.2],
        [0.34,0.33,0.33]
    ]
    for a in examples:
        val,cfg=best_Xiang_for_a(a, inner_samples=20000)
        print(f"a {a} best Xiang {val:.4f} cfg {cfg[0]}")

test_specific()
print("\nGRID SEARCH")
search_Liu_n2(grid_step=0.05, inner=2000)
