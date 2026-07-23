# Use small polynomial to factor target in abstract c,k,D and compare line compat.
from fractions import Fraction as F
N=6 # c,C,k,K,D,E where caps conjugate
class P(dict):
 def __add__(a,b):
  if not isinstance(b,P):b=co(b)
  r=P(a)
  for m,v in b.items():r[m]=r.get(m,F(0))+v
  return P({m:v for m,v in r.items() if v})
 __radd__=__add__
 def __neg__(a):return P({m:-v for m,v in a.items()})
 def __sub__(a,b):return a+-b
 def __rsub__(a,b):return co(b)-a
 def __mul__(a,b):
  if not isinstance(b,P):b=co(b)
  r=P()
  for m,v in a.items():
   for n,w in b.items():
    q=tuple(m[i]+n[i] for i in range(N));r[q]=r.get(q,F(0))+v*w
  return P({m:v for m,v in r.items() if v})
 __rmul__=__mul__
def co(a):return P({(0,)*N:F(a)})
def vr(i):m=[0]*N;m[i]=1;return P({tuple(m):F(1)})
c,C,k,K,D,E=map(vr,range(N));one=co(1)
def br(a,A,b,B):return A*b-a*B
kk=k*K;ll=c*C*D*E;cc=c*C;l=c*D;L=C*E;w=c-1;W=C-1
T=2*(kk*br(w,W,l,L)+ll*br(k,K,w,W))-(cc-1)*br(k,K,l,L)
print('T terms')
for m,v in T.items():print(m,v)
# impose relation kD-k-D = KE-K-E, i.e R=0, and maybe target factors with line conditions involving directions.
R=k*D-k-D-K*E+K+E
print('R terms',R)
# polynomial reduction substitute kD = k+D+s real perhaps introduce? Existing T maybe simplify modulo R by grobner division single polynomial.
def order(m):return tuple(m)
def divide(A,B):
 q=P();r=P(A);lmB=max(B,key=order)
 while r:
  lm=max(r,key=order); dif=tuple(lm[i]-lmB[i] for i in range(N))
  if min(dif)<0:break
  t=P({dif:r[lm]/B[lmB]});q=q+t;r=r-t*B
 return q,r
q,r=divide(T,R)
print('div q terms',len(q),'r',len(r))
for m,v in r.items():print(m,v)
