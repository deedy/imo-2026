import random, math

def f_val(pieces):
    q=sorted(pieces, reverse=True)
    s=0
    for i in range(0,len(q),2):
        s+=q[i]
    return s

def best_Xiang_n2_fast(a):
    # a list of 3
    best=1.0
    # 0 cuts
    best=min(best, f_val(a))
    # 1 cut
    for i in range(3):
        ai=a[i]
        others=[a[j] for j in range(3) if j!=i]
        # evaluate f as function of r in (0,1)
        # Since pieces = r*ai, (1-r)*ai, others
        # We can sample dense
        N=2001
        for k in range(1,N):
            r=k/N
            pieces=[r*ai,(1-r)*ai]+others
            fv=f_val(pieces)
            if fv<best:
                best=fv
    # 2 cuts: one piece into 3
    for i in range(3):
        ai=a[i]
        others=[a[j] for j in range(3) if j!=i]
        # parameterize by c1<c2
        # dense grid 101
        G=81
        for k in range(1,G):
            c1=k/G
            for l in range(k+1,G):
                c2=l/G
                pieces=[c1*ai,(c2-c1)*ai,(1-c2)*ai]+others
                fv=f_val(pieces)
                if fv<best:
                    best=fv
    # 2 cuts: two pieces each into 2
    idx_pairs=[(0,1),(0,2),(1,2)]
    for i,j in idx_pairs:
        ai=a[i]; aj=a[j]
        ak=[a[k] for k in range(3) if k!=i and k!=j][0]
        G=81
        for ki in range(1,G):
            ri=ki/G
            for kj in range(1,G):
                rj=kj/G
                pieces=[ri*ai,(1-ri)*ai,rj*aj,(1-rj)*aj,ak]
                fv=f_val(pieces)
                if fv<best:
                    best=fv
    return best

def best_Xiang_n2_precise(a):
    # more precise refinement around best found by fast via local search
    best=best_Xiang_n2_fast(a)
    # attempt random refinement near best minima: we can do random search around promising r's
    # simple random extra
    for _ in range(20000):
        # choose case randomly
        case=random.choice(['1cut','3','11'])
        if case=='1cut':
            i=random.randrange(3)
            ai=a[i]
            others=[a[j] for j in range(3) if j!=i]
            r=random.random()
            if r==0 or r==1: continue
            pieces=[r*ai,(1-r)*ai]+others
            fv=f_val(pieces)
            if fv<best:
                best=fv
        elif case=='3':
            i=random.randrange(3)
            ai=a[i]
            others=[a[j] for j in range(3) if j!=i]
            c1=random.random(); c2=random.random()
            if c1>c2: c1,c2=c2,c1
            if c1==0 or c2==1 or c1==c2: continue
            pieces=[c1*ai,(c2-c1)*ai,(1-c2)*ai]+others
            fv=f_val(pieces)
            if fv<best:
                best=fv
        else:
            i,j=random.choice([(0,1),(0,2),(1,2)])
            ai=a[i]; aj=a[j]
            ak=[a[k] for k in range(3) if k!=i and k!=j][0]
            ri=random.random(); rj=random.random()
            pieces=[ri*ai,(1-ri)*ai,rj*aj,(1-rj)*aj,ak]
            fv=f_val(pieces)
            if fv<best:
                best=fv
    return best

# test
for a in [[0.4,0.4,0.2],[0.6,0.3,0.1],[0.333,0.333,0.334],[0.57,0.285,0.145]]:
    print(a, best_Xiang_n2_fast(a), best_Xiang_n2_precise(a))

def search_best_n2(iterations=2000):
    best_L=-1
    best_a=None
    for it in range(iterations):
        exps=[-math.log(random.random()+1e-12) for _ in range(3)]
        s=sum(exps)
        a=[e/s for e in exps]
        # fast eval
        val=best_Xiang_n2_fast(a)
        if val>best_L:
            # refine
            val_precise=best_Xiang_n2_precise(a)
            # if still good
            if val_precise>best_L:
                best_L=val_precise
                best_a=list(a)
                print(f"iter {it} new best {best_L:.6f} a {[f'{x:.4f}' for x in a]}")
    # refine best_a with local search
    if best_a:
        cur_a=best_a[:]
        cur_val=best_L
        for step in range(500):
            # perturb
            sigma=0.02
            new_a=[max(1e-6, x+random.gauss(0,sigma)) for x in cur_a]
            s=sum(new_a)
            new_a=[x/s for x in new_a]
            val=best_Xiang_n2_precise(new_a)
            if val>cur_val:
                cur_val=val
                cur_a=new_a
                print(f" local {step} improved to {cur_val:.6f} a {[f'{x:.4f}' for x in cur_a]}")
        print(f"FINAL best {cur_val:.6f} a {cur_a}")
        return cur_val,cur_a
    return best_L,best_a

search_best_n2(500)
