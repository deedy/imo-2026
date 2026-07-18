exec(open('code/grid.py').read().split('for n in range')[0])
for n in [1,2,3,4,5]:
 for M in [60,120]:
  candidates=[]
  # geometric first n positions scale t
  for t in range(1, M//(2**n)):
   L=tuple(t*(2**i-1) for i in range(1,n+1))
   worst=2; wa=None
   rem=[x for x in range(1,M) if x not in L]
   for j in range(n+1):
    for X in combinations(rem,j):
     v=val(tuple(sorted(L+X)),M)
     if v<worst:worst,wa=v,X
   candidates.append((worst,L,wa))
  print(n,M,max(candidates) if candidates else None)
  if n>=4 or M==120:break
