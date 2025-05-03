import numpy as np
import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from shapely.affinity import translate
from mpl_toolkits.mplot3d import Axes3D


def generate_irregular_polygon(center, radius, num_vertices):
    angles = np.sort(np.random.rand(num_vertices) * 2 * np.pi)
    points = []
    for angle in angles:
        r = radius * (0.6 + 0.4 * random.random())  # randomize radius for irregularity
        x = center[0] + r * np.cos(angle)
        y = center[1] + r * np.sin(angle)
        points.append((x, y))
    return Polygon(points)


def generate_room_walls_and_floor(polygon: Polygon, height, resolution=1.0, noise_level=0.05):
    minx, miny, maxx, maxy = polygon.bounds
    all_points = []

    # Floor and ceiling
    for z in [0, height]:
        for x in np.arange(minx, maxx, resolution):
            for y in np.arange(miny, maxy, resolution):
                if polygon.contains(Point(x, y)):
                    noise = np.random.uniform(-noise_level, noise_level, 2)
                    all_points.append([x + noise[0], y + noise[1], z])

    # Vertical walls (extruded edges)
    coords = list(polygon.exterior.coords)
    for i in range(len(coords) - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]
        for z in np.arange(0, height, resolution):
            steps = max(int(np.hypot(x2 - x1, y2 - y1) / resolution), 1)
            for j in range(steps + 1):
                x = x1 + (x2 - x1) * j / steps
                y = y1 + (y2 - y1) * j / steps
                noise = np.random.uniform(-noise_level, noise_level, 2)
                all_points.append([x + noise[0], y + noise[1], z])
    return np.array(all_points)


def generate_box_points(x_start, y_start, z_start, width, depth, height, noise_level=0.1):
    points = []
    for x in np.linspace(x_start, x_start + width, int(width * 2)):
        for y in np.linspace(y_start, y_start + depth, int(depth * 2)):
            for z in np.linspace(z_start, z_start + height, int(height * 2)):
                noise = np.random.uniform(-noise_level, noise_level, 3)
                points.append([x + noise[0], y + noise[1], z + noise[2]])
    return points


def create_irregular_room_with_boxes(center, radius, num_vertices, height, box_specs):
    polygon = generate_irregular_polygon(center, radius, num_vertices)
    room_points = generate_room_walls_and_floor(polygon, height)

    all_points = room_points.tolist()
    for spec in box_specs:
        box = generate_box_points(*spec)
        all_points.extend(box)
    return np.array(all_points), polygon


def remove_random_points(points, removal_percentage=0.2):
    num_remove = int(len(points) * removal_percentage)
    indices = random.sample(range(len(points)), num_remove)
    return np.delete(points, indices, axis=0)


def plot_point_cloud(points, polygon: Polygon, height):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot point cloud
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='blue', s=1, alpha=0.7)

    # Plot 2D boundary (floor projection)
    coords = np.array(polygon.exterior.coords)
    ax.plot(coords[:, 0], coords[:, 1], zs=0, zdir='z', color='red', linewidth=2)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Irregular Room with Point Cloud")
    ax.set_zlim(0, height)
    plt.tight_layout()
    plt.show()


def save_point_cloud_to_file(points, filename='point_cloud.txt'):
    np.savetxt(filename, points, fmt='%.6f', delimiter=' ', header="X Y Z", comments='')


# === MAIN EXECUTION ===
if __name__ == "__main__":
    room_center = (25, 25)
    room_radius = 20
    num_sides = 8
    room_height = 10

    # Boxes defined by: x, y, z, width, depth, height
    box_specs = [
        (20, 20, 0, 3, 3, 3),
        (15, 30, 0, 2, 4, 2),
        (30, 20, 0, 4, 2, 5)
    ]

    point_cloud, polygon = create_irregular_room_with_boxes(
        center=room_center,
        radius=room_radius,
        num_vertices=num_sides,
        height=room_height,
        box_specs=box_specs
    )

    # Optionally remove some points to simulate sensor dropout
    point_cloud = remove_random_points(point_cloud, removal_percentage=0.15)

    save_point_cloud_to_file(point_cloud)
    plot_point_cloud(point_cloud, polygon, height=room_height)

    print("Point cloud data saved to 'point_cloud.txt'.")
