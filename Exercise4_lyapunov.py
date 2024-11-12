import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np

def logistic_map(lamda, x):
    return 4 * lamda * x * (1 - x)
def generate_data(lamda, x0, x_prime0, iterations):
    x = np.zeros(iterations)
    x_prime = np.zeros(iterations)
    x[0] = x0
    x_prime[0] = x_prime0

    for n in range(1, iterations):
        x[n] = logistic_map(lamda, x[n-1])
        x_prime[n] = logistic_map(lamda, x_prime[n-1])

    return x, x_prime


def plot_lyapunov_exponent(lamda, x0, x_prime0, iterations):
    # Generate data
    x, x_prime = generate_data(lamda, x0, x_prime0, iterations)

    # Calculate separation
    delta = np.abs(x_prime - x)

    # Calculate ln(Δn)
    ln_delta = np.log(delta)

    # Plotting ln(Δn) vs step number
    plt.figure(figsize=(10, 6))
    plt.plot(ln_delta[1:], label='ln(Δn)', color='blue')  # Skip first value since it's zero
    plt.title(f'Lyapunov Exponent for λ={lamda}')
    plt.xlabel('Step Number (n)')
    plt.ylabel('ln(Δn)')
    plt.grid()
    plt.legend()
    plt.show()

# Parameters for simulation
lambda_value = 3.9  # Choose λ > λ∞ for chaotic behavior
x0 = 0.5          # Initial condition 1
x_prime0 = 0.5001 # Initial condition 2 (very close to x0)
iterations = 1000   # Number of iterations

plot_lyapunov_exponent(lambda_value, x0, x_prime0, iterations)