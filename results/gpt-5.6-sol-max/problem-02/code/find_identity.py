import sympy as s
# Construct polynomial setup with rational trig variables. Target numerator, constraints. Try sequential polynomial division/factor.
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D', nonzero=True)
V=S*X+C*U
# mid simplified = U*(2 C U X -2 S U²+3S)
mid=U*(2*C*U*X-2*S*U**2+3*S)
# polynomial constraints after divide common U (x>0)
ER= s.expand(-R**2*V*c + R*c*(2*C*U*X-2*S*U**2+3*S)-2*S*X*c+2*U*b-2*C*U*c)
ED= s.expand(-D**2*V*b + D*b*(2*C*U*X-2*S*U**2+3*S)-2*S*X*b+2*U*c-2*C*U*b)
# Check ED form cot beta yes
# target geometry
r=c*R/2;d=b*D/2;u=U/S;v=V/S
ks=c-r*v;kt=r*u;ls=d*u;lt=b-d*v
Q=lambda xx,yy:s.expand(xx**2+yy**2+2*C*xx*yy)
Rk=Q(ks,kt);Rl=Q(ls,lt);det=s.expand(ks*lt-kt*ls)
p=s.cancel((Rk*lt-kt*Rl)/det);q=s.cancel((ks*Rl-Rk*ls)/det)
Tden=s.together(2*b*q-2*c*p-b*b+c*c)
T=s.factor(Tden.as_numer_denom()[0])
print('target fact initial',s.factor(T))
# target may have S denominators scaling. Substitute identities via tailored reductions.
# Need ideal membership. Correct groebner likely prior ER retained common U then ideal component issue doesn't matter. Order issue/relation should yield 0 if all identities enough.
rels=[C**2+S**2-1,U**2+X**2-1,b**2+c**2+2*C*b*c-S**2] # WAIT side relation sign! c=sin(A+B)=S cosB+C b. relation (c-Cb)^2=S²(1-b²) => c²-2Cbc+C²b²=S²-S²b²; C²b²+S²b²=b² => b²+c²-2Cbc-S²=0. original right.
rels[-1]=b**2+c**2-2*C*b*c-S**2
# numeric substitutions verify ER ED
num={S:s.sin(s.pi/3),C:s.Rational(1,2),U:s.sin(s.pi/18),X:s.cos(s.pi/18),b:s.sin(7*s.pi/18),c:s.sin(5*s.pi/18),R:s.Float(.7086216595646668),D:s.Float(.8202483623838547)}
print('numeric ER ED T rel',*[s.N(e.subs(num)) for e in [ER,ED,T,*rels]])
# use lex groebner different variable orders. Membership theoretically order independent, previous nonzero means formulas mismatch due V substituted in T after numerator denominator issue okay.
for gens in [(R,D,b,c,C,X,U,S),(R,D,b,c,S,C,U,X),(D,R,c,b,C,X,U,S),(C,S,X,U,b,c,R,D)]:
 print('try',gens)
 try:
  G=s.groebner([ER,ED]+rels,*gens,order='grevlex')
  rem=G.reduce(T)[1]
  print('basis',len(G.polys),'remzero',rem==0,'factor',s.factor(rem) if len(str(rem))<1000 else 'length '+str(len(str(rem))))
 except Exception as e: print(type(e),e)
# Maybe T is numerator before V relation but yes V expression from outset.
