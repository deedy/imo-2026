exec(open('code/symbolic.py').read().split("# circle")[0])
P1=s.together(f1).as_numer_denom()[0];P2=s.together(f2).as_numer_denom()[0]
dsol=s.solve(P1,d)[0]
R=s.factor(s.together(P2.subs(d,dsol)).as_numer_denom()[0])
print('R',R)
# reconstruct g quietly
u,ub=s.symbols('u ub');sol=s.solve([u*k+ub*bar(k)+k*bar(k),u*l+ub*bar(l)+l*bar(l)],[u,ub],simplify=False)
q=lambda w:s.cancel(w*bar(w)+sol[u]*w+sol[ub]*bar(w))
G=s.factor(s.together((q(1)-q(n)).subs(d,dsol)).as_numer_denom()[0])
print('G fact',s.factor(G))
print('ratio',s.factor(G/R))
