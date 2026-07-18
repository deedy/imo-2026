import sympy as S
p,q,s,t=S.symbols('p q s t', positive=True)
# introduce lambda components U,V and derive factor at abstract level possibly discover simple invariant
U,V=S.symbols('U V', real=True)
# K abstract in p,s; L B+t direction
kx=(2*p+s)/(p+s); ky=p*s/(p+s)
lx=2-t*(1-p*q); ly=t*(p+q)
# N = L/(U+iV), convention lambda=U+iV
W=U**2+V**2
nx=(lx*U+ly*V)/W; ny=(ly*U-lx*V)/W
cross=lambda x,y,a,b:x*b-y*a
Tx=(1-p*s)*nx-(p+s)*ny; Ty=(p+s)*nx+(1-p*s)*ny
Q=S.factor(cross(kx-2*nx,ky-2*ny,Tx,Ty))
k2=kx*kx+ky*ky;l2=lx*lx+ly*ly;n2=nx*nx+ny*ny
D=S.factor(cross(kx,ky,lx,ly)*(n2-1)-cross(kx,ky,nx-1,ny)*l2+cross(lx,ly,nx-1,ny)*k2)
# impose U=(2p+q)/(p+q), V=-pq/(p+q); seek understand ratio before substitution maybe factor D*something-Q*coeff
print('abstract Q terms=',S.factor(Q))
print('abstract D=',S.factor(D))
# Maybe identities via dot/cross lambda and geometry.
# substitute U,V only in D/Q gave. print ratio abstract factor maybe
print('abstract ratio=',S.factor(D/Q))
