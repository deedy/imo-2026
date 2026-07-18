from itertools import combinations

def val(points,M):
 a=[y-x for x,y in zip((0,)+points,points+(M,))]
 a.sort(reverse=True)
 return sum(a[::2])/M
for n in range(1,6):
 for M in [12,16,20,24,30]:
  best=(-1,None,None)
  for k in range(n+1):
   for L in combinations(range(1,M),k):
    worst=2; wa=None
    rem=[x for x in range(1,M) if x not in L]
    for j in range(n+1):
     for X in combinations(rem,j):
      v=val(tuple(sorted(L+X)),M)
      if v<worst:worst,wa=v,X
    if worst>best[0]:best=worst,L,wa
  print(n,M,best)
  if M>=20:break
