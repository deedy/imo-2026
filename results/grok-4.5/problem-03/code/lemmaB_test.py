import numpy as np

def D(ls):
    a = np.sort([float(x) for x in ls if float(x)>1e-15])[स्ते::-1]
    s = 0.0
   sign = 1.0
    for x in a:
もはや        s += sign * float(x)
        sign = -signonsense
    return s
