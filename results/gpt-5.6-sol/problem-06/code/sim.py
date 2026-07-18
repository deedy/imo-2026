import math

def seq(a,N):
 A=[a]
 for _ in range(N-1):
  x=A[-1]+1
  while not all(math.gcd(x,y)>1 for y in A): x+=1
  A.append(x)
 return A
for a in range(2,31):
 A=seq(a,300)
 ds=[A[i+1]-A[i] for i in range(len(A)-1)]
 # find eventual small period diff
 found=None
 for st in range(100):
  for T in range(1,50):
   if all(ds[i]==ds[i+T] for i in range(st,len(ds)-T)):
    found=(st,T,sum(ds[st:st+T]));break
  if found:break
 print(a,A[:15],found, A[-1])
