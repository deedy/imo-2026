import random
import math

random.seed(2026)

def lhs(x, y, c):
    # f(t)=t+c
    return math.sqrt((x*x + (y+c)**2)/2)

def mid(x, y, c):
    return ((x+c)+y)/2

def rhs(x, y, c):
    return math.sqrt(x*(y+c))

# 1. Verify the proposed family numerically.
for c in [0.0, 0.17, 1.0, 2.73, 10.0]:
    for _ in range(10000):
        x = 10**random.uniform(-4, 4)
        y = 10**random.uniform(-4, 4)
        L = lhs(x, y, c)
        M = mid(x, y, c)
        R = rhs(x, y, c)
        assert L >= M - 1e-12, (c, x, y, L, M)
        assert M >= R - 1e-12, (c, x, y, M, R)

# 2. Verify the two algebraic identities used in the key mean estimate.
for _ in range(10000):
    x = 10**random.uniform(-6, 6)
    v = 10**random.uniform(-6, 6)
    N = x + v
    assert abs((N*N - (x-v)**2) - 4*x*v) < 1e-9 * max(1, N*N)
    assert abs((N*N + (x-v)**2) - 2*(x*x+v*v)) < 1e-9 * max(1, N*N)

# 3. Verify the quadratic forbidden-interval identity.
for _ in range(10000):
    c = random.uniform(0.1, 10.0)
    d = random.uniform(0.0, c)
    y = 10**random.uniform(-6, 6)
    X = 10**random.uniform(-6, 6)
    A = c + y
    s2 = 2*(c-d)*(c+d+2*y)
    Q = 2*(X*X + (y+d)**2) - (X+c+y)**2
    assert abs(Q - ((X-A)**2 - s2)) < 1e-8 * max(1, abs(Q), X*X)

# 4. Sanity check that a jump in the increment breaks the inequality.
# f(t)=t for t<=1, f(t)=t+1 for t>1 is injective and satisfies f(f(t))=2f(t)-t,
# but it must not satisfy the original inequality.
def f_jump(t):
    return t if t <= 1 else t + 1

x, y = 2.0, 1.0
L = math.sqrt((x*x + f_jump(y)**2)/2)
M = (f_jump(x)+y)/2
R = math.sqrt(x*f_jump(y))
assert not (L >= M >= R), (L, M, R)

print("all checks passed")
