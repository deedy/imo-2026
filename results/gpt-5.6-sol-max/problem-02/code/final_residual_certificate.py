import sympy as s
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D')
V=S*X+C*U;W=C*X-S*U
F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=s.expand(2*U*b-c*F(R));ED=s.expand(2*U*c-b*F(D))
IA=C**2+S**2-1;Ix=X**2+U**2-1;Is=b**2+c**2-2*C*b*c-S**2
r=c*R/2;d=b*D/2;kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r;L2=b*b-2*b*d*X+d*d
P=K2*ly-ky*L2;Q=kx*L2-K2*lx;det=kx*ly-ky*lx
T=s.expand(2*(b*(C*P+S*Q)-c*P)-(b*b-c*c)*det)
qR,remR=s.div(T,ER,R);qD,H=s.div(remR,ED,D)
# all rational due leading V. clear denominator 4V: cert Hc=4V H polynomial
Hc=s.cancel(4*V*H);assert s.denom(Hc)==1;Hc=s.expand(Hc)
print('Hc terms',len(s.Poly(Hc).terms()),'factor',s.factor(Hc),flush=True)
# sequential divide Hc by simple identities with smart variables. Try all 6 permutations/orders and report remainder/quotient complexity.
import itertools
items=[('IA',IA,C),('Ix',Ix,X),('Is',Is,b)]
for perm in itertools.permutations(items):
 rem=Hc; qs=[]
 for name,e,var in perm:
  q,rem=s.div(rem,e,var);qs.append((name,s.factor(q)))
 if s.expand(rem)==0:
  print('SUCCESS order',[a[0] for a in perm])
  for name,q in qs: print('Q'+name,'=',q)
  break
else:
 print('no sequential zero; try groebner quotient unavailable')
 for perm in itertools.permutations(items):
  rem=Hc;qs=[]
  for name,e,var in perm:
   q,rem=s.div(rem,e,var);qs.append((name,q))
  print([a[0] for a in perm],'rem terms',len(s.Poly(rem).terms()),'factor',s.factor(rem) if len(str(rem))<2000 else 'long')
# Alternative reduce Hc by Groebner with lex and recover division quotients G.reduce returns quotients relative to basis. If input generators already GB under clever order, use.
for gens in [(C,X,b,c,S,U,R,D),(b,C,X,c,S,U,R,D),(C,b,X,c,S,U,R,D),(X,C,b,c,S,U,R,D)]:
 G=s.groebner([IA,Ix,Is],*gens,order='lex')
 quo,rem=G.reduce(Hc)
 print('G gens',gens[:3],'basis', [s.factor(p.as_expr()) for p in G.polys], 'remzero',rem==0)
 if rem==0:
  print('quotients',[(s.factor(G.polys[i].as_expr()),s.factor(q)) for i,q in enumerate(quo)]);break
