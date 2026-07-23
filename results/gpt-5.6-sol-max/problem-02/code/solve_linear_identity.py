import sympy as s
# Seek resultant P = A*ER+B*ED modulo base identities, with low-degree A,B. Instead derive relation elegantly by solving ER for b in terms c,R and ED for c in b,D.
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D', nonzero=True)
V=S*X+C*U
H=2*C*U*X-2*S*U**2+3*S
ER=-R**2*V*c+R*c*H-2*S*X*c+2*U*b-2*C*U*c
ED=-D**2*V*b+D*b*H-2*S*X*b+2*U*c-2*C*U*b
# write 2U b/c = F(R), 2U c/b=F(D), where F(t)=t²V-tH+2SX+2CU
T=s.symbols('T')
F=s.expand(T**2*V-T*H+2*S*X+2*C*U)
print('F=',s.factor(F))
# constraints exactly b/c=F(R)/(2U), c/b=F(D)/(2U), hence F(R)F(D)=4U². This is key combined relation. Perhaps target resultant only depends on product relation! Test reduce resultant modulo side and Fproduct.
FR=s.expand(F.subs(T,R));FD=s.expand(F.subs(T,D));Prod=s.expand(FR*FD-4*U**2)
print('ER compare',s.factor(ER-(2*U*b-c*FR)));print('EDcompare',s.factor(ED-(2*U*c-b*FD)))
# Since individually also gives side ratio. Circle target may follow from one plus side identity.
# Reconstruct compact elimination resultant P/(2bc) from fast, but use direct coeff.
r=c*R/2;d=b*D/2;k=c-r*V/S;m=r*U/S;l=d*U/S;n=b-d*V/S
QK=c*c*(1-R*X+R**2/4);QL=b*b*(1-D*X+D**2/4)
p=s.symbols('p');q=(2*c*p+b*b-c*c)/(2*b)
EK=s.together(p*k+q*m-QK).as_numer_denom()[0];EL=s.together(p*l+q*n-QL).as_numer_denom()[0]
P=s.expand(EK.coeff(p)*EL.coeff(p,0)-EL.coeff(p)*EK.coeff(p,0))
# substitutions b = c FR/(2U) should make P zero using side identity perhaps and product.
Pb=s.factor(s.together(P.subs(b,c*FR/(2*U))).as_numer_denom()[0])
print('P after b ratio factor=',Pb)
# reduce trig then factor
Gt=s.groebner([S**2+C**2-1,U**2+X**2-1],C,X,S,U,R,D,c,order='grevlex')
rem=s.factor(Gt.reduce(s.expand(Pb))[1]);print('reduced factor=',rem)
# include product relation maybe division
Gprod=s.groebner([S**2+C**2-1,U**2+X**2-1,Prod],R,D,C,X,S,U,c,order='grevlex')
rem2=s.factor(Gprod.reduce(s.expand(Pb))[1]);print('with prod rem=',rem2)
# side relation after b ratio yields c relation that may be needed: b²+c²-2Cbc=S² -> c²(FR²+4U²-4CU FR)=4U²S².
SideR=s.expand(c**2*(FR**2+4*U**2-4*C*U*FR)-4*U**2*S**2)
G3=s.groebner([S**2+C**2-1,U**2+X**2-1,Prod,SideR],R,D,c,C,X,S,U,order='grevlex')
rem3=s.factor(G3.reduce(s.expand(Pb))[1]);print('with side rem=',rem3)
