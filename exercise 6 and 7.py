import numpy as np

# Example bifurcation values; replace with actual values
lambda_2 = 0.700000
lambda_3 = 0.862256
lambda_4 = 0.885989
lambda_16 = 0.891089

lambda_prime_1 = 0.75
lambda_prime_2 = 3.00
lambda_prime_3 = 3.5

def calculate_feigenbaum_delta(lambda_n, lambda_n_minus_1, lambda_n_plus_1):
    """Calculate Feigenbaum delta."""
    return (lambda_n - lambda_n_minus_1) / (lambda_n_plus_1 - lambda_n)

# Calculations for Exercise 6
delta_a = calculate_feigenbaum_delta(lambda_3, lambda_2, lambda_4)
print(f"Feigenbaum δ (part a): {delta_a}")

delta_b = calculate_feigenbaum_delta(lambda_prime_2, lambda_prime_1, lambda_prime_3)
print(f"Feigenbaum δ (part b): {delta_b}")

delta_c = calculate_feigenbaum_delta(lambda_4, lambda_3, lambda_16)
print(f"Feigenbaum δ (part c): {delta_c}")

delta_d = calculate_feigenbaum_delta(lambda_prime_3, lambda_prime_2, lambda_16)
print(f"Feigenbaum δ (part d): {delta_d}")

# Example distances between stable points; replace with actual values
d_4 = 0.2
d_8 = 0.08

def calculate_feigenbaum_alpha(d_n, d_n_plus_1):
    """Calculate Feigenbaum alpha."""
    return d_n / d_n_plus_1

# Calculation for Exercise 7
alpha = calculate_feigenbaum_alpha(d_4, d_8)
print(f"Feigenbaum α: {alpha}")
