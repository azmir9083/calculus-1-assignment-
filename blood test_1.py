import numpy as np

# Parameters
N = 100  # Total population
q = 0.95  # Probability any person tests negative

# Function to calculate the average number of blood tests
def avg_tests(x):
    return N * (1 - q**x + 1/x)

# Range for x (group size)
x_values = np.linspace(1, 150, 10000)  # High granularity for accuracy

# Calculate the average tests for each group size
avg_values = avg_tests(x_values)

# Find the optimal group size (minimizes the average tests)
optimal_x = x_values[np.argmin(avg_values)]
min_avg_tests = np.min(avg_values)

# Output the results
print(f"Optimal group size: {optimal_x:.2f}")
print(f"Minimum average tests: {min_avg_tests:.2f}")


