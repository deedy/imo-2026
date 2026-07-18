from random import random, randint, seed


def D(xs):
    xs=sorted(xs, reverse=True)
    return sum(xs[::2])-sum(xs[1::2])


def random_refinement(a, maxcuts):
    alloc=[0]*len(a)
    for _ in range(randint(0,maxcuts)):
        alloc[randint(0,len(a)-1)] += 1
    out=[]
    for L,c in zip(a,alloc):
        pts=sorted(random() for _ in range(c))
        old=0
        for p in pts+[1]:
            out.append(L*(p-old)); old=p
    return out


def min_subset_gap(a):
    sums=[]
    m=len(a)
    for mask in range(1<<m):
        sums.append(sum(a[i] for i in range(m) if mask>>i&1))
    sums.sort()
    return min(y-x for x,y in zip(sums,sums[1:]))

seed(2603)
for n in range(1,9):
    den=2**(n+1)-1
    a=[2**i/den for i in range(n+1)]
    for _ in range(20000):
        xs=random_refinement(a,n)
        assert D(xs) >= 1/den-1e-12, (n,a,xs,D(xs))
    for _ in range(1000):
        raw=[random() for _ in range(n+1)]
        s=sum(raw); raw=[x/s for x in raw]
        assert min_subset_gap(raw) <= 1/den+1e-12
    print(f'n={n}: random refinement and subset-gap checks passed; d={1/den:.12g}')
