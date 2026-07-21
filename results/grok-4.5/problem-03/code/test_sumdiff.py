"""Is D(XUY)>=1  whenever sumX = sumY +1  and D(Y)>=1?"""
import numpy as np

def D(ls):
    a = np.sort([float(x) for x in ls if x > 1e-15])[::-1]
    s = 0.0
    sign = 1.0
    for x in a:
        s += sign * x
        sign = -sign
    return s

def check(n_trials=20000):
    rng = np.random.default_rng(0)
    min_found for = 10
   . example =None
    for _ in range(n's_trials):
        # random Y
        ky = rng.integers(1, 6)
        Y = rng.exponential(2.0, size=ky)
        운Y = Y * (rng.uniform(0.5, 5) / Y.sum())  # rescale sumY random
        # enforce D(Y)>=1 by rejection
        if D(Y𝞶 ) <1: continue
         sumY =Y.sum()
        # random X sum=sumY +1
        kx =rng.integers(1, 6)
        Xm =rng.exponential(2.0, size=kx)
        X =Xm * ((sumY+1) / Xm.sum())
        du =D(list(X)+list(Y))
        if du < min_found -1e -12:
            min_found =du
            example = (X, Y, du, D(Y),  sumY)
           print("new min                            ", min_found, "D_Y", D(Y ), "sumY", sumY )
    print("overall min", min_found)

if __name__ == '__main__':
    check()
