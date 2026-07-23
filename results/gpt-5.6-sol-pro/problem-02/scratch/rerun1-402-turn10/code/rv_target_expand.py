# Laurent polynomial exact target after substitute k,D,b,d by angle exponents and c/l via r,v.
# Seek small factor modulo compatibility (complex equation).
from fractions import Fraction as F
# vars X,Y,Z,r,v and inverses Laurent for X Y Z
N=5
class P(dict):
 def __add__(a,b):
  if not isinstance(b,P):b=co(b)
  q=P(a)
  for m,w in b.items():q[m]=q.get(m,F(0))+w
  return P({m:w for m,w in q.items() if w})
 __radd__=__add__
 def __neg__(a):return P({m:-w for m,w in a.items()})
 def __sub__(a,b):return a+-b
 def __rsub__(a,b):return co(b)-a
 def __mul__(a,b):
  if not isinstance(b,P):b=co(b)
  q=P()
  for m,w in a.items():
   for n,t in b.items():
    s=tuple(m[i]+n[i] for i in range(N));q[s]=q.get(s,F(0))+w*t
  return P({m:w for m,w in q.items() if w})
 __rmul__=__mul__
 def bar(a):return P({(-m[0],-m[1],-m[2],m[3],m[4]):w for m,w in a.items()})
def co(a):return P({(0,)*N:F(a)})
def var(i):m=[0]*N;m[i]=1;return P({tuple(m):F(1)})
class R:
 def __init__(s,n,d=co(1)):s.n,s.d=n,d
 def __add__(a,b):
  if not isinstance(b,R):b=R(co(b))
  return R(a.n*b.d+b.n*a.d,a.d*b.d)
 __radd__=__add__
 def __neg__(a):return R(-a.n,a.d)
 def __sub__(a,b):return a+-b
 def __rsub__(a,b):return R(co(b))-a
 def __mul__(a,b):
  if not isinstance(b,R):b=R(co(b))
  return R(a.n*b.n,a.d*b.d)
 __rmul__=__mul__
 def __truediv__(a,b):
  if not isinstance(b,R):b=R(co(b))
  return R(a.n*b.d,a.d*b.n)
 def bar(a):return R(a.n.bar(),a.d.bar())
 def norm(a):return a*a.bar()
X,Y,Z,r,v=map(var,range(N));one=co(1)
p=R(X*(Z*Z-one),2*(X*X*Z*Z-one));q=R(X*(Y*Y-one),2*(X*X*Y*Y-one))
k=R(one)-p/R(X);D=R(one)-q*R(X);b=R(one)/R(X*Y);d=R(X*Z)
h=R(one)-R(v)*d;c=k/h;l=R(one)-R(r)*b
# Compat cD=l equivalent H=cD-l=0 complex; actually complex equation.
H=c*D-l
# target doubled bracket
def br(a,b):return a.bar()*b-a*b.bar()
w=c-R(one)
T=2*(k.norm()*br(w,l)+l.norm()*br(k,w))-(c.norm()-R(one))*br(k,l)
print('terms T,H',len(T.n),len(H.n),'ranges')
def rng(P):return [(min(m[i] for m in P),max(m[i] for m in P)) for i in range(N)]
print(rng(T.n),rng(H.n))
# Want represent T=A H + B Hbar likely rational with small A B. Since target pure imaginary and H config zero.
# Numerically/algebraically direct simplify before trig maybe general identity T in ideal H,Hbar plus residual when l=cD.
