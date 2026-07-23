# inspect solved examples for simple formulas involving R,D and angles
from math import *
examples=[(60,70,10,36.539361868763606,22.15905911586103),(50,60,8,25.773865378444977,31.95863942463148),(80,40,12,18.134582334730165,34.911143921228664),(35,85,5,31.89479519634615,20.810624802116656),(100,30,7,15.156547215431676,32.56710477157553)]
for A,B,x,y,z in examples:
 G=180-A-B; A,B,G,x,y,z=map(radians,(A,B,G,x,y,z));b=sin(B);c=sin(G)
 R=sin(z)/sin(x+z);D=sin(y)/sin(x+y)
 print('\nangles',*[round(degrees(v),3) for v in (A,B,G,x,y,z)],'R,D',R,D)
 vals={
 'R+D':R+D,'RD':R*D,'(1-RX)':1-R*cos(x),'(1-DX)':1-D*cos(x),
 '(2-R)/(2-D)':(2-R)/(2-D),'R(2-D)/D(2-R)':R*(2-D)/(D*(2-R)),
 'b/c':b/c,'tan ratios z/y':tan(z)/tan(y),'sin(x+y/z)':sin(x+y)/sin(x+z),
 'cotz+cot?':1/tan(z)+1/tan(y),
 'cross':(R-D)/(b-c),'prodscaled':R*D*b*c/(sin(A)**2),
 }
 for k,v in vals.items():print(k,round(v,8),end='; ')
 print()
