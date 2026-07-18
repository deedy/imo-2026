import sympy as S
p,q,s,u,v=S.symbols('p q s u v', nonzero=True, real=True)

kx=(2*p+s)/(2*(p+s)); ky=s*p/(2*(p+s))
lx=((2*p+q)*u+p*q*v)/(2*(p+q))
ly=((2*p+q)*v-p*q*u)/(2*(p+q))

F=S.factor((1-p*q)*ly+(p+q)*(lx-1))
print('F=',F)
Vx=(1-p*s)*u-(p+s)*v
Vy=(p+s)*u+(1-p*s)*v
G=S.factor((kx-u)*Vy-(ky-v)*Vx)
print('G=',G)

k2=S.factor(kx**2+ky**2); l2=S.factor(lx**2+ly**2)
det=S.factor(kx*ly-ky*lx)
Dnum=S.factor(-k2*ly+ky*l2)
Enum=S.factor(-kx*l2+k2*lx)
# 4*det H
Hnum=S.factor(det*(u*u+v*v-1)+2*Dnum*(u-1)+2*Enum*v)
print('det=',det)
print('H numerator factored=',S.factor(Hnum))
# numerator all together
Fn=S.together(F).as_numer_denom()[0]
Gn=S.factor(S.together(G).as_numer_denom()[0])
Hn=S.factor(S.together(Hnum).as_numer_denom()[0])
print('Fn=',S.factor(Fn))
print('Gn=',S.factor(Gn))
print('Hn=',S.factor(Hn))
# reduce H modulo F,G lex v perhaps Groebner
print('divide?')
# eliminate v through F linear
vsol=S.solve(F,v)[0]
Gsub=S.factor(S.together(G.subs(v,vsol)))
Hsub=S.factor(S.together(Hnum.subs(v,vsol)))
print('vsol=',vsol)
print('Gsub=',Gsub)
print('Hsub=',Hsub)
print('ratio=',S.factor(Hsub/Gsub))
