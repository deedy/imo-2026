import sympy as s
S,C,U,X,h,R,D=s.symbols('S C U X h R D', nonzero=True)
V=S*X+C*U;W=C*X-S*U
# omit common 2/c coordinates
# inverse K normalized qK=(2-RX + i RU)/gR because 1/(2-Ru)=(2-R/u)/gR
# inverse L qL = v*u/[h(2u-D)]; multiply conjugate: vu*(2/u-D)/(h gD)=v*(2-Du)/(h gD)
# components v(2-Du): real 2C-DW, imag 2S-DV
gR=R**2-4*R*X+4;gD=D**2-4*D*X+4
kx=(2-R*X)/gR;ky=R*U/gR
lx=(2*C-D*W)/(h*gD);ly=(2*S-D*V)/(h*gD)
wx=(h*C-1)/(h**2-1);wy=h*S/(h**2-1)
cross=s.factor((kx-wx)*(ly-wy)-(ky-wy)*(lx-wx))
num,den=s.together(cross).as_numer_denom();num=s.expand(num)
print('num terms',len(s.Poly(num).terms()),'factor',s.factor(num));print('den',s.factor(den))
F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=2*U*h-F(R);ED=2*U-h*F(D) # second 2U/h=FD -> 2U-hFD=0
# sequential divide numerator constraints
for first,e1,var1,e2,var2 in [('R',ER,R,ED,D),('D',ED,D,ER,R)]:
 q1,rem=s.div(num,e1,var1);q2,rem2=s.div(rem,e2,var2)
 print(first,'q1',s.factor(q1),'q2',s.factor(q2),'remfactor',s.factor(rem2))
 # clear denominators and reduce IA IX
 nrem,drem=s.together(rem2).as_numer_denom()
 G=s.groebner([C**2+S**2-1,X**2+U**2-1],C,X,S,U,R,D,h,order='grevlex')
 print('base rem',s.factor(G.reduce(s.expand(nrem))[1]))
# Try reduce num by unit first, then constraints
G=s.groebner([C**2+S**2-1,X**2+U**2-1],C,X,S,U,R,D,h,order='grevlex')
nr=s.factor(G.reduce(num)[1]);print('unit reduced',nr)
q1,rr=s.div(nr,ER,R);q2,rr=s.div(rr,ED,D);print('post q',s.factor(q1),s.factor(q2),'rem',s.factor(rr))
