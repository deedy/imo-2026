import sympy as s
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D')
V=S*X+C*U;W=C*X-S*U;F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=2*U*b-c*F(R);ED=2*U*c-b*F(D);IA=C**2+S**2-1;Ix=X**2+U**2-1
r=c*R/2;d=b*D/2;kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r;L2=b*b-2*b*d*X+d*d
P0=K2*ly-ky*L2;Q0=kx*L2-K2*lx;Delta=kx*ly-ky*lx
T=s.expand(2*(b*(C*P0+S*Q0)-c*P0)-(b*b-c*c)*Delta)
# division q values generated; print exact qR qD and check guessed factored
qR,rem=s.div(T,ER,R);qD,Hrem=s.div(rem,ED,D)
ARguess=b*c*(C**2*D*U*b-C*D*U*c+D*S**2*U*b-D*S*X*c+2*S*c)/(4*V)
ADguess=b*c*(C*R*U*b+R*S*X*b-R*U*c-2*S*b)/(4*V)
G=U*b*c**2*(2*C*D*R*U*X*b-2*C*D*U*b+2*D*R*S*X**2*b-D*R*S*b-2*D*S*X*b-2*R*U*c)
H=S*b*c*(C*D*R*U*b**2-C*D*R*U*c**2+D*R*S*X*b**2-D*R*S*X*c**2-2*D*S*b**2+2*R*S*c**2)
print('q checks',s.simplify(qR-ARguess),s.simplify(qD-ADguess))
print('residual certificate',s.factor(s.together(4*V*Hrem-IA*G-Ix*H)))
# Therefore exact identity T=qR ER+qD ED+(IA G+Ix H)/(4V)
Final=s.factor(s.together(4*V*T-(4*V*ARguess)*ER-(4*V*ADguess)*ED-IA*G-Ix*H))
print('FINAL remainder',Final)
print('multipliers scaled A=',s.factor(4*V*ARguess),'B=',s.factor(4*V*ADguess))
# numeric random exact substitutions sanity
