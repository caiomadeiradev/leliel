import numpy as np
import matplotlib.pyplot as plt

R = 340 

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

volume = (4/3) * np.pi * R**3
area = 4 * np.pi * R**2

print(f"Volume da esfera: {volume:.3e} m³")
print(f"Área da superfície da esfera: {area:.3e} m²")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', alpha=0.6)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Sombra de Leliel com R = 340m')

plt.show()
