import random, itertools
from functools import lru_cache

def game_value(pieces):
    # returns first player's optimal total (both maximize own total)
    pieces = tuple(sorted(pieces, reverse=True))
    @lru_cache(maxsize=None)
    def val(rem):  # rem: tuple sorted desc; returns optimal total for player to move
        if not rem: return 0
        tot = sum(rem)
        best = -1
        for i in set(range(len(rem))):
            nxt = rem[:i] + rem[i+1:]
            # player gets rem[i] plus (tot - rem[i] - opponent's optimal on nxt)
            best = max(best, rem[i] + (tot - rem[i]) - val(nxt))
        return best
    return val(pieces)

random.seed(1)
for trial in range(300):
    m = random.randint(1, 8)
    pieces = [random.randint(1, 20) for _ in range(m)]
    v = game_value(pieces)
    s = sorted(pieces, reverse=True)
    odd = sum(s[0::2])
    assert v == odd, (pieces, v, odd)
print("Lemma A verified on 300 random multisets: value = odd-rank sum")
