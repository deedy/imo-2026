"""Case analysis n=2: bins 1,2,4, total cuts <=2. Optimize splits to min LB-get."""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def lb_from_list(lengths):
    a = np.sort([l for l in lengths if l > 1e-14])[::-1]
    return a[0::2].sum()

def worst_split(bin_sizes, cuts_per_bin):
    """bin_sizes list, cuts_per_bin list same length. Each bin i split into c_i+1 positive parts summing to size."""
    # Parameterize each bin's parts by ordered positive fractions
    # Use differential evolution on break points
    dims = []
    for c in cuts_per_bin:
        dims.append(c)  # c break fractions in (0,1) sortedd
    
    total_cuts = sum(cuts_per_bin)
    if total_cuts == 0:
        return lb_from_list(bin_sizes), bin_sizes

    # Parameters: for each bin with c cuts, c numbers in [0,1] as ordered cum fractions
    bounds = []
    for c in cuts_per_bin:
        for _ in range(c):
            bounds.append((0.0,1.0))
    
    def obj(x):
        lengths = []
        idx=0
        for bi, (sz, c) in enumerate(zip(bin_sizes, cuts_per_bin)):
            if c==0:
                lengths.append(sz)
            else:
                fr = np.sort(x[idx:idx+c])
                idx+=c
                pts = np.concatenate(([0.0], fr, [1.0]))
                parts = np.diff(pts) * sz
                lengths.extend(parts.tolist())
        return lb_from_list(lengths)
    
    # multi start
    best = 999
    best_l = None
    rng = np.random.default_rng(42)
    # DE
    if bounds:
        res = differential_evolution(obj, bounds, popsize=30, seed=1, mutation=0.7, recombination=0.8, tol=1e-12)
        best = res.fun
        # reconstruct
        x=res.x
        lengths=[]
        idx=0
        for sz,c in zip(bin_sizes,cuts_per_bin):
            if c==0: lengths.append(sz)
            else:
                fr=np.sort(x[idx:idx+c]); idx+=c
            pts=np.concatenate(([0.],fr,[1.])) if c>0 else None
            if c>0: lengths.extend((np.diff(pts)*sz).tolist())
        best_l = lengths
    for trial in range(80):
        x0 = rng.uniform(0,1,len(bounds))
        r = minimize(obj, x0, method='Nelder-Mead', tol=1e-14)
        if r.fun < best - 1e-12:
            best = r.fun
            x=r.x
            lengths=[]
            idx=0
            for sz,c in zip(bin_sizes, cuts_per_bin):
                if c==0: lengths.append(sz)
                else:
                    fr=np.sort(np.clip(x[idx:idx+c],0,1)); idx+=c
                    pts=np.concatenate(([0.],fr,[1.]))
                    lengths.extend((np.diff(pts)*sz).tolist())
            best_l = lengths
    return best, best_l

def all_distributions(n_bins=3, max_cuts=2):
    # all nonnegative int vectors sum <= max_cuts
    from itertools import product
    res = []
    for tup in product(range(max_cuts+1), repeat=n_bins):
        if sum(tup) <= max_cuts:
            res.append(tup)
    return res

def main():
    bins = [1.0,2.0,4.0]
    dists = all_distributions(3,2)
    print("num dists", len(dists))
    overall = 999
    for d in dists:
        w, lens = worst_split(bins, d)
        print(d, "->", w, "lens example", None if lens is None else np.round(lens,4))
        overall = min(overall, w)
    print("OVERALL MIN", overall)

if __name__ == '__main__':
    main()
