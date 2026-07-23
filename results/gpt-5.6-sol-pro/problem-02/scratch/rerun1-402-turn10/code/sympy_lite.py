# Tiny Laurent/rational symbolic via sympy unavailable; use sympy vendoring impossible.
# Use polynomial dictionaries with rational coefficients and variables X,Y,Z,V.
from fractions import Fraction as F
from math import prod
NV=4
class P(dict):
 def __add__(a,b):
  if not isinstance(b,P):b=const(b)
  c=P(a)
  for m,v in b.items(): c[m]=c.get(m,F(0))+v
  return P({m:v for m,v in c.items() if v})
 __radd__=__add__
 def __neg__(a):return P({m:-v for m,v in a.items()})
 def __sub__(a,b):return a+-b
 def __rsub__(a,b):return const(b)+-a
 def __mul__(a,b):
  if not isinstance(b,P):b=const(b)
  c=P()
  for m,v in a.items():
   for n,w in b.items():
    q=tuple(m[i]+n[i] for i in range(NV));c[q]=c.get(q,F(0))+v*w
  return P({m:v for m,v in c.items() if v})
 __rmul__=__mul__
 def __pow__(a,n):
  r=const(1)
  for i in range(n):r=r*a
  return r
 def bar(a):return P({(-m[0],-m[1],-m[2],m[3]):v for m,v in a.items()})
 def shift(a,m): return P({tuple(n[i]+m[i] for i in range(NV)):v for n,v in a.items()})
def const(v):return P({(0,0,0,0):F(v)}) if v else P()
def var(i):
 m=[0]*NV;m[i]=1;return P({tuple(m):F(1)})
X,Y,Z,V=map(var,range(4));one=const(1)
# represent rational N/D pair
class R:
 def __init__(s,n,d=one):s.n,s.d=n,d
 def __add__(a,b):
  if not isinstance(b,R):b=R(const(b))
  return R(a.n*b.d+b.n*a.d,a.d*b.d)
 __radd__=__add__
 def __neg__(a):return R(-a.n,a.d)
 def __sub__(a,b):return a+-b
 def __rsub__(a,b):return R(const(b))+-a
 def __mul__(a,b):
  if not isinstance(b,R):b=R(const(b))
  return R(a.n*b.n,a.d*b.d)
 __rmul__=__mul__
 def __truediv__(a,b):
  if not isinstance(b,R):b=R(const(b))
  return R(a.n*b.d,a.d*b.n)
 def bar(a):return R(a.n.bar(),a.d.bar())
 def norm(a):return a*a.bar()
# p=(Z-Z^-1)/(2(XZ-X^-1Z^-1)); clear negative = X(Z^2-1)/(2(X^2 Z^2-1))
p=R(X*(Z**2-one),2*(X**2*Z**2-one))
q=R(X*(Y**2-one),2*(X**2*Y**2-one))
k=R(one)-p/R(X)
D=R(one)-q*R(X)
d=R(X*Z)
c=k/(R(one)-R(V)*d)
l=c*D
# bracket numerator rational a_bar*b-a*b_bar
def bracket(a,b):return a.bar()*b-a*b.bar()
w=c-R(one)
E=2*(k.norm()*bracket(w,l)+l.norm()*bracket(k,w))-(c.norm()-R(one))*bracket(k,l)
Comp=bracket(R(one/(1) if False else one/(1)),R(one)) if False else bracket(R(one/(1)) if False else R(one),R(one))
# compatibility [b,l-1], b=1/(XY). scaling harmless. bracket b,l-1
b=R(one)/(R(X*Y)); Comp=bracket(b,l-R(one))
# Cross multiply E / Comp: prove E numerator zero if comp numerator zero. seek polynomial divisibility.
EN=E.n; ED=E.d; CN=Comp.n; CD=Comp.d
print('terms EN',len(EN),'CN',len(CN),'degrees/ranges')
def ranges(p):return [(min(m[i] for m in p),max(m[i] for m in p)) for i in range(NV)]
print(ranges(EN),ranges(CN));
# shift nonnegative and divide multivariate polynomials lex with var order V,Z,Y,X maybe custom lex tuple V,Z,Y,X
def normalize(p):
 mins=[min(m[i] for m in p) for i in range(NV)]
 return p.shift(tuple(-a for a in mins)),mins
A,ash=normalize(EN);B,bsh=normalize(CN)
order=lambda m:(m[3],m[2],m[1],m[0])
def div(A,B):
 Q=P();R=P(A);lmB=max(B,key=order);lcB=B[lmB];steps=0
 while R:
  lm=max(R,key=order);lc=R[lm]
  dif=tuple(lm[i]-lmB[i] for i in range(NV))
  if min(dif)<0: break
  t=P({dif:lc/lcB});Q=Q+t;R=R-t*B;steps+=1
  if steps%1000==0:print('steps',steps,len(R))
  if steps>100000:break
 return Q,R
Q,Rem=div(A,B)
print('quotient terms',len(Q),'rem',len(Rem),'rangesQ',ranges(Q) if Q else None,'rangesR',ranges(Rem) if Rem else None)
if Rem:
 for m in sorted(Rem,key=order,reverse=True)[:10]:print(m,Rem[m])
