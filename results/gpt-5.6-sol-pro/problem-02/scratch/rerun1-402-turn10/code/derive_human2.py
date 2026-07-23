import sympy as s
a,b,c,T=s.symbols('a b c T', nonzero=True)
# simplified explicitly
# Rgamma = a(c2-1)/(a2c2-1)? (c-1/c)/(ac-1/ac)=a(c2-1)/(a2c2-1)
k=s.factor(1-(c**2-1)/(2*(a**2*c**2-1)))
# Rbeta = a(b2-1)/(a2b2-1); times a /2
g=s.factor(1-a**2*(b**2-1)/(2*(a**2*b**2-1)))
l=1-T/(a*b)
w=s.factor(l/g)
# hand transformed bar then simplify
kb=s.factor(k.subs({a:1/a,c:1/c}, simultaneous=True))
gb=s.factor(g.subs({a:1/a,b:1/b}, simultaneous=True))
lb=1-T*a*b
wb=s.factor(lb/gb)
print('k',k);print('kb',kb);print('g',g);print('gb',gb);print('w',w);print('wb',wb)
# determinant formula directly
x=(1-w*wb)/4;y=(1-w)/2;yb=(1-wb)/2
D=s.factor(k*kb*(l*yb-lb*y)-k*(l*lb*yb-lb*x)+kb*(l*lb*y-l*x))
print('D fact',s.factor(D))
Q=s.factor((w-k)*wb/(a*c))
Qb=s.factor((wb-kb)*w*a*c)
H2=s.factor(Q-Qb)
print('H2 fact',H2)
print('ratio',s.factor(s.cancel(D/H2)))
