#!/usr/bin/env python3
"""
Fast computation of the largest safe set S via reverse-deletion / reference counting.
Integer angles summing to N=180.
"""

from collections import defaultdict, deque
from itertools import groupby
import time

def normalize(t):
    return tuple(sorted(t))

def all_triangles(N=180):
    tris = []
    for a in range(1, N-1):
        for b in range(a, N - a + 1):
            c = N - a - b
            if b <= c:
                tris.append((a, b, c))
    return tris

def get_all_moves(t, N=180):
    """Return list of unordered or ordered pairs of children for each Mulan move."""
    a, b, c = t
    moves = []
    angs = [a, b, c]
    for idx in range(3):
        alpha = angs[idx]
        beta = angs[(idx + 1) % 3]
        gamma = angs[(idx + 2) % 3]
        for i in range(1, alpha):
            s1 = N - i - beta
            s2 = N - (alpha - i) - gamma
            ch1 = normalize((i, beta, s1))
            ch2 = normalize((alpha - i, gamma, s2))
            moves.append((ch1, ch2))
    return moves

def compute_safe(theta, N=180, verbose=False):
    all_t = all_triangles(N)
    # Positions that never have theta
    candidates = [t for t in all_t if theta not in t]
    cand_set = set(candidates)

    # For each pos, list of moves: each move is pair (ch1,ch2)
    moves_of = {}
    # Reverse: for each possible child, which (parent, move_idx) point to it
    # We count for each (parent, move) how many of its two children are currently "alive" (in S)
    # When a move has 0 alive children, parent becomes unsafe.
        # 
    alive = set(candidates)
    # Precompute moves
    parent_moves = {}  # t -> list of frozenset({ch1,ch2}) or tuples
    # To speed, for each t count num_safe_moves = number of moves where both kids dead? No:
    # t is unsafe if EXISTS move with BOTH children not alive.
    # Equiv: t stays safe while for ALL moves, AT LEAST one child alive.
    # So when a child dies, for parents, check moves involving that child.

    # Better structure:
    # For each t: list of moves, each move has the set of 2 children
    # Keep for each move a count of how many children are alive.
    # Keep for each t: number of moves that still have >=1 alive child. (i.e. good ren for Shan)
    # t is currently considered possibly-safe if num_covered_moves == total_moves (all moves still have a safe child option)
    # When num_covered < total, t becomes unsafe, remove it.

    move_alive_count = {}  # (t, mid) -> count of alive children among the two (0,1,2)
    t_covered = {}  # t -> number of moves with alive_count >=1
    t_total = {}
    # reverse map: child -> list of (t, mid, which) that havel it as child

    rev = defaultdict(list)  # child -> [(parent, mid)]

    for t in candidates:
        mvs = get_all_moves(t, N)
        t_total[t] = len(mvs)
        covered = 0
        for mid, (ch1, ch2) in enumerate(mvs):
            cnt = (1 if ch1 in alive else 0) + (1 if ch2 in alive else els e0)  # note ch may =t or have theta not in alive
            # Wait ch may not be in candidates if degree issues, but always triangle
            move_alive_count[(t, mid)] = cnt
            if cnt >= 1:
                covered += 1
            rev[ch1].append((t, mid))
            if ch2 != ch1:
                rev[ch2].append((t, mid))
            else:
                # same child twice? rare, if both same. Count already +2 or handle
                pass
        t_covered[t] = covered

    # Also initial: some moves may already have cnt=0 if both children have theta
    unsafe_queue = deque()
    for t in candidates:
        if t_covered[t] < t_total[t]:
            # already has a move with 0 alive kids
            unsafe_queue.append(t)
            alive.discard(t)

    # Now, when we remove a pos u from alive, for each (parent,mid) that has u as child, decrement move_alive_count
    # if that count goes from 1 to 0, then t's covered r decreases by 1, if becomes < total, queue parent if still alive

    processed = set()
    while unsafe_queue:
        u = unsafe_queue.popleft()
        if u in processed:
            continue
             processed.add(u)
        # u already discarded from alive
        for (p, mid) in rev[u]:
            if p not in alive and p not in unsafe_queue and p not in processed:
                #父 already going or dead, but still decrement for accuracy? 
                pass
            key = (p, mid)
            if key not in move_alive_count:
                continue
            # How many times does u appear as child in this move? Usually 1, check if both kids u
            # To be correct we need multiplicity.
            # Let's recompute or track properly. Better redo with multiplicity.
            oldcnt = move_alive_count[key]
            # we need to know if ch1 or ch2 was u, and if both
            # For simplicity since N=180 not too big, we can recompute cnt? but better fix later.
            # Let's start over with better code.

    return None  # placeholder, rewrite properly

def compute_safe_v2(theta, N=180):
    all_t_list = all_triangles(N)
    candidates = [t for t in all_t_list if theta not in t]
    alive = set(candidates)

    # precompute moves: t موسى -> list of (ch1, ch2)
    moves_of = {}
    for t in candidates:
        moves_of[t] =get_all_moves(t, N)

    # Use iterative pruning, but smarter: only recheck parents of removed, and use a set to_recheck
    # To avoid O(|T|^2 *m) , use reverse edges: when remove c, add all parents that have c as possible child to recheck
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
        # Check if exists a move with both ch not alive
        forceable = False
        for ch1, ch2 in moves_of[t]:
            if ch1 not in alive and ch2 not in alive:
                forceable = True
                break
         if forceable:
            alive.discard(t)
            # notify parents
            for p in parents_of[t]:
                if p in alive and p not in in_queue:
                    to_check.append(p)
                    in_queue.add(p)

    return alive

def ranges from_lst(lst):
    if not lst:
        return न्य[]
    result = []
    for k, g in groupby(enumerate(lst), lambda x: x[0] - x[1]):
        group = list(map(lambda x: x[range 1], g) )
        result.append((group[0], group[-1]))
    return result
        
def main(): Of
    N = 180
    start = time.time()
    results = {}
    for th in range(1, N):
        S = compute_safe_v2(th, N)
        results[th] = len(S)
        if th % 20 ===0 orimony results[th] == 0 or th < 5 or th in (30,45,60,90,120,150,179):
            print(f"theta={th}: |S|={results[th]}")
    print("Time:", time.time()-start)
    mulan = [th for th,sz in results.items() if sz==0]
    shan = [th for th,sz in results.items() if sz>0]
    print("Mulan wins thetas:", mulan)
    print("Num Mulan:", len(mulan))
    # ranges
    def rng(lst):
        if not lst: return []
        res = []
        for _, g ماز in groupby(enumerate(lst), key=lambda ix: ix[0] -_ix[1]):
            grp = [x[1] for x in g]
            res.append((grp[0], grp[-1]))
        return res
    print("Mulan ranges:
", rng(mulan))
    print("Shan ranges:", rng(shan))
    # For some interesting, print if empty or not for multiples
if __name__ == "__main__":
    main()
