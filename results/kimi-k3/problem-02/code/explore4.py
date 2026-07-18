import numpy as np
from explore import run, ang, dirv, intersect, circumcircle, power, cross2

def explore(Adeg, Bdeg, phi_deg):
    res = run(Adeg, Bdeg, phi_deg, verbose=False)
    r = res[0]
    Ap,Bp,Cp,M,N,K,L = r['A'],r['B'],r['C'],r['M'],r['N'],r['K'],r['L']
    beta,gamma,phi = np.degrees(r['beta']),np.degrees(r['gamma']),np.degrees(r['phi'])
    print(f"=== A={Adeg},B={Bdeg},C={180-Adeg-Bdeg}; phi={phi_deg:.3f} beta={beta:.4f} gamma={gamma:.4f}")
    print(f"  angle LKC = {ang(L,K,Cp):.4f}   angle KLC = {ang(K,L,Cp):.4f}")
    print(f"  angle BKL = {ang(Bp,K,L):.4f}   angle BLK = {ang(Bp,L,K):.4f}")
    print(f"  angle MKL = {ang(M,K,L):.4f}   angle MLK = {ang(M,L,K):.4f}")
    print(f"  angle NKL = {ang(N,K,L):.4f}   angle NLK = {ang(N,L,K):.4f}")
    print(f"  angle BKM = {ang(Bp,K,M):.4f}   angle CLN = {ang(Cp,L,N):.4f}")
    print(f"  angle BKC = {ang(Bp,K,Cp):.4f}   angle BLC = {ang(Bp,L,Cp):.4f}")
    print(f"  angle MKC = {ang(M,K,Cp):.4f}   angle NLB = {ang(N,L,Bp):.4f}")
    print(f"  angle MKN = {ang(M,K,N):.4f}   angle NLM = {ang(N,L,M):.4f}")
    print(f"  angle KMN = {ang(K,M,N):.4f}   angle LNM = {ang(L,N,M):.4f}")
    print(f"  angle MNL = {ang(M,N,L):.4f}   angle NMK = {ang(N,M,K):.4f}")
    print(f"  sums: LKC+KLC+LCK = {ang(L,K,Cp)+ang(K,L,Cp)+gamma:.4f}")
    print()

if __name__ == "__main__":
    explore(70,60,12)
    explore(60,70,12)
    explore(75,65,10)
