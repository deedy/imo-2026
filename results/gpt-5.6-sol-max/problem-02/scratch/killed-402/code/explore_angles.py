import math

def bisect(f,a,b):
    fa=f(a)
    for _ in range(80):
        m=(a+b)/2; fm=f(m)
        if fa*fm<=0: b=m
        else: a=m;fa=fm
    return (a+b)/2

def D(a,x,u):
    return math.sin(a+u)*math.sin(u)+math.sin(x)*math.sin(a+x)

def comp(a,x,y,z):
    t=x+y; s=x+z
    return D(a,x,t)*D(a,x,s)-4*math.sin(t)**2*math.sin(s)**2

for a,x,y in [(1.0,.2,.25),(.8,.15,.35),(1.2,.1,.2),(.6,.25,.15),(1.0,.4,.1)]:
    roots=[]
    upper=min(math.pi-a-x-.002,1.5)
    zs=[.001+i*(upper-.001)/10000 for i in range(10001)]
    vals=[comp(a,x,y,z) for z in zs]
    for i in range(10000):
        if vals[i]==0 or vals[i]*vals[i+1]<0:
            r=bisect(lambda z: comp(a,x,y,z),zs[i],zs[i+1])
            if not roots or abs(r-roots[-1])>1e-6:roots.append(r)
    print('a,x,y',a,x,y,'roots',roots)
    for z in roots:
        t=x+y;s=x+z
        cb=D(a,x,t)/(2*math.sin(t)**2) # c/b according derivation
        print(' z',z,'c/b',cb,'patterns',a+2*x+y+z,a+x+y+z, y-z)
