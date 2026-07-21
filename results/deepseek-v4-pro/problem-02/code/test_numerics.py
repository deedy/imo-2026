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

def dir_angle(z1, z2, z3):
    # directed angle ∠Z1 Z2 Z3 modulo pi: arg((z1-z2)/(z3-z2))
    return cmath.phase((z1 - z2) / (z3 - z2))

def angle_eq_err_mod_pi(a, b):
    # difference modulo pi
    diff = (a - b) % math.pi
    if diff > math.pi/2:
        diff = math.pi - diff
    return diff

def total_error(pts):
    A=pts['A']; B=pts['B']; C=pts['C']; M=pts['M']; N=pts['N']; K=pts['K']; L=pts['L']
    # condition 1: ∠KBA = ∠ACL
    a1 = dir_angle(K, B, A)  # ∠KBA
    a2 = dir_angle(A, C, L)  # ∠ACL
    e1 = angle_eq_err_mod_pi(a1, a2)
    # condition 2: ∠LBK = ∠LNC
    a3 = dir_angle(L, B, K)  # ∠LBK
    a4 = dir_angle(L, N, C)  # ∠LNC
    e2 = angle_eq_err_mod_pi(a3, a4)
    # condition 3: ∠LCK = ∠BMK
    a5 = dir_angle(L, C, K)  # ∠LCK
    a6 = dir_angle(B, M, K)  # ∠BMK
    e3 = angle_eq_err_mod_pi(a5, a6)
    return e1, e2, e3

# Generate random triangle
random.seed(42)
A = 0+0j
B = 4 + random.random()*2j  # real axis
C = complex(random.uniform(1,3), random.uniform(2,5))
M = (A+B)/2
N = (A+C)/2

print(f"A={A}, B={B}, C={C}")
print(f"M={M}, N={N}")

# Search for K,L satisfying conditions
# We'll use optimization from random starts
best_total = float('inf')
best_pts = None

for trial in range(20000):
    # K inside triangle BMC: B, M, C
    # param: K = (1-u-v)*B + u*M + v*C, u,v >=0, u+v <=1
    u = random.random()
    v = random.random()
    if u + v > 1:
        u, v = 1-u, 1-v
    K = (1-u-v)*B + u*M + v*C
    
    # L inside triangle BNC: B, N, C
    u2 = random.random()
    v2 = random.random()
    if u2 + v2 > 1:
        u2, v2 = 1-u2, 1-v2
    L = (1-u2-v2)*B + u2*N + v2*C
    
    pts = {'A':A,'B':B,'C':C,'M':M,'N':N,'K':K,'L':L}
    e1, e2, e3 = total_error(pts)
    total = e1 + e2 + e3
    if total < best_total:
        best_total = total
        best_pts = pts.copy()
        # print(f"new best {total}: K={K}, L={L}")
    if best_total < 1e-6:
        break

print(f"Best total error: {best_total}")
if best_pts:
    K = best_pts['K']
    L = best_pts['L']
    print(f"K = {K}")
    print(f"L = {L}")
    O = circumcenter(A, K, L)
    print(f"O = {O}")
    print(f"|OM| = {abs(O-M)}")
    print(f"|ON| = {abs(O-N)}")
    print(f"Equal? {abs(abs(O-M)-abs(O-N)) < 1e-6}")
