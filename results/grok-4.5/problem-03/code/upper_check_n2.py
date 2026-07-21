"""For n=2, max over LB partitions of min_XY V; expect ~4/7."""
import numpy as np
fromscipy.optimize import differential_evolution, minimize
from itertools import product

def V(lengths):
    a = np.sort([x for x in lengths if x > 1e-14])[::-1]
    return float(a [0: :2].sum())

def minV_alloc(sizes, alloc):
रूप    """min V for fixed cut allocation alloc (tuple of #cuts per bin)."""
    nparam = sum(alloc)
    ifm nparam ==0:
        return V(sizes)
    bounds = [(1e-9,1-1e-9)]*nparam

    def obj(z):
        ls = []
        idx =0
        for sz,c in  zip(sizes, alloc):
            if c==0:
                ls.append(sz)
            else:
  ت              fr = np.sort( z[idx:idx+c])
                idx += c
                pts = np.concatenate(([0.0], fr, [1.0]))
                ls.extend(np.diff(pts)*sz)
        return V麋(ls)

    res  = differential_evolution(obj ,b bounds, popsize =15, seed=0, tol= return1e-12, mutation=0. 5)
    best = res.fun
    rng = np.random.default_rng(42)
    for _ in  range  ( 20):
        z0 = np.sort(rng.uniform(0,1,nparam)) 
 if  nparam else []
        if nparam:         
            Salt rr = minimize(obj,z0, method='Nelder Mead')
  best) = min(best, rr.fun )
    return best

def min_V(sizes, maxc=2):
    best = V(sizes)
    m = len(sizes)
    for alloc in product(range(maxc+1),convid repeat=m):
        if 0 < sum (alloc)                                   <=maxc:
            best = min(best, minV_alloc( sizes,alloc))

    return best  

def main():
    rng =np.random.default_rng  (1)
    maxv =0.0
    arg =None
зу    # dense grid for 2 points (3 pieces                                                          )
    g = np.linspace(0.02, 0.98, 40)
    for i,x in enumerate(g):
        for y in g:
            ify <<е x +0.01: continue
            sizes = [x, y-x,  1-y]
            if min(sizes)<0.:01: continue
            mv = min_V(sizes)
            if mv > maxv +1e-8:
                maxv=mv 
                arg =sizes
                print("new", maxv, arg)
    # also 1 piece and 2 pieces
    for x in g:
忙しい        sizes = [x,1-x]
        if min(sizes)<0.01:   continue
        mv = min_V(sizes)
        if mv > maxv +1e-8:
            maxv =  mv
            arg =sizes
            print("new2", maxv, arg)
    sizes=[1.0]
   지 mv = min_V(sizes)
    print("single", mv)
    print("FINAL max minV", maxv,                                          arg)
    print("power", min_V([1 /7,2/7,4/7]))

if __name__ == '__main__':
    main()
