import random, math
def f_val(pieces):
    q=sorted(pieces, reverse=True)
    s=0.0
    for i in range(0,len(q),2):
        s+=q[i]
    return s

def best_Xiang_n2(a):
    # a list length 3 sorted descending maybe but order matters for which piece is which (but symmetric)
    # enumerate t distributions summing <=2 (allow unused cuts)
    best=1.0
    # helper to evaluate f after splits given params
    # We'll do global optimization per t via differential evolution simple.

    # Case 0 cuts
    best = min(best, f_val(a))

    # Case 1 cut: split one piece
    for i in range(3):
        ai=a[i]
        # optimize over r in (0,1)
        # we can sample many points and also include critical points where r*ai equals other aj or (1-r)*ai equals other
        others=[a[j] for j in range(3) if j!=i]
        # For minimal f, we can brute force over fine grid 0-1 with 2001 points
        for k in range(1,2000):
            r=k/2000
            pieces=[]
            for j in range(3):
                if j==i:
                    pieces.append(r*ai)
                    pieces.append((1-r)*ai)
                else:
                    pieces.append(a[j])
            fv=f_val(pieces)
            if fv<best:
                best=fv
        # also test near equality points
        for b in others:
            if b<ai:
                r=b/ai
                for delta in [-0.001, -0.0001, 0, 0.0001,0.001]:
                    rr=r+delta
                    if 0<rr<1:
                        pieces=[]
                        for j in range(3):
                            if j==i:
                                pieces.append(rr*ai)
                                pieces.append((1-rr)*ai)
                            else:
                                pieces.append(a[j])
                        fv=f_val(pieces)
                        if fv<best:
                            best=fv

    # Case 2 cuts distribution (2,0,0): one piece into 3
    for i in range(3):
        ai=a[i]
        # optimize over (r1,r2) with r1>0,r2>0,r1+r2<1
        # grid 50x50
        for k in range(1,50):
            for l in range(1,50-k):
                r1=k/50
                r2=l/50
                # r1,r2, remaining =1 - r1 - r2
                pieces=[]
                for j in range(3):
                    if j==i:
                        pieces.append(r1*ai)
                        pieces.append(r2*ai)
                        pieces.append((1-r1-r2)*ai)
                    else:
                        pieces.append(a[j])
                fv=f_val(pieces)
                if fv<best:
                    best=fv
        # more random
        for _ in range(2000):
            u1=random.random()
            u2=random.random()
            if u1+u2>1:
                u1=1-u1
                u2=1-u2
                if u1+u2>1:
                    continue
                # actually need proper simplex sampling
            # Sample 2 cuts uniform
            c1=random.random()
            c2=random.random()
            if c1>c2:
                c1,c2=c2,c1
            r1=c1
            r2=c2-c1
            # r3=1-c2
            pieces=[]
            for j in range(3):
                if j==i:
                    pieces.append(r1*ai)
                    pieces.append(r2*ai)
                    pieces.append((1-c2)*ai)
                else:
                    pieces.append(a[j])
            fv=f_val(pieces)
            if fv<best:
                best=fv

    # Case (1,1,0): two pieces each split into 2
    # iterate over pairs i<j
    for i in range(3):
        for j in range(i+1,3):
            ai=a[i]; aj=a[j]
            ak_a = a[3 - i - j] if 3!=2 else None # need correct: total set {0,1,2}
            # compute remaining piece
            # Actually if i=0,j=1, remaining k=2 etc.
            rem_idx = [x for x in range(3) if x!=i and x!=j][0]
            ak=a[rem_idx]
            # grid over r_i, r_j
            for ri in range(1,50):
                r_i=ri/50
                for rj in range(1,50):
                    r_j=rj/50
                    pieces=[r_i*ai, (1-r_i)*ai, r_j*aj, (1-r_j)*aj, ak]
                    fv=f_val(pieces)
                    if fv<best:
                        best=fv
            # random extra
            for _ in range(5000):
                r_i=random.random()
                r_j=random.random()
                pieces=[r_i*ai, (1-r_i)*ai, r_j*aj, (1-r_j)*aj, ak]
                fv=f_val(pieces)
                if fv<best:
                    best=fv

    return best

def outer_search(iterations=2000):
    best_L=-1
    best_a=None
    best_f=1
    for it in range(iterations):
        # sample a via dirichlet
        exps=[-math.log(random.random()+1e-12) for _ in range(3)]
        s=sum(exps)
        a=[e/s for e in exps]
        a_sorted=sorted(a, reverse=True)
        val=best_Xiang_n2(a_sorted)
        if val>best_L:
            best_L=val
            best_a=list(a_sorted)
            print(f"iter {it} new best {best_L:.5f} a {best_a}")
    return best_L,best_a

# First test known a's
for a in [[0.4,0.4,0.2],[0.6,0.3,0.1],[0.5,0.3,0.2],[0.5,0.25,0.25],[0.34,0.33,0.33]]:
    a_sorted=sorted(a, reverse=True)
    val=best_Xiang_n2(a_sorted)
    print(f"a {a_sorted} -> best Xiang {val:.5f}")

print("\nStarting outer search")
outer_search(200)
