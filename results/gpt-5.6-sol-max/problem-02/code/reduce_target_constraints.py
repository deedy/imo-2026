import sympy as s
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D')
V=S*X+C*U;W=C*X-S*U
F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=s.expand(2*U*b-c*F(R));ED=s.expand(2*U*c-b*F(D))
IA=S**2+C**2-1;Ix=U**2+X**2-1;Is=b**2+c**2-2*C*b*c-S**2
r=c*R/2;d=b*D/2;kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r;L2=b*b-2*b*d*X+d*d
P=K2*ly-ky*L2;Q=kx*L2-K2*lx;det=kx*ly-ky*lx
T=s.expand(2*(b*(C*P+S*Q)-c*P)-(b*b-c*c)*det)
# divide sequentially by ER in R and ED in D, print quotient/rem; then perhaps base identities.
qR,remR=s.div(T,ER,R);print('qR=',s.factor(qR));print('remR terms',len(s.Poly(remR).terms()),'factor',s.factor(remR))
qD,remD=s.div(remR,ED,D);print('qD=',s.factor(qD));print('remD terms',len(s.Poly(remD).terms()),'factor',s.factor(remD))
# reverse
qd,rd=s.div(T,ED,D);qr,rr=s.div(rd,ER,R);print('reverse qD',s.factor(qd));print('reverse qR',s.factor(qr));print('reverse rem factor',s.factor(rr))
# reduce rem by trig identities using groebner and inspect
G=s.groebner([IA,Ix,Is],C,X,b,c,U,S,R,D,order='grevlex')
print('base reduced rem',s.factor(G.reduce(s.expand(remD))[1]))
# Maybe qR/qD already clean and final rem base zero? check
