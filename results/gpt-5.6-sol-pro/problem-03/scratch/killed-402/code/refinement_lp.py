"""Numerically solve the refinement minimization for small n by enumerating
orders of final subpieces and applying linear programming.  This is only an
exploratory/sanity-check tool; the proof will be independent.
"""
from itertools import product
from functools import lru_cache
import numpy as np
from scipy.optimize import linprog, differential_evolution

@lru_cache(None)
def words(m, max_extra):
    ans=[]
    for k in range(m,m+max_extra+1):
        for w in product(range(m), repeat=k):
            if len(set(w))<m: continue
            # Canonicalize equal adjacent lengths? No need. Keep every order.
            c=np.zeros((m,k))
            for j,x in enumerate(w): c[x,j]=1
            # descending z_j >= z_{j+1}
            Aub=np.zeros((k-1,k))
            for j in range(k-1):
                Aub[j,j+1]=1; Aub[j,j]=-1
            obj=np.array([1 if j%2==0 else -1 for j in range(k)],float)
            ans.append((w,obj,Aub,c))
    return ans

def val(a,n, return_word=False):
    a=np.asarray(a,float); m=len(a)
    best=1e9; bw=None; bx=None
    for w,obj,Aub,c in words(m,n):
        r=linprog(obj,A_ub=Aub,b_ub=np.zeros(len(w)-1),A_eq=c,b_eq=a,
                  bounds=[(0,None)]*len(w),method='highs')
        if r.success and r.fun<best:
            best=r.fun; bw=w; bx=r.x
    return (best,bw,bx) if return_word else best

def outer(n,m=None):
    if m is None:m=n+1
    # softmax coordinates, then sort (labels symmetric)
    def fun(x):
        ex=np.exp(x-np.max(x)); a=np.sort(ex/ex.sum())[::-1]
        return -val(a,n)
    r=differential_evolution(fun,[(-3,3)]*m,tol=1e-7,popsize=12,workers=1,seed=3,
                             maxiter=500,polish=True)
    ex=np.exp(r.x-r.x.max()); a=np.sort(ex/ex.sum())[::-1]
    return -r.fun,a,val(a,n,True),r

if __name__=='__main__':
    import sys
    n=int(sys.argv[1]) if len(sys.argv)>1 else 2
    print('word count',len(words(n+1,n)))
    out=outer(n)
    print('n',n,'best',out[0],'a',out[1])
    print('adversary',out[2])
