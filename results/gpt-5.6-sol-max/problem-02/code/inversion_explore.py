from math import *
examples=[(60,70,10,36.539361868763606,22.15905911586103),(50,60,8,25.773865378444977,31.95863942463148),(80,40,12,18.134582334730165,34.911143921228664),(35,85,5,31.89479519634615,20.810624802116656),(100,30,7,15.156547215431676,32.56710477157553)]
for av,bv,xv,yv,zv in examples:
 g=180-av-bv; A,B,x,y,z=map(radians,(av,bv,xv,yv,zv));G=radians(g); b=sin(B);c=sin(G)
 R=sin(z)/sin(x+z);D=sin(y)/sin(x+y)
 k=c*(1-R/2*complex(cos(x),-sin(x)))
 l=b*complex(cos(A),sin(A))*(1-D/2*complex(cos(x),sin(x)))
 ki=1/k.conjugate();li=1/l.conjugate()
 if abs(c*c-b*b)>1e-10:
  w=2*(c-b*complex(cos(A),sin(A)))/(c*c-b*b)
  lam=((w-li)/(ki-li)).real
  print('R,D',R,D,'lambda',lam,'imag',((w-li)/(ki-li)).imag,
        'candidates',{'R/2':R/2,'D/2':D/2,'(2-R)':2-R,'ratio':R*(2-D)/(R*(2-D)+D*(2-R)),'RD':R*D/4,
        'normK':abs(k)**2/c**2,'normL':abs(l)**2/b**2})
