#!/usr/bin/env python3
"""
Numerical verification for imo-2026-02.

Construction (converse direction):
  Triangle ABC (counterclockwise), M mid AB, N mid AC.
  Pick x in (0,c).  X on AB with AX=x.  y := c*x/b, Y on AC with AY=y.
  omega1 := circle(B,C,X)  -- check Y on it (should hold since AX*AB=AY*AC).
  omegaK := circle(C,M,X)  (or tangent circle if X=M); K := intersection of
            line BY with omegaK chosen inside triangle BMC.
  omegaL := circle(B,N,Y); L := intersection of line CX with omegaL chosen
            inside triangle BNC.
  omega  := circle(A,K,L), O its center.

Checks:
  (a) original angle conditions: ang(KBA)=ang(ACL), ang(LBK)=ang(LNC),
      ang(LCK)=ang(BMK); K inside angle LBA; L inside angle ACK;
      K inside BMC; L inside BNC.
  (b) |OM| = |ON|.
  (c) F(Z) = pow(Z,omega)-pow(Z,omegaK)-pow(Z,omegaL)+pow(Z,omega1) == 0
      for random Z.
  (d) pow(B,omega) = BM*BX, pow(C,omega) = CN*CY, c*x = b*y.
"""
import math, random

def sub(P,Q): return (P[0]-Q[0], P[1]-Q[1])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def dist(P,Q): return math.hypot(P[0]-Q[0], P[1]-Q[1])

def circle3(P,Q,R):
    ax,ay=P; bx,by=Q; cx,cy=R
    d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
    uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
    O=(ux,uy); return O, dist(O,P)**2

def circle_tangent_at(M, T_dir, P):
    # circle through M and P, tangent at M to direction T_dir:
    # center on line M + s * n, n = rot90(T_dir); |center-P|=|center-M|
    n=(-T_dir[1], T_dir[0])
    # |M + s n - P|^2 = s^2 |n|^2  =>  |M-P|^2 + 2 s n.(M-P) = 0
    s = -dot(sub(M,P),sub(M,P))/(2*dot(n,sub(M,P)))
    O=(M[0]+s*n[0], M[1]+s*n[1]); return O, dist(O,M)**2

def line_circle(P, d, O, r2):
    # points P + t d on circle (O,r2); returns list of t
    a=dot(d,d); b=2*dot(d,sub(P,O)); c=dot(sub(P,O),sub(P,O))-r2
    disc=b*b-4*a*c
    if disc<0: return []
    s=math.sqrt(disc)
    return [(-b-s)/(2*a), (-b+s)/(2*a)]

def power(Z, C): O,r2=C; return dot(sub(Z,O),sub(Z,O))-r2

def ang(P,V,Q):  # unsigned angle P-V-Q in degrees
    u=sub(P,V); v=sub(Q,V)
    return math.degrees(math.acos(max(-1,min(1,dot(u,v)/math.hypot(*u)/math.hypot(*v)))))

def inside_tri(P, T):
    A,B,C=T
    s1=cross(sub(B,A),sub(P,A)); s2=cross(sub(C,B),sub(P,B)); s3=cross(sub(A,C),sub(P,C))
    return (s1>0 and s2>0 and s3>0) or (s1<0 and s2<0 and s3<0)

def run(A,B,C,x, verbose=True):
    M=((A[0]+B[0])/2,(A[1]+B[1])/2); N=((A[0]+C[0])/2,(A[1]+C[1])/2)
    b=dist(A,C); c=dist(A,B)
    assert cross(sub(B,A),sub(C,A))>0, "need ccw"
    y=c*x/b
    assert 0<x<c and 0<y<b
    ux=sub(B,A); X=(A[0]+x*ux[0]/c, A[1]+x*ux[1]/c)
    uy=sub(C,A); Y=(A[0]+y*uy[0]/b, A[1]+y*uy[1]/b)
    om1=circle3(B,C,X)
    chk_Y_on_om1 = power(Y,om1)
    if abs(x-c/2)<1e-12:
        omK=circle_tangent_at(M, ux, C)   # tangent to AB at M, through C
    else:
        omK=circle3(C,M,X)
    # K on line B->Y inside BMC
    dBY=sub(Y,B)
    ts=line_circle(B,dBY,omK[0],omK[1])
    Ks=[(B[0]+t*dBY[0],B[1]+t*dBY[1]) for t in ts]
    Ks=[K for K in Ks if inside_tri(K,(B,M,C))]
    if not Ks: return None
    K=Ks[0]
    omL=circle3(B,N,Y)
    dCX=sub(X,C)
    ts=line_circle(C,dCX,omL[0],omL[1])
    Ls=[(C[0]+t*dCX[0],C[1]+t*dCX[1]) for t in ts]
    Ls=[L for L in Ls if inside_tri(L,(B,N,C))]
    if not Ls: return None
    L=Ls[0]
    om=circle3(A,K,L); O=om[0]
    res={}
    res['Y on om1']=chk_Y_on_om1
    res['ang KBA - ACL']=ang(K,B,A)-ang(A,C,L)
    res['ang LBK - LNC']=ang(L,B,K)-ang(L,N,C)
    res['ang LCK - BMK']=ang(L,C,K)-ang(B,M,K)
    # K inside angle LBA: ray BK strictly between BA and BL
    def between(V, r1, r2, P):  # ray VP strictly inside angle r1-V-r2
        u1=sub(r1,V); u2=sub(r2,V); w=sub(P,V)
        return cross(u1,w)*cross(u1,u2)>0 and cross(u2,w)*cross(u2,u1)>0
    res['K inside angle LBA']=between(B,L,A,K)
    res['L inside angle ACK']=between(C,A,K,L)
    res['OM-ON']=dist(O,M)-dist(O,N)
    res['pow(B,om)-BM*BX']=power(B,om)-(c/2)*(c-x)
    res['pow(C,om)-CN*CY']=power(C,om)-(b/2)*(b-y)
    res['cx-by']=c*x-b*y
    random.seed(1)
    mx=0
    for _ in range(20):
        Z=(random.uniform(-10,10),random.uniform(-10,10))
        F=power(Z,om)-power(Z,omK)-power(Z,omL)+power(Z,om1)
        mx=max(mx,abs(F))
    res['max|F(Z)| random']=mx
    if verbose:
        print(f"A={A} B={B} C={C} x={x:.4g}")
        print(f"  K={K}  L={L}")
        for k,v in res.items(): print(f"  {k}: {v}")
    return res

if __name__=='__main__':
    run((0,0),(4,0),(1,3),1.2)
    print()
    run((0,0),(4,0),(1,3),2.0)   # X = M tangency case
    print()
    run((0,0),(5,0),(0.5,2.5),0.9)
    print()
    run((0,0),(3.2,0),(2.5,2.2),1.4)
