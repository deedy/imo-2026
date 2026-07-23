import sympy as s
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D')
V=S*X+C*U;W=C*X-S*U
F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=2*U*b-c*F(R);ED=2*U*c-b*F(D);IA=C**2+S**2-1;IX=X**2+U**2-1
r=c*R/2;d=b*D/2;kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r;L2=b*b-2*b*d*X+d*d
P0=K2*ly-ky*L2;Q0=kx*L2-K2*lx;delta=kx*ly-ky*lx
T=s.expand(2*(b*(C*P0+S*Q0)-c*P0)-(b*b-c*c)*delta)
A=b*c*(C**2*D*U*b-C*D*U*c+D*S**2*U*b-D*S*X*c+2*S*c)
B=b*c*(C*R*U*b+R*S*X*b-R*U*c-2*S*b)
G=U*b*c**2*(2*C*D*R*U*X*b-2*C*D*U*b+2*D*R*S*X**2*b-D*R*S*b-2*D*S*X*b-2*R*U*c)
H=S*b*c*(C*D*R*U*b**2-C*D*R*U*c**2+D*R*S*X*b**2-D*R*S*X*c**2-2*D*S*b**2+2*R*S*c**2)
# Expand each side and compare term dictionaries statistics, output optional terms
lhs=s.Poly(s.expand(4*V*T),R,D,b,c,C,S,U,X)
rhs=s.Poly(s.expand(A*ER+B*ED+IA*G+IX*H),R,D,b,c,C,S,U,X)
print('lhs terms',len(lhs.terms()),'rhs terms',len(rhs.terms()),'equal',lhs==rhs,'diff',s.expand(lhs.as_expr()-rhs.as_expr()))
