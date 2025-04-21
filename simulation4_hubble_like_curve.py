
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
c = 3e8
M_sun = 1.989e30
pc_to_m = 3.086e16
r_fixed = 1 * pc_to_m

distances_mpc = np.linspace(10, 1000, 200)
distances_m = distances_mpc * 1e6 * pc_to_m
M_proxy = np.linspace(1e8, 1e9, 200) * M_sun

tau_proxy = np.sqrt(1 - (2 * G * M_proxy) / (r_fixed * c**2))
z_proxy = (1 / tau_proxy) - 1

plt.plot(distances_mpc, z_proxy)
plt.xlabel("Distance (Mpc)")
plt.ylabel("Redshift z")
plt.title("Redshift vs Apparent Distance (No Cosmic Expansion)")
plt.grid(True)
plt.tight_layout()
plt.show()
