import cmath, math, random

def solve_full(a):
    """Find K,L satisfying the three angle equations, and check interior conditions."""
    A = a
    M = 0+0j
    N = 1+0j
    B = -a
    C = 2 - a
    
    def angle_eqs(k, l):
        U = k + a
        V = l + a
        # Eq1: Im( a(a-1) / (U*(V-2)) ) = 0
        r1 = (a * (a-1)) / (U * (V - 2))
        e1 = r1.imag
        # Eq2: Im( U*(l-1) / (V*(1-a)) ) = 0
        r2 = (U * (l - 1)) / (V * (1 - a))
        e2 = r2.imag
        # Eq3: Im( a*(U-2) / (k*V) ) = 0  (since k+a-2 = U-2, l+a-2 = V-2? Wait no)
        # Actually eq3: a*(k+a-2) / (k*(l+a-2)) real. 
        # k+a-2 = U-2, l+a-2 = V-2.
        # So a*(U-2) / (k*(V-2)) real.
        r3 = a * (U - 2) / (k * (V - 2))
        e3 = r3.imag
        return e1, e2, e3
    
    def total_err(k, l):
        e1, e2, e3 = angle_eqs(k, l)
        return e1**2 + e2**2 + e3**2
    
    def inside_triangle(P, A, B, C):
        """Check if P is strictly inside triangle ABC using barycentric."""
        v0 = C - A
        v1 = B - A
        v2 = P - A
        d00 = v0.real**2 + v0.imag**2
        d01 = v0.real*v1.real + v0.imag*v1.imag
        d11 = v1.real**2 + v1.imag**2
        d20 = v2.real*v0.real + v2.imag*v0.imag
        d21 = v2.real*v1.real + v2.imag*v1.imag
        denom = d00*d11 - d01*d01
        if abs(denom) < 1e-12:
            return False
        s = (d11*d20 - d01*d21) / denom
        t = (d00*d21 - d01*d20) / denom
        return s > 1e-9 and t > 1e-9 and s + t < 1 - 1e-9
    
    def inside_angle(P, Q, R, S):
        """P inside angle RQS: P-Q = λ(R-Q) + μ(S-Q) with λ,μ > 0."""
        vR = R - Q
        vS = S - Q
        vP = P - Q
        det = vR.real * vS.imag - vR.imag * vS.real
        if abs(det) < 1e-12:
            return False
        lam = (vP.real * vS.imag - vP.imag * vS.real) / det
        mu = (vR.real * vP.imag - vR.imag * vP.real) / det
        return lam > 1e-9 and mu > 1e-9
    
    # Search
    best = float('inf')
    best_kl = None
    for _ in range(5000):
        r = random.random()*0.8
        s = random.random()*0.8
        if r + s > 0.9:
            r, s = r*0.7, s*0.7
        K_cand = (1-r-s)*B + r*M + s*C
        
        r2 = random.random()*0.8
        s2 = random.random()*0.8
        if r2 + s2 > 0.9:
            r2, s2 = r2*0.7, s2*0.7
        L_cand = (1-r2-s2)*B + r2*N + s2*C
        
        err = total_err(K_cand, L_cand)
        if err < best:
            # Check interior conditions
            ok = inside_triangle(K_cand, B, M, C) and inside_triangle(L_cand, B, N, C) and \
                 inside_angle(K_cand, B, L_cand, A) and inside_angle(L_cand, C, A, K_cand)
            if ok:
                best = err
                best_kl = (K_cand, L_cand)
    
    if best_kl is None:
        print("No valid initial found!")
        return None
    
    K, L = best_kl
    # Gradient descent refinement
    vars = [K.real, K.imag, L.real, L.imag]
    for step in range(50000):
        err = total_err(K, L)
        if err < 1e-18:
            break
        grad = [0.0]*4
        h = 1e-8
        for i in range(4):
            vp = vars[:]
            vp[i] += h
            kp = vp[0] + 1j*vp[1]
            lp = vp[2] + 1j*vp[3]
            grad[i] = (total_err(kp, lp) - err) / h
        for i in range(4):
            vars[i] -= 0.02 * grad[i]
        K = vars[0] + 1j*vars[1]
        L = vars[2] + 1j*vars[3]
        # Check if still inside
        if not (inside_triangle(K, B, M, C) and inside_triangle(L, B, N, C) and \
                inside_angle(K, B, L, A) and inside_angle(L, C, A, K)):
            # Step back and reduce step size
            vars = [K_old.real, K_old.imag, L_old.real, L_old.imag] if 'K_old' in dir() else vars
            break
        K_old, L_old = K, L
    
    return K, L, total_err(K, L)

# Test
a = complex(0.3400, 2.0861)
result = solve_full(a)
if result:
    K, L, err = result
    print(f"A = {a}")
    print(f"K = {K}")
    print(f"L = {L}")
    print(f"Error: {err:.2e}")
    
    # Compute O and check OM, ON
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
    
    O = circumcenter(a, K, L)
    print(f"O = {O}")
    print(f"Re(O) = {O.real:.10f}")
    print(f"OM = {abs(O):.10f}")
    print(f"ON = {abs(O-1):.10f}")
    print(f"Diff = {abs(O)-abs(O-1):.10e}")
    
    # G_num
    x1, y1 = K.real, K.imag
    x2, y2 = L.real, L.imag
    G_num = x1**2*y2 - x1*y2 - x2**2*y1 + x2*y1 + y1**2*y2 - y1*y2**2
    print(f"G_num = {G_num:.10e}")
