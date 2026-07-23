exec(open('code/explore_numeric.py').read().split("print('inside tests')")[0])
import cmath,math

def angle(u,v):return abs(cmath.phase(v/u))
def phase(z):return cmath.phase(z)
for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4)]:
 x,y,z=xyz;k,D,vals=configuration(*xyz)
 for v,c,r in vals:
  l=c*D;m=.5;n=c/2
  # circle center solve via determinant
  det=(k.conjugate()*l).imag
  # ux*kx+uy*ky=|k|2/2 etc
  ux=(abs(k)**2*l.imag-abs(l)**2*k.imag)/(2*det)
  uy=(k.real*abs(l)**2-l.real*abs(k)**2)/(2*det)
  o=ux+1j*uy
  print('\nxyz',xyz,'branch c',c,'O',o)
  seg={'AK':k,'AL':l,'KL':l-k,'MN':(c-1)/2,'OM':m-o,'ON':n-o,'BC':c-1,
  'BM':-.5,'BK':k-1,'BL':l-1,'CN':-c/2,'CL':l-c,'CK':k-c}
  for aa,bb in [('OM','ON'),('KL','MN'),('AK','BC'),('AL','BC'),('OM','AK'),('ON','AL'),('OM','BK'),('ON','CL')]:
   print(aa,bb,'angle',phase(seg[bb]/seg[aa]),'ratio',abs(seg[bb]/seg[aa]))
