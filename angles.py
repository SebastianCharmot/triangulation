import numpy as np

# Define the three points
points = np.array([
    [-22.06772558, 0.62831029, 75.64824721],
    [-2.86662473, -1.92949574, 82.46572483],
    [-4.78215405, 10.56614672, 35.18198051]
])

# Compute the normal vector of the plane formed by the three points
# The normal vector is the cross product of two vectors on the plane
vector1 = points[1] - points[0]
vector2 = points[2] - points[0]
normal_vector = np.cross(vector1, vector2)

# Normalize the normal vector
normal_vector /= np.linalg.norm(normal_vector)

angles = np.abs(np.arcsin(normal_vector))

print(angles)

# Compute the angles required to rotate the normal vector to align with the z-axis
theta_x = np.arctan2(normal_vector[1], normal_vector[2])
theta_y = -np.arctan2(normal_vector[0], np.sqrt(normal_vector[1]**2 + normal_vector[2]**2))

# Compute the angle required to rotate the normal vector into the xy-plane (around the z-axis)
theta_z = -np.arctan2(normal_vector[0], normal_vector[1])

# Print the angles
print("Rotation angles (in radians):")
print("Rotation around x-axis:", theta_x)
print("Rotation around y-axis:", theta_y)
print("Rotation around z-axis:", theta_z)
