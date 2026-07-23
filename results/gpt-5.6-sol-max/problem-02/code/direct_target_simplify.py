import sympy as s
# derive target T directly in terms of r,d,b,c and trig x,A; seek factor after using raw angle constraints in cot y,z perhaps.
S,C,U,X,V,b,c,R,D=s.symbols('S C U X V b c R D', nonzero=True)
# treat identities V=SX+CU, maybe define W=cos(A+x)=CX-SU; perhaps coords cleaner complex.
W=s.symbols('W')
# Cartesian complex: K=c-r e^{-?} = c - r X + i r U. L=b e^{iA} + d direction from C toward? L Cartesian from coords = dU/S + (b-dV/S)e^{iA}; simplify equals b eA + d? calculate vector CL angle: coords delta yields dU/S e1-dV/S e2 => Cartesian x d(U-CV)/S, y -dV. likely direction angle A+x+pi? expected CL from C toward A, angle A+pi, rotated toward CB clockwise? Given angle ACL=x, ray CL from C to A direction A+pi; into triangle toward B is CCW? absolute A+pi+x; vector = -d(cos(A+x), sin(A+x))=(-d W,-d V). Check x component C point (bC,bS)+(-dW,-dV). oblique formula Cartesian l+nC=dU/S+C(b-dV/S)=bC+d(U-CV)/S. identity (U-CV)/S=-W yes. Great.
# So K=(c-rX, rU), L=(bC-dW,bS-dV).
# circle through origin equation Cartesian |z|²-Px-Qy=0. desired center equidistant M=(c/2,0),N=(bC/2,bS/2): vector linear b(CP+SQ)-cP=(b²-c²)/2 (depending P=2Ox etc). Oblique p=P, q=C P+S Q; same.
# Solve circle determinant and target maybe complex cross formulas.
r=c*R/2;d=b*D/2
kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r; L2=b*b-2*b*d*(C*W+S*V)+d*d # inner eA with e(A+x)=cosx X
L2=L2.subs(C*W+S*V,X)
det=kx*ly-ky*lx
P=s.cancel((K2*ly-ky*L2)/det);Q=s.cancel((kx*L2-K2*lx)/det)
Target=s.factor(s.together(b*(C*P+S*Q)-c*P-(b*b-c*c)/2).as_numer_denom()[0])
print('target factor raw=',Target)
# substitute W=CX-SU,V=SX+CU, identities reduce and factor
T=s.expand(Target.subs({W:C*X-S*U,V:S*X+C*U}))
G=s.groebner([C**2+S**2-1,U**2+X**2-1,b**2+c**2-2*C*b*c-S**2],C,X,b,c,U,S,R,D,order='grevlex')
Tr=s.factor(G.reduce(T)[1]);print('reduced=',Tr)
# Express angle constraints F compact and try inspect target in terms of FR etc via polynomial linear ansatz.
