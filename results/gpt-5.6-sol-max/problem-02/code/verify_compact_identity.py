import sympy as s
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D')
V=S*X+C*U;W=C*X-S*U
F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=2*U*b-c*F(R); ED=2*U*c-b*F(D)
r=c*R/2;d=b*D/2
kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r;L2=b*b-2*b*d*X+d*d
P0=K2*ly-ky*L2;Q0=kx*L2-K2*lx;Delta=kx*ly-ky*lx
T=s.expand(2*(b*(C*P0+S*Q0)-c*P0)-(b*b-c*c)*Delta)
A=s.expand(b*c*(D*U*b-D*V*c+2*S*c))
B=s.expand(b*c*(R*V*b-R*U*c-2*S*b))
diff=s.factor(s.expand(4*V*T-A*ER-B*ED))
print('raw diff factor=',diff)
# find compact decomposition by IA,Ix
IA=C*C+S*S-1;IX=X*X+U*U-1
q1,rem=s.div(diff,IA,C);q2,rem2=s.div(rem,IX,X)
print('q1=',s.factor(q1)); print('q2=',s.factor(q2));print('rem=',s.factor(rem2))
# substitute trig identities numerical symbolic parametrization confirms
# perhaps raw diff factors simply IA/IX combo from prior G etc.
