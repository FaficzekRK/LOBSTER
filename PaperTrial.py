import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

# Define two opposite corners of the rectangle
corner1 = np.array([1, 2, 3])
corner2 = np.array([4, 5, 6])

# Extract the min and max bounds
x = [corner1[0], corner2[0]]
y = [corner1[1], corner2[1]]
z = [corner1[2], corner2[2]]

# Define vertices of the cuboid
vertices = [
    [x[0], y[0], z[0]],
    [x[1], y[0], z[0]],
    [x[1], y[1], z[0]],
    [x[0], y[1], z[0]],
    [x[0], y[0], z[1]],
    [x[1], y[0], z[1]],
    [x[1], y[1], z[1]],
    [x[0], y[1], z[1]]
]

# Define the 6 faces of the cuboid
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[4], vertices[7], vertices[3], vertices[0]]
]

# Define edges of the cuboid
edges = [
    (0,1), (1,2), (2,3), (3,0),  # bottom
    (4,5), (5,6), (6,7), (7,4),  # top
    (0,4), (1,5), (2,6), (3,7)   # verticals
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add faces
face_color = (0, 0.5, 1, 0.2)  # RGBA: blue with transparency
ax.add_collection3d(Poly3DCollection(faces, facecolors=face_color, linewidths=0, edgecolors='none'))

# Add edges
for edge in edges:
    xs = [vertices[edge[0]][0], vertices[edge[1]][0]]
    ys = [vertices[edge[0]][1], vertices[edge[1]][1]]
    zs = [vertices[edge[0]][2], vertices[edge[1]][2]]
    ax.plot(xs, ys, zs, color=(0, 0.5, 1, 1))  # solid border, same color without transparency

# Set limits (optional)
ax.set_xlim(min(x)-1, max(x)+1)
ax.set_ylim(min(y)-1, max(y)+1)
ax.set_zlim(min(z)-1, max(z)+1)

plt.show()