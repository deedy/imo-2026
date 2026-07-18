import sympy as S
# derive simple special quantities in sine trig to present algebra proof via identities.
x,y,z,t=S.symbols('x y z t', real=True)
sx,sy,sz,sxy,sxz,cx,cy,cz,cxy,cxz=S.symbols('sx sy sz sxy sxz cx cy cz cxy cxz', real=True)
# manually complex vectors, use dot/cross operations pairs. k, l, lambda.
h=sx/sxz;g=sx/sxy
k=(1+h*cz,h*sz)
l=(2-t*cxy,t*sxy)
la=(1+g*cy,-g*sy)
def dot(a,b):return S.expand(a[0]*b[0]+a[1]*b[1])
def cr(a,b):return S.expand(a[0]*b[1]-a[1]*b[0])
def cmul(a,b):return (S.expand(a[0]*b[0]-a[1]*b[1]),S.expand(a[0]*b[1]+a[1]*b[0]))
W=dot(la,la)
n=(S.factor(dot(l,la)/W),S.factor(cr(la,l)/W)) # divide complex
print('W=',S.factor(W))
print('n=',n)
# Need use identities sxy=sx cy+cx sy etc. Maybe W simplifies dramatically: 1+2g cy+g² = ? sin? lambda from triangle ratios; |lambda|=CL/CN perhaps sin? CNL CN=1 unit, L? angle N=y L=x => CL/sin y? Wait lambda L/N; |L|/|N|=CL/CN. CN=1 in relative vector? In CNL, CN=|N|, NL=g|N|, CL=|lambda||N|. By sine law CL/sin y = CN/sin(pi-x-y)=CN/sin(x+y), so |lambda|=sin y/sin(x+y)! Contradiction numeric lambda >1 while sin y/sin sum <1. Check triangle labels: C=2N, N=N, L=lambda N. vectors from N: C-N=N; L-N=g e^-iy N. At N angle between NC=N and NL? g e^-iy N angle y. CN length |N|, NL=g|N|. Given angle LNC=y. At C angle between CN direction -N and CL=(lambda-2)N? x. Sine law: NL opposite x => g=sin x/sin(angle L = pi-x-y) yes. CL opposite y => |lambda-2|=sin y/sin(x+y). But lambda magnitude AL relation no simple.
# l ray relation may simplify n dot values.
# Derive D in terms of n=(u,v) then use L=lambda n, but n expressions perhaps can list identities dot/cross with K.
