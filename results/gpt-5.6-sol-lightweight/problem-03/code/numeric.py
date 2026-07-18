import numpy as np
from scipy.optimize import differential_evolution
from itertools import product

def softmax(z):
 e=np.exp(np.r_[z,0]-max(np.r_[z,0])); return e/e.sum()
def payoff(p):
 q=np.sort(p)[::-1]; return q[::2].sum()
def comps(total,m):
 if m==1: yield (total,); return
 for i in range(total+1):
  for x in comps(total-i,m-1): yield (i,)+x

def inner(a,n):
 best=payoff(a); arg=None
 for cuts in range(n+1):
  for cc in comps(cuts,len(a)):
   dim=sum(cc)
   if not dim:
    val=payoff(a); z=[]
   else:
    def f(z):
     out=[]; pos=0
     for ai,k in zip(a,cc):
      out.extend(ai*softmax(z[pos:pos+k])); pos+=k
     return payoff(out)
    r=differential_evolution(f,[(-8,8)]*dim,tol=1e-9,popsize=12,seed=cuts+31*len(a),polish=True)
    val=r.fun; z=r.x
   if val<best: best,arg=val,(cc,z)
 return best,arg

for n in range(1,5):
 cache={}
 def outer(z):
  a=softmax(z)
  return -inner(a,n)[0]
 r=differential_evolution(outer,[(-5,5)]*n,tol=2e-5,popsize=20,seed=2,polish=True,workers=1)
 a=softmax(r.x); inn=inner(a,n)
 print(n,-r.fun,a,inn)
