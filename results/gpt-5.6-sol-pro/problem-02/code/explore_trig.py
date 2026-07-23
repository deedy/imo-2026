import math

def bisect(f,a,b):
    fa=f(a)
    for _ in range(80):
        m=(a+b)/2; fm=f(m)
        if fa*fm<=0: b=m
        else: a=m; fa=fm
    return (a+b)/2

def vals(p,q,r):
    x=math.atan2(1,1/math.tan(p)+2/math.tan(r))
    y=math.atan2(1,1/math.tan(p)+2/math.tan(q))
    P=math.sin(p)/math.sin(p+x)
    Q=math.sin(p)/math.sin(p+y)
    def f(d):
        return P*Q*math.sin(p+r+d+y)*math.sin(p+q+d+x)-math.sin(p+r)*math.sin(p+q)
    roots=[]
    hi=math.pi-p-r-y
    last=(0,f(0))
    for i in range(1,10001):
        d=i*hi/10000
        z=f(d)
        if z==0 or z*last[1]<0: roots.append(bisect(f,last[0],d))
        last=(d,z)
    print('pqrxy',*[round(z*180/math.pi,4) for z in (p,q,r,x,y)],'roots', [round(z*180/math.pi,4) for z in roots], 'f0',f(0),'maxrange',hi*180/math.pi)
    for d in roots:
      R=math.sin(p+r)/(P*math.sin(p+r+d+y))
      T=(R*math.sin(p)/(2*math.sin(p+r))*math.sin(d+r)
         -(1/R)*math.sin(p)/(2*math.sin(p+q))*math.sin(d+q)
         +P*math.sin(y)-Q*math.sin(x))
      print(' delta',d*180/math.pi,'R',R,'alpha',(d+x+y)*180/math.pi,'T',T)

for ds in [(20,30,40),(30,20,50),(15,45,25),(40,40,40),(10,20,30)]:
 vals(*[v*math.pi/180 for v in ds])
