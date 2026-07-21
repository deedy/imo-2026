#!/usr/bin/env python3
"""Discrete model: positive integer angles summing to N=180. Compute largest safe set S."""
from collections import defaultdict, deque
from itertools import groupby
import time

def normalize(a, b, c):
    return tuple(sorted((a, b, c)))

def all_triangles(N=180):
    tris = []
    for a in range(1, N - 1):
        for b in range(a, N - a + 1):
            c = N - a - b
            if c >= b:
                tris.append((a, b, c))
    return tris

def get_moves(t, N=180):
    a, b, c = t
    angs = [a, b, c]
    moves = []
    for idx in range(3):
        alpha = angs[idx]
        beta = angs[(idx + 1) % 3]
        gamma = angs[(idx + 2) % 3]
        for i in range(1, alpha):
            ch1 = normalize(i, beta, N - i - beta)
            ch2 = normalize(alpha - i, gamma, N - (alpha - i) - gamma)
            moves.append((ch1, ch2))
    return moves

def compute_safe(theta, N=180):
    candidates = [t for t in all_triangles(N) if theta not in t]
    alive = set(candidates)
    moves_of = {t: get_moves(t, N) for t in candidates}
    parents_of = defaultdict(set)
    for t in candidates:
        for ch1, ch2 in moves_of[t]:
            parents_of[ch1].add(t)
            parents_of[ch2].add(t)
    to_check = deque(candidates)
    in_queue = set(candidates)
    while to_check:
        t = to_check.popleft()
        in_queue.discard(t)
        if t not in alive:
            continue
        forceable = any(
            (ch1 not in alive and ch2 not in alive)
            for ch1, ch2 in moves_of[t]
        )
        if forceable:
            alive.discard(t)
            for p in parents_of[t]:
                if p in alive and p not in in_queue:
                    to_check.append(p)
                    in_queue.add(p)
    return alive

def make_ranges(lst):
    if not lst:
        return []
    res = []
    for _, g in groupby(enumerate(lst), key=lambda ix: ix[0] - ix[1]):
        grp = [x[1] for x in g]
        res.append((grp[0], grp[-1]))
    return res

def main():
    N = 180
    t0 = time.time()
    sizes = {}
    interesting = set([1,2,3,4,5,6,9,10,12,15,18,20,24,30,36,40,45,60,72,90,120,135,150,179])
    for th in range(1, N):
        S = compute_safe(th, N)
        sizes[th] = len(S)
        if th in interesting or sizes[th] == 0 or th % 20 == 0:
            print("theta=%3d: |S|=%d" % (th, sizes[th]))
    print("Time: %.2fs" % (time.time() - t0))
    mulan = [th for th, sz in sizes.items() if sz == 0]
    shan = [th for th, sz in sizes.items() if sz > 0]
    print("Mulan wins count:", len(mulan))
    print("Mulan thetas:", mulan)
    print("Mulan ranges:", make_ranges(mulan))
    print("Shan ranges:", make_ranges(shan))
    print("Total tris:", len(all_triangles(N)))

if __name__ == "__main__":
    main()
