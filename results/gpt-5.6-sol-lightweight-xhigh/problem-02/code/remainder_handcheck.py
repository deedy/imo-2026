import sympy as S
p,q,s,t=S.symbols('p q s t', real=True)
# denominator choices: H=p2q2+4p2+4pq+q2; E=pq2t+pt+q coefficient
H=p*p*q*q+4*p*p+4*p*q+q*q
E=p*q*q*t+p*t+q
# data
kx=(2*p+s)/(p+s);ky=p*s/(p+s)
lx=2-t*(1-p*q);ly=t*(p+q)
nx=(p+q)*(p*p*q*t-2*p*t+4*p-q*t+2*q)/H
ny=(p+q)*(p*p*q*q*t+2*p*p*t+2*p*q*t+2*p*q+q*q*t)/H
cross=lambda x,y,a,b:S.expand(x*b-y*a)
Tx=S.expand((1-p*s)*nx-(p+s)*ny);Ty=S.expand((p+s)*nx+(1-p*s)*ny)
Q=S.factor(cross(kx-2*nx,ky-2*ny,Tx,Ty))
k2=S.expand(kx*kx+ky*ky);l2=S.expand(lx*lx+ly*ly);n2=S.expand(nx*nx+ny*ny)
D=S.factor(cross(kx,ky,lx,ly)*(n2-1)-cross(kx,ky,nx-1,ny)*l2+cross(lx,ly,nx-1,ny)*k2)
R=S.factor((p+q)*(p+s)*D-p*E*Q)
print(R)
# To present hand verification perhaps list common-denominator numerator coefficients in s? Identity R=0 direct.
# Find more elegant by simplify N formulas via lambda perhaps H factors!
print('H factor',S.factor(H), 'E',E)
# H=(p+q)^2? etc + p2(1+q2)*3?
# Extract Q common polynomial maybe no need.
# Could state after substitution both D and Q equal common P with P listed? avoid huge.
# Verify using CAS only, but write "straight expansion" accepted perhaps identity compact even though internal huge. Need rigorous enough can assert algebra lemma and prove via organizing.
# Look for alternate param of lambda simplifies if choose cot? lambda perhaps lambda=(sin?); use trig vectors could coefficient geometrically.
