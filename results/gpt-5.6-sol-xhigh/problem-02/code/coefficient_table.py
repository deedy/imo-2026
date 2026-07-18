import sympy as S
# Generate compact coefficient tables for Q and D in trig variables after choosing strategic denominators.
a,b,c,d,e,f,t=S.symbols('a b c d e f t', real=True)
P=a*f+b*e # sinxz
R=a*d+b*c # sinxy
C=b*d-a*c # cosxy
G=a*a*c*c+4*a*a*d*d+4*a*b*c*d+b*b*c*c # numerator lambda norm *R²
kx=(2*a*f+b*e)/P; ky=a*e/P
lx=2-t*C;ly=t*R
nx=R*(a*a*c*d*t-2*a*b*d*d*t+4*a*d-b*b*c*d*t+2*b*c)/G
ny=R*(a*a*c*c*t+2*a*a*d*d*t+2*a*b*c*d*t+2*a*c+b*b*c*c*t)/G
Cxz=b*f-a*e
cross=lambda x,y,u,v:S.expand(x*v-y*u)
Tx=Cxz*nx-P*ny;Ty=P*nx+Cxz*ny
Q=S.factor(cross(kx-2*nx,ky-2*ny,Tx,Ty))
k2=S.factor(kx*kx+ky*ky);l2=S.factor(lx*lx+ly*ly);n2=S.factor(nx*nx+ny*ny)
D=S.factor(cross(kx,ky,lx,ly)*(n2-1)-cross(kx,ky,nx-1,ny)*l2+cross(lx,ly,nx-1,ny)*k2)
# reduce using b2=1-a2 etc perhaps Q numerator is still big. ratio direct suffices.
for name,expr,den in [('Q',Q,P*G),('D',D,P**2*G)]:
 num=S.factor(S.together(expr*den))
 # Groebner reduce substituting b²? trig identities all 3. Try factor currently
 print(name,'scaled factor=',num)
 print('degree t',S.degree(num,t))
 for j in range(3):
  co=S.factor(S.expand(num).coeff(t,j))
  if co: print(j,co)
