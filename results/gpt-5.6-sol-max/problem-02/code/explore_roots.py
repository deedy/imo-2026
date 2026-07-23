from math import *
def roots(A,x,th):
 # coefficients in q=cot t: 2sinA (sx q+cx)(s(th-x)q-c(th-x))-sin th(cP+q sP)=0
 aa=2*sin(A)*sin(x)*sin(th-x)
 bb=2*sin(A)*(cos(x)*sin(th-x)-sin(x)*cos(th-x))-sin(th)*sin(A+2*x)
 cc=-2*sin(A)*cos(x)*cos(th-x)-sin(th)*cos(A+2*x)
 D=bb*bb-4*aa*cc
 for q in [(-bb+sqrt(D))/(2*aa),(-bb-sqrt(D))/(2*aa)]:
  print('q',q,'t atan',degrees(atan2(1,q)),'q comparisons')
for A,x,th in [(60,10,70),(50,8,60),(80,12,40),(35,5,85)]:
 print('\n',A,x,th);roots(*map(radians,(A,x,th)))
