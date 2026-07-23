import sympy as s
S,C,U,X,R,D=s.symbols('S C U X R D')
V=S*X+C*U
f=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
P=s.factor(f(R)*f(D)-4*U**2)
print('raw=',P)
# ordinary factor after impose trig via parametrizations half tangent perhaps.
# Groebner reduce identities then factor different leading substitutions
for subs,name in [({S**2:1-C**2,U**2:1-X**2},'sq'),({C**2:1-S**2,X**2:1-U**2},'cos sq')]:
 q=s.expand(P)
 # repeated xreplace only exact powers after poly remainder
 vars=(C,X,S,U,R,D) if name=='sq' else (S,U,C,X,R,D)
 rels=[S**2+C**2-1,U**2+X**2-1]
 G=s.groebner(rels,*vars,order='grevlex')
 rem=s.factor(G.reduce(q)[1]);print(name,'remfactor=',rem)
# rational tangent substitutions alpha and x: S=2a/(1+a²),C=(1-a²)/(1+a²), etc
a,t=s.symbols('a t')
rat=s.factor(s.together(P.subs({S:2*a/(1+a*a),C:(1-a*a)/(1+a*a),U:2*t/(1+t*t),X:(1-t*t)/(1+t*t)})))
print('rational factor=',rat)
# solve fD=4u²/fR roots symbolically discriminant factor
Disc=s.factor(s.discriminant(s.Poly(P,D),D));print('discriminant raw',Disc)
Drat=s.factor(s.together(Disc.subs({S:2*a/(1+a*a),C:(1-a*a)/(1+a*a),U:2*t/(1+t*t),X:(1-t*t)/(1+t*t)})));print('disc rat',Drat)
