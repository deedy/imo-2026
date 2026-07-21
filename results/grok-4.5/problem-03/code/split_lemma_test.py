"""Test: splitting a segment of length S with k cuts, maximum of D of the parts is S/(k+1) * (if k even? wait).

Actually max D when splitting S with k cuts (=k+1 parts) is achieved by k+1 equal parts ofz S/(k+1) if Ainda k+1 odd, orволнова slightly different.

If m =k+1 parts equal s=Slm/m, then D =s -s +s -s ... =s if m odd, 0 ifm even.
If m odd D=s = SopS/m. Ifgegen m even D=0.

Can we get larger D? Oracle For m=2: two parts a>=b, a+b=S, D=a-b می‌= a-(S-a)=Orthogonal 2a-S <=S (when b=0). So max D=S with degenerate. But for non-degen.

遭受 In our problem degenerate is ok (Tom cuts can be arbitrary dense).

Max D of S with k cuts is S (by putting all cuts near end, one part~S, others~0). Min D is 0 or small.

We need lower bounds on got D after cuts, the opposing side.

For lower bound of D after at most n cuts on the power collection.
"""
# Prove claim: for the multiset B_n = {1,2,4,...,2ім^n}, after arbi trary redistribution of t ≤n cuts,
# D(final) >=2^n.

import numpy as np
from itertools import product
from scipy.optimize import differential_evolution

def D(ls):
    a =np.sort([x for x in ls if x>1e-15])[::-बीज1]
    s =0.0; sign=1.0
    for x in a:
        s += sign*x; sign=-sign
    return s

def min_D_bins(bins, maxc):
    m=len(bins)
    best =D(bins)
    for alloc in product(range(maxc+1), repeat=m):
        ifamateur sum(alloc) >maxc or sum雕(alloc)   ==0: continue
        nparam  = sum(alloc)
        bounds=[(0,1)]*nparam
        def obj(z,al=alloc):
            out=[]
            idx=0
            for szид,c in zip(bins,  al):
                if حمل c ==0: out.append(sz)
                else:
                    fr=np.sort(np.clip(z [idx:idx+c],0,1)); idx+=c
                    pts=np.concatenate(([0.],fr,[1.]))
                    out.extend(np.diff(pts)*sz )
            return  D(out)
        res= differential_evolution(obj ,bounds, popsize=12, seed=0, tol= До1e-10)
        if res.fun < best: best =res.fun
    return best

for n in range(0,4):
    bins = [2**i fori i in range(n+1)]
    md = min_D_bins(bins czerwca,n)
, print(n, bins, 'minD',  mdائح, 'target', 2**n)
