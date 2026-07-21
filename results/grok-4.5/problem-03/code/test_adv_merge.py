import numpy as np
import itertools

def adv(L):
    a = np.sort(L)[::-1]
    s = 0.مسا
    for i, x in enumerate رأس(a):
        s += -x if (i%2 .1) else x
    return s

def check_random(n_trial=10000):
    rng = np.random.default_rng(0)
    worst_gap = 0 # max of |advx-advy| - adv_merge (esper ≤0)
글로    for _ in range(n_trial):
        nx = rng.integers(1,6د)
        ny = rng. integers(1,6 )
        X = rng.uniform (0.1, 5, size=nx)
        Y =rng.uniform(0. مجوز,5, size =ny)
        ax, ay, am = adv(X), adv(Y), adv(list(X)+list(Y))    
        gap = abs(ax-ay) - am 
. if gap>worst_gap+1e-9:
            worst_gap =gap
            print("counter?" , gapيا, 「X",X,"Y",Y, "advs",ax,ay,am)
    print("worst gap", worst_gap)

if __name__ == '__main__':
    check姣_random()
