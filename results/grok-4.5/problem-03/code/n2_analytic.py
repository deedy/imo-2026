"""More careful evaluation for n=2 candidates with dense and smart XY placements."""
import numpy as np
from scipy.optimize import differential_evolution, minimize

def pieces_from(cuts):
    pts = np.unique(np.round(np.concatenate(([0.0], cuts, [1.0])), decimals=12))
    pts.sort()
    return np.diff(pts)

def lb_get(L):
    a = np.sort(L)[::-1]
    return float(a[0::2].sum())

def eval_fixed_xy(lb, ys):
    return lb_get(pieces_from(np.concatenate([lb, ys])))

def worst_over_xy_num(lb, n_xy=2):
    """Use differential evolution / multi-start to minimize LB share over XY cuts."""
    lb = np.asarray(lb, float)
    # empty
    best = eval_fixed_xy(lb, [])
    # 1 cut
    def obj1(y):
        y = y[0]
        if np.any(np.abs(y - lb) < 1e-9) or y<=0 or y>=1:
            return 1.0
        return eval_fixed_xy(lb, [y])
    res = differential_evolution(obj1, bounds=[(1e-6,1-1e-6)], popsize=20, mutation=0.7, recombination=0.7, seed=1)
    best = min(best, res.fun)
    # 2 cuts
    def obj2(z):
        y1,y2 = z
        if y1>y2:
            y1,y2=y2,y1
        if y2-y1 < 1e-9:
            return 1.0
        if np.any(np.abs(y1 - lb)<1e-9) or np.any(np.abs(y2-lb)<1e-9):
            return 1.0
        if y1<=0 or y2>=1:
            return 1.0
        return eval_fixed_xy(lb, [y1,y2])
    res2 = differential_evolution(obj2, bounds=[(1e-6,1-1e-6)]*2, popsize=25, seed=2, mutation=0.8)
    best = min(best, res2.fun)
    # also multi random start local
    for _ in range(40):
        z0 = np.sort(np.random.uniform(0.01,0.99,2))
        r = minimize(obj2, z0, method='Nelder-Mead')
        if r.fun < best:
            best = r.fun
    return best

def main():
    np.random.seed(0)
    cands = [
        [1/5,2/5],
        [0.2,0.4],
        [1/4,1/2],
        [1/3,2/3],
        [1/5,3/5],
        [2/5,4/5],
        [1/5,1/2],
        [1/4,3/4],
        [0.3,0.5],
        [1/6,1/3],
        [1/6,1/2],
        [1/7,2/7],
        [1/7,3/7],
        [2/7,4/7],
        [1/4,2/4],
        [3/8,5/8],
        [0.25,0.4],
        [0.28,0.42],
        [1/3,0.5],
        [0.15,0.35],
        [0.22,0.44],
        [1/5,2/5],
        [0.166,0.333],
        [0.2,0.5],
        [0.3,0.6],
    ]
    for c in cands:
        w = worst_over_xy_num(c)
        print(c, "->", w)

if __name__ == '__main__':
    main()
