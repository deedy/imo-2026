import numpy as np
from explore import run, ang, dirv, intersect, circumcircle, power, cross2

def second_intersect(P, d, O, R):
    dd = np.dot(d,d)
    bcoef = 2*np.dot(d, P-O)
    ccoef = np.dot(P-O,P-O) - R*R
    disc = bcoef*bcoef - 4*dd*ccoef
    if disc < -1e-12: return None
    sq = np.sqrt(max(disc,0))
    return ((-bcoef - sq)/(2*dd), (-bcoef + sq)/(2*dd))

def on_circle(P, O, R): return abs(np.linalg.norm(P-O)-R) < 1e-8

def explore(Adeg, Bdeg, phi_deg):
    res = run(Adeg, Bdeg, phi_deg, verbose=False)
    r = res[0]
    Ap,Bp,Cp,M,N,K,L,O,R = r['A'],r['B'],r['C'],r['M'],r['N'],r['K'],r['L'],r['O'],r['R']
    beta,gamma,phi = r['beta'],r['gamma'],r['phi']
    c = np.linalg.norm(Bp-Ap); bb = np.linalg.norm(Cp-Ap); a = np.linalg.norm(Cp-Bp)
    print(f"=== A={Adeg},B={Bdeg},C={180-Adeg-Bdeg}, phi={phi_deg}")
    # reflected points
    K2 = Ap+Bp-K; L2 = Ap+Cp-L
    # circles AKL and AK''L''
    O2, R2 = circumcircle(Ap, K2, L2)
    print(f"  R(AKL)={R:.6f}  R(AK''L'')={R2:.6f}  equal? {abs(R-R2)<1e-9}")
    print(f"  O={O}, O''={O2}")
    print(f"  O''-O={O2-O},  B-A={Bp-Ap}, C-A={Cp-Ap}, (B+C)/2-A={(Bp+Cp)/2-Ap}")
    # KL parallel K''L''?
    d1 = (L-K)/np.linalg.norm(L-K); d2=(L2-K2)/np.linalg.norm(L2-K2)
    print(f"  KL || K''L''? {abs(cross2(d1,d2))<1e-8}")
    # second intersections
    dBK=(K-Bp)/np.linalg.norm(K-Bp); tX = second_intersect(Bp, dBK, O, R)
    X = Bp + tX[1]*dBK if abs(tX[0]-np.linalg.norm(K-Bp))<1e-6 else Bp+tX[0]*dBK
    print(f"  BX={np.linalg.norm(X-Bp):.6f}, X={X}")
    dCL=(L-Cp)/np.linalg.norm(L-Cp); tY = second_intersect(Cp, dCL, O, R)
    Y = Cp + tY[1]*dCL if abs(tY[0]-np.linalg.norm(L-Cp))<1e-6 else Cp+tY[0]*dCL
    print(f"  CY={np.linalg.norm(Y-Cp):.6f}, Y={Y}")
    # is X on line AC? line MN? 
    dAC=(Cp-Ap)/np.linalg.norm(Cp-Ap)
    print(f"  dist(X, line AC)={abs(cross2(X-Ap,dAC)):.2e}; dist(X,line MN):", end=" ")
    dMN=(N-M)/np.linalg.norm(N-M)
    print(f"{abs(cross2(X-M,dMN)):.2e}; dist(X, line CL)={abs(cross2(X-Cp,dCL)):.2e}")
    print(f"  dist(Y, line AB)={abs(cross2(Y-Ap,(Bp-Ap)/c)):.2e}; dist(Y, line MN)={abs(cross2(Y-M,dMN)):.2e}; dist(Y,line BK)={abs(cross2(Y-Bp,dBK)):.2e}")
    # maybe X = reflection of something; test distances
    print(f"  X to A: {np.linalg.norm(X-Ap):.6f}, X to M: {np.linalg.norm(X-M):.6f}, X to N: {np.linalg.norm(X-N):.6f}")
    print(f"  Y to A: {np.linalg.norm(Y-Ap):.6f}, Y to M: {np.linalg.norm(Y-M):.6f}, Y to N: {np.linalg.norm(Y-N):.6f}")
    # cyclic tests
    def cyclic4(P,Q,Rr,S):
        try:
            Oc,Rc = circumcircle(P,Q,Rr)
            return on_circle(S,Oc,Rc)
        except: return False
    print(f"  BKLN cyclic? {cyclic4(Bp,K,L,N)};  CKLM cyclic? {cyclic4(Cp,K,L,M)}")
    print(f"  BKLM cyclic? {cyclic4(Bp,K,L,M)};  CKNL cyclic? {cyclic4(Cp,K,N,L)}")
    print(f"  K L K'' L'' cyclic? {cyclic4(K,L,K2,L2)}")
    # angles
    print(f"  angle BAK={ang(Bp,Ap,K):.4f} angle CAL={ang(Cp,Ap,L):.4f}")
    print(f"  angle AK''L''={ang(K2,Ap,L2):.4f}, A+2phi={Adeg+2*phi_deg}")
    print(f"  angle AKL={ang(Ap,K,L):.4f}, angle ABK? {ang(Ap,Bp,K):.4f}")
    # test: does circle pass through reflection of A in O_line? centroid? orthocenter?
    # orthocenter
    H = Ap+Bp+Cp - 2*np.array([a/2,0])  # rough; skip
    # Test: pow(B) vs BK*BX formula
    print(f"  pow(B)={power(Bp,O,R):.6f} BK*BX={np.linalg.norm(K-Bp)*np.linalg.norm(X-Bp):.6f}")
    print(f"  pow(C)={power(Cp,O,R):.6f} CL*CY={np.linalg.norm(L-Cp)*np.linalg.norm(Y-Cp):.6f}")
    # Interesting: is BX related to b=CA?  or CY related to c?
    print(f"  b={bb:.6f} c={c:.6f} BX={np.linalg.norm(X-Bp):.6f} CY={np.linalg.norm(Y-Cp):.6f}")
    print(f"  BX-b*cos(phi)={np.linalg.norm(X-Bp)-bb*np.cos(phi):.6f}, CY-c*cos(phi)={np.linalg.norm(Y-Cp)-c*np.cos(phi):.6f}")
    print()

if __name__ == "__main__":
    explore(70,60,12)
    explore(60,70,12)
    explore(80,50,12)
