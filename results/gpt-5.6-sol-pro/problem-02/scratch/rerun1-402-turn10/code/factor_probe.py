import math,cmath,random

def cross(a,b): return (a.conjugate()*b).imag
for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4)]:
 x,y,z=xyz
 p=math.sin(z)/(2*math.sin(x+z));q=math.sin(y)/(2*math.sin(x+y))
 k=1-p*cmath.exp(-1j*x);D=1-q*cmath.exp(1j*x);d=cmath.exp(1j*(x+z));b=cmath.exp(-1j*(x+y))
 print('\n',xyz,'k,D',k,D)
 for v in [.1,.3,.7,1.1,1.8,3]:
  c=k/(1-v*d);l=c*D
  E=2*(abs(k)**2*cross(c-1,l)+abs(l)**2*cross(k,c-1))-(abs(c)**2-1)*cross(k,l)
  comp=cross(b,l-1)
  print(v,E/comp, 'raw',E,comp, 'scaled', E/comp*(abs(1-v*d)**2))
