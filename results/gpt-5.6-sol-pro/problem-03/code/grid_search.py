"""Exact integer-grid brute force for conjecture generation (not part of proof)."""
from functools import lru_cache
from itertools import combinations_with_replacement
import sys

def parts_int(a,r):
    """Ordered positive compositions into r parts (internal order irrelevant for D, use sorted)."""
    if r==1:
        yield (a,); return
    # unordered positive partitions suffice because only resulting multiset matters
    def rec(rem,k,lo,pref):
      if k==0:
        if rem==0: yield tuple(pref)
        return
      for x in range(lo, rem//k+1):
        yield from rec(rem-x,k-1,x,pref+[x])
    yield from rec(a,r,1,[])

@lru_cache(None)
def refinements(a,maxcuts):
    out=[]
    for k in range(maxcuts+1):
      for p in parts_int(a,k+1):out.append((k,p))
    return out

def D(ps):
    q=sorted(ps,reverse=True)
    return sum(q[::2])-sum(q[1::2])

def inner(a,n):
    best=(sum(a),None)
    def rec(i,left,ps,desc):
      nonlocal best
      if i==len(a):
        val=D(ps)
        if val<best[0]:best=(val,desc)
        return
      for k,p in refinements(a[i],left):
        rec(i+1,left-k,ps+p,desc+(p,))
    rec(0,n,(),())
    return best

def partitions(total,k,lo=1):
    if k==1:
      if total>=lo:yield (total,)
      return
    for x in range(lo,total//k+1):
      for r in partitions(total-x,k-1,x):yield (x,)+r

def search(n,M):
    best=(-1,None,None)
    counts=0
    for a in partitions(M,n+1):
      val,ref=inner(a,n);counts+=1
      if val>best[0]:
        best=(val,a,ref);print('best',best,'ratio D',val/M,flush=True)
    print('FINAL n M count',n,M,counts,best,'c',(1+best[0]/M)/2)

if __name__=='__main__': search(int(sys.argv[1]),int(sys.argv[2]))
