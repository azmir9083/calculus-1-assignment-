import math

# Part a: Verify that 0 is a root of multiplicity 2
def f_a(x):
    return math.exp(2 * math.sin(x)) - 2 * x - 1

def f_a_prime(x):
    return 2 * math.exp(2 * math.sin(x)) * math.cos(x) - 2

def f_a_double_prime(x):
    return 4 * math.exp(2 * math.sin(x)) * math.cos(x)**2 - 2 * math.exp(2 * math.sin(x)) * math.sin(x)

# Verify at x = 0
f0 = f_a(0)
f0_prime = f_a_prime(0)
f0_double_prime = f_a_double_prime(0)

print(f"Part (a): f(0) = {f0}, f'(0) = {f0_prime}, f''(0) = {f0_double_prime}")
if f0 == 0 and f0_prime == 0 and f0_double_prime != 0:
    print("0 is a root of multiplicity 2.")
else:
    print("0 is NOT a root of multiplicity 2.")

# Part b: Newton's and Modified Newton's Method
def newtons_method(f, f_prime, x0, max_iterations=9, tolerance=1e-6):
    x_n = x0
    for _ in range(max_iterations):
        f_prime_value = f_prime(x_n)
        if abs(f_prime_value) < tolerance:  # Handle near-zero derivative
            return round(x_n, 6)
        x_n = x_n - f(x_n) / f_prime_value
    return round(x_n, 6)

def modified_newtons_method(f, f_prime, x0, max_iterations=9, tolerance=1e-6):
    x_n = x0
    for _ in range(max_iterations):
        f_prime_value = f_prime(x_n)
        if abs(f_prime_value) < tolerance:  # Handle near-zero derivative
            return round(x_n, 6)
        x_n = x_n - 2 * f(x_n) / f_prime_value
    return round(x_n, 6)

# Apply Newton's and Modified Newton's methods with x0 = 0.1
x0 = 0.1
newton_x9 = newtons_method(f_a, f_a_prime, x0)
modified_newton_x9 = modified_newtons_method(f_a, f_a_prime, x0)

print(f"Part (b): Newton's Method x9 = {newton_x9}")
print(f"Part (b): Modified Newton's Method x9 = {modified_newton_x9}")

# Part c: Modified Newton's Method for f(x) = (8x^2) / (3x^2 + 1)
def f_c(x):
    return (8 * x**2) / (3 * x**2 + 1)

def f_c_prime(x):
    numerator = (16 * x) * (3 * x**2 + 1) - (24 * x**3)
    denominator = (3 * x**2 + 1)**2
    return numerator / denominator

# Apply Modified Newton's method with x0 = 0.15
x0_c = 0.15
modified_newton_x9_c = modified_newtons_method(f_c, f_c_prime, x0_c)

print(f"Part (c): Modified Newton's Method x9 = {modified_newton_x9_c}")


