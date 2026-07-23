# exact Laurent rational, factor target after c=l/D and compare G.
exec(open('code/rv_target_expand.py').read().split("p=R")[0])
pp=R(X*(Z*Z-one),2*(X*X*Z*Z-one));q=R(X*(Y*Y-one),2*(X*X*Y*Y-one))
k=R(one)-pp/R(X);D=R(one)-q*R(X);b=R(one)/R(X*Y);d=R(X*Z)
l=R(one)-R(r)*b;c=l/D

def br(a,b):return a.bar()*b-a*b.bar()
w=c-R(one)
T=2*(k.norm()*br(w,l)+l.norm()*br(k,w))-(c.norm()-R(one))*br(k,l)
G=l.bar()*(l-k*D)-l*d*d*(l.bar()-k.bar()*D.bar())
# Compare rational T/G after cross products then multivariate divide Laurent.
A=T.n*G.d;B=T.d*G.n
print('terms A B',len(A),len(B))
def normalize(poly):
 mi=[min(m[i] for m in poly) for i in range(N)]
 return P({tuple(m[i]-mi[i] for i in range(N)):w for m,w in poly.items()}),mi
A,sa=normalize(A);B,sb=normalize(B)
# multivariate polynomial divide orders permutations search
for perm in [(4,3,2,1,0),(3,4,2,1,0),(3,2,1,0,4),(0,1,2,3,4),(2,1,0,3,4)]:
 def order(m):return tuple(m[i] for i in perm)
 Q=P();Rem=P(A);lmB=max(B,key=order);steps=0
 while Rem:
  lm=max(Rem,key=order);dif=tuple(lm[i]-lmB[i] for i in range(N))
  if min(dif)<0:break
  term=P({dif:Rem[lm]/B[lmB]});Q=Q+term;Rem=Rem-term*B;steps+=1
  if steps>10000:break
 print(perm,'Q',len(Q),'R',len(Rem),'step',steps)
 if not Rem:
  print('shifts',sa,sb,'Qranges',[(min(m[i] for m in Q),max(m[i] for m in Q)) for i in range(N)])
  # print quotient if small
  if len(Q)<100:
   for m,w in Q.items():print(m,w)
  break
