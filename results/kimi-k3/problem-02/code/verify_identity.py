import sympy as sp

# Symbols
A, phi, b, c, p, q = sp.symbols('A phi b c p q', positive=True)

sA, cA = sp.sin(A), sp.cos(A)
sP, cP = sp.sin(phi), sp.cos(phi)
S1 = sp.sin(A+phi)          # sin(A+phi)
S2 = sp.sin(A+2*phi)        # sin(A+2phi)

# Constraint polynomials
ConsP = 2*S1*p**2 - (2*sA+S2)*c*p + c**2*S1 - b*c*sP
ConsQ = 2*S1*q**2 - (2*sA+S2)*b*q + b**2*S1 - b*c*sP

# Quantities
K2 = c**2 - 2*c*cP*p + p**2     # |K|^2
L2 = b**2 - 2*b*cP*q + q**2     # |L|^2
W = (c*sP - b*S1)*p + b*c*sA    # = S1 * X
Z = (c*S1 - b*sP)*q - b*c*sA    # = S1 * Y
Delta = b*c*sA - (b*p + c*q)*S1 + p*q*S2

# The identity:  Z*ConsP + W*ConsQ - S1*(2*L2*W + 2*K2*Z - (b**2-c**2)*Delta) == 0
E = Z*ConsP + W*ConsQ - S1*(2*L2*W + 2*K2*Z - (b**2-c**2)*Delta)
E = sp.expand(E)
# Expand trig: sin(A+phi), sin(A+2phi) into sin/cos of A, phi
E2 = sp.expand_trig(E)
E2 = sp.expand(E2)
# Simplify using sin^2+cos^2=1
E3 = sp.trigsimp(E2)
print("trigsimp result:", E3)
# Stronger check: reduce powers of cos/sin
E4 = sp.simplify(E2)
print("simplify result:", E4)
