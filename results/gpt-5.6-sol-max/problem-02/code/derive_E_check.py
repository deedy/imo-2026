import sympy as s
# Verify equation (11)->E relation exactly, track sign.
a,x,th,rho=s.symbols('a x th rho', real=True)
S=s.sin(a);C=s.cos(a);U=s.sin(x);X=s.cos(x);V=s.sin(a+x)
J=-rho**2*s.sin(th)*U*V+rho*s.sin(th)*(s.cos(a-x)-X*s.cos(a+2*x))-2*S*U*s.sin(th-x)
# divide U sin th
j=s.trigsimp(J/(U*s.sin(th)),method='fu')
print('j generic=',s.trigsimp(s.expand_trig(j),method='fu'))
# Expected -rho²V+rho H -2S(cosx-cotth U)
H=2*C*U*X-2*S*U**2+3*S
expected=-rho**2*V+rho*H-2*S*(X-s.cot(th)*U)
print('diff expected',s.trigsimp(j-expected,method='fu'))
# theta gamma cot=(b-Cc)/(S c), E relation: expected=0 => multiply c: -rho²Vc+rho Hc-2SXc+2U(b-Cc)=0 = -[rho²Vc-rhoHc+2SXc-2Ub+2CUc]
# F expanded = V rho² -H rho+2SX+2CU, cF-2Ub = rho²Vc-rhoHc+2SXc+2CUc-2Ub. expected*c negative yes.
