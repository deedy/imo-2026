import sympy as s
b,c,r,d,u,v,h=s.symbols('b c r d u v h', nonzero=True)
ks=c-r*v; kt=r*u
ls=d*u; lt=b-d*v
Q=lambda X,Y: s.expand(X**2+Y**2+2*h*X*Y)
Rk=Q(ks,kt); Rl=Q(ls,lt)
Delta=s.expand(ks*lt-kt*ls)
P=s.cancel((Rk*lt-kt*Rl)/Delta)
Qc=s.cancel((ks*Rl-Rk*ls)/Delta)
T=s.factor(2*b*Qc-2*c*P-(b**2-c**2))
print('Delta=',s.factor(Delta))
print('T numerator raw factor:')
print(s.factor(s.together(T).as_numer_denom()[0]))
# impose h relation via h=(v-w)/u and u^2(1-h^2)=1-w^2 maybe first substitute h relation
w=s.symbols('w')
num=s.together(T).as_numer_denom()[0]
numw=s.factor(num.subs(h,(v-w)/u))
print('after h=(v-w)/u:')
print(numw)
# relation among uvw from sin: u^2-(v-w)^2=1-w^2 -> u²-v²+2vw=1. solve u2=1+v²-2vw
print('reduce u2 relation')
poly=s.Poly(s.expand(numw),u)
# reduce modulo u²-(1+v²-2vw)
rem=s.rem(s.Poly(s.expand(numw),u),s.Poly(u**2-(1+v**2-2*v*w),u)).as_expr()
print(s.factor(rem))
