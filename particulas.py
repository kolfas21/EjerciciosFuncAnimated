import numpy as np
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt

# Número de partículas
N = 50

# Posiciones iniciales aleatorias
x = np.random.rand(N)
y = np.random.rand(N)

fig, ax = plt.subplots()
scat = ax.scatter(x, y)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

def update(frame):
    global x, y
    # Movimiento aleatorio pequeño
    x += (np.random.rand(N) - 0.5) * 0.05
    y += (np.random.rand(N) - 0.5) * 0.05
    # Mantener dentro de los límites
    x = np.clip(x, 0, 1)
    y = np.clip(y, 0, 1)
    scat.set_offsets(np.c_[x, y])
    return scat,

ani = FuncAnimation(fig, update, frames=150, interval=50, blit=True)
ani.save('animaciones/particulaseno.gif', writer='pillow')
plt.show()
