import cmath, math, random

def circumcenter(z1, z2, z3):
    a, b, c = z1, z2, z3
    d = 2 * ((a.real - b.real) * (a.imag - c.imag) - (a.real - c.real) * (a.imag - b.imag))
    if abs(d) < 1e-12:
        return None
    ux = ((a.real**2 + a.imag**2 - b.real**2 - b.imag**2) * (a.imag - c.imag) - 
          (a.real**2 + a.imag**2 - c.real**2 - c.imag**2) * (a.imag - b.imag)) / d
    uy = ((a.real - b.real) * (a.real**2 + a.imag**2 - c.real**2 - c.imag**2) - 
          (a.real - c.real) * (a.real**2 + a.imag**2 - b.real**2 - b.imag**2)) / d
    return complex(ux, uy)

# Use scipy? Not available. Let's implement simple gradient descent for solving the equations.

# We'll set up variables: K = (x1, y1), L = (x2, y2)
# The three angle equalities each are of the form Im(expression) = 0.
# We can minimize sum of squares of Im(expression) / |expression| (to normalize).

def angle_condition_im(z1, z2, z3, w1, w2, w3):
    # condition: ∠Z1 Z2 Z3 = ∠W1 W2 W3 mod pi
    # Equivalent: arg((z1-z2)/(z3-z2)) = arg((w1-w2)/(w3-w2)) mod pi
    # => ((z1-z2)/(z3-z2)) / ((w1-w2)/(w3-w2)) is real
    num = (z1 - z2) / (z3 - z2)
    den = (w1 - w2) / (w3 - w2)
    ratio = num / den
    # Return imaginary part
    return ratio.imag / abs(ratio) if abs(ratio) > 1e-12 else 0.0

def equations(vars, A, B, C, M, N):
    x1, y1, x2, y2 = vars
    K = complex(x1, y1)
    L = complex(x2, y2)
    
    # Eq1: ∠KBA = ∠ACL
    e1 = angle_condition_im(K, B, A, A, C, L)
    # Eq2: ∠LBK = ∠LNC
    e2 = angle_condition_im(L, B, K, L, N, C)
    # Eq3: ∠LCK = ∠BMK
    e3 = angle_condition_im(L, C, K, B, M, K)
    
    return [e1, e2, e3]

def check_inside(K, B, L, A):
    """K inside angle LBA: K is in convex cone of rays BA and BL from B"""
    vA = A - B
    vL = L - B
    vK = K - B
    # Solve vK = lam * vA + mu * vL
    det = vA.real * vL.imag - vA.imag * vL.real
    if abs(det) < 1e-12:
        return False
    lam = (vK.real * vL.imag - vK.imag * vL.real) / det
    mu = (vA.real * vK.imag - vA.imag * vK.real) / det
    return lam > -1e-9 and mu > -1e-9

def check_inside2(L, C, A, K):
    """L inside angle ACK: L is in convex cone of CA and CK from C"""
    vA = A - C
    vK = K - C
    vL = L - C
    det = vA.real * vK.imag - vA.imag * vK.real
    if abs(det) < 1e-12:
        return False
    lam = (vL.real * vK.imag - vL.imag * vK.real) / det
    mu = (vA.real * vL.imag - vA.imag * vL.real) / det
    return lam > -1e-9 and mu > -1e-9

def total_error(vars, A, B, C, M, N):
    e = equations(vars, A, B, C, M, N)
    return sum(x*x for x in e)

# Fixed triangle
A = 0+0j
B = 2+0j
C = complex(1.0, 2.0)
M = (A+B)/2  # 1+0j
N = (A+C)/2  # 0.5+1j

# Use random search + local optimization via gradient descent
best_err = float('inf')
best_vars = None

for trial in range(50000):
    # Random K inside BMC, L inside BNC
    # K inside triangle with vertices B, M, C
    u1 = random.random()
    v1 = random.random()
    if u1 + v1 > 1:
        u1, v1 = 1-u1, 1-v1
    K = (1-u1-v1)*B + u1*M + v1*C
    
    u2 = random.random()
    v2 = random.random()
    if u2 + v2 > 1:
        u2, v2 = 1-u2, 1-v2
    L = (1-u2-v2)*B + u2*N + v2*C
    
    vars = [K.real, K.imag, L.real, L.imag]
    err = total_error(vars, A, B, C, M, N)
    if err < best_err:
        # Check inside conditions
        if check_inside(K, B, L, A) and check_inside2(L, C, A, K):
            best_err = err
            best_vars = vars
            if err < 1e-12:
                break

print(f"Best error: {best_err}")

if best_vars and best_err < 1e-6:
    x1, y1, x2, y2 = best_vars
    K = complex(x1, y1)
    L = complex(x2, y2)
    O = circumcenter(A, K, L)
    print(f"K = {K}")
    print(f"L = {L}")
    print(f"O = {O}")
    print(f"|OM| = {abs(O-M):.10f}")
    print(f"|ON| = {abs(O-N):.10f}")
    print(f"diff = {abs(O-M) - abs(O-N):.10e}")
