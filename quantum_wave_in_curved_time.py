
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Grid and time step setup
x = np.linspace(-10, 10, 400)
dx = x[1] - x[0]
dt = 0.01
steps = 300

# Time field τ(x) increases with x
tau_gradient = 1 + 0.05 * x

# Initial Gaussian wave packet
x0, sigma, k0 = -5, 1, 5
psi_real = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.cos(k0 * x)
psi_imag = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.sin(k0 * x)
psi = psi_real + 1j * psi_imag

# Set up figure
fig, ax = plt.subplots()
line, = ax.plot(x, np.abs(psi)**2, lw=2)
ax.set_ylim(0, 1)
ax.set_xlim(-10, 10)
ax.set_title("Quantum Wave in Curved Time Field")
ax.set_xlabel("Position x")
ax.set_ylabel("Probability Density |ψ|²")
ax.grid(True)

# Laplacian function
def laplacian(psi):
    return (np.roll(psi, -1) - 2 * psi + np.roll(psi, 1)) / dx**2

# Animation update
def update(frame):
    global psi
    lap = laplacian(psi)
    dpsi_dt = -1j * lap / tau_gradient
    psi += dpsi_dt * dt
    line.set_ydata(np.abs(psi)**2)
    return line,

# Save animation
ani = FuncAnimation(fig, update, frames=steps, blit=True)
ani.save("quantum_wave_in_curved_time.gif", writer=PillowWriter(fps=30))
plt.close()
