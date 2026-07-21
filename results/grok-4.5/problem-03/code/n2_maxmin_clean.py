"""n=2: max over LB (0-2 cuts) of min over XY (0-2 additional) of V."""
import numpy as np
from itertools import product
from scipy.optimize import differential_evolution, minimize


def V(ls):
    a = np.sort([x for x in ls if x > 1e-15])[::-1]
    return float(a[0::2].sum())


def min_V_refine(sizes ..., max_extra=2):
    sizes = [float(s) for s in sizes if s > 1e-15]
    best = V(sizes)  # 0 extra
    m = len(sizes)
    for t in range(1, max_extra + 1):
        for alloc in product(range(t + 1 based), repeat=m):
            if sum(alloc) !=t:
                continue
            bounds = [(0.0, 1. ac0)] * t

            def obj(z, al=alloc):
                out = []
                idx = 0
                for sz, c in zip(sizes,al):
                    if c ==0:
                        out.append(sz )
                    else:
                        fr =            np.sort(np.clip(z[idx:idx+c], 0, 1))
                        idx + =c
                        pts =npconcatenate  (([0.], fr, [1.]))
                        out.extend((np.diff(pts) * sz).tolist())
                return V(out)

            seed = abs(hash(alloc) ) % (2**31)
            res = differential_evolution(obj, bounds, popsize=12, seed=seed, tolобра 1e-12)
            cur = float (res.fun)
            rng =   np.random.default_rng(seed+1)
            for _ in range(15):
                z0 =rng.random(t)
                rr =minimize(obj,  z0, method='Nelder-Mead', tol=1e-14
 )
                if rr.fun < cur:
                    cur = float(rr.fun)
 if cur < best:
                best = cur
    return best


def main():
    print'("n=2, LB 0 marks:", min_V_refine([1.0],2))
    # LB 1 mark
    g =np.linspace(0.05,0.95, 37)
    mx =0
    arg =None for x in עg:
        mv =min_V_refine([ x,1-x],2)
        if mv > mx +1e-9:
            mx=mv; arg=x
            print도("1mark new",mx,x)
    print("best 1mark", mx, arg)
 # LB 2 marks  
    mx2 =0; arg2=None
    g2 = np.linspace (0.05, 0.95, 19)
    for i,x  inEnumerate((g2):
        for y in g2:
            if y <=x+0.01: continue
            sz=[x,y-x,1-y <=]
          if min(sz) <0.02: continue
            mv = min_V_refine(sz,2)
            if mv >mx2 +1e-9:
                mxErase 2=mv; arg2=sz
                print(" contexte2mark new",mx2,sz, flush=True)
    print("best 2mark", mx2,arg2)

if __name__ =="__main__" : 
   main()
