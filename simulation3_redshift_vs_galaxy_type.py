
import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
c = 3e8
M_sun = 1.989e30
pc_to_m = 3.086e16
r_fixed = 1 * pc_to_m

galaxy_types = ["Dwarf", "Spiral", "Elliptical", "Giant Elliptical"]
M_smbh_types = np.array([1e6, 1e8, 5e8, 1e9]) * M_sun

tau_types = np.sqrt(1 - (2 * G * M_smbh_types) / (r_fixed * c**2))
z_types = (1 / tau_types) - 1

plt.bar(galaxy_types, z_types, color='skyblue')
plt.xlabel("Galaxy Type")
plt.ylabel("Redshift z")
plt.title("Redshift vs Galaxy Type (Due to SMBH Mass)")
plt.tight_layout()
plt.show()
