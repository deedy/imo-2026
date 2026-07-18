"""Verification for imo-2026-04.

1) Geometric sanity check of the cut parametrization (floats).
2) Exact simulation of Mulan's strategy for theta = 180/n against random Shan-Yu.
3) Exact check of Shan-Yu's invariant closure when 180 is NOT an integer multiple of theta.
"""
import math, random
from fractions import Fraction as F

random.seed(12345)

# ---------- 1) geometric check of parametrization ----------
def geo_check(trials=2000):
    for _ in range(trials):
        # random triangle angles
        A = random.uniform(5, 170)
        B = random.uniform(1, 179 - A - 1)
        C = 180 - A - B
        # place: vertex A at origin? easier: vertices: B0=(0,0), C0=(1,0), A0 determined by angles B (at B0), C (at C0)
        b = math.radians(B); c = math.radians(C)
        # A0 = intersection of ray from B0 at angle b and from C0 at angle pi-c
        # line1: t*(cos b, sin b); line2: (1,0)+s*(cos(pi-c), sin(pi-c)) = (1 - s cos c, s sin c)
        # t sin b = s sin c ; t cos b = 1 - s cos c
        s = math.sin(b) / math.sin(b + c)
        A0 = (1 - s*math.cos(c), s*math.sin(c))
        B0 = (0.0, 0.0); C0 = (1.0, 0.0)
        # P on BC
        t = random.uniform(0.05, 0.95)
        P = (t, 0.0)
        def ang(U, V, W):  # angle at V in triangle UVW
            ux, uy = U[0]-V[0], U[1]-V[1]
            wx, wy = W[0]-V[0], W[1]-V[1]
            cosv = (ux*wx+uy*wy)/math.hypot(ux,uy)/math.hypot(wx,wy)
            return math.degrees(math.acos(max(-1,min(1,cosv))))
        alpha = ang(B0, A0, P)   # angle BAP
        # predicted children
        T1p = sorted([B, alpha, 180-B-alpha])
        T2p = sorted([C, A-alpha, B+alpha])
        T1 = sorted([ang(A0,B0,P), ang(B0,A0,P), ang(A0,P,B0)])
        T2 = sorted([ang(A0,C0,P), ang(C0,A0,P), ang(A0,P,C0)])
        for x, y in zip(T1p+T2p, T1+T2):
            assert abs(x-y) < 1e-6, (x, y)
    print("geometry parametrization check OK")

# ---------- 2) Mulan strategy for theta = 180/n, exact ----------
def multiples(theta):
    m = []
    k = 1
    while k*theta < 180:
        m.append(k*theta)
        k += 1
    return set(m)

def mulan_game(n, A, B, C, verbose=False):
    theta = F(180, n)
    M = multiples(theta)
    tri = [A, B, C]
    cuts = 0
    while True:
        assert sum(tri) == 180 and all(x > 0 for x in tri)
        if theta in tri:
            return cuts  # Mulan wins
        assert cuts <= n, "too many cuts!"
        # strategy
        mult_angles = [x for x in tri if x in M]
        if mult_angles:
            # chain lemma: cut at a vertex whose angle is k*theta, alpha = theta
            a = mult_angles[0]
            rest = list(tri); rest.remove(a)
            b, c = rest
            alpha = theta
            T1 = [b, alpha, 180-b-alpha]
            T2 = [c, a-alpha, b+alpha]
        else:
            # cut at largest angle A0; choose k*theta in (C0, 180-B0)
            tri_sorted = sorted(tri)
            a = tri_sorted[2]; b, c = tri_sorted[0], tri_sorted[1]
            # find k
            k = None
            j = 1
            while j*theta < 180:
                if c < j*theta < 180 - b:
                    k = j; break
                j += 1
            assert k is not None, (n, tri)
            alpha = 180 - b - k*theta
            assert 0 < alpha < a
            T1 = [b, alpha, k*theta]
            T2 = [c, a-alpha, b+alpha]
            assert (a-alpha) == k*theta - c and (b+alpha) == (n-k)*theta
            assert any(x in M for x in T1) and any(x in M for x in T2)
        # Shan-Yu random choice
        tri = random.choice([T1, T2])
        cuts += 1

def test_mulan():
    for n in range(2, 9):
        for trial in range(400):
            # random rational triangle, sometimes with multiples planted
            theta = F(180, n)
            if trial % 3 == 0:
                k = random.randint(1, n-1)
                A = k*theta
                B = F(random.randint(1, int((180-A)*7)-1), 7)
                C = 180 - A - B
                if C <= 0: continue
            else:
                A = F(random.randint(1, 178*11), 11)
                B = F(random.randint(1, int((180-A)*11)-1), 11)
                C = 180 - A - B
                if B <= 0 or C <= 0: continue
            cuts = mulan_game(n, A, B, C)
            assert cuts <= n - 1, (n, A, B, C, cuts)
    print("Mulan strategy check OK (wins within n-1 cuts for n=2..8)")

# ---------- 3) Shan-Yu invariant closure, exact ----------
def test_shanyu():
    for theta in [F(72), F(50), F(100), F(170), F(7), F(180,7)*F(3,2), F(61)]:
        # require 180 not an integer multiple of theta
        assert (F(180)/theta).denominator != 1
        M = multiples(theta)
        for trial in range(3000):
            # random safe triangle
            while True:
                A = F(random.randint(1, 178*13), 13)
                B = F(random.randint(1, max(1,int((180-A)*13)-1)), 13)
                C = 180 - A - B
                if B > 0 and C > 0 and all(x not in M for x in (A,B,C)):
                    break
            # Mulan tries every vertex and adversarial alphas
            for i in range(3):
                a = [A,B,C][i]
                b, c = [x for j,x in enumerate([A,B,C]) if j != i]
                cand = set()
                for m in M:
                    for al in (m, 180-b-m, a-m, m-b):
                        if 0 < al < a:
                            cand.add(al)
                for _ in range(5):
                    al = a * F(random.randint(1, 999), 1000)
                    cand.add(al)
                for al in cand:
                    T1 = [b, al, 180-b-al]
                    T2 = [c, a-al, b+al]
                    safe1 = all(x not in M for x in T1)
                    safe2 = all(x not in M for x in T2)
                    assert safe1 or safe2, (theta, A, B, C, i, al, T1, T2)
    print("Shan-Yu invariant closure check OK for several non-divisor thetas")

geo_check()
test_mulan()
test_shanyu()
print("ALL CHECKS PASSED")
