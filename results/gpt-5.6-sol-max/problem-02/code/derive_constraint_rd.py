import sympy as s
A,x,t,theta=s.symbols('A x t theta', real=True)
# dimensionless R = r/c = 1/2 sin t/sin(x+t)
# constraint sin theta sin t sin(A+2x+t)=2 sinA sin(x+t) sin(theta-x-t)
# substitute R via cot t. Let rho=2r/c. cot t = (1/rho - cos x)/sin x.
rho=s.symbols('rho', nonzero=True)
q=(1/rho-s.cos(x))/s.sin(x)
# divide equation sin²t, represent sin(P+t)/sin t = sinP q+cosP; sin(theta-x-t)/sin t=sin(theta-x)*q-cos(theta-x); sin(x+t)/sin t=sinx*q+cosx=1/rho
E=s.expand_trig(s.sin(theta)*(s.sin(A+2*x)*q+s.cos(A+2*x))-2*s.sin(A)*(1/rho)*(s.sin(theta-x)*q-s.cos(theta-x)))
print(s.trigsimp(s.factor(E*rho**2*s.sin(x)**2),method='fu'))
print('expanded trig simplify:',s.simplify(s.expand_trig(E*rho**2*s.sin(x)**2)))
# use theta relation sides maybe theta=B and c? law sines. Need constraint for d/b based B, and r/c based gamma.
