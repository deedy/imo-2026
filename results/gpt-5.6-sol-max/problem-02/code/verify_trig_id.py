import sympy as s
A,x=s.symbols('A x', real=True)
S=s.sin(A);C=s.cos(A);U=s.sin(x);X=s.cos(x)
lhs=s.cos(A-x)-X*s.cos(A+2*x)
rhs=U*(2*C*U*X-2*S*U**2+3*S)
print(s.trigsimp(s.expand_trig(lhs-rhs)))
# Generic equation derivation algebra via q=cot t
q,rho,th=s.symbols('q rho th')
# original divided sin²t:
# sinth (sin(P+t)/sint) = 2S (sin(x+t)/sint)(sin(th-x-t)/sint)
# ratios sin(P+t)/sint=sinP q+cosP; sin(x+t)/sint=Uq+X; sin(th-x-t)/sint=sin(th-x)q-cos(th-x)
P=A+2*x
E=s.sin(th)*(s.sin(P)*q+s.cos(P))-2*S*(U*q+X)*(s.sin(th-x)*q-s.cos(th-x))
# q=(1/rho-X)/U and multiply rho² U? Compare J expression
Esub=s.factor(s.together(E.subs(q,(1/rho-X)/U)))
J=-rho**2*s.sin(th)*U*s.sin(A+x)+rho*s.sin(th)*(s.cos(A-x)-X*s.cos(A+2*x))-2*S*U*s.sin(th-x)
print('factor comparison E vs J',s.trigsimp(s.expand_trig(Esub*rho**2*U-J)))
