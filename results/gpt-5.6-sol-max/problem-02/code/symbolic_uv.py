import sympy as s
# symbols
U,V,C,A=s.symbols('U V C A') # U=sinx, V=sin(A+x), C=cosA ; A perhaps sinA H
b,c,r,d=s.symbols('b c r d', nonzero=True)
# use u=U/S, v=V/S h=C. retain S=sinA
S=s.symbols('S', nonzero=True)
u=U/S; v=V/S; h=C
ks=c-r*v; kt=r*u; ls=d*u; lt=b-d*v
Q=lambda X,Y:s.expand(X**2+Y**2+2*h*X*Y)
Rk=Q(ks,kt);Rl=Q(ls,lt);D=s.expand(ks*lt-kt*ls)
p=s.cancel((Rk*lt-kt*Rl)/D);q=s.cancel((ks*Rl-Rk*ls)/D)
T=s.factor(s.together(2*b*q-2*c*p-b*b+c*c).as_numer_denom()[0])
# substitute identities V= S cosx + C U; derive useful inner simplifications manually print R
print('Rk=',s.factor(Rk*S**2))
print('Rl=',s.factor(Rl*S**2))
print('D=',s.factor(D*S**2))
print('T=',T)
# groebner reduce C²+S²=1 and V? add cos x X, U²+X²
X=s.symbols('X')
T2=s.expand(T.subs(V,S*X+C*U))
# reduction C²+S² and X²+U². lex perhaps
G=s.groebner([C**2+S**2-1,X**2+U**2-1],C,X,S,U,b,c,r,d, order='grevlex')
# can't reduction order all. simply repeated substitutions powers maybe groebner remainder
print('compute rem')
rem=G.reduce(T2)[1]
print(s.factor(rem))
