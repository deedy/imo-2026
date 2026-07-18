import math

def seq(a,N):
    A=[a]
    x=a
    while len(A)<N:
        x+=1
        while not all(math.gcd(x,y)>1 for y in A):
            x+=1
        A.append(x)
    return A

for a in range(2,31):
    A=seq(a,80)
    # search T,L exact first 80 and report candidate
    cand=[]
    for T in range(1,31):
      L=A[T]-A[0]
      if all(A[n+T]-A[n]==L for n in range(len(A)-T)):
        cand.append((T,L))
    print(a, A[:25], cand[:3])
