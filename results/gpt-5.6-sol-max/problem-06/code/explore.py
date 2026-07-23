import math

def factorint(n):
    d=2; z={}
    while d*d<=n:
        while n%d==0: z[d]=z.get(d,0)+1; n//=d
        d+=1
    if n>1:z[n]=1
    return z

def seq(a1,N):
    A=[a1]
    x=a1
    while len(A)<N:
        x+=1
        while not all(math.gcd(x,a)>1 for a in A):
            x+=1
        A.append(x)
    return A

for a in range(2,31):
    A=seq(a,100)
    per=[]
    for T in range(1,50):
        vals={A[i+T]-A[i] for i in range(len(A)-T)}
        if len(vals)==1: per.append((T,vals.pop()))
    print(a,A[:20], 'factors',[factorint(x) for x in A[:8]], 'period',per[:1])
