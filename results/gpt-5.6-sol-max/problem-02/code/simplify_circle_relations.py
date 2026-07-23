import sympy as s
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D', nonzero=True)
V=S*X+C*U
r=c*R/2;d=b*D/2
k=c-r*V/S; m=r*U/S # K coords k,m
l=d*U/S; n=b-d*V/S # L coords l,n
Q=lambda xx,yy:s.factor(xx**2+yy**2+2*C*xx*yy)
QK=s.factor(Q(k,m));QL=s.factor(Q(l,n))
# reduce using trig identities only
Gtr=s.groebner([S**2+C**2-1,U**2+X**2-1],C,X,U,S,b,c,R,D,order='grevlex')
def red(expr):
 num,den=s.together(expr).as_numer_denom();return s.factor(Gtr.reduce(s.expand(num))[1]),s.factor(den)
print('K coord scaled',s.factor(k),s.factor(m))
print('QK raw/reduced',red(QK))
print('QL raw/reduced',red(QL))
print('det reduced',red(k*n-m*l))
# Better geometry: Euclidean |BK|=r implies Q(K)=? K=B+r direction, QK=c²-2cr cosx+r² indeed direction angle pi-x from AB => dot B to vector -cosx,+sinx.
print('expected qk',s.factor(c*c-2*c*r*X+r*r))
# Indeed K cartesian B + r(-cosx,sinx): oblique formulas. L=C+d(direction angle? from CA toward interior, absolute angle alpha? CL direction angle alpha? C to L ray toward A rotated CCW? coordinates leads QL=b²-2bdX+d².)
# circle equations p*k+q*m=QK etc. target q relation. Avoid solve perhaps desired target equivalent linear functional.
# Let desired q = (2cp+b²-c²)/(2b). Plug into K,L equations solve p separately consistency gives one determinant identity.
p=s.symbols('p')
qdes=(2*c*p+b*b-c*c)/(2*b)
EK=s.factor(2*b*(p*k+qdes*m-QK))
EL=s.factor(2*b*(p*l+qdes*n-QL))
# each linear p. eliminate p resultant
res=s.factor(s.resultant(s.together(EK).as_numer_denom()[0],s.together(EL).as_numer_denom()[0],p))
print('result factor raw=',res)
num=s.expand(res)
# reduce trig & side identities
Gall=s.groebner([S**2+C**2-1,U**2+X**2-1,b**2+c**2-2*C*b*c-S**2],C,X,b,c,U,S,R,D,order='grevlex')
rem=s.factor(Gall.reduce(num)[1]); print('result reduced base=',rem)
# Then factor modulo constraints maybe simple combination ER ED.
ER=s.expand(-R**2*V*c+R*c*(2*C*U*X-2*S*U**2+3*S)-2*S*X*c+2*U*b-2*C*U*c)
ED=s.expand(-D**2*V*b+D*b*(2*C*U*X-2*S*U**2+3*S)-2*S*X*b+2*U*c-2*C*U*b)
# See resultant perhaps factor involving D ER - R ED etc after ordinary factor plus identities substitutions.
print('ER',s.factor(ER));print('ED',s.factor(ED))
# Try candidate combinations coefficients low degree: factor rem; divide by R,D etc.
# calculate reductions of combinations D? difference b? 
for combo,name in [(D*ER-R*ED,'D ER-R ED'),(D*b*ER-R*c*ED,'DbER-RcED'),((2-D)*ER-(2-R)*ED,'etc')]:
 rr=s.factor(Gall.reduce(s.expand(combo))[1]);print(name,rr)
