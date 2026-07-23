import math

def factor_support(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0: n//=p
        p += 1 if p==2 else 2
    if n>1: out.append(n)
    return frozenset(out)

def run(start, N=10000):
    A=[start]
    for x in range(start+1,N+1):
        if all(math.gcd(x,a)>1 for a in A):
            A.append(x)
    return A

for s in range(2,31):
    A=run(s,5000)
    aset=set(A)
    per=None
    for L in range(1,1001):
        if all(((x in aset)==(x+L in aset)) for x in range(s,5001-L)):
            per=L; break
    supports=[]
    for a in A:
        S=factor_support(a)
        if not any(T <= S for T in supports):
            supports=[T for T in supports if not S<T]
            supports.append(S)
    print(s, 'period',per,'mins',sorted([tuple(sorted(x)) for x in supports],key=str))
