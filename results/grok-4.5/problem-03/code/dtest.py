import numpy as np

def D(ls):
    a=np.sort([float(x) for x in ls if float(x)>1e-15])[::-1]
    s=0.0
    sign=1.0
    for x in a:
        s+=sign*float(x)
        sign=-sign
    return s

print(D([1,2,4]))
print(D([1,2,4,8]))
