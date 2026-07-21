import random, math
from collections import Counter

def step(m,n):
    g=math.gcd(m,n)
    l=m*n//g
    return g, l//g

def simulate(initial):
    arr=initial[:]
    moves=0
    while True:
        idx=[i for i,v in enumerate(arr) if v>1]
        if len(idx)<2:
            break
        i,j=random.sample(idx,2)
        m=arr[i]; n=arr[j]
        g,l_g=step(m,n)
        arr[i]=g; arr[j]=l_g
        moves+=1
        if moves>10000:
            print("too many")
            break
    return arr, moves

def compute_M_formula(initial):
    # factor each, compute G_p
    # get primes up to max via trial division
    # For each number factor
    facs=[]
    for x in initial:
        d=2
        tmp=x
        cnt={}
        while d*d<=tmp:
            while tmp%d==0:
                cnt[d]=cnt.get(d,0)+1
                tmp//=d
            d+=1 if d==2 else 2
        if tmp>1:
            cnt[tmp]=cnt.get(tmp,0)+1
        facs.append(cnt)
    primes=set()
    for c in facs:
        primes.update(c.keys())
    M=1
    for p in primes:
        vals=[c.get(p,0) for c in facs]
        from math import gcd
        from functools import reduce
        g=0
        for v in vals:
            g=math.gcd(g,v)
        M*=p**g
    return M

for _ in range(100):
    N=5
    init=[random.randint(2,100) for _ in range(N)]
    expected=compute_M_formula(init)
    for trial in range(20):
        final, moves=simulate(init)
        ones=[x for x in final if x>1]
        assert len(ones)==1, f"{init} -> {final}"
        assert ones[0]==expected, f"{init} expected {expected} got {ones[0]} final {final}"
print("all ok")
