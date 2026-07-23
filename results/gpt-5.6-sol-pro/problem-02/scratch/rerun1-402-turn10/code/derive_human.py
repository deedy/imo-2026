import sympy as s
# unit complex symbols a,b,c, with bars reciprocals. T real.
a,b,c,T=s.symbols('a b c T', nonzero=True)
# a=e^{i alpha}, b=e^{i beta}, c=e^{i gamma}; sin ratios convert
# sin gamma / sin(alpha+gamma) = (c-c^-1)/(a*c-(a*c)^-1)
Rgamma=s.factor((c-1/c)/(a*c-1/(a*c)))
Rbeta=s.factor((b-1/b)/(a*b-1/(a*b)))
k=s.factor(1-Rgamma/(2*a)) # e^-ia
# g = 1 - Rbeta*a/2
g=s.factor(1-Rbeta*a/2)
l=1-T/(a*b)
w=s.factor(l/g)
def bar(expr): return s.factor(expr.xreplace({a:1/a,b:1/b,c:1/c}))
kb,gb,lb,wb=map(bar,[k,g,l,w])
print('k=',k)
print('g=',g)
print('w=',w)
print('kb=',kb)
# D
rows=[[k*kb,k,kb],[l*lb,l,lb],[(1-w*wb)/4,(1-w)/2,(1-wb)/2]]
D=s.factor(s.det(s.Matrix(rows)))
# H=Im((w-k)wb e^-ir)= (Q-Qbar)/(2i). Compare D = coefficient*(Q-Qbar)/2 because D/i=coeff*H
Q=s.factor((w-k)*wb/(a*c))
H2=s.factor(Q-bar(Q))
print('D=',s.factor(D))
print('H2=',s.factor(H2))
print('D/H2=',s.factor(D/H2)) # equals coeff/2
# break D via row operations maybe normalize rows subtract values
# manually determinant formula identify factors
print('D/(k*kb*l*lb?)',s.factor(D/(k*kb*l*lb)))
