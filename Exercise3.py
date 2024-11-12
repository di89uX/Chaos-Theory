import numpy as np
import matplotlib.pyplot as plt

def logistic_map(lam, x):
    return 4 * lam * x * (1 - x)

def find_fixed_points(lam):
    # Fixed points: x = 0 and non-trivial fixed point
    fixed_points = [0]
    if lam > 0.25:
        non_trivial_fp = (4 * lam - 1) / (4 * lam)
        if non_trivial_fp >= 0 and non_trivial_fp <= 1:
            fixed_points.append(non_trivial_fp)
    return fixed_points

# Parameters
lam_values = np.linspace(3.57, 4, num=1000)
fixed_points_list = []

for lam in lam_values:
    f_points = find_fixed_points(lam)
    fixed_points_list.append(f_points)

# Plotting
plt.figure(figsize=(10, 6))
for i, f_points in enumerate(fixed_points_list):
    for fp in f_points:
        plt.plot(lam_values[i], fp, 'bo') # blue dots for fixed points

plt.title('Fixed Points in Logistic Map')
plt.xlabel('λ')
plt.ylabel('Fixed Points')
plt.grid()
plt.show()