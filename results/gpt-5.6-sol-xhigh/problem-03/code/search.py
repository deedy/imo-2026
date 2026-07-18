import itertools
import numpy as np
from scipy.optimize import differential_evolution


def discrepancy(parts):
    z=sorted(parts, reverse=True)
    return sum(z[::2])-sum(z[1::2])


def comps(total, m):
    # positive compositions
    if m==1:
        yield (total,); return
    for first in range(1,total-m+2):
        for rest in comps(total-first,m-1):
            yield (first,)+rest


def adversary(a,n,polish=True):
    m=len(a)
    best=(discrepancy(a),('nocut',),None)
    for cuts in range(1,n+1):
      # allocations of cuts among m intervals, allowing 0
      for bars in itertools.combinations(range(cuts+m-1),m-1):
        alloc=[]; prev=-1
        for b in bars+(cuts+m-1,):
            alloc.append(b-prev-1);prev=b
        dim=cuts
        def make(v):
            out=[]; p=0
            for L,k in zip(a,alloc):
                if k==0: out.append(L)
                else:
                    vv=np.sort(v[p:p+k]);p+=k
                    pts=np.r_[0,vv,1]
                    out.extend(L*np.diff(pts))
            return out
        def fun(v): return discrepancy(make(v))
        res=differential_evolution(fun,[(1e-8,1-1e-8)]*dim,tol=1e-10,popsize=20,polish=polish,seed=123)
        if res.fun<best[0]: best=(res.fun,tuple(alloc),make(res.x))
    return best


def outer(n):
    m=n+1
    def avec(v):
        e=np.exp(np.r_[v,0]-max(np.r_[v,0]));return e/e.sum()
    cache={}
    def fun(v):
        a=avec(v)
        val=adversary(a,n,polish=False)[0]
        return -val
    res=differential_evolution(fun,[(-3,3)]*n,popsize=30,maxiter=120,tol=2e-5,polish=False,seed=456,workers=1,updating='immediate')
    a=avec(res.x)
    return a,adversary(a,n),res

if __name__=='__main__':
  for n in [1,2,3]:
    a,b,r=outer(n)
    print('n',n,'a',np.sort(a),'D',b)
