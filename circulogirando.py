import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Crear figura y eje
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Mantener proporciones iguales
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)

# Punto que gira
point, = ax.plot([], [], 'ro')  # punto rojo
trail, = ax.plot([], [], 'b-', lw=1)  # trayectoria azul

# Lista para almacenar la trayectoria
xdata, ydata = [], []

def init():
    point.set_data([], [])
    trail.set_data([], [])
    return point, trail

def update(frame):
    t = frame / 20
    x = np.cos(t)
    y = np.sin(t)
    point.set_data([x], [y])  # Actualiza la posición del punto
    xdata.append(x)
    ydata.append(y)
    trail.set_data(xdata, ydata)  # Dibuja la trayectoria
    return point, trail

# Crear animación
ani = animation.FuncAnimation(
    fig, update, frames=range(0, 500),
    init_func=init, blit=True, interval=20
)


import os
plt.title("Punto girando en círculo")
# Crear la carpeta si no existe
os.makedirs('animaciones', exist_ok=True)
ani.save('animaciones/circulogirando.gif')
plt.show()
