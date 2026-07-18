import sympy as S
# derive D and Q in basis exploiting L=lambda N; keep vector N=(u,v), lambda=(U,V), K=(r,w), T rotation=(c,d)
u,v,U,V,r,w,c,d=S.symbols('u v U V r w c d', real=True)
cross=lambda a,b,e,f:a*f-b*e
dot=lambda a,b,e,f:a*e+b*f
# L=lambda N
lx=U*u-V*v;ly=V*u+U*v
l2=S.factor(lx**2+ly**2); n2=u*u+v*v;k2=r*r+w*w
D=S.factor(cross(r,w,lx,ly)*(n2-1)-cross(r,w,u-1,v)*l2+cross(lx,ly,u-1,v)*k2)
# T N=(c+id)N
Tx=c*u-d*v;Ty=d*u+c*v
Q=S.factor(cross(r-2*u,w-2*v,Tx,Ty))
print('D=',S.collect(S.expand(D),[r,w]))
print('D fact=',D)
print('Q=',S.collect(S.expand(Q),[r,w]))
# geometry also L on line from (2,0): imposes l=...; K formula relations.
# simplify D in invariants A=dot(K,N), B=cross(K,N), n2
A,B=S.symbols('AA BB')
# replace r*u+w*v=A, r*v-w*u=B maybe solve r,w
rsol=(A*u+B*v)/n2; wsol=(A*v-B*u)/n2
Di=S.factor(D.subs({r:rsol,w:wsol}))
Qi=S.factor(Q.subs({r:rsol,w:wsol}))
print('Di=',Di)
print('Qi=',Qi)
