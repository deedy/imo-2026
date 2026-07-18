import numpy as np

# Verify the algebraic identity (star) numerically, and find X,Y linear in p,q
# such that star = X*ConsP + Y*ConsQ.

def compute_coeffs(A, phi, b, c):
    sA, cA = np.sin(A), np.cos(A)
    sP, cP = np.sin(phi), np.cos(phi)
    s1 = np.sin(A+phi)   # sin(A+phi)
    s2 = np.sin(A+2*phi) # sin(A+2phi)
    # ConsP: 2*s1*p^2 - (2*sA+s2)*c*p + (c^2*s1 - b*c*sP) = 0
    P2 = 2*s1; P1 = -(2*sA+s2)*c; P0 = c*c*s1 - b*c*sP
    # ConsQ: 2*s1*q^2 - (2*sA+s2)*b*q + (b^2*s1 - b*c*sP) = 0
    Q2 = 2*s1; Q1 = -(2*sA+s2)*b; Q0 = b*b*s1 - b*c*sP
    # star polynomial in p,q: 2[|L|^2 W + |K|^2 Z] - (c^2-b^2)*Delta
    # |L|^2 = b^2 - 2 b cP q + q^2 ; |K|^2 = c^2 - 2 c cP p + p^2
    # W = p c sP - b p s1 + b c sA = p(c*sP - b*s1) + b*c*sA
    # Z = q(c*s1 - b*sP) - b*c*sA
    # Delta = b c sA - (b p + c q) s1 + p q s2
    # Build as dict of monomial -> coeff. Monomials: (i,j) meaning p^i q^j.
    def add(poly, mon, coef):
        poly[mon] = poly.get(mon, 0.0) + coef
    # |L|^2 as poly in q: l2q2=1, l2q1=-2*b*cP, l2q0=b*b
    # |K|^2 as poly in p: k2p2=1, k2p1=-2*c*cP, k2p0=c*c
    l2 = {(0,2):1.0, (0,1):-2*b*cP, (0,0):b*b}
    k2 = {(2,0):1.0, (1,0):-2*c*cP, (0,0):c*c}
    W = {(1,0):(c*sP - b*s1), (0,0):b*c*sA}
    Z = {(0,1):(c*s1 - b*sP), (0,0):-b*c*sA}
    def mul(p1, p2):
        r = {}
        for (i1,j1),v1 in p1.items():
            for (i2,j2),v2 in p2.items():
                add(r, (i1+i2, j1+j2), v1*v2)
        return r
    def scale(p, s):
        return {k:v*s for k,v in p.items()}
    def addp(p1, p2):
        r = dict(p1)
        for k,v in p2.items(): add(r, k, v)
        return r
    L2W = mul(l2, W)
    K2Z = mul(k2, Z)
    LHS = scale(addp(L2W, K2Z), 2.0)
    Delta = {(0,0):b*c*sA, (1,0):-b*s1, (0,1):-c*s1, (1,1):s2}
    RHS = scale(Delta, b*b-c*c)
    star = addp(LHS, scale(RHS, -1.0))  # star = LHS - RHS; want =0
    return star, (P2,P1,P0), (Q2,Q1,Q0)

def solve_and_check(A, phi, b, c, label=""):
    star, (P2,P1,P0), (Q2,Q1,Q0) = compute_coeffs(A, phi, b, c)
    print(f"--- {label}: A={A:.3f} phi={phi:.3f} b={b:.3f} c={c:.3f}")
    print("   star coeffs:", {k: round(v,6) for k,v in sorted(star.items())})
    print("   ConsP:", round(P2,6), round(P1,6), round(P0,6))
    print("   ConsQ:", round(Q2,6), round(Q1,6), round(Q0,6))
    # Guess X = x2*q + x3, Y = y1*p + y3
    x2 = star[(2,1)]/P2       # coeff of p^2 q
    y1 = star[(1,2)]/Q2       # coeff of p q^2
    x3 = star[(2,0)]/P2       # coeff of p^2
    y3 = star[(0,2)]/Q2       # coeff of q^2
    print(f"   x2={x2:.6f} x3={x3:.6f} y1={y1:.6f} y3={y3:.6f}")
    # check remaining monomials: (1,1),(1,0),(0,1),(0,0)
    rem = {}
    rem[(1,1)] = star.get((1,1),0) - (x2*P1 + y1*Q1)
    rem[(1,0)] = star.get((1,0),0) - (x3*P1 + y1*Q0)
    rem[(0,1)] = star.get((0,1),0) - (x2*P0 + y3*Q1)
    rem[(0,0)] = star.get((0,0),0) - (x3*P0 + y3*Q0)
    print("   residuals (should be ~0):", {k: round(v,9) for k,v in rem.items()})
    # print candidate forms for x2,x3,y1,y3 in terms of trig constants
    sA, cA = np.sin(A), np.cos(A)
    sP, cP = np.sin(phi), np.cos(phi)
    s1 = np.sin(A+phi); s2 = np.sin(A+2*phi)
    print(f"   trig: sA={sA:.4f} cA={cA:.4f} sP={sP:.4f} cP={cP:.4f} s1={s1:.4f} s2={s2:.4f}")
    print(f"   x2/(?) guess: x2={x2:.6f}; 2cP={2*cP:.6f}; 2*s2/s1={2*s2/s1:.6f}; -2cP={-2*cP:.6f}")
    print(f"   x3={x3:.6f}; candidates: 2cos(A)? 2*cA={2*cA:.6f}; (c^2? ) c={c:.4f}")
    print(f"   y1={y1:.6f}; y3={y3:.6f}")
    # also print residual of evaluating star at the true p,q (from ConsP,ConsQ roots)
    # pick roots consistent with geometry: solve quadratics
    rp = np.roots([P2,P1,P0]); rq = np.roots([Q2,Q1,Q0])
    print("   roots p:", rp, " roots q:", rq)
    for p in rp:
        for q in rq:
            if p>0 and q>0:
                val = sum(v*(p**i)*(q**j) for (i,j),v in star.items())
                print(f"     star at p={p:.5f},q={q:.5f}: {val:.2e}")

if __name__ == "__main__":
    solve_and_check(np.radians(70), np.radians(12), 0.9216, 0.8152, "case1")
    solve_and_check(np.radians(60), np.radians(12), 1.0851, 0.8846, "case2")
    solve_and_check(np.radians(65), np.radians(15), 1.1, 0.8, "case3")
    solve_and_check(np.radians(80), np.radians(10), 0.9, 1.2, "case4")
