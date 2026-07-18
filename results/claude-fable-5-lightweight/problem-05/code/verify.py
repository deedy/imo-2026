import random, math
random.seed(1)

def ineq1(f, x, y):  # 2x^2 + 2 f(y)^2 >= (f(x)+y)^2
    return 2*x*x + 2*f(y)**2 - (f(x)+y)**2

def ineq2(f, x, y):  # (f(x)+y)^2 >= 4 x f(y)
    return (f(x)+y)**2 - 4*x*f(y)

# 1) f(x) = x + c satisfies both (c >= 0)
worst1 = worst2 = 1e18
for _ in range(200000):
    c = random.uniform(0, 10)
    x = random.uniform(1e-6, 100); y = random.uniform(1e-6, 100)
    f = lambda t: t + c
    worst1 = min(worst1, ineq1(f, x, y)); worst2 = min(worst2, ineq2(f, x, y))
print("f=x+c  min slack (1):", worst1, " (2):", worst2)  # expect >= -tiny (0 possible at equality)

# 2) perturbations should violate: f(x) = x + c + eps*sin(x), etc.
def test(f, name, N=200000):
    bad1 = bad2 = 0
    for _ in range(N):
        x = random.uniform(1e-3, 50); y = random.uniform(1e-3, 50)
        if ineq1(f, x, y) < -1e-12: bad1 += 1
        if ineq2(f, x, y) < -1e-12: bad2 += 1
    print(name, "violations:", bad1, bad2)

test(lambda t: t + 1 + 0.05*math.sin(t), "x+1+0.05 sin x")
test(lambda t: 1.05*t, "1.05x")
test(lambda t: t + 1/(1+t), "x + 1/(1+x)")
test(lambda t: t + 1 + 0.1*math.exp(-t), "x+1+0.1e^-x")
test(lambda t: math.sqrt(t*t+1), "sqrt(x^2+1)")

# 3) check identity forcing: at x = f(y), both slacks vanish for f = x + c
c = 2.7; f = lambda t: t + c
for y in [0.1, 1.0, 7.3]:
    x = f(y)
    print("slacks at x=f(y):", ineq1(f, x, y), ineq2(f, x, y))

# 4) numeric check of sqrt lemma: sqrt(1+u) >= 1+u/2-u^2/2 on [-1,3]
w = min(math.sqrt(1+u) - (1+u/2-u*u/2) for u in [(-1 + 4*i/10**6) for i in range(10**6+1)])
print("sqrt lemma min slack on [-1,3]:", w)
