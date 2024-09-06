import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure

# Define the grid size for the cube
grid_size = 50
x = np.linspace(-np.pi, np.pi, grid_size)
y = np.linspace(-np.pi, np.pi, grid_size)
z = np.linspace(-np.pi, np.pi, grid_size)

# Create a 3D meshgrid for X, Y, Z
X, Y, Z = np.meshgrid(x, y, z)
gyroid = np.sin(X) * np.cos(Y) + np.sin(Y) * np.cos(Z) + np.sin(Z) * np.cos(X)

# Use marching cubes to obtain the surface
verts, faces, normals, values = measure.marching_cubes(gyroid, level=0)

# Plot the gyroid surface
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(verts[:, 0], verts[:, 1], verts[:, 2], triangles=faces, cmap='viridis', lw=1)

# Set plot parameters
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gyroid Cube')

plt.show()
