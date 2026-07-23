import math
from math import sin,cos,pi
import sympy as s
# example
A=60*pi/180;B=70*pi/180;G=50*pi/180;x=10*pi/180
y=36.539361868763606*pi/180;z=22.15905911586103*pi/180
b=sin(B);c=sin(G);a=sin(A)
r=c/2*sin(z)/sin(x+z);d=b/2*sin(y)/sin(x+y)
R=2*r/c;D=2*d/b
mid=cos(A-x)-cos(x)*cos(A+2*x)
def eq(th,rho):return -rho*rho*sin(th)*sin(x)*sin(A+x)+rho*sin(th)*mid-2*sin(A)*sin(x)*sin(th-x)
print('r d R D',r,d,R,D,'constraints',eq(G,R),eq(B,D))
S=sin(A); C=cos(A);U=sin(x);X=cos(x);V=sin(A+x)
# coords
ks=c-r*V/S;kt=r*U/S;ls=d*U/S;lt=b-d*V/S
Q=lambda xx,yy:xx*xx+yy*yy+2*C*xx*yy
Rk=Q(ks,kt);Rl=Q(ls,lt);det=ks*lt-kt*ls
p=(Rk*lt-kt*Rl)/det;q=(ks*Rl-Rk*ls)/det
print('coords',ks,kt,ls,lt,'p q target',p,q,2*b*q-2*c*p-b*b+c*c)
print('omdiff',-c*p/2+b*q/2+(c*c-b*b)/4)
# Direct Cartesian compute circle to ensure geometry
K=(ks+kt*C,kt*S);L=(ls+lt*C,lt*S)
print('K,L',K,L)
# angle calculations helper
import numpy as np
# no numpy; hand cross dot angle
Apt=(0,0);Bp=(c,0);Cp=(b*C,b*S);Mp=(c/2,0);Np=(b*C/2,b*S/2)
def angle(P,Q,R):
 u=(P[0]-Q[0],P[1]-Q[1]);v=(R[0]-Q[0],R[1]-Q[1]);
 return math.degrees(math.acos(max(-1,min(1,(u[0]*v[0]+u[1]*v[1])/math.hypot(*u)/math.hypot(*v)))))
for name,tr in [('KBA',(K,Bp,Apt)),('ACL',(Apt,Cp,L)),('LBK',(L,Bp,K)),('LNC',(L,Np,Cp)),('LCK',(L,Cp,K)),('BMK',(Bp,Mp,K))]:print(name,angle(*tr))
