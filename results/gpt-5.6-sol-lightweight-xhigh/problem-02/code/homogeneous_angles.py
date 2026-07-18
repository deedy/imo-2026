import sympy as S
# Use sine/cos pairs for angles x,y,z: P=sinx, P0=cosx etc. derive no tangent.
a,b,c,d,e,f,t=S.symbols('a b c d e f t', real=True) # a=sinx,b=cosx,c=siny,d=cosy,e=sinz,f=cosz
# normalize AB2. K=1+ sinx/sin(x+z)*(cosz,sinz)
Sxz=a*f+b*e; Sxy=a*d+b*c
kx=S.factor(1+a*f/Sxz); ky=S.factor(a*e/Sxz)
# L=2 + T*(-cos(x+y),sin(x+y)); choose actual BL t, unit
Cxy=b*d-a*c
lxy=Sxy
lx=2-t*Cxy;ly=t*Sxy
# lambda=1+sinx/sin(x+y) e^-iy
U=S.factor(1+a*d/Sxy);V=S.factor(-a*c/Sxy)
W=S.factor(U*U+V*V)
nx=S.factor((lx*U+ly*V)/W);ny=S.factor((ly*U-lx*V)/W)
# true rotation x+z matrix c0=cos sum, d0=sin sum
Cxz=b*f-a*e
Tx=Cxz*nx-Sxz*ny;Ty=Sxz*nx+Cxz*ny
cross=lambda x,y,u,v:S.expand(x*v-y*u)
Q=S.factor(cross(kx-2*nx,ky-2*ny,Tx,Ty))
k2=S.factor(kx*kx+ky*ky);l2=S.factor(lx*lx+ly*ly);n2=S.factor(nx*nx+ny*ny)
D=S.factor(cross(kx,ky,lx,ly)*(n2-1)-cross(kx,ky,nx-1,ny)*l2+cross(lx,ly,nx-1,ny)*k2)
# reduce using b2+a2=1 etc via Groebner and find ratio D/Q modulo unit identities.
# Substitute trig rational numerical random infer ratio from tangent formula conversion: prior tangent t_old where L=(2-told(1-pq), told(p+q)). Compare actual: told/(b*d)=t? (1-pq)=(bd-ac)/bd; p+q=(ad+bc)/bd. so told=t*b*d.
# prior T map=(1-ps,p+s)= rotation /(b f). Qprior cross with T = Qtrue/(bf)? Tprior=R/(bf), so Qprior=Qtrue/(bf).
# coefficient prior p(p q2 told+p told+q)/((p+q)(p+s)). transform.
p=a/b;q=c/d;s=e/f;told=t*b*d
ratio=S.factor(p*(p*q*q*told+p*told+q)/((p+q)*(p+s))/(b*f)) # D/ Qtrue because D=coef Qprior=coef Qtrue/(bf)
print('ratio=',ratio)
# simplify ratio use unit maybe
print('ratio fact=',S.factor(ratio))
R=S.together(D-ratio*Q)
num=S.factor(R.as_numer_denom()[0])
print('raw rem factor=',num)
# Reduce num modulo unit circles
G=S.groebner([a*a+b*b-1,c*c+d*d-1,e*e+f*f-1],a,c,e,b,d,f,t,order='lex')
rem=G.reduce(num)[1]
print('remainder',S.factor(rem))
print('coordinates k',kx,ky,'lambda',U,V)
print('N',nx,ny)
