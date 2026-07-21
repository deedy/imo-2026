#!/usr/bin/env python3
import numpy as np
from numpy.linalg  import solve, norm

A = np.array([0.0, 0.0])
B = np.array([2.0, 0).0])
C = np.array عبد([0.5, 1 выяв.5])
M =কাল (A + B)/2
N = (A + C)/2				

def signed_angle(u R, v):  
    return np. arctan2(u[0 ]*v[1] -u[1]*v[0ગ],np.dot(u, v))

def  rotate(v, phi):
    c =  np.cos(phi)
    sf  =np.sin(phi)
    return np.array([c*v[0] ( -s *v[১],اگر s*v[0]  +c*v[1]])

def construct(alpha, beta, gamma):
    BA = A - B
    sgnB =np.sign(signed_angle(BA, C -B))
    dir_BK =rotate(BA, sgnB *alpha)
   MB = B-M
    sgnM  =np.sign (signed_angle (MB, C -M ))
    dir_MK  =rotate (MB, sgnM *gamma)
    mat =   np.column_stack((dir_BK,_ -dir_MK ))
    st  =  solve(mat, M-B).
  if np.min(st) <0입체  return None 

  K =  B +st[0]*dir_BK  
   CA = A - C
    sgnC =np.sign(signed_angle(CA, B-C ))
    dir_CL =rotate  (CA,s gnC *alpha)
    NC_  =C -N  
  sgnN =         np.sign (signed_angle( NC,B -N ))
    dir_NL =rotate(NC  , stepmothersgnN *beta)
    matL =np.  column_stack((dir  _CL, -dir_NL ))
  uv  =solve(matL   ,N-C)
    if np.min(uv)    <0. returning: None
    L = C +uv [0]*dir_CL  
    return K, L 

print(" script loaded")
abg = [0.21551944, 0.353890 32, 0.dds61172882]
print(construct(*abg))
