import math, cmath, numpy as np

def cross(a,b): return (a.conjugate()*b).imag

def solve(xd,yd,zd):
 x,y,z=map(math.radians,(xd,yd,zd))
 a=math.sin(x)/math.sin(x+z)
 b=math.sin(x)/math.sin(x+y)
 k=1+a*cmath.exp(1j*z)
 lam=1+b*cmath.exp(-1j*y)
 d=-cmath.exp(-1j*(x+y)) # L=2+T*d
 # w=(2+T*d)/lam; require (k-2w) parallel to w*exp(i(x+z))
 # cross(w*rot, k-2w)=0; quadratic
 rot=cmath.exp(1j*(x+z))
 def f(T):
  w=(2+T*d)/lam
  return cross(w*rot,k-2*w)
 vals=[f(0),f(1),f(2)]
 c=vals[0]; aa=(vals[2]-2*vals[1]+vals[0])/2; bb=vals[1]-c-aa
 roots=np.roots([aa,bb,c]) if abs(aa)>1e-10 else [-c/bb]
 print('angles',xd,yd,zd,'k',k,'quad',aa,bb,c,'roots',roots)
 for T in roots:
  if abs(T.imag if hasattr(T,'imag') else 0)<1e-8:
   T=float(np.real(T)); l=2+T*d; w=l/lam; C=2*w
   # line scalar k-2w = -U/r? direction w rot; scalar
   ratio=(k-2*w)/(w*rot)
   print(' T',T,'w',w,'alpha',math.degrees(cmath.phase(w)),'r',abs(w),'L',l,'CKratio',ratio)
   # center
   mat=np.array([[k.real,k.imag],[l.real,l.imag]])*2
   rhs=np.array([abs(k)**2,abs(l)**2])
   try:o=complex(*np.linalg.solve(mat,rhs))
   except:continue
   print(' center',o,'OM-ON',abs(o-1)-abs(o-w))
   pts={'A':0,'B':2,'C':C,'M':1,'N':w,'K':k,'L':l}
   # interesting angles/cyclic powers; determinants circles of quadruples maybe
   for pair in [('B','C'),('M','N')]: pass
   # distances
   for nm in ['BK','MK','CL','NL','KL','BL','CK','AL','AK']:
    P,Q=pts[nm[0]],pts[nm[1]]
    print(nm,abs(P-Q),end='; ')
   print()

for a in [(20,25,30),(10,15,20),(30,20,25),(15,35,25),(40,10,20)]: solve(*a)
