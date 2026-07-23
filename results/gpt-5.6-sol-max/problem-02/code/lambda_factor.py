import sympy as s
S,C,U,X,V,b,c,R,D,Lam=s.symbols('S C U X V b c R D Lam', nonzero=True)
# oblique coords, circle coeff p,q, impose target p=c/2+Lam/c q=b/2+Lam/b
p=c/s.Integer(2)+Lam/c;q=b/s.Integer(2)+Lam/b
ks=c*(1-R*V/(2*S));kt=c*R*U/(2*S)
ls=b*D*U/(2*S);lt=b*(1-D*V/(2*S))
K2=c*c*(1-R*X+R**2/4);L2=b*b*(1-D*X+D**2/4)
EK=s.factor(s.together(p*ks+q*kt-K2)*4*S*b/c) # clear
EL=s.factor(s.together(p*ls+q*lt-L2)*4*S*c/b)
print('EK=',EK)
print('EL=',EL)
# solve lam
lk=s.factor(s.solve(s.Eq(EK,0),Lam)[0]);ll=s.factor(s.solve(s.Eq(EL,0),Lam)[0]);print('lk=',lk);print('ll=',ll)
# substitute b/c=F(R)/2U and c/b=F(D)/2U; V definition/trig reduce, see lambda simplification
F=lambda T:V*(T**2-2*X*T+2)-S*T
lks=s.factor(lk.subs(b,c*F(R)/(2*U)));lls=s.factor(ll.subs(c,b*F(D)/(2*U)))
print('lks=',lks);print('lls=',lls)
# reduce using V=SX+CU and identities
C0=s.symbols('C') # same C
for expr,name in [(lks,'lks'),(lls,'lls')]:
 e=s.factor(expr.subs(V,S*X+C*U)); num,den=s.together(e).as_numer_denom()
 G=s.groebner([C**2+S**2-1,U**2+X**2-1],C,X,S,U,R,D,b,c,order='grevlex')
 nr=s.factor(G.reduce(s.expand(num))[1]);dr=s.factor(G.reduce(s.expand(den))[1])
 print(name,'reduced ratio=',nr,'/',dr)
# Difference lks-lls with both? They depend R vs D likely not universal.
