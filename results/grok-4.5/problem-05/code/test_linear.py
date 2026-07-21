import numpy as np

def check_ineq(c, num_samples=1000):
    """Check if f(x)=c*x satisfies the ineq for random x,y>0"""
    xs = np.random.uniform(0.01, 100, num_samples)
    ys = np.random.uniform(0.01, 100, num_samples)
    fxs = c * xs
    fys = c * ys
    left = np.sqrt((xs**2 + fys**2)/2)
    mid = (fxs + ys)/2
    right = np.sqrt(xs * fys)
    return np.all(left + 1e-9 >= mid) and np.all(mid + 1e-9 >= right)

for c in [0.5, 1.0, 1.2, 1.5, np.sqrt(2), 2.0]:
    print(c, check_ineq(c))
