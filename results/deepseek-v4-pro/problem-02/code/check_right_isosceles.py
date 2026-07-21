import cmath, math, random

# For right-isosceles triangle A=(0,0), B=(2,0), C=(0,2), M=(1,0), N=(0,1)

# We can parametrize the non-degenerate branch by solving the cubic.
# cubic: x1^3 - 3x1^2 + x1*y1^2 + 2x1 - y1^2 + 2y1 = 0
# => (x1-1) y1^2 + 2y1 + x1(x1-1)(x1-2) = 0
# For a given x1 (excluding 1), solve for y1.

def solve_cubic_y1(x1):
    # (x1-1) y1^2 + 2 y1 + x1(x1-1)(x1-2) = 0
    if abs(x1 - 1) < 1e-12:
        return []
    A = x1 - 1
    B = 2
    C = x1 * (x1-1) * (x1-2)
    disc = B*B - 4*A*C
    if disc < 0:
        return []
    sqrt_disc = math.sqrt(disc)
    y1a = (-B + sqrt_disc) / (2*A)
    y1b = (-B - sqrt_disc) / (2*A)
    return [y1a, y1b]

# Then x2 = y1*(y2-2)/(x1-2) from eq1.
# And eq2_sub numerator (after eliminating y1^2 using cubic) gave:
# num2_mod = -2*(x1 - y2)*(x1**2*y2 - x1**2 + x1*y1 - 3*x1*y2 + 3*x1 + y1*y2 - 3*y1 + 2*y2 - 2)/(x1 - 1)
# So either x1 = y2, or the second factor = 0.

# If x1 != y2, we set the second factor to 0 and solve for y2:
# new_factor = x1**2*y2 - x1**2 + x1*y1 - 3*x1*y2 + 3*x1 + y1*y2 - 3*y1 + 2*y2 - 2 = 0
# => y2*(x1**2 - 3*x1 + y1 + 2) = x1**2 - x1*y1 - 3*x1 + 3*y1 + 2
# => y2 = (x1**2 - x1*y1 - 3*x1 + 3*y1 + 2) / (x1**2 - 3*x1 + y1 + 2)

# Let's try some x1 values and find y1, y2, then compute X-Y.

for x1 in [0.5, 1.5, 0.3, 1.8, 0.1, 1.9]:
    y1_vals = solve_cubic_y1(x1)
    for y1 in y1_vals:
        # First branch: x1 = y2
        y2 = x1
        if x1 != 2:
            x2 = y1*(y2-2)/(x1-2)
            # Check interior conditions
            # K inside BMC: B=(2,0), M=(1,0), C=(0,2)
            # barycentric
            # L inside BNC: B=(2,0), N=(0,1), C=(0,2)
            # Also K inside angle LBA, L inside angle ACK
            # Let's just compute X-Y
            X = (x1**2*y2 - x2**2*y1 + y1**2*y2 - y1*y2**2) / (2*(x1*y2 - x2*y1)) if abs(x1*y2 - x2*y1) > 1e-12 else None
            if X is not None:
                Y = (x1*(x1**2 + y1**2 - 2*X*x1) ) # wrong formula
                # Actually compute Y from 2(X x2 + Y y2) = x2^2 + y2^2
                Y = (x2**2 + y2**2 - 2*X*x2) / (2*y2) if abs(y2) > 1e-12 else 0
                print(f"x1={x1:.4f}, y1={y1:.4f}, x2={x2:.4f}, y2=x1={y2:.4f}: X={X:.6f}, Y={Y:.6f}, X-Y={X-Y:.10e}")
        
        # Second branch: solve for y2 from linear factor
        denom = x1**2 - 3*x1 + y1 + 2
        if abs(denom) > 1e-12:
            y2 = (x1**2 - x1*y1 - 3*x1 + 3*y1 + 2) / denom
            if y2 != x1:  # skip if degenerate
                x2 = y1*(y2-2)/(x1-2) if x1 != 2 else None
                if x2 is not None:
                    X = (x1**2*y2 - x2**2*y1 + y1**2*y2 - y1*y2**2) / (2*(x1*y2 - x2*y1)) if abs(x1*y2 - x2*y1) > 1e-12 else None
                    if X is not None:
                        Y = (x2**2 + y2**2 - 2*X*x2) / (2*y2) if abs(y2) > 1e-12 else 0
                        print(f"x1={x1:.4f}, y1={y1:.4f}, x2={x2:.4f}, y2={y2:.4f}: X={X:.6f}, Y={Y:.6f}, X-Y={X-Y:.10e}")
