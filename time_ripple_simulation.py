
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
dx = x[1] - x[0]
dt = 0.001
T = 0.5
c = 1.0
steps = int(T / dt)

# Initial bump in τ(x)
tau = np.exp(-100 * (x - 5)**2)
tau_prev = np.copy(tau)
tau_next = np.zeros_like(tau)

snapshots = []
snapshot_times = [0, int(0.1 / dt), int(0.25 / dt), int(0.5 / dt)]

# Time evolution loop
for t in range(steps):
    tau_next[1:-1] = (2 * tau[1:-1] - tau_prev[1:-1] +
                      (c * dt / dx)**2 * (tau[2:] - 2 * tau[1:-1] + tau[:-2]))
    tau_prev, tau = tau, tau_next.copy()
    if t in snapshot_times:
        snapshots.append(tau.copy())

# Plot snapshots
fig, ax = plt.subplots()
for t, s in zip(["t=0", "t=0.1", "t=0.25", "t=0.5"], snapshots):
    ax.plot(x, s, label=t)
ax.set_title("Time Ripple Propagation")
ax.set_xlabel("Position x")
ax.set_ylabel("τ(x)")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig("time_ripple_snapshots.png")
plt.close()
