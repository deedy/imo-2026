import cmath, math
from explore_angles import D,comp,bisect

def cross(u,v): return (u.conjugate()*v).imag

def target(a,x,y,z,rho):
    p=math.sin(x)/math.sin(x+z)
    q=math.sin(x)/math.sin(x+y)
    U=rho*(1+p*cmath.exp(1j*z))
    V=cmath.exp(1j*a)*(1+q*cmath.exp(-1j*y))
    B=rho+0j; C=cmath.exp(1j*a); W=C-B
    return cross(W,V)*abs(U)**2+cross(U,W)*abs(V)**2-(1-rho**2)*cross(U,V)

def circum(a,x,y,z,rho):
    p=math.sin(x)/math.sin(x+z);q=math.sin(x)/math.sin(x+y)
    U=rho*(1+p*cmath.exp(1j*z));V=cmath.exp(1j*a)*(1+q*cmath.exp(-1j*y))
    # X coordinate solve 2 dot X,U=|U|2
    det=cross(U,V)
    # representation perhaps solve np manually
    ux,uy=U.real,U.imag;vx,vy=V.real,V.imag
    rhs1=abs(U)**2/2;rhs2=abs(V)**2/2
    X=complex((rhs1*vy-uy*rhs2)/det,(ux*rhs2-rhs1*vx)/det)
    return X,abs(X-rho)-abs(X-cmath.exp(1j*a)),U,V

samples=[(1.0,.2,.25,.8810667328109274),(.8,.15,.35,.6802085831668412),(1.2,.1,.2,1.0511891415775834),(.6,.25,.15,1.0515717302274403),(1,.4,.1,1.0140655954761684)]
for a,x,y,z in samples:
 t=x+y
 rho=D(a,x,t)/(2*math.sin(t)**2)
 print(target(a,x,y,z,rho),circum(a,x,y,z,rho)[:2])
