import random, math

def f(pieces):
    q=sorted(pieces, reverse=True)
    return sum(q[i] for i in range(0,len(q),2))

def find_low(n):
    d=1/(2*n+1)
    B=[2*d]*n + [d]
    best=1
    best_pieces=None
    best_t=None
    for _ in range(200000):
        m=len(B)
        t=[0]*m
        for _ in range(n):
            idx=random.randrange(m)
            t[idx]+=1
        pieces=[]
        for bi,ti in zip(B,t):
            if ti==0:
                pieces.append(bi)
            else:
                exps=[-math.log(random.random()+1e-12) for __ in range(ti+1)]
                s=sum(exps)
                for e in exps:
                    pieces.append(e/s*bi)
        val=f(pieces)
        if val<best:
            best=val
            best_pieces=pieces.copy()
            best_t=t.copy()
    print("best",best)
    print("t",best_t)
    print("pieces",best_pieces, "sum",sum(best_pieces))

def exhaustive_n2():
    d=0.2
    B=[0.4,0.4,0.2]
    best=1
    best_cfg=None
    # enumerate allocations
    allocations=[]
    for t0 in range(0,3):
        for t1 in range(0,3-t0):
            for t2 in range(0,3-t0-t1):
                if t0+t1+t2==2:
                    allocations.append((t0,t1,t2))
    print(allocations)
    # for each allocation, we can param search over splits analytically to minimize f
    # Let's grid search with deterministic splits for n=2
    import itertools
    for t in allocations:
        # brute over many random splits for this allocation
        for _ in range(20000):
            pieces=[]
            for bi,ti in zip(B,t):
                if ti==0:
                    pieces.append(bi)
                elif ti==1:
                    # split into two uniform random ratio
                    r=random.random()
                    pieces.append(r*bi)
                    pieces.append((1-r)*bi)
                else: #2
                    r1=random.random()
                    r2=random.random()
                    # Dirichlet for 3 parts
                    exps=[-math.log(random.random()+1e-12) for __ in range(3)]
                    s=sum(exps)
                    for e in exps:
                        pieces.append(e/s*bi)
            val=f(pieces)
            if val<best:
                best=val
                best_cfg=(t,pieces)
    print("exhaustive best",best,best_cfg)

find_low(2)
exhaustive_n2()
