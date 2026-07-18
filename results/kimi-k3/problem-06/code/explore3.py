"""Systematic study: eventual period, validity of a_{n+T}=a_n+L for ALL n, M_n boundedness."""
from math import gcd
from sympy import factorint
from explore1 import simulate_H, rad_primes, prod

def find_period(seq):
    """Find (T, L) such that a_{n+T} = a_n + L for a tail, using gap periodicity."""
    gaps = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(gaps)
    # find smallest T with gaps eventually periodic with period T dividing pattern
    half = N // 2
    for T in range(1, half):
        ok = True
        for i in range(N - T - 1, half - 1, -1):
            if gaps[i] != gaps[i + T]:
                ok = False
                break
        if ok:
            # L = sum of one period of gaps
            L = sum(gaps[N-T:N])
            return T, L
    return None, None

def check_all(seq, T, L):
    bad = []
    for n in range(len(seq) - T):
        if seq[n+T] != seq[n] + L:
            bad.append(n+1)  # 1-indexed
    return bad

def M_of(H):
    return min(prod(h) for h in H)

def run_case(a1, N=3000, quiet=True):
    seq, shrinks, H = simulate_H(a1, N)
    T, L = find_period(seq)
    if T is None:
        return dict(a1=a1, ok=False, msg="no period found", shrinks=len(shrinks))
    bad = check_all(seq, T, L)
    # M_n trajectory: recompute quickly
    return dict(a1=a1, ok=(len(bad)==0), T=T, L=L, bad=bad[:5],
                shrinks=len(shrinks), last_shrink=shrinks[-1] if shrinks else None,
                finalM=M_of(H), finalHsize=len(H))

if __name__ == "__main__":
    import sys
    cases = [2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,21,22,24,26,27,28,30,
             33,35,36,39,40,42,44,45,46,48,50,52,54,55,56,60,63,66,70,72,
             77,78,80,84,88,90,91,96,99,100,102,104,105,108,110,114,120,126,
             130,132,138,140,144,150,154,156,165,168,170,180,182,190,195,198,
             204,210,220,230,231,240,255,273,286,300,330,360,390,420,462,510,
             546,570,630,660,690,714,770,780,840,910,1001,1155,1230,1290,1386,
             1470,1710,1925,2002,2310,2431,2730,3003,3315,3990,4290,5005,6006]
    results = []
    for a1 in cases:
        r = run_case(a1, N=1500)
        results.append(r)
        flag = "OK " if r.get('ok') else "FAIL"
        if r.get('T'):
            print(f"{flag} a1={a1:6d} T={r['T']:4d} L={r['L']:8d} shrinks={r['shrinks']:4d} "
                  f"last={r['last_shrink']} finalM={r['finalM']} |H|={r['finalHsize']}")
        else:
            print(f"{flag} a1={a1}: {r}")
    nfail = sum(1 for r in results if not r.get('ok'))
    print(f"\n{nfail} failures out of {len(results)}")
