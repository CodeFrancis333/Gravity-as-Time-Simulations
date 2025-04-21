
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
c = 3e8
M_sun = 1.989e30
M = 5e8 * M_sun
pc_to_m = 3.086e16
r_range_pc = np.linspace(0.001, 10, 200)
r_range = r_range_pc * pc_to_m

tau_r = np.sqrt(1 - (2 * G * M) / (r_range * c**2))
z_r = (1 / tau_r) - 1

plt.plot(r_range_pc, z_r)
plt.xlabel("Distance from SMBH (pc)")
plt.ylabel("Redshift z")
plt.title("Redshift vs Distance from SMBH")
plt.grid(True)
plt.show()
