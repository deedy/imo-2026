from fractions import Fraction

def canon(s): return tuple(sorted(s))

def solve(q,p):
    states={canon((a,b,q-a-b)) for a in range(1,q) for b in range(1,q-a)}
    W={s for s in states if p in s}
    ranks={s:0 for s in W}
    changed=True; r=0
    while changed:
        changed=False; r+=1
        for s in states-W:
            # choose a distinguished coordinate index (handle values)
            arr=list(s)
            ok=False
            for i,a in enumerate(arr):
                b=arr[(i+1)%3]; c=arr[(i+2)%3]
                for x in range(1,a):
                    s1=canon((b,x,q-b-x))
                    s2=canon((c,a-x,b+x))
                    if s1 in W and s2 in W:
                        ok=True; break
                if ok: break
            if ok:
                W.add(s); ranks[s]=r; changed=True
        # iteration simultaneous issue currently additions in same scan; still closure, ranks loose
    return states,W,ranks

for q in range(2,21):
    row=[]
    for p in range(1,q):
        S,W,R=solve(q,p)
        if W==S: row.append(p)
    print(q,row)
