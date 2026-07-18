import random, math

# 1) verify f(x)=x+c satisfies both inequalities
random.seed(1)
bad = 0
for _ in range(200000):
    c = random.uniform(0, 10)
    x = random.uniform(1e-3, 100)
    y = random.uniform(1e-3, 100)
    f = lambda t: t + c
    lhs = math.sqrt((x*x + f(y)**2)/2)
    mid = (f(x) + y)/2
    rhs = math.sqrt(x*f(y))
    if lhs < mid - 1e-12 or mid < rhs - 1e-12:
        bad += 1
print("violations for f=x+c:", bad)

# 2) algebraic identity: (x+y+d)^2 - 4x(y+e) == (x-y-d)^2 + 4x(d-e)
for _ in range(100000):
    x = random.uniform(-10, 10); y = random.uniform(-10, 10)
    d = random.uniform(-10, 10); e = random.uniform(-10, 10)
    L = (x+y+d)**2 - 4*x*(y+e)
    R = (x-y-d)**2 + 4*x*(d-e)
    assert abs(L-R) < 1e-8
print("identity (B') ok")

# 3) sanity: check that e.g. f(x)=2x fails (should not satisfy f(f(y))=2f(y)-y)
def test(f, name):
    ok = True
    for _ in range(20000):
        x = random.uniform(1e-3, 50); y = random.uniform(1e-3, 50)
        lhs = math.sqrt((x*x + f(y)**2)/2)
        mid = (f(x)+y)/2
        rhs = math.sqrt(x*f(y))
        if lhs < mid - 1e-9 or mid < rhs - 1e-9:
            ok = False; break
    print(name, "satisfies?" , ok)
test(lambda t: 2*t, "f=2x")
test(lambda t: t + math.sin(t)**2, "f=x+sin^2 x")
test(lambda t: t*1.0, "f=x")
test(lambda t: t+3, "f=x+3")
test(lambda t: math.sqrt(t*t+1), "f=sqrt(x^2+1)")
