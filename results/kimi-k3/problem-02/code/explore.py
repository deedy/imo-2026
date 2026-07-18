import numpy as np

def dirv(t): return np.array([np.cos(t), np.sin(t)])

def intersect(P, d, Q, e):
    M = np.column_stack([d, -e])
    t, s = np.linalg.solve(M, Q - P)
    return P + t*d, t, s

def ang(X, P, Y):
    u = X-P; v = Y-P
    c = np.dot(u,v)/np.linalg.norm(u)/np.linalg.norm(v)
    return np.degrees(np.arccos(np.clip(c,-1,1)))

def circumcircle(P, Q, R):
    D = 2*(Q-P); E = 2*(R-P)
    rhs = np.array([np.dot(Q,Q)-np.dot(P,P), np.dot(R,R)-np.dot(P,P)])
    O = np.linalg.solve(np.vstack([D,E]), rhs)
    Rr = np.linalg.norm(O-P)
    return O, Rr

def power(X, O, R):
    return np.dot(X-O, X-O) - R*R

# Constraint equations derived by hand (Eq*):
# beta:  sin B sin(A-beta) sin(beta+2phi) = 2 sin A cos B sin^2(beta+phi)
# gamma: sin C sin(A-gamma) sin(gamma+2phi) = 2 sin A cos C sin^2(gamma+phi)
def f_beta(beta, A, B, phi):
    return np.sin(B)*np.sin(A-beta)*np.sin(beta+2*phi) - 2*np.sin(A)*np.cos(B)*np.sin(beta+phi)**2

def f_gamma(gam, A, C, phi):
    return np.sin(C)*np.sin(A-gam)*np.sin(gam+2*phi) - 2*np.sin(A)*np.cos(C)*np.sin(gam+phi)**2

def find_roots(f, lo, hi, n=4000):
    xs = np.linspace(lo, hi, n)
    fs = np.array([f(x) for x in xs])
    roots = []
    for i in range(n-1):
        if fs[i]*fs[i+1] < 0:
            a_, b_ = xs[i], xs[i+1]; fa, fb = fs[i], fs[i+1]
            for _ in range(80):
                m = 0.5*(a_+b_); fm = f(m)
                if fa*fm <= 0: b_, fb = m, fm
                else: a_, fa = m, fm
            roots.append(0.5*(a_+b_))
    return roots

def cross2(u, v): return u[0]*v[1]-u[1]*v[0]

def in_triangle(P, X, Y, Z):
    d1 = cross2(Y-X, P-X); d2 = cross2(Z-Y, P-Y); d3 = cross2(X-Z, P-Z)
    has_neg = (d1<-1e-12) or (d2<-1e-12) or (d3<-1e-12)
    has_pos = (d1>1e-12) or (d2>1e-12) or (d3>1e-12)
    return not (has_neg and has_pos)

def run(Adeg, Bdeg, phi_deg, verbose=True):
    Cdeg = 180-Adeg-Bdeg
    A = np.radians(Adeg); B = np.radians(Bdeg); C = np.radians(Cdeg)
    phi = np.radians(phi_deg)
    a = 1.0
    b = a*np.sin(B)/np.sin(A); c = a*np.sin(C)/np.sin(A)
    Bp = np.array([0.,0.]); Cp = np.array([a,0.])
    Ap = np.array([c*np.cos(B), c*np.sin(B)])
    M = (Ap+Bp)/2; N = (Ap+Cp)/2
    betas = find_roots(lambda x: f_beta(x,A,B,phi), 1e-9, B-phi-1e-9)
    gammas = find_roots(lambda x: f_gamma(x,A,C,phi), 1e-9, C-phi-1e-9)
    if verbose:
        print(f"Triangle A={Adeg},B={Bdeg},C={Cdeg}, phi={phi_deg}")
        print("  beta roots (deg):", np.round(np.degrees(betas),6))
        print("  gamma roots (deg):", np.round(np.degrees(gammas),6))
    results = []
    for beta in betas:
        for gamma in gammas:
            K,_,_ = intersect(Bp, dirv(B-phi), Cp, dirv(np.pi-C+gamma+phi))
            L,_,_ = intersect(Bp, dirv(B-beta-phi), Cp, dirv(np.pi-C+phi))
            c1 = abs(ang(K,Bp,Ap)-phi_deg)<1e-6
            c2 = abs(ang(Ap,Cp,L)-phi_deg)<1e-6
            c3 = abs(ang(L,Bp,K)-np.degrees(beta))<1e-6
            c4 = abs(ang(L,N,Cp)-np.degrees(beta))<1e-6
            c5 = abs(ang(L,Cp,K)-np.degrees(gamma))<1e-6
            c6 = abs(ang(Bp,M,K)-np.degrees(gamma))<1e-6
            insideK = in_triangle(K, Bp, M, Cp)
            insideL = in_triangle(L, Bp, N, Cp)
            inangK = abs(ang(L,Bp,Ap) - (ang(L,Bp,K)+ang(K,Bp,Ap)))<1e-6
            inangL = abs(ang(Ap,Cp,K) - (ang(Ap,Cp,L)+ang(L,Cp,K)))<1e-6
            O, R = circumcircle(Ap, K, L)
            OM = np.linalg.norm(O-M); ON = np.linalg.norm(O-N)
            if verbose:
                print(f"  beta={np.degrees(beta):.4f}, gamma={np.degrees(gamma):.4f}")
                print(f"    angle checks: {c1}{c2}{c3}{c4}{c5}{c6}  insideK={insideK} insideL={insideL} inangK={inangK} inangL={inangL}")
                print(f"    OM={OM:.8f} ON={ON:.8f} diff={abs(OM-ON):.2e}")
                print(f"    pow(B)-pow(C) = {power(Bp,O,R)-power(Cp,O,R):.8f}, (c^2-b^2)/2 = {(c*c-b*b)/2:.8f}")
            results.append(dict(A=Ap,B=Bp,C=Cp,M=M,N=N,K=K,L=L,O=O,R=R,beta=beta,gamma=gamma,phi=phi,
                                insideK=insideK,insideL=insideL,inangK=inangK,inangL=inangL))
    return results

if __name__ == "__main__":
    for (A_,B_) in [(70,60),(80,50),(60,70),(75,65)]:
        for phi_ in [8, 12, 18]:
            run(A_,B_,phi_)
            print()
