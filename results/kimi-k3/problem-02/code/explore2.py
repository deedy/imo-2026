import numpy as np
from explore import run, ang, dirv, intersect, circumcircle, power, cross2

def second_intersect(P, d, O, R):
    dd = np.dot(d,d)
    bcoef = 2*np.dot(d, P-O)
    ccoef = np.dot(P-O,P-O) - R*R
    disc = bcoef*bcoef - 4*dd*ccoef
    if disc < -1e-12:
        return None
    sq = np.sqrt(max(disc,0))
    t1 = (-bcoef - sq)/(2*dd); t2 = (-bcoef + sq)/(2*dd)
    return t1, t2

def dist_to_line(P, X, d):
    # distance from P to line through X with direction d
    return abs(cross2(P-X, d))/np.linalg.norm(d)

def explore(Adeg, Bdeg, phi_deg):
    res = run(Adeg, Bdeg, phi_deg, verbose=False)
    r = res[0]
    Ap,Bp,Cp,M,N,K,L,O,R = r['A'],r['B'],r['C'],r['M'],r['N'],r['K'],r['L'],r['O'],r['R']
    beta,gamma,phi = r['beta'],r['gamma'],r['phi']
    print(f"=== A={Adeg},B={Bdeg},C={180-Adeg-Bdeg}, phi={phi_deg}, beta={np.degrees(beta):.4f}, gamma={np.degrees(gamma):.4f}")
    # basic angles of triangle AKL
    print("  angle KAL =", ang(K,Ap,L), " A =", Adeg)
    print("  angle AKL =", ang(Ap,K,L), " angle ALK =", ang(Ap,L,K))
    print("  angle KAB =", ang(K,Ap,Bp), " angle LAC =", ang(L,Ap,Cp))
    print("  angle BAK =", ang(Bp,Ap,K), " angle CAK =", ang(Cp,Ap,K))
    print("  angle BAL =", ang(Bp,Ap,L), " angle CAL =", ang(Cp,Ap,L))
    # second intersections of circle with lines AB, AC, BC
    dAB = (Bp-Ap)/np.linalg.norm(Bp-Ap)
    dAC = (Cp-Ap)/np.linalg.norm(Cp-Ap)
    dBC = (Cp-Bp)/np.linalg.norm(Cp-Bp)
    tAB = second_intersect(Ap, dAB, O, R)
    tAC = second_intersect(Ap, dAC, O, R)
    tBC = second_intersect(Bp, dBC, O, R)
    c = np.linalg.norm(Bp-Ap); bb = np.linalg.norm(Cp-Ap); a = np.linalg.norm(Cp-Bp)
    print(f"  a={a:.6f} b={bb:.6f} c={c:.6f}")
    if tAB:
        pts = [Ap+t*dAB for t in tAB]
        print("  circle x line AB at distances from A along AB:", tAB, " (c/2 =", c/2, ", c =", c, ")")
    if tAC:
        print("  circle x line AC at distances from A along AC:", tAC, " (b/2 =", bb/2, ", b =", bb, ")")
    if tBC:
        pts = [Bp+t*dBC for t in tBC]
        print("  circle x line BC at distances from B along BC:", tBC, " (a/2 =", a/2, ", a =", a, ")")
    # reflected points K'', L''
    K2 = Ap+Bp-K; L2 = Ap+Cp-L
    for name, P in [("K''",K2),("L''",L2),("D mid BC",(Bp+Cp)/2),("centroid",(Ap+Bp+Cp)/3)]:
        print(f"   is {name} on circle? {abs(np.linalg.norm(P-O)-R)<1e-9}")
    # is MNKL cyclic?
    try:
        O2, R2 = circumcircle(M, N, K)
        print("   MNKL cyclic?", abs(np.linalg.norm(L-O2)-R2)<1e-9)
    except Exception as e:
        print("   MNKL err", e)
    # line KL meets BC?
    dKL = (L-K)/np.linalg.norm(L-K)
    # intersect with BC (y=0)
    if abs(dKL[1])>1e-12:
        t = -K[1]/dKL[1]
        X = K + t*dKL
        print("   KL meets BC at x =", X[0], " (B=0, C=1);  BK?  midpoint?")
    # check if O lies on perpendicular bisector of MN (the claim) and what line that is
    midMN = (M+N)/2
    dMN = (N-M)/np.linalg.norm(N-M)
    print("   O . perp-bisector-of-MN check:", abs(cross2(O-midMN, dMN))<1e-9)
    # angle of KL with BC
    print("   angle KLB? angle(KL,BC):", np.degrees(np.arctan2(dKL[1], dKL[0])))
    # distances
    print("   BK =", np.linalg.norm(K-Bp), " CL =", np.linalg.norm(L-Cp), " MK =", np.linalg.norm(M-K), " NL =", np.linalg.norm(N-L))
    print("   AK =", np.linalg.norm(Ap-K), " AL =", np.linalg.norm(Ap-L), " KL =", np.linalg.norm(K-L))
    # test: BK*CL ? AK*AL?
    BK=np.linalg.norm(K-Bp); CL=np.linalg.norm(L-Cp); MK=np.linalg.norm(M-K); NL=np.linalg.norm(N-L)
    AK=np.linalg.norm(Ap-K); AL=np.linalg.norm(Ap-L); KL=np.linalg.norm(K-L)
    print("   BK/c? CL/b?", BK/c, CL/bb, " MK/(c/2)?", MK/(c/2), " NL/(b/2)?", NL/(bb/2))
    # maybe AK*AL = AM*? 
    print("   AK*AL =", AK*AL, " AM*AN =", (c/2)*(bb/2), " AK^2+AL^2?", AK*AK+AL*AL)
    # power of M,N
    print("   pow(M) =", power(M,O,R), " pow(N) =", power(N,O,R), " MK*? ")
    # second intersection of line MK with circle
    dMK = (K-M)/np.linalg.norm(K-M)
    tMK = second_intersect(M, dMK, O, R)
    if tMK: print("   line MK x circle t's:", tMK, " (MK =", np.linalg.norm(K-M), ")")
    dNL = (L-N)/np.linalg.norm(L-N)
    tNL = second_intersect(N, dNL, O, R)
    if tNL: print("   line NL x circle t's:", tNL, " (NL =", np.linalg.norm(L-N), ")")
    print()

if __name__ == "__main__":
    explore(70,60,12)
    explore(60,70,12)
    explore(75,65,10)
