import sympy as S
x,y,z,t=S.symbols('x y z t', real=True)
i=S.I
h=S.sin(x)/S.sin(x+z); j=S.sin(x)/S.sin(x+y)
k=1+h*S.exp(i*z); lam=1+j*S.exp(-i*y)
l=2-t*S.exp(-i*(x+y)); a=l/lam
phi=x+z
# reality numerator Q = Im((k*lam*conj(l)-2|l|2)e^-iphi)
conj=lambda q:S.conjugate(S.expand_complex(q)) # probably
Q=S.im(S.expand_complex((k*lam*S.conjugate(l)-2*l*S.conjugate(l))*S.exp(-i*phi)))
print('Q raw collect t')
for power in range(3):
 co=S.expand(Q).coeff(t,power)
 print(power, S.trigsimp(S.simplify(co),method='fu'))
# use fu
from sympy.simplify.fu import fu
print('fu coeff')
qco=[]
for power in range(3):
 co=fu(S.expand_trig(S.expand(Q).coeff(t,power)))
 qco.append(S.factor(co))
 print(power,S.factor(co))
# derive target determinant in real vectors, clear |lam| denominators perhaps
# circle determinant rows k,l,a-1 with norm terms. Multiply a rows etc.
def cr(P,Q): return S.im(S.conjugate(P)*Q)
D=cr(k,l)*(abs(1)**2-a*S.conjugate(a)) # derive determinant carefully
# determinant row k,l,w: cross(k,l)*R_w - cross(k,w)|l|2 + cross(l,w)|k|2 where Rw=|a|2-1
w=a-1
Det=cr(k,l)*(a*S.conjugate(a)-1)-cr(k,w)*(l*S.conjugate(l))+cr(l,w)*(k*S.conjugate(k))
Det=S.simplify(S.expand_complex(Det))
# clear |lambda|2 likely
Dc=S.trigsimp(Det*(lam*S.conjugate(lam)),method='fu')
print('D coeff after lamnorm')
for power in range(4):
 co=S.expand(Dc).coeff(t,power)
 if co!=0: print(power, S.factor(fu(S.expand_trig(co))))
print('compute ratios coefficients numeric simplify')
for idx in range(3):
 print(idx, S.trigsimp(S.simplify(S.expand(Dc).coeff(t,idx)/S.expand(Q).coeff(t,idx)),method='fu'))
