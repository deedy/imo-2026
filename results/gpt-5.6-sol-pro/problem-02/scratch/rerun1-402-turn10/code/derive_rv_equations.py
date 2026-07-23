import math,cmath,random
for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4)]:
 x,y,z=xyz;p=math.sin(z)/(2*math.sin(x+z));q=math.sin(y)/(2*math.sin(x+y));
 k=1-p*cmath.exp(-1j*x);D=1-q*cmath.exp(1j*x);b=cmath.exp(-1j*(x+y));d=cmath.exp(1j*(x+z))
 # equation c=(1-rb)/D=k/(1-vd) => (1-rb)(1-vd)=kD
 # expand: 1-rb-vd+rv bd=kD = 1-p/e-qe+pq
 # b*d=e^{i(z-y)}
 # maybe imaginary/real yields trig relation simple. unknown r,v.
 # Target E after substitute c=(1-rb)/D; perhaps factor by equation kD equality, derive using vector equation.
 print(xyz,'constant 1-kD',1-k*D,'dirs b,d,bd',b,d,b*d)
