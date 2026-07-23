import math,cmath,random
# Evaluate ratio T/G away compatibility varying r; see simple function

def br(a,b):return a.conjugate()*b-a*b.conjugate()
for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4)]:
 x,y,z=xyz;p=math.sin(z)/(2*math.sin(x+z));q=math.sin(y)/(2*math.sin(x+y));k=1-p*cmath.exp(-1j*x);D=1-q*cmath.exp(1j*x);b=cmath.exp(-1j*(x+y));d=cmath.exp(1j*(x+z))
 print('\n',xyz)
 for r in [.1,.3,.7,1.2,2]:
  l=1-r*b;c=l/D;w=c-1
  T=2*(abs(k)**2*br(w,l)+abs(l)**2*br(k,w))-(abs(c)**2-1)*br(k,l)
  G=l.conjugate()*(l-k*D)-l*d*d*(l.conjugate()-k.conjugate()*D.conjugate())
  ratio=T/G
  cand={
  'T/G':ratio,
  '/l2':ratio/abs(l)**2,
  '*D2':ratio*abs(D)**2,
  '*D2/l2':ratio*abs(D)**2/abs(l)**2,
  '/(l-kD?)':ratio/(l-k*D) if l!=k*D else 0,
  }
  print(r, cand)
