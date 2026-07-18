#!/usr/bin/env python3
"""Extra checks:
 1. Tangency case Y=N (x = b^2/(2c)) of the construction.
 2. Random sanity test of Lemma 2 (directed inscribed angle iff) and
    Lemma 3 (directed tangent-chord).
"""
import math, random, cmath
from verify import sub, dot, cross, dist, circle3, circle_tangent_at, line_circle, power, ang, inside_tri

def run_tangentY(A,B,C):
    M=((A[0]+B[0])/2,(A[1]+B[1])/2); N=((A[0]+C[0])/2,(A[1]+C[1])/2)
    b=dist(A,C); c=dist(A,B)
    x=b*b/(2*c); y=c*x/b   # = b/2  ->  Y=N
    ux=sub(B,A); X=(A[0]+x*ux[0]/c, A[1]+x*ux[1]/c)
    uy=sub(C,A); Y=(A[0]+y*uy[0]/b, A[1]+y*uy[1]/b)
    assert dist(Y,N)<1e-12
    om1=circle3(B,C,X)
    omK=circle3(C,M,X) if abs(x-c/2)>1e-12 else circle_tangent_at(M,ux,C)
    dBY=sub(Y,B)
    Ks=[(B[0]+t*dBY[0],B[1]+t*dBY[1]) for t in line_circle(B,dBY,omK[0],omK[1])]
    K=[k for k in Ks if inside_tri(k,(B,M,C))][0]
    omL=circle_tangent_at(N, uy, B)   # tangent to AC at N, through B
    dCX=sub(X,C)
    Ls=[(C[0]+t*dCX[0],C[1]+t*dCX[1]) for t in line_circle(C,dCX,omL[0],omL[1])]
    L=[l for l in Ls if inside_tri(l,(B,N,C))][0]
    om=circle3(A,K,L); O=om[0]
    print("tangency case Y=N :", A,B,C)
    print("  angle checks:", ang(K,B,A)-ang(A,C,L), ang(L,B,K)-ang(L,N,C), ang(L,C,K)-ang(B,M,K))
    def between(V,r1,r2,P):
        u1=sub(r1,V);u2=sub(r2,V);w=sub(P,V)
        return cross(u1,w)*cross(u1,u2)>0 and cross(u2,w)*cross(u2,u1)>0
    print("  K in angle LBA:", between(B,L,A,K), " L in angle ACK:", between(C,A,K,L))
    print("  OM-ON =", dist(O,M)-dist(O,N))
    print("  pow(B,om)-BM*BX =", power(B,om)-(c/2)*(c-x))
    print("  pow(C,om)-CN*CY =", power(C,om)-(b/2)*(b-y))

run_tangentY((0,0),(4,0),(1,3))
print()

# Lemma 2 sanity: P,Q,R random on random circle, S on/off circle
random.seed(7)
def dirang(d1,d2):  # directed angle between directions mod pi
    a=cmath.phase(d2/d1)%math.pi
    return a
bad=0
for _ in range(2000):
    O=complex(random.uniform(-3,3),random.uniform(-3,3)); r=random.uniform(.5,3)
    P,Q,R=[O+r*cmath.exp(1j*random.uniform(0,2*math.pi)) for _ in range(3)]
    if random.random()<.5:
        S=O+r*cmath.exp(1j*random.uniform(0,2*math.pi)); on=True
    else:
        S=complex(random.uniform(-6,6),random.uniform(-6,6)); on=abs(abs(S-O)-r)<1e-9
    d=abs((dirang(P-R,Q-R)-dirang(P-S,Q-S)+math.pi/2)%math.pi-math.pi/2)
    if on != (d<1e-7): bad+=1
print("Lemma2 mismatches:", bad)

# Lemma 3 sanity: tangent-chord
bad=0
for _ in range(2000):
    O=complex(random.uniform(-3,3),random.uniform(-3,3)); r=random.uniform(.5,3)
    M_,K_,C_=[O+r*cmath.exp(1j*random.uniform(0,2*math.pi)) for _ in range(3)]
    t=1j*(M_-O)  # tangent direction at M_
    d=abs((dirang(t,K_-M_)-dirang(M_-C_,K_-C_)+math.pi/2)%math.pi-math.pi/2)
    if d>1e-7: bad+=1
print("Lemma3 mismatches:", bad)
