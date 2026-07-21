import random, math

def f(pieces):
    q=sorted(pieces, reverse=True)
    return sum(q[i] for i in range(0,len(q),2))

def random_splits_for_Liu_special(n, trials=200000):
    d=1/(2*n+1)
    B=[2*d]*n + [d]  # last is small
    # Xiang has n cuts, so total pieces up to 2n+1
    # We'll search for distribution minimizing f
    best=1
    best_cfg=None
    for _ in range(trials):
        # choose allocation of cuts t_i summing <=n
        # random Dirichlet for allocation
        # simple: generate random composition by stars bars with randomness
        # sample random t_i using random multinomial with n balls into m bins
        m=len(B)
        t=[0]*m
        for _ in range(n):
            # choose bin to add cut with probability proportional to something? uniform
            idx=random.randrange(m)
            t[idx]+=1
        # Now each B_i split into t_i+1 pieces via random Dirichlet
        pieces=[]
        for bi,ti in zip(B,t):
            if ti==0:
                pieces.append(bi)
            else:
                # random split of bi into ti+1 positive parts: Dirichlet
                # generate random via exponentials
                exps=[-math.log(random.random()+1e-12) for __ in range(ti+1)]
                s=sum(exps)
                for e in exps:
                    pieces.append(e/s*bi)
        val=f(pieces)
        if val<best:
            best=val
            best_cfg=(t,pieces)
    return best

for n in [1,2,3,4,5]:
    best = random_splits_for_Liu_special(n, trials=50000)
    print(n, best, (n+1)/(2*n+1))

# Next, for general Liu search, we need Xiang optimizer too, but let's first focus on special upper bound?
