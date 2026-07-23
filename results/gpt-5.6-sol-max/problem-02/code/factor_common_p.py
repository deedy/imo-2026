import sympy as s
S,C,U,X,b,c,R,D,p=s.symbols('S C U X b c R D p', nonzero=True)
V=S*X+C*U
H=2*C*U*X-2*S*U**2+3*S
T=s.symbols('T');F=lambda t:s.expand(V*t**2-H*t+2*S*X+2*C*U)
# compact equations with denominators clear ourselves.
# coords
k=c*(2*S-R*V)/(2*S);m=c*R*U/(2*S);l=b*D*U/(2*S);n=b*(2*S-D*V)/(2*S)
QK=c*c*(4-4*R*X+R**2)/4; QL=b*b*(4-4*D*X+D**2)/4
q=(2*c*p+b*b-c*c)/(2*b)
e1=s.factor(s.together(p*k+q*m-QK)*8*S*b/c) # perhaps simple
# substitute b=c FR/(2U) into e1 and factor solve p
FR=F(R)
e1sub=s.factor(s.together(e1.subs(b,c*FR/(2*U))))
print('e1=',e1)
print('e1sub=',e1sub)
print('p coefficient/fixed',s.factor(s.together(e1sub).as_numer_denom()[0].coeff(p)),s.factor(s.together(e1sub).as_numer_denom()[0].coeff(p,0)))
e2=s.factor(s.together(p*l+q*n-QL)*8*S/b)
e2sub=s.factor(s.together(e2.subs(b,c*FR/(2*U))))
print('e2=',e2)
print('e2sub=',e2sub)
# quotient e2sub/e1sub should be factor if literally same linear polynomial. find ratio coeffs
n1=s.together(e1sub).as_numer_denom()[0];n2=s.together(e2sub).as_numer_denom()[0]
ratio=s.factor(n2.coeff(p)/n1.coeff(p)); print('ratio',ratio);print('difference',s.factor(n2-ratio*n1))
# Perhaps F(R) itself simplifies/factors: factor as products in R using V,H definitions. Discover relation to geometry maybe F(R)=2U b/c.
print('FR factor=',s.factor(FR))
# Calculate common p solution factor
psol=s.factor(-n1.coeff(p,0)/n1.coeff(p));print('psol=',psol)
# simplify psol perhaps physical nice. substitute FR expanded? already
