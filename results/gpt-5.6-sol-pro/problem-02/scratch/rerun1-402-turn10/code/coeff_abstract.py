# Basic symbolic expression dictionary in variables k,K,D,E,b where b invertible; output S coeff in r
from fractions import Fraction as F
N=5
class P(dict):
 def __add__(a,z):
  if not isinstance(z,P):z=C(z)
  q=P(a)
  for m,w in z.items():q[m]=q.get(m,F(0))+w
  return P({m:w for m,w in q.items() if w})
 __radd__=__add__
 def __neg__(a):return P({m:-w for m,w in a.items()})
 def __sub__(a,z):return a+-z
 def __rsub__(a,z):return C(z)-a
 def __mul__(a,z):
  if not isinstance(z,P):z=C(z)
  q=P()
  for m,w in a.items():
   for n,v in z.items():
    s=tuple(m[i]+n[i] for i in range(N));q[s]=q.get(s,F(0))+w*v
  return P({m:w for m,w in q.items() if w})
 __rmul__=__mul__
 def __pow__(a,n):
  q=C(1)
  for _ in range(n):q=q*a
  return q
def C(z):return P({(0,)*N:F(z)})
def V(i):m=[0]*N;m[i]=1;return P({tuple(m):F(1)})
k,K,D,E,b=map(V,range(N));bi=P({(0,0,0,0,-1):F(1)});one=C(1)
# univariate r list coeff operations
def add(a,z):
 n=max(len(a),len(z));return [(a[i] if i<len(a) else C(0))+(z[i] if i<len(z) else C(0)) for i in range(n)]
def neg(a):return [-x for x in a]
def sub(a,z):return add(a,neg(z))
def mul(a,z):
 q=[C(0)]*(len(a)+len(z)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(z):q[i+j]=q[i+j]+x*y
 return q
def scale(a,z):return [x*z for x in a]
l=[one,-b];L=[one,-bi];ll=mul(l,L)
# S formula
# 2 kK [lL(D-E)+DE(L-l)]
S=scale(add(scale(ll,D-E),scale(sub(L,l),D*E)),2*k*K)
# +2lL[K l E - k L D + DE(k-K)]
inside=add(add(scale(l,K*E),scale(L,-k*D)),[D*E*(k-K)])
S=add(S,scale(mul(ll,inside),2))
# -(lL-DE)(K l-kL)
S=add(S,neg(mul(add(ll,[-D*E]),add(scale(l,K),scale(L,-k)))))
print('S degrees terms',[(i,len(c)) for i,c in enumerate(S)])
# print compact strings
def fmt(P):
 names=['k','K','D','E','b'];ss=[]
 for m,w in sorted(P.items()):
  mon=[]
  for n,e in zip(names,m):
   if e:mon.append(n+(('^'+str(e)) if e!=1 else ''))
  ms='*'.join(mon) or '1';ss.append(f'{w}*{ms}')
 return ' + '.join(ss).replace('+ -','- ')
for i,c in enumerate(S):print('S',i,'=',fmt(c))
