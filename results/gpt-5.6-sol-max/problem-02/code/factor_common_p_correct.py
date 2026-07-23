import sympy as s
S,C,U,X,b,c,R,D,p=s.symbols('S C U X b c R D p', nonzero=True)
V=S*X+C*U;H=2*C*U*X-2*S*U**2+3*S
F=lambda t:s.expand(V*t**2-H*t+2*S*X+2*C*U)
k=c*(2*S-R*V)/(2*S);m=c*R*U/(2*S);l=b*D*U/(2*S);n=b*(2*S-D*V)/(2*S)
QK=c*c*(4-4*R*X+R**2)/4; QL=b*b*(4-4*D*X+D**2)/4
q=(2*c*p+b*b-c*c)/(2*b)
e1=s.together(p*k+q*m-QK).as_numer_denom()[0]
e2=s.together(p*l+q*n-QL).as_numer_denom()[0]
e1=s.expand(e1);e2=s.expand(e2)
A1=e1.coeff(p);B1=e1.coeff(p,0);A2=e2.coeff(p);B2=e2.coeff(p,0)
P=s.factor(A1*B2-A2*B1)
print('A1 B1=',s.factor(A1),s.factor(B1));print('A2 B2=',s.factor(A2),s.factor(B2));print('P=',P)
FR=F(R);FD=F(D)
# substitute both b/c relation. Since ER says b=cFR/2U. ED then imposes c/b=FD/2U -> FR FD=4U².
Pb=s.factor(s.together(P.subs(b,c*FR/(2*U))).as_numer_denom()[0]);print('Pb factor=',Pb)
# divide/factor by product condition
Prod=s.expand(FR*FD-4*U**2)
print('division prod',s.factor(s.div(Pb,Prod,D)[0]),s.factor(s.div(Pb,Prod,D)[1]))
# reduce with trig identities if remainder nonzero
rem=s.div(Pb,Prod,D)[1]
G=s.groebner([S**2+C**2-1,U**2+X**2-1],C,X,S,U,R,D,c,order='grevlex')
print('remainder trig=',s.factor(G.reduce(s.expand(rem))[1]))
# Maybe Pb exactly product * factor modulo identities. Reduce Pb and Prod then division.
PbR=s.factor(G.reduce(s.expand(Pb))[1]); PrR=s.factor(G.reduce(s.expand(Prod))[1]);print('PbR',PbR);print('ProdR',PrR);print('div reduced',tuple(s.factor(a) for a in s.div(PbR,PrR,D)))
