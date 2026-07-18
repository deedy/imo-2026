import sympy as S
# real vars represent complex a=C/2, k, l. Use alpha variables?
# derive with unit complex exponentials X=e(ix),Y=e(iy),Z=e(iz), conjugates reciprocal.
X,Y,Z=S.symbols('X Y Z', nonzero=True)
I=S.I
# Normalize A=0 B=2 M=1, a=N=C/2.
# k formula triangle BMK: k=1 + sin x/sin(x+z) e^(iz)
# simplify Laurent to rational in X,Z
sin=lambda W:(W-1/W)/(2*I)
k=S.factor(1+sin(X)/sin(X*Z)*Z)
# lambda so l=a*lambda, lambda=1+sin x/sin(x+y)e^-iy
lam=S.factor(1+sin(X)/sin(X*Y)/Y)
print('k',k,'lam',lam)
# Let l=2+t*d where d direction angle pi-(x+y): -1/(XY). BL incidence.
t=S.symbols('t', real=True)
l=2-t/(X*Y)
a=S.factor(l/lam)
print('a=',a)
# CK condition: (k-2a)/(a X Z) real. conjugation maps X,Y,Z reciprocal, t fixed.
def cj(expr): return S.together(expr.xreplace({X:1/X,Y:1/Y,Z:1/Z}))
r=S.factor((k-2*a)/(a*X*Z))
condition=S.factor(r-cj(r))
print('r=',r)
print('condition=',condition)
# Circle center o solves o conj(k)+conj(o)k=|k|2 etc. Complex circumcenter
kb=cj(k); lb=cj(l); ab=cj(a)
o=S.factor((k*kb*l-l*lb*k)/(kb*l-lb*k)) # wait equations o kb+ob k=kk; solve numerator: det rhs? o=(kk*l - ll*k)/(kb*l-lb*k)
print('o=',o)
# target |o-1|2=|o-a|2 equivalently o(ab-1)+ob(a-1)+1-aab=0
ob=cj(o)
H=S.factor(o*(ab-1)+ob*(a-1)+1-a*ab)
print('H=',H)
print('ratio H/cond=',S.factor(H/condition))
