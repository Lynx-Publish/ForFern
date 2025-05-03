import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from scipy.spatial import ConvexHull
from sklearn.decomposition import PCA


# ==== Object Generators ====

def generate_box(center, size, num_points=500):
    """
    Generate a point cloud representing a box (rectangular prism) by sampling random points
    inside the box volume.
    """
    points = []
    for _ in range(num_points):
        # Random points inside a rectangular box
        x = random.uniform(center[0] - size[0] / 2, center[0] + size[0] / 2)
        y = random.uniform(center[1] - size[1] / 2, center[1] + size[1] / 2)
        z = random.uniform(center[2] - size[2] / 2, center[2] + size[2] / 2)
        points.append([x, y, z])

    return np.array(points)


def generate_random_object():
    """
    Randomly generate an object. Currently only a box.
    """
    center = np.random.uniform(-2, 2, size=3)
    size = np.random.uniform(0.5, 1.0, size=3)  # Box size
    return generate_box(center, size), "box"


# ==== Adaptive Grip Prediction ====

def calculate_normals(points, hull):
    """
    Calculate the surface normals of the convex hull faces.
    """
    normals = []
    for simplex in hull.simplices:
        # Extract the vertices of the face
        v0, v1, v2 = points[simplex]

        # Calculate the vectors along two edges of the triangle
        edge1 = v1 - v0
        edge2 = v2 - v0

        # Compute the normal by taking the cross product of the two edges
        normal = np.cross(edge1, edge2)

        # Normalize the normal
        normal = normal / np.linalg.norm(normal)

        normals.append(normal)

    return np.array(normals)


def find_flat_region(normals):
    """
    Find the flat region based on the surface normals.
    The flatter regions will have normals that point in a consistent direction.
    """
    # Apply PCA to the normals to determine the dominant direction
    pca = PCA(n_components=1)
    pca.fit(normals)

    # The normal vector with the largest eigenvalue is the direction of maximal flatness
    dominant_normal = pca.components_[0]
    return dominant_normal


def calculate_grip_points_on_faces(points):
    """
    Calculate the best grip points for an object by analyzing the faces of the convex hull.
    """
    if points.shape[0] < 3:
        raise ValueError("At least 3 points are required to calculate the convex hull.")

    # Create a convex hull from the points
    try:
        hull = ConvexHull(points)
    except Exception as e:
        raise ValueError(f"Error computing ConvexHull: {e}")

    # Get the convex hull vertices
    hull_points = points[hull.vertices]

    # Calculate the normals for the faces of the hull
    normals = calculate_normals(points, hull)

    # Find the most dominant direction (flat region)
    dominant_normal = find_flat_region(normals)

    grip_faces = []
    # Loop through each face to find the most suitable grip region
    for idx, normal in enumerate(normals):
        if np.dot(normal, dominant_normal) > 0.9:  # Flat face
            face_points = points[hull.simplices[idx]]
            grip_faces.append(face_points)

    return grip_faces


# ==== Visualization ====

def plot_convex_hull_and_grip(points, grip_faces, object_label="Object"):
    """
    Plot the convex hull mesh and the selected grip faces.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the object points
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], label=object_label, alpha=0.6, s=10)

    # Plot the convex hull faces
    for face in grip_faces:
        ax.plot_trisurf(face[:, 0], face[:, 1], face[:, 2], color='green', alpha=0.3)

    ax.set_title(f"{object_label} with Convex Hull and Grip Faces")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()


# ==== Main Code ====

# Generate a box object
object_points, object_label = generate_random_object()

# Check if the number of points is sufficient
if object_points.shape[0] < 3:
    print("Generated object has too few points for ConvexHull calculation.")
else:
    # Calculate the best grip points for the object based on the convex hull faces
    grip_faces = calculate_grip_points_on_faces(object_points)

    # Plot the object and its convex hull mesh with grip faces
    plot_convex_hull_and_grip(object_points, grip_faces, object_label)
