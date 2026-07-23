"""Nested differential-evolution search for the cutting game, for conjecture generation only."""
import numpy as np
from scipy.optimize import differential_evolution, minimize
from itertools import product


def D_of(pieces):
    x=np.sort(np.asarray(pieces))[::-1]
    return float(np.dot(x, np.where(np.arange(len(x))%2==0,1.,-1.)))

def comps(total, k):
    if k==1:
        yield (total,); return
    for a in range(total+1):
        for rest in comps(total-a,k-1):
            yield (a,)+rest

def softmax_parts(z, mass):
    z=np.asarray(z); zz=np.r_[z,0.]
    e=np.exp(zz-np.max(zz)); return mass*e/e.sum()

def inner_for_alloc(a,ks, seed=1, polish=True):
    # k_i cuts gives k_i+1 pieces; parameterize each simplex by k_i logits
    dim=sum(ks)
    if dim==0: return D_of(a),None
    bounds=[(-12,12)]*dim
    def fun(z):
        out=[]; q=0
        for ai,ki in zip(a,ks):
            out.extend(softmax_parts(z[q:q+ki],ai));q+=ki
        return D_of(out)
    res=differential_evolution(fun,bounds,tol=1e-9,popsize=20,maxiter=1500,seed=seed,polish=polish,workers=1)
    return res.fun,res.x

def inner(a,n, **kw):
    best=(D_of(a), tuple([0]*len(a)), None)
    # permit at most n cuts
    for tot in range(n+1):
      for ks in comps(tot,len(a)):
        val,z=inner_for_alloc(a,ks,**kw)
        if val<best[0]:best=(val,ks,z)
    return best

def eval_a_logits(z,n,quick=False):
    a=softmax_parts(z,1.)
    return inner(a,n, seed=3, polish=not quick)[0]

if __name__=='__main__':
  import sys
  n=int(sys.argv[1]) if len(sys.argv)>1 else 2
  # outer direct maximize nested (expensive)
  def obj(z):
    a=softmax_parts(z,1.)
    val,ks,_=inner(a,n, seed=7)
    print('a',np.round(a,7),'D',val,'ks',ks,flush=True)
    return -val
  res=differential_evolution(obj,[(-4,4)]*n,popsize=8,maxiter=30,tol=2e-5,seed=2,polish=False)
  a=softmax_parts(res.x,1)
  print('FINAL',a,inner(a,n,seed=11),res)
