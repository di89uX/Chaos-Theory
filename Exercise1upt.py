import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(x, lambd):
    return 4*lambd * x * (1 - x)

# Parameters for exercise
lambda_range = np.linspace(0.7, 1.0, 10000)  # Expanded range of λ values to explore
num_iterations = 5000  # Total iterations for each λ
num_transients = 4000  # Number of transient iterations to discard
x0 = 0.01  # Initial condition

# Dictionary to store onset λ values for each cycle length
cycle_onsets = {}

# Function to detect cycles
def detect_cycle(values):
    n = len(values)
    for cycle_length in [2, 4, 8, 16]:
        # Check if there are enough points to form a cycle
        if n < cycle_length * 2:
            continue
        
        # Compare segments of the list to find cycles
        is_cycle = True
        for i in range(cycle_length):
            if not np.allclose(values[i::cycle_length], values[i], atol=1e-4):  # Check if segments match
                is_cycle = False
                break
        
        if is_cycle:
            return cycle_length
    
    return None

# Loop through λ values to detect cycle onsets
for lambd in lambda_range:
    x = x0  # Set initial x value for each λ
    x_values = []
    
    # Run iterations
    for i in range(num_iterations):
        x = logistic_map(x, lambd)
        # Collect values after transient phase
        if i >= num_transients:
            x_values.append(x)
    
    # Detect cycles in collected values
    cycle_length = detect_cycle(np.array(x_values))
    
    # Record λ value at the onset of cycles if found
    if cycle_length is not None and cycle_length not in cycle_onsets:
        cycle_onsets[cycle_length] = lambd
        print(f"{cycle_length}-cycle onset at λ = {lambd:.6f}")

# Print detected cycle onsets
print("\nDetected cycle onsets for various λ values:")
for cycle_length, lambd in sorted(cycle_onsets.items()):
    print(f"{cycle_length}-cycle onset at λ = {lambd:.6f}")

# Plotting the bifurcation diagram to visualize cycles and chaos
# Initialize lists for bifurcation plot
lambda_bifurcation = []
x_bifurcation = []

for lambd in lambda_range:
    x = x0  # Reset initial condition
    # Run logistic map iterations
    for i in range(num_iterations):
        x = logistic_map(x, lambd)
        # Collect values after transient phase
        if i >= num_transients:
            lambda_bifurcation.append(lambd)
            x_bifurcation.append(x)

# Plot the bifurcation diagram
plt.figure(figsize=(12, 8))
plt.plot(lambda_bifurcation, x_bifurcation, ',k', alpha=0.5)  # Small dots for clarity
plt.xlabel('λ')
plt.ylabel('x')
plt.title('Bifurcation Diagram of the Logistic Map')
plt.xlim(0.7, 1.0)
plt.ylim(-0.1, 1.1)
plt.grid()
plt.show()