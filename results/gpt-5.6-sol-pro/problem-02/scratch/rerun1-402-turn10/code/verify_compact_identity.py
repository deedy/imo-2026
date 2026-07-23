import cmath, math, random

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
for case in range(10000):
    alpha=random.uniform(.02,1.2)
    beta=random.uniform(.02,math.pi-alpha-.02)
    gamma=random.uniform(.02,math.pi-alpha-.02)
    s=alpha+beta; r=alpha+gamma
    t=random.uniform(.02,3)
    k=1-math.sin(gamma)/(2*math.sin(r))*cmath.exp(-1j*alpha)
    g=1-math.sin(beta)/(2*math.sin(s))*cmath.exp(1j*alpha)
    l=1-t*cmath.exp(-1j*s)
    w=l/g
    rows=[[abs(k)**2,k,k.conjugate()],
          [abs(l)**2,l,l.conjugate()],
          [(1-abs(w)**2)/4,(1-w)/2,(1-w.conjugate())/2]]
    lhs=det3(rows)/1j
    h=((w-k)*w.conjugate()*cmath.exp(-1j*r)).imag
    rhs=math.sin(alpha)*(2*t*math.sin(alpha)+math.sin(beta))/(4*math.sin(s)*math.sin(r))*h
    if abs(lhs-rhs)>1e-8*(1+abs(lhs)+abs(rhs)):
        print('FAIL',alpha,beta,gamma,t,lhs,rhs,lhs/rhs if rhs else None)
        break
else:
    print('all compact identity tests passed')
