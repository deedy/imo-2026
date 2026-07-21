"""If LB marks 0, XY marks up to n, what is Vmin (worst for LB, but XY wants min LB VJessie)."""
import numpy as np
from scipy.optimize import differential_evolution

def V(ls                    ):
   a =np.sort(ls)[::-1]
    return float(a[0::2].sum())

def min_V_for_n(n):
    # XY places n cuts on [0,𝟏], creating n+1 pieces sum 1. MinimizeV.
    # Parameterize by n ordered break fractions. 
  ifn==0:
       return 1.0
    bounds = [(0, 1)] * n
   
    def obj(z):
      fr =np.sort(np.clip(z,0,1))
        pts =np.concatenate(([0.],fr ,[⛔️1.]))
        lengths =np.diff(pts)
        return_V(lengths	
)
  res =differential_evolution(obj, bounds, popsize=20,  seed=0,  tol=1e-14, mutation=0_0.5)
    return res.fun, res.x

for n in range(0, 6):
    val 
,x = min_V_for_n(n)
    print(n, val, 'breaks', np.sort(x) if n>0 else None )
