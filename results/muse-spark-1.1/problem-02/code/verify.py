import math

def rot(vec, theta):
    x,y = vec
    c = math.cos(theta)
    s = math.sin(theta)
    return (x*c - y*s, x*s + y*c)

def cross(ax,ay,bx,by):
    return ax*by - ay*bx

def intersect(B, dB, M, dM):
    d1x,d1y = dB
    d2x,d2y = dM
    rhsx = M[0]-B[0]
    rhsy = M[1]-B[1]
    det = d1x*(-d2y) - (-d2x)*d1y
    if abs(det) < 1e-12:
        return None
    det_t = -rhsx*d2y + d2x*rhsy
    det_s = d1x*rhsy - rhsx*d1y
    t = det_t / det
    s = det_s / det
    px = B[0] + t*d1x
    py = B[1] + t*d1y
    return (px, py, t, s)

def point_in_triangle(P, A,B,C):
    def sign(p1,p2,p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    d1 = sign(P,A,B)
    d2 = sign(P,B,C)
    d3 = sign(P,C,A)
    has_neg = (d1 < -1e-9) or (d2 < -1e-9) or (d3 < -1e-9)
    has_pos = (d1 > 1e-9) or (d2 > 1e-9) or (d3 > 1e-9)
    return not (has_neg and has_pos)

u = 0.3
v = 2.5
M = (-1.0, 0.0)
N = (1.0, 0.0)
A = (u, v)
B = (-2 - u, -v)
C = (2 - u, -v)
BA = (A[0]-B[0], A[1]-B[1])
CA_dir = (u-1.0, v)
MB = (B[0]-M[0], B[1]-M[1])
NC_vec = (C[0]-N[0], C[1]-N[1])

print(f"A {A} B {B} C {C} BA {BA} CA {CA_dir} MB {MB} NC {NC_vec}")

def eval_f(gamma, alpha):
    BK_dir = rot(BA, -alpha)
    MK_dir = rot(MB, gamma)
    inter = intersect(B, BK_dir, M, MK_dir)
    if inter is None:
        return None
    Kx,Ky,tB,sM = inter
    K = (Kx,Ky)
    CK_dir = rot(CA_dir, alpha+gamma)
    KC = (Kx - C[0], Ky - C[1])
    cr = cross(KC[0], KC[1], CK_dir[0], CK_dir[1])
    return cr, K, tB, sM, BK_dir, MK_dir, CK_dir

def eval_g(beta, alpha):
    CL_dir = rot(CA_dir, alpha)
    NL_dir = rot(NC_vec, -beta)
    inter = intersect(C, CL_dir, N, NL_dir)
    if inter is None:
        return None
    Lx,Ly,tC,sN = inter
    L = (Lx,Ly)
    BL_dir = rot(BA, -(alpha+beta))
    BL_vec = (Lx - B[0], Ly - B[1])
    cr = cross(BL_vec[0], BL_vec[1], BL_dir[0], BL_dir[1])
    return cr, L, tC, sN, BL_dir, NL_dir, CL_dir

def find_gamma(alpha):
    n=2000
    prev=None
    prev_g=None
    for i in range(1,n):
        gamma = i * (math.pi*0.9)/n
        res = eval_f(gamma, alpha)
        if res is None:
            continue
        cr, *_ = res
        if prev is not None:
            if cr==0 or prev*cr < 0:
                lo = prev_g
                hi = gamma
                for _ in range(80):
                    mid = (lo+hi)/2
                    res_mid = eval_f(mid, alpha)
                    if res_mid is None:
                        break
                    cr_mid = res_mid[0]
                    res_lo = eval_f(lo, alpha)
                    if res_lo is None:
                        break
                    cr_lo = res_lo[0]
                    if cr_lo*cr_mid <= 0:
                        hi = mid
                    else:
                        lo = mid
                sol_gamma = (lo+hi)/2
                res_sol = eval_f(sol_gamma, alpha)
                if res_sol is None:
                    prev=cr
                    prev_g=gamma
                    continue
                _, K, tB, sM,_,_,_ = res_sol
                if tB>1e-9 and sM>1e-9:
                    if point_in_triangle(K, B, M, C):
                        return sol_gamma, K
        prev = cr
        prev_g = gamma
    return None

def find_beta(alpha):
    n=2000
    prev=None
    prev_b=None
    for i in range(1,n):
        beta = i*(math.pi*0.9)/n
        res = eval_g(beta, alpha)
        if res is None:
            continue
        cr, *_ = res
        if prev is not None:
            if cr==0 or prev*cr <0:
                lo = prev_b
                hi = beta
                for _ in range(80):
                    mid = (lo+hi)/2
                    res_mid = eval_g(mid, alpha)
                    if res_mid is None:
                        break
                    cr_mid=res_mid[0]
                    res_lo = eval_g(lo, alpha)
                    if res_lo is None:
                        break
                    cr_lo=res_lo[0]
                    if cr_lo*cr_mid <=0:
                        hi=mid
                    else:
                        lo=mid
                sol_beta=(lo+hi)/2
                res_sol = eval_g(sol_beta, alpha)
                if res_sol is None:
                    prev=cr
                    prev_b=beta
                    continue
                _, L, tC, sN,_,_,_ = res_sol
                if tC>1e-9 and sN>1e-9:
                    if point_in_triangle(L, B, N, C):
                        return sol_beta, L
        prev=cr
        prev_b=beta
    return None

for alpha_deg in [2,5,10,15,20,25,30]:
    alpha=math.radians(alpha_deg)
    gres=find_gamma(alpha)
    bres=find_beta(alpha)
    print(f"\nalpha {alpha_deg} deg")
    print(f"  gamma res {gres}")
    print(f"  beta res {bres}")
    if gres and bres:
        gamma,K=gres
        beta,L=bres
        Ax,Ay=A
        Kx,Ky=K
        Lx,Ly=L
        D=2*(Ax*(Ky-Ly)+Kx*(Ly-Ay)+Lx*(Ay-Ky))
        if abs(D)<1e-12:
            print("  degenerate AKL")
            continue
        Ax2=Ax*Ax+Ay*Ay
        K2=Kx*Kx+Ky*Ky
        L2=Lx*Lx+Ly*Ly
        Ox=(Ax2*(Ky-Ly)+K2*(Ly-Ay)+L2*(Ay-Ky))/D
        Oy=(Ax2*(Lx-Kx)+K2*(Ax-Lx)+L2*(Kx-Ax))/D
        OM=math.hypot(Ox-M[0], Oy-M[1])
        ON=math.hypot(Ox-N[0], Oy-N[1])
        print(f"  K {K} L {L} O ({Ox:.6f},{Oy:.6f}) OM {OM:.6f} ON {ON:.6f} diff {OM-ON:.3e} Ox approx {Ox}")
        def angle_between(v1,v2):
            dot=v1[0]*v2[0]+v1[1]*v2[1]
            n1=math.hypot(*v1)
            n2=math.hypot(*v2)
            if n1*n2<1e-12:
                return 0
            c=dot/(n1*n2)
            c=max(-1,min(1,c))
            return math.acos(c)
        BA_vec=BA
        BK_vec=(K[0]-B[0], K[1]-B[1])
        KBA=angle_between(BA_vec, BK_vec)
        CA_vec=(A[0]-C[0], A[1]-C[1])
        CL_vec=(L[0]-C[0], L[1]-C[1])
        ACL=angle_between(CA_vec, CL_vec)
        BL_vec=(L[0]-B[0], L[1]-B[1])
        LBK=angle_between(BL_vec, BK_vec)
        NCv=NC_vec
        NL_vec=(L[0]-N[0], L[1]-N[1])
        LNC=angle_between(NCv, NL_vec)
        CK_vec=(K[0]-C[0], K[1]-C[1])
        LCK=angle_between(CL_vec, CK_vec)
        BM_vec=MB
        MK_vec=(K[0]-M[0], K[1]-M[1])
        BMK=angle_between(BM_vec, MK_vec)
        print(f"    angles deg: KBA {math.degrees(KBA):.4f} ACL {math.degrees(ACL):.4f} LBK {math.degrees(LBK):.4f} LNC {math.degrees(LNC):.4f} LCK {math.degrees(LCK):.4f} BMK {math.degrees(BMK):.4f}")

# test other A positions
print("\n\nSecond triangle shape")
for (u2,v2) in [(-0.8,1.5), (0.0,2.0), (1.2,3.0)]:
    u=u2; v=v2
    M = (-1.0,0.0); N=(1.0,0.0); A=(u,v); B=(-2-u, -v); C=(2-u, -v)
    BA = (A[0]-B[0], A[1]-B[1]); CA_dir=(u-1.0, v); MB=(B[0]-M[0], B[1]-M[1]); NC_vec=(C[0]-N[0], C[1]-N[1])
    print(f"\nShape u={u} v={v} A {A} B {B} C {C}")
    for alpha_deg in [5,15]:
        alpha=math.radians(alpha_deg)
        gres=find_gamma(alpha)
        bres=find_beta(alpha)
        if gres and bres:
            gamma,K=gres; beta,L=bres
            Ax,Ay=A; Kx,Ky=K; Lx,Ly=L
            D=2*(Ax*(Ky-Ly)+Kx*(Ly-Ay)+Lx*(Ay-Ky))
            if abs(D)<1e-12:
                print(f"  alpha {alpha_deg} degenerate")
                continue
            Ax2=Ax*Ax+Ay*Ay; K2=Kx*Kx+Ky*Ky; L2=Lx*Lx+Ly*Ly
            Ox=(Ax2*(Ky-Ly)+K2*(Ly-Ay)+L2*(Ay-Ky))/D
            Oy=(Ax2*(Lx-Kx)+K2*(Ax-Lx)+L2*(Kx-Ax))/D
            OM=math.hypot(Ox-M[0], Oy-M[1]); ON=math.hypot(Ox-N[0], Oy-N[1])
            print(f"  alpha {alpha_deg} Ox {Ox:.6f} OM {OM:.6f} ON {ON:.6f} diff {OM-ON:.3e}")
        else:
            print(f"  alpha {alpha_deg} no solution gres {gres is not None} bres {bres is not None}")
