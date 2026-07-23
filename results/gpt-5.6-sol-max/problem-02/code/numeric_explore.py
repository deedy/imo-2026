import sympy as s
from math import sin,cos,tan,pi
# use sympy nsolve for y,z given alpha,beta,x
for vals in [(60,70,10),(50,60,8),(80,40,12),(35,85,5),(100,30,7)]:
    ad,bd,xd=vals; gd=180-ad-bd
    A,B,G,X=map(lambda q:q*pi/180,(ad,bd,gd,xd))
    Y,Z=s.symbols('Y Z')
    fy=sin(B)*s.sin(Y)*s.sin(A+2*X+Y)-2*sin(A)*s.sin(X+Y)*s.sin(B-X-Y)
    fz=sin(G)*s.sin(Z)*s.sin(A+2*X+Z)-2*sin(A)*s.sin(X+Z)*s.sin(G-X-Z)
    roots=[]
    for gy in [i*pi/180 for i in range(1,max(2,int(B*180/pi-X*180/pi)),3)]:
      try:
       yy=float(s.nsolve(fy,Y,gy))
       yy=(yy%pi)
       if 0<yy<B-X and all(abs(yy-r)>1e-7 for r in roots): roots.append(yy)
      except: pass
    rootsz=[]
    for gz in [i*pi/180 for i in range(1,max(2,int(G*180/pi-X*180/pi)),3)]:
      try:
       zz=float(s.nsolve(fz,Z,gz)); zz%=pi
       if 0<zz<G-X and all(abs(zz-r)>1e-7 for r in rootsz): rootsz.append(zz)
      except: pass
    print('A B G X',vals[0],vals[1],gd,vals[2], 'Yroots',[r*180/pi for r in roots], 'Zroots',[r*180/pi for r in rootsz])
    for yy in roots:
     for zz in rootsz:
      # sides circumdiameter 1
      b=sin(B); c=sin(G); a=sin(A)
      r=c/2*sin(zz)/sin(X+zz)
      d=b/2*sin(yy)/sin(X+yy)
      print(' y,z',yy*180/pi,zz*180/pi,'r,d',r,d,'tests',
            'y+z', (yy+zz)*180/pi,
            'd/r',d/r,
            'br-cr?', b*r-c*d,
            'br2?', b*d-c*r,
            'expr', b*c-2*b*r*cos(A+X)-2*c*d*cos(A+X))
