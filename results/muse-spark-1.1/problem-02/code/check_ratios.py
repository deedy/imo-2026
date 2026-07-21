import math

def rot(vec, theta):
    x,y=vec
    c=math.cos(theta); s=math.sin(theta)
    return (x*c - y*s, x*s + y*c)

def cross(ax,ay,bx,by): return ax*by - ay*bx

def intersect(P1,d1,P2,d2):
    d1x,d1y=d1; d2x,d2y=d2
    rhsx=P2[0]-P1[0]; rhsy=P2[1]-P1[1]
    det=d1x*(-d2y) - (-d2x)*d1y
    if abs(det)<1e-12: return None
    det_t=-rhsx*d2y + d2x*rhsy
    det_s=d1x*rhsy - rhsx*d1y
    t=det_t/det; s=det_s/det
    return (P1[0]+t*d1x, P1[1]+t*d1y, t,s)

def point_in_tri(P,A,B,C):
    def sign(p1,p2,p3): return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
    d1=sign(P,A,B); d2=sign(P,B,C); d3=sign(P,C,A)
    has_neg=(d1<-1e-9) or (d2<-1e-9) or (d3<-1e-9)
    has_pos=(d1>1e-9) or (d2>1e-9) or (d3>1e-9)
    return not (has_neg and has_pos)

u=0.3; v=2.5
M=(-1.0,0.0); N=(1.0,0.0); A=(u,v); B=(-2-u,-v); C=(2-u,-v)
BA=(A[0]-B[0], A[1]-B[1]); CA_dir=(u-1.0,v); MB=(B[0]-M[0], B[1]-M[1]); NC_vec=(C[0]-N[0], C[1]-N[1])

def eval_f(gamma,alpha):
    BK_dir=rot(BA,-alpha); MK_dir=rot(MB,gamma)
    inter=intersect(B,BK_dir,M,MK_dir)
    if inter is None: return None
    Kx,Ky,tB,sM=inter
    CK_dir=rot(CA_dir, alpha+gamma)  # direction from C?
    KC=(Kx-C[0],Ky-C[1])
    cr=cross(KC[0],KC[1],CK_dir[0],CK_dir[1])
    return cr,(Kx,Ky),tB,sM

def eval_g(beta,alpha):
    CL_dir=rot(CA_dir,alpha); NL_dir=rot(NC_vec,-beta)
    inter=intersect(C,CL_dir,N,NL_dir)
    if inter is None: return None
    Lx,Ly,tC,sN=inter
    BL_dir=rot(BA, -(alpha+beta))
    BL_vec=(Lx-B[0], Ly-B[1])
    cr=cross(BL_vec[0],BL_vec[1],BL_dir[0],BL_dir[1])
    return cr,(Lx,Ly),tC,sN

def find_gamma(alpha):
    n=2000; prev=None; prev_g=None
    for i in range(1,n):
        gamma=i*(math.pi*0.9)/n
        res=eval_f(gamma,alpha)
        if res is None: continue
        cr,_,_,_=res
        if prev is not None and (cr==0 or prev*cr<0):
            lo=prev_g; hi=gamma
            for _ in range(80):
                mid=(lo+hi)/2
                rm=eval_f(mid,alpha)
                if rm is None: break
                crm=rm[0]
                rlo=eval_f(lo,alpha)
                if rlo is None: break
                crlo=rlo[0]
                if crlo*crm<=0: hi=mid
                else: lo=mid
            sol=(lo+hi)/2
            rs=eval_f(sol,alpha)
            if rs is None: 
                prev=cr; prev_g=gamma; continue
            _,K,tB,sM=rs
            if tB>0 and sM>0 and point_in_tri(K,B,M,C):
                return sol,K
        prev=cr; prev_g=gamma
    return None

def find_beta(alpha):
    n=2000; prev=None; prev_b=None
    for i in range(1,n):
        beta=i*(math.pi*0.9)/n
        res=eval_g(beta,alpha)
        if res is None: continue
        cr,_,_,_=res
        if prev is not None and (cr==0 or prev*cr<0):
            lo=prev_b; hi=beta
            for _ in range(80):
                mid=(lo+hi)/2
                rm=eval_g(mid,alpha)
                if rm is None: break
                crm=rm[0]
                rlo=eval_g(lo,alpha)
                if rlo is None: break
                crlo=rlo[0]
                if crlo*crm<=0: hi=mid
                else: lo=mid
            sol=(lo+hi)/2
            rs=eval_g(sol,alpha)
            if rs is None:
                prev=cr; prev_b=beta; continue
            _,L,tC,sN=rs
            if tC>0 and sN>0 and point_in_tri(L,B,N,C):
                return sol,L
        prev=cr; prev_b=beta
    return None

alpha=math.radians(10)
gres=find_gamma(alpha)
bres=find_beta(alpha)
gamma,K=gres
beta,L=bres
print(f"gamma {math.degrees(gamma)} beta {math.degrees(beta)}")
print(f"K {K} L {L} A {A} M {M} N {N}")
def dist(P,Q): return math.hypot(P[0]-Q[0],P[1]-Q[1])
print("AK",dist(A,K),"AM",dist(A,M),"AL",dist(A,L),"AN",dist(A,N))
print("BK",dist(B,K),"BM",dist(B,M))
print("MK",dist(M,K))
print("CL",dist(C,L),"CK",dist(C,K))
print("NL",dist(N,L))
# ratios
print("BK/BM",dist(B,K)/dist(B,M),"sin gamma / sin(alpha+gamma)",math.sin(gamma)/math.sin(alpha+gamma))
print("LC/NC",dist(C,L)/dist(N,C),"sin beta / sin(alpha+beta)",math.sin(beta)/math.sin(alpha+beta))
# check if triangles ABK similar to?
# compute angles of triangle AKL vs AMN?
def angle(P,Q,R): # angle PQR at Q between QP and QR
    ux=P[0]-Q[0]; uy=P[1]-Q[1]
    vx=R[0]-Q[0]; vy=R[1]-Q[1]
    dot=ux*vx+uy*vy
    nu=math.hypot(ux,uy); nv=math.hypot(vx,vy)
    if nu*nv<1e-12: return 0
    c=dot/(nu*nv); c=max(-1,min(1,c))
    return math.acos(c)
print("angle KAM",math.degrees(angle(K,A,M)), "angle LAN",math.degrees(angle(L,A,N)))
print("angle AMK",math.degrees(angle(A,M,K)), "angle ANL",math.degrees(angle(A,N,L)))
# try to see if quadrilateral MK B? 
# Compute oriented angles for spiral similarity at K?
# Might look at triangles M K A and ?
# compute cross ratios
# Check if MK/CK = MB/LC?
print("MB",dist(M,B),"LC",dist(L,C),"MK",dist(M,K),"CK",dist(C,K))
print("MB/LC",dist(M,B)/dist(L,C),"MK/CK",dist(M,K)/dist(C,K))
print("LB",dist(L,B),"CN?",dist(C,N),"KB/NC",dist(K,B)/dist(N,C),"LB/NL",dist(L,B)/dist(N,L))
# Check if quadrilateral K M N L cyclic?
# Compute opposite angles
print("angle KMN",math.degrees(angle(K,M,N)), "angle KLN",math.degrees(angle(K,L,N)))
print("angle KNM",math.degrees(angle(K,N,M)), "angle KLM",math.degrees(angle(K,L,M)))
