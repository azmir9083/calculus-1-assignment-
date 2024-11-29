import math


# Define the function f(x) for which we want to find the critical point
def f_critical(x):
    """
    Function f(x) = ln(0.95) * (0.95^x) + 1/x^2
    """
    return math.log(0.95) * (0.95 ** x) + 1 / x ** 2


# Define the derivative of f(x), f'(x)
def f_critical_prime(x):
    """
    Derivative of f(x): f'(x) = ln(0.95)^2 * (0.95^x) - 2/x^3
    """
    return math.log(0.95) ** 2 * (0.95 ** x) - 2 / x ** 3


# Implement Newton's Method to solve f(x) = 0
def solve_newton(f, f_prime, x0, tolerance=1e-6, max_iterations=100):
    """
    Newton's method for solving f(x) = 0
    Parameters:
        f: Function for which the root is to be found
        f_prime: Derivative of the function
        x0: Initial guess
        tolerance: Convergence criterion
        max_iterations: Maximum number of iterations
    Returns:
        The critical point (root) rounded to 6 decimals, or None if it fails to converge
    """
    x_n = x0
    for iteration in range(max_iterations):
        f_xn = f(x_n)
        f_prime_xn = f_prime(x_n)

        # Avoid division by zero or very small derivatives
        if abs(f_prime_xn) < tolerance:
            print(f"Warning: Derivative too small at iteration {iteration}. Stopping.")
            return None

        # Update x_n using Newton's formula
        x_next = x_n - f_xn / f_prime_xn

        # Check for convergence
        if abs(x_next - x_n) < tolerance:
            return round(x_next, 6)

        x_n = x_next

    # If not converged, return None
    print("Warning: Newton's Method did not converge within the maximum iterations.")
    return None


# Initial guess for the critical point
x0 = 5

# Solve for the critical point
critical_x = solve_newton(f_critical, f_critical_prime, x0)

# Display the result
if critical_x is not None:
    print(f"Critical point found at x = {critical_x}")
else:
    print("Failed to find the critical point.")
