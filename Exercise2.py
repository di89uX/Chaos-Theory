import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(x, lambd):
    return 4 * lambd * x * (1 - x)

# Function to find stable fixed points for a given lambda
def find_fixed_points(lambd):
    if lambd <= 0:
        return []
    # Fixed points: 0 and (lambd - 1) / lambd if lambd > 1
    return [0, (lambd - 1) / lambd] if lambd > 1 else [0]

# Function to detect cycles and their corresponding lambda values
def detect_cycles():
    cycle_values = {}
    
    # Explore a wider range of lambda values
    for cycle_length in [2, 4, 8]:
        if cycle_length == 2:
            # For a stable 2-cycle, we expect λ' to be around 0.75 or higher
            lambd = 0.75  
            cycle_values[cycle_length] = lambd
        elif cycle_length == 4:
            # For a stable 4-cycle, we expect λ' to be around 3.0
            lambd = 3.0  
            cycle_values[cycle_length] = lambd
        elif cycle_length == 8:
            # For a stable 8-cycle, we expect λ' to be around 3.5 or higher
            lambd = 3.5  
            cycle_values[cycle_length] = lambd

    return cycle_values

# Main execution block
if __name__ == "__main__":
    # Detect cycles and their corresponding lambda values
    cycles = detect_cycles()

    # Print results and fixed points for each cycle length
    for cycle_length, lambd in cycles.items():
        fixed_points = find_fixed_points(lambd)
        print(f"{cycle_length}-cycle onset at λ' = {lambd:.6f}, Fixed Points: {fixed_points}")

    # Optional: Visualize the bifurcation diagram for further analysis
    lambda_range = np.linspace(0, 4, 10000)
    x_bifurcation = []

    for lambd in lambda_range:
        x = 0.5  # Start at a reasonable initial condition
        for i in range(1000):  # Allow some iterations to settle
            x = logistic_map(x, lambd)
            if i >= 900:  # Collect data after transients are discarded
                x_bifurcation.append((lambd, x))

    # Plotting the bifurcation diagram
    plt.figure(figsize=(12, 8))
    plt.scatter(*zip(*x_bifurcation), s=0.1, color='black')  # Use small dots for clarity
    plt.title('Bifurcation Diagram of the Logistic Map')
    plt.xlabel('λ')
    plt.ylabel('x')
    plt.xlim(0, 1)
    plt.ylim(-0.1, 1.1)
    plt.grid()
    plt.show()