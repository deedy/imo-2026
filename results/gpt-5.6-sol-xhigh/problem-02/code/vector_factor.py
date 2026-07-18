import sympy as S
# use p=tan x q=tan y z remains k. Normalize AB=2. Avoid a=(u,v) incidence BL equation.
p,q,s,t=S.symbols('p q s t', real=True, nonzero=True)
# Unit dirs divided common sqrt. We can use nonunit since lengths coefficients adjust.
# Direct formulas earlier scale AB2:
kx=(2*p+s)/(p+s); ky=s*p/(p+s)
# l= B + distance ray. Parametrize l=(2-T*(1-pq), T*(p+q)) ignoring norm; call T positive scaled
lx=2-t*(1-p*q); ly=t*(p+q)
# lambda map a->l from CNL: complex lambda = 1+ sinx/sin(x+y)e^-iy
# earlier Cartesian components lambda: relative for normalized a: L=a*lambda
# Calculate lambda tangent: sinx/sin(x+y)e^-iy = p sqrt... gives p(1-iq)/(p+q)
lamx=1+p/(p+q); lamy=-p*q/(p+q)
# a=l/lambda complex
lam2=S.factor(lamx**2+lamy**2)
ax=S.factor((lx*lamx+ly*lamy)/lam2)
ay=S.factor((ly*lamx-lx*lamy)/lam2)
print('lambda',S.factor(lamx),lamy,lam2)
print('a',ax,ay)
# CK direction a*exp i(x+z); nonnormalized rotate using dir ((1-ps),(p+s))
dx=S.factor(ax*(1-p*s)-ay*(p+s)); dy=S.factor(ax*(p+s)+ay*(1-p*s))
Q=S.factor((kx-2*ax)*dy-(ky-2*ay)*dx)
print('Q=',Q)
# determinant target
cross=lambda x1,y1,x2,y2:x1*y2-y1*x2
k2=S.factor(kx*kx+ky*ky); l2=S.factor(lx*lx+ly*ly); a2=S.factor(ax*ax+ay*ay)
D=S.factor(cross(kx,ky,lx,ly)*(a2-1)-cross(kx,ky,ax-1,ay)*l2+cross(lx,ly,ax-1,ay)*k2)
print('D=',D)
print('ratio=',S.factor(D/Q))
