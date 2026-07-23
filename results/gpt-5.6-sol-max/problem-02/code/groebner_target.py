import sympy as s
# trig constants A angle and x: S,C,U,X; sides can be represented b=sin B, c=sin G, with B+G=pi-A
# Need relations involving b,c,A: law cosine a? normalize a=sinA; relation between b,c: sin? cos B=(a²+c²-b²)/2ac.
# derive length quadratic Etheta rho: -rho² sinθ sinx sin(A+x) + rho sinθ[-cosx cos(A+2x)+cos(A-x)] -2 sinA sinx sin(θ-x)=0
# simplify middle coefficient.
A,x,th,rho=s.symbols('A x th rho')
mid=s.trigsimp(-s.cos(x)*s.cos(A+2*x)+s.cos(A-x),method='fu')
print('mid=',mid, 'expand',s.expand_trig(mid))
print(s.trigsimp(mid/s.sin(x),method='fu'))
# likely sinx? cos(A-x)-cosx cos(A+2x)
# express E / sinx perhaps.

# Algebra in abstract side variables and trig A,x. Generate E_gamma for R=2r/c, E_beta D=2d/b using sin gamma=c/Rcirc etc.
# Normalize circumdiameter=1: a=sinA,b=sinB,c=sinG. sin(theta-x)=sinθ cosx-cosθ sinx.
# cos gamma=(a²+b? sides adjacent at C: (a²+b²-c²)/(2ab)); c cosgamma=(a²+b²-c²)/(2a*b)*c problematic but sin gamma=c.
# Since E includes sinθ and sin(theta-x); divide sinθ: sin(theta-x)/sinθ = cosx-cotθ sinx.
# Etheta/r sinθ:
# -rho² U V + rho*mid -2 S U(cosx-cotθ U)=0.
# cot gamma=(a²+b²-c²)/(2 a? sin gamma=c, circumdiam 1; cosgamma=(a²+b²-c²)/(2ab), divide c => /c)
# cot gamma=(a²+b²-c²)/(2*a*b*c). But circumradius relation sides constrained; perhaps express cot gamma=(cos?); in b,c,A use gamma=pi-A-B; derive cot gamma=(? C? relation b?)
# Identity c=sin(A+B)=S cosB+C b; cosB = (c-C*b)/S. cotB=(c-C*b)/(S*b).
# cotgamma=(b-C*c)/(S*c). Great.
S,C,U,X,V,b,c,R,D=s.symbols('S C U X V b c R D', nonzero=True)
# V=sin(A+x)=S X+C U; mid direct algebra
# mid = cos(A-x)-cosx cos(A+2x)
# compute algebra expression expanded using trig representations and reduce U²+X²
# cos(A-x)=C*X+S*U; cos(A+2x)=C*(X²-U²)-S*2UX
midalg=C*X+S*U-X*(C*(X**2-U**2)-2*S*U*X)
midalg=s.rem(s.Poly(s.expand(midalg),X),s.Poly(X**2-(1-U**2),X)).as_expr() # questionable reduction X² substitute, x^3
print('midalg reduced',s.factor(midalg))
# manually simplify with sympy trig and rewrite expected perhaps sinx*sin(A+?)+
print('mid factor trig',s.trigsimp(mid.rewrite(s.sin),method='fu'))
# constraints ER gamma, ED beta
cotg=(b-C*c)/(S*c)
cotb=(c-C*b)/(S*b)
ER=s.cancel(-R**2*U*V + R*midalg -2*S*U*(X-cotg*U))*c
ED=s.cancel(-D**2*U*V + D*midalg -2*S*U*(X-cotb*U))*b
ER=s.expand(ER); ED=s.expand(ED)
print('ER=',s.factor(ER))
# target substitute r=cR/2,d=bD/2 into prior geometry and reduce trig identities
r=c*R/2;d=b*D/2
u=U/S;v=V/S;h=C
ks=c-r*v;kt=r*u;ls=d*u;lt=b-d*v
Q=lambda xx,yy:s.expand(xx**2+yy**2+2*h*xx*yy)
Rk=Q(ks,kt);Rl=Q(ls,lt);det=s.expand(ks*lt-kt*ls)
p=s.cancel((Rk*lt-kt*Rl)/det);q=s.cancel((ks*Rl-Rk*ls)/det)
T=s.factor(s.together(2*b*q-2*c*p-b*b+c*c).as_numer_denom()[0])
# substitute V relation then reduce identities S²+C²=1 U²+X²=1 using groebner, plus side relation? b,c relation from B+G: derive c=S cosB+C b -> (c-Cb)^2=S²(1-b²), equivalently b²+c²-2Cbc=S². Yes!
T=s.expand(T.subs(V,S*X+C*U))
ER=s.expand(ER.subs(V,S*X+C*U));ED=s.expand(ED.subs(V,S*X+C*U))
rels=[C**2+S**2-1,U**2+X**2-1,b**2+c**2-2*C*b*c-S**2,ER,ED]
print('degrees T',s.Poly(T,C,S,U,X,b,c,R,D).total_degree())
print('groebner...')
G=s.groebner(rels,R,D,b,c,C,X,U,S,order='grevlex')
print('basis len',len(G.polys))
rem=G.reduce(T)[1]
print('remainder=',s.factor(rem))
