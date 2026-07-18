import sympy as sp

A, phi, b, c, p, q = sp.symbols('A phi b c p q', positive=True)
sA, cA = sp.sin(A), sp.cos(A)
sP, cP = sp.sin(phi), sp.cos(phi)
S1 = sp.sin(A+phi)
S2 = sp.sin(A+2*phi)

ConsP = 2*S1*p**2 - (2*sA+S2)*c*p + c**2*S1 - b*c*sP
ConsQ = 2*S1*q**2 - (2*sA+S2)*b*q + b**2*S1 - b*c*sP

K2 = c**2 - 2*c*cP*p + p**2
L2 = b**2 - 2*b*cP*q + q**2
Delta = b*c*sA - (b*p + c*q)*S1 + p*q*S2

# pow(B) = c^2 + c*(L2*p*sP - K2*(b*sA - q*S1))/Delta
# Claim: 2*S1*Delta*(powB - (c^2*S1-b*c*sP)/(2*S1)) == c*(S1*q - b*sA)*ConsP + c*sP*p*ConsQ
IBpoly = Delta*(c**2*S1 + b*c*sP) + 2*S1*c*(L2*p*sP - K2*(b*sA - q*S1))
presB = c*(S1*q - b*sA)*ConsP + c*sP*p*ConsQ
diffB = sp.expand_trig(sp.expand(IBpoly - presB))
print("IB-poly - presentation =", sp.trigsimp(diffB))

# pow(C) = b^2 + b*(L2*(p*S1 - c*sA) + K2*q*sP)/Delta
# Claim: 2*S1*Delta*(powC - (b^2*S1-b*c*sP)/(2*S1)) == b*sP*q*ConsP + b*(S1*p - c*sA)*ConsQ
ICpoly = Delta*(b**2*S1 + b*c*sP) + 2*S1*b*(L2*(p*S1 - c*sA) + K2*q*sP)
presC = b*sP*q*ConsP + b*(S1*p - c*sA)*ConsQ
diffC = sp.expand_trig(sp.expand(ICpoly - presC))
print("IC-poly - presentation =", sp.trigsimp(diffC))

# Verify ConsP derivation: R1: 2*p*sin(phi+g)=c*sin(g); R3(EqC): p*sin(A+g+2phi)=c*sin(A+g+phi)-b*sin(g+phi)
# Eliminate g.
g = sp.symbols('g', real=True)
R1 = 2*p*sp.sin(phi+g) - c*sp.sin(g)
R3 = p*sp.sin(A+g+2*phi) - c*sp.sin(A+g+phi) + b*sp.sin(g+phi)
# expand
R1e = sp.expand_trig(R1)
R3e = sp.expand_trig(R3)
# treat sin(g), cos(g) as vars: solve for tan(g) from each and cross multiply
sg, cg = sp.symbols('sg cg')
R1p = sp.expand(R1e.subs({sp.sin(g):sg, sp.cos(g):cg}))
R3p = sp.expand(R3e.subs({sp.sin(g):sg, sp.cos(g):cg}))
# R1p: coefficient form: alpha*sg + beta*cg = 0
a1 = R1p.coeff(sg); b1 = R1p.coeff(cg)
a3 = R3p.coeff(sg); b3 = R3p.coeff(cg)
# cross: a1*b3 - a3*b1 = 0 gives tan relation; this should equal ConsP (up to factor)
elim = sp.expand(a1*b3 - a3*b1)
elimt = sp.expand_trig(elim)
# compare with ConsP
print("elimination vs ConsP (should be proportional):")
ratio_check = sp.trigsimp(sp.expand(elimt - ConsP))
print("  elim - ConsP =", ratio_check)
# maybe elim = k*ConsP; check elim/ConsP by evaluating both - find constant factor
print("  elim =", sp.trigsimp(elimt))
