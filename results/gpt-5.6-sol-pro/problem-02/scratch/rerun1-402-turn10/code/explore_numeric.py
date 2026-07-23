import cmath,math

def configuration(x,y,z):
    p=math.sin(z)/(2*math.sin(x+z))
    q=math.sin(y)/(2*math.sin(x+y))
    k=1-p*cmath.exp(-1j*x)
    D=1-q*cmath.exp(1j*x)
    E=cmath.exp(1j*(x+z))
    # Im ((tD-1)/(-exp(-i(x+y))))=0 for t=k/(1-vE).
    def f(v):
        t=k/(1-v*E)
        return ((t*D-1)/(-cmath.exp(-1j*(x+y)))).imag
    vals=[]
    n=10000; hi=10
    va=.0001; fa=f(va)
    for i in range(1,n+1):
      vb=.0001+(hi-.0001)*i/n; fb=f(vb)
      if fb*fa<0:
       a,b=va,vb
       for j in range(60):
        m=(a+b)/2
        if f(a)*f(m)<=0:b=m
        else:a=m
       v=(a+b)/2;t=k/(1-v*E)
       r=(t*D-1)/(-cmath.exp(-1j*(x+y)))
       if r.real>0 and t.imag>0 and v>0:
        vals.append((v,t,r.real))
      va,fa=vb,fb
    return k,D,vals

for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4),(.5,.2,.1)]:
 k,D,vals=configuration(*xyz)
 print('xyz',xyz,'solutions',vals)
 for v,t,r in vals:
  x,y,z=xyz
  P=2*k-1;L=t*D;Q=2*L-t
  print('C',t,'P',P,'Q',Q, 'angles ABC',cmath.phase((t-1)/(-1)), 'A',cmath.phase(t))

def cross(a,b):return (a.conjugate()*b).imag
def inside(p,a,b,c):
 vals=[cross(b-a,p-a),cross(c-b,p-b),cross(a-c,p-c)]
 return all(t>1e-8 for t in vals) or all(t< -1e-8 for t in vals)
print('inside tests')
for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4),(.5,.2,.1)]:
 k,D,vals=configuration(*xyz)
 for v,c,r in vals:
  l=c*D
  print(xyz, inside(k,1,.5,c),inside(l,1,c/2,c), 'P,Q',2*k-1,2*l-c)
