# Minimal multivariate Laurent-polynomial algebra, to factor the final trig identity
# after z=e^{i delta}. Coefficients are numerical for exploration.
import cmath, math, random

def mul(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items(): c[i+j]=c.get(i+j,0)+x*y
 return c
def add(a,b,k=1):
 c=a.copy()
 for i,y in b.items(): c[i]=c.get(i,0)+k*y
 return c
def scale(a,k): return {i:k*x for i,x in a.items()}
def sine(theta, shift=0):
 # sin(theta + shift*d), z=e^(id)
 return {shift:cmath.exp(1j*theta)/(2j),-shift:-cmath.exp(-1j*theta)/(2j)}

def polys(p,q,r):
 x=math.atan2(1,1/math.tan(p)+2/math.tan(r)); y=math.atan2(1,1/math.tan(p)+2/math.tan(q))
 P=math.sin(p)/math.sin(p+x);Q=math.sin(p)/math.sin(p+y)
 U=sine(p+r+y,1);V=sine(p+q+x,1)
 C=add(scale(mul(U,V),P*Q),{0:-math.sin(p+r)*math.sin(p+q)})
 T=add(scale(mul(sine(r,1),V),Q*math.sin(p)),scale(mul(sine(q,1),U),-P*math.sin(p)))
 T=add(T,{0:2*(P*math.sin(y)-Q*math.sin(x))*math.sin(p+r)*math.sin(p+q)})
 return C,T
for a in [(0.2,.3,.4),(.1,.2,.3)]:
 C,T=polys(*a);print('\n',a,'C',C,'T',T)
 # both exponents -2,0,2. If T is scalar times C, ratios equal. Evidently earlier no.
 print({k:T[k]/C[k] for k in C})
