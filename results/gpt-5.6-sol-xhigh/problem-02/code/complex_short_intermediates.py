import sympy as S
X,Y,Z=S.symbols('X Y Z', nonzero=True)
t,h,g=S.symbols('t h g', real=True, nonzero=True)
def cj(expr): return S.together(expr.xreplace({X:1/X,Y:1/Y,Z:1/Z}))
k=1+h*Z; lam=1+g/Y;l=2-t/(X*Y);n=S.factor(l/lam); R=X*Z
br=lambda u,v:S.factor((cj(u)*v-u*cj(v))/(2*S.I))
Q=S.factor(br(k-2*n,R*n))
D=S.factor(br(k,l)*(n*cj(n)-1)-br(k,n-1)*l*cj(l)+br(l,n-1)*k*cj(k))
print('Q=',Q)
print('D=',D)
print('ratio=',S.factor(D/Q))
# impose h,g definitions into ratio only
hs=(X-1/X)/(X*Z-1/(X*Z)); gs=(X-1/X)/(X*Y-1/(X*Y))
print('ratio specialized=',S.factor((D/Q).subs({h:hs,g:gs})))
