import numpy as np
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt

# Crear figura y eje
fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 1000)
line, = ax.plot(x, np.sin(x))

# Limitar ejes
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, 4 * np.pi)

# Función de animación
def animate(t):
    line.set_ydata(np.sin(x + t))  # Desplaza la onda
    return line,

# Crear animación
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 128), interval=50, blit=True)

# Guardar la animación como GIF
ani.save('animaciones/ondaseno.gif', writer='pillow')

plt.show()
