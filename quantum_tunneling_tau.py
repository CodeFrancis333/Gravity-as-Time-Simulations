
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)
dx = x[1] - x[0]

# Potential barrier and τ(x)
V = np.zeros_like(x)
V[np.abs(x) < 2] = 5
tau_x = 1 + 0.5 * np.exp(-((x) / 2)**2)

# Initial wave packet
x0, sigma, k0 = -6, 1, 3
psi_real = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.cos(k0 * x)
psi_imag = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.sin(k0 * x)
psi = psi_real + 1j * psi_imag

dt = 0.005
steps = [0, 200, 400, 600, 800]
snapshots = []

def laplacian(psi):
    return (np.roll(psi, -1) - 2 * psi + np.roll(psi, 1)) / dx**2

# Time evolution
for step in range(max(steps)+1):
    lap = laplacian(psi)
    dpsi_dt = -1j * (-0.5 * lap + V * psi) / tau_x
    psi += dpsi_dt * dt
    if step in steps:
        snapshots.append(np.abs(psi)**2)

# Plot
fig, ax = plt.subplots()
for i, s in zip(steps, snapshots):
    ax.plot(x, s, label=f"Step {i}")
ax.plot(x, V / max(V) * max(snapshots[-1]), 'k--', label="Barrier (scaled)")
ax.set_title("Quantum Tunneling in Warped Time Field")
ax.set_xlabel("Position x")
ax.set_ylabel("Probability Density |ψ|²")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("tunneling_tau_snapshots.png")
plt.close()
