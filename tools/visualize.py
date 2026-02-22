import matplotlib.pyplot as plt

# This script visualizes the 32% residual anomaly 
# predicted by the 6D Unitary Branch.

velocities = [0.1, 0.3, 0.5, 0.7, 0.9] 
standard_force = [1.0, 1.0, 1.0, 1.0, 1.0]
unitary_force = [1.01, 1.09, 1.25, 1.49, 1.81] 

plt.plot(velocities, standard_force, label='Standard Hybrid (4D)', linestyle='--')
plt.plot(velocities, unitary_force, label='6D Unitary (Phase-Lag)', marker='o', color='red')

plt.title("6D Metric Framework: Force Divergence")
plt.xlabel("Velocity (v/c)")
plt.ylabel("Effective Force Factor")
plt.legend()
plt.grid(True)
plt.show()
