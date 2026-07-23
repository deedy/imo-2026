# Minimal multivariate rational polynomial arithmetic using fractions.
# Goal: derive and reduce target identity in u,v over Q(X,Y,Z), eventually manually.
from fractions import Fraction

# Instead leverage C++? Print formulas and numerical checks only for now.
# Variables X,Y,Z,u,v. Constants:
# d=2(X+Z), e=2(X+Y)
# r=(X+2Z)/d,s=1/d,a=(X+2Y)/e,b=1/e
# lx=a*u+b*v, ly=a*v-b*u
# circle coefficients U,V via matrix [[r,s],[lx,ly]] [U,V]=[r2,l2].
# target F = 1-u2-v2+2U(u-1)+2Vv.
# Substitute linear B condition to seek factor.

import random, math

def calc(X,Y,Z,u,v):
 d=2*(X+Z); e=2*(X+Y)
 r=(X+2*Z)/d; s=1/d; a=(X+2*Y)/e; b=1/e
 lx=a*u+b*v; ly=a*v-b*u
 rr=r*r+s*s; ll=(a*a+b*b)*(u*u+v*v)
 det=r*ly-s*lx
 U=(rr*ly-s*ll)/det; V=(r*ll-rr*lx)/det
 F=1-u*u-v*v+2*U*(u-1)+2*V*v
 T=(X*Y-1)/(X+Y); W=(X*Z-1)/(X+Z)
 E1=a*u+b*v-1+T*(a*v-b*u)
 E2=u*u+v*v-u*r-v*s-W*(r*v-s*u)
 return F,E1,E2

if __name__=='__main__':
 for _ in range(5):
  q=[random.uniform(.5,5) for i in range(5)]
  print(calc(*q))
