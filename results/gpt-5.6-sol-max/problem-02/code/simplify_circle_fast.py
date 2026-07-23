import sympy as s
S,C,U,X,b,c,R,D,p=s.symbols('S C U X b c R D p', nonzero=True)
V=S*X+C*U
r=c*R/2;d=b*D/2
k=c-r*V/S;m=r*U/S;l=d*U/S;n=b-d*V/S
QK=c*c-2*c*r*X+r*r
QL=b*b-2*b*d*X+d*d
# target qdes
q=(2*c*p+b*b-c*c)/(2*b)
EK=s.together(p*k+q*m-QK).as_numer_denom()[0]
EL=s.together(p*l+q*n-QL).as_numer_denom()[0]
# coefficients p
Ak=s.expand(EK).coeff(p);Bk=s.expand(EK).coeff(p,0)
Al=s.expand(EL).coeff(p);Bl=s.expand(EL).coeff(p,0)
res=s.factor(Ak*Bl-Al*Bk)
print('coords',k,m,l,n,flush=True)
print('EK coeff',s.factor(Ak),s.factor(Bk),flush=True)
print('EL coeff',s.factor(Al),s.factor(Bl),flush=True)
print('result fact',res,flush=True)
# make substitutions C²=1-S², X²=1-U² manually via groebner only target modest
rels=[C**2+S**2-1,U**2+X**2-1,b**2+c**2-2*C*b*c-S**2]
gens=(C,X,b,c,U,S,R,D)
G=s.groebner(rels,*gens,order='grevlex')
rem=s.factor(G.reduce(s.expand(res))[1]);print('result reduced',rem,flush=True)
ER=s.expand(-R**2*V*c+R*c*(2*C*U*X-2*S*U**2+3*S)-2*S*X*c+2*U*b-2*C*U*c)
ED=s.expand(-D**2*V*b+D*b*(2*C*U*X-2*S*U**2+3*S)-2*S*X*b+2*U*c-2*C*U*b)
print('ER',s.factor(ER));print('ED',s.factor(ED),flush=True)
for combo,name in [(D*ER-R*ED,'D ER-R ED'),(D*b*ER-R*c*ED,'DbER-RcED'),((2-D)*ER-(2-R)*ED,'etc'),(b*D*(2-D)*ER-c*R*(2-R)*ED,'weighted')]:
 rr=s.factor(G.reduce(s.expand(combo))[1]);print(name,rr,flush=True)
