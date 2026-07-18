import sympy as s
X,Y,Z,T,d=s.symbols('X Y Z T d', nonzero=True)
def bar(e):
    e=s.sympify(e)
    return s.cancel(e.xreplace({X:1/X,Y:1/Y,Z:1/Z,T:1/T}))
p=s.cancel((X-1/X)/(X*Z-1/(X*Z)))
h=s.cancel((X-1/X)/(X*Y-1/(X*Y)))
k=s.cancel(1+p*Z)
l=s.cancel(d*T*(1+h/Y))
n=d*T
# line constraints ratio real
r1=s.cancel((2*d*T-k)*X*Z/T)
f1=s.factor(s.together(r1-bar(r1)))
r2=s.cancel((l-2)*X*Y)
f2=s.factor(s.together(r2-bar(r2)))
print('k',s.factor(k));print('l/dT',s.factor(l/(d*T)))
print('f1=',f1)
print('f2=',f2)
# circle q=w bw + u w + ub bw. solve u,ub from k,l
u,ub=s.symbols('u ub')
sol=s.solve([u*k+ub*bar(k)+k*bar(k),u*l+ub*bar(l)+l*bar(l)],[u,ub], simplify=False)
q=lambda w:s.cancel(w*bar(w)+sol[u]*w+sol[ub]*bar(w))
g=s.factor(s.together(q(1)-q(n)))
print('g factor=',g)
