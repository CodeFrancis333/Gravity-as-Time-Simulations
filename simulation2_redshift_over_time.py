
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
c = 3e8
M_sun = 1.989e30
pc_to_m = 3.086e16

time_gyr = np.linspace(0, 13.8, 200)
M_growth = np.linspace(1e8, 1e9, 200) * M_sun
r_fixed = 1 * pc_to_m

tau_t = np.sqrt(1 - (2 * G * M_growth) / (r_fixed * c**2))
z_t = (1 / tau_t) - 1

plt.plot(time_gyr, z_t)
plt.xlabel("Time (Gyr)")
plt.ylabel("Redshift z")
plt.title("Redshift Over Time from SMBH Growth")
plt.grid(True)
plt.show()
