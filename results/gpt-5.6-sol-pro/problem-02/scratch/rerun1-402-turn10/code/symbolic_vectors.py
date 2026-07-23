# Numerical coefficient fitting/exploration for an abstract vector lemma.
# Let unit e direction x; k=1-p ebar, D=1-q e.
# trig p,z and q,y with relation? p and q not arbitrary: directions b and d tied to p,q via y,z.
import math,cmath,random
for _ in range(5):
 x,y,z=[random.uniform(.1,.7) for i in range(3)]
 p=math.sin(z)/(2*math.sin(x+z));q=math.sin(y)/(2*math.sin(x+y))
 k=1-p*cmath.exp(-1j*x);D=1-q*cmath.exp(1j*x)
 print('angles',x,y,z)
 print('kD',k,D,'k+D',k+D,'kDprod',k*D,'kbD',k.conjugate()*D)
 print('a= ratios', (1-k).conjugate()/(1-D), 'mod relations',abs(k)**2,abs(D)**2)
 # identities p trigonometric: 2p sin(x+z)=sinz => 2p(sinx cosz+cosx sinz)=sinz
 # cot z = (1-2p cosx)/(2p sinx).
 # similarly cot y=(1-2q cosx)/(2q sinx).
