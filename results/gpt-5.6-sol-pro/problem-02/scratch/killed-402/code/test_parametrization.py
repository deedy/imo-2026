import math

def acot_pos(t): return math.atan2(1.0,t)
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def norm(p): return math.sqrt(dot(p,p))
def solve2(a,b,c,d,e,f):
    det=a*d-b*c
    return ((e*d-b*f)/det,(a*f-e*c)/det)
def bary(P,X,Y,Z):
    u,v=solve2(X[0]-Z[0],Y[0]-Z[0],X[1]-Z[1],Y[1]-Z[1],P[0]-Z[0],P[1]-Z[1])
    return (u,v,1-u-v)
def config(x,y,z):
    kap=acot_pos(2/math.tan(z)+1/math.tan(x))
    lam=acot_pos(2/math.tan(y)+1/math.tan(x))
    g=math.sin(x)/math.sin(x+kap)
    h=math.sin(x)/math.sin(x+lam)
    def f(a):
        return g*h*math.sin(a-lam+x+y)*math.sin(a-kap+x+z)-math.sin(x+y)*math.sin(x+z)
    roots=[]; lo=max(kap,lam)+1e-5; hi=math.pi-1e-5
    grid=[lo+(hi-lo)*i/2000 for i in range(2001)]
    for aa,bb in zip(grid[:-1],grid[1:]):
        fa,fb=f(aa),f(bb)
        if fa*fb<0:
            for _ in range(60):
                cc=(aa+bb)/2
                if f(aa)*f(cc)<=0: bb=cc
                else: aa=cc
            rr=(aa+bb)/2
            if all(abs(rr-r)>1e-5 for r in roots): roots.append(rr)
    out=[]
    for a in roots:
        v=g*math.sin(a-kap+x+z)/math.sin(x+z)
        B=(1.,0.); C=(v*math.cos(a),v*math.sin(a))
        K=(g*math.cos(kap),g*math.sin(kap)); L=(v*h*math.cos(a-lam),v*h*math.sin(a-lam))
        O=solve2(2*K[0],2*K[1],2*L[0],2*L[1],dot(K,K),dot(L,L))
        out.append((a,v,norm(sub(O,(.5,0)))-norm(sub(O,(C[0]/2,C[1]/2))),bary(K,B,(.5,0),C),bary(L,B,(C[0]/2,C[1]/2),C),B,C,K,L,O))
    return kap,lam,g,h,out
for vals in [(0.3,0.2,0.25),(0.5,0.3,0.4),(0.2,0.4,0.3),(0.7,0.2,0.3)]:
    result=config(*vals); print('xyz',vals,'klgh',result[:4])
    for o in result[4]: print(' root',o[:5])
