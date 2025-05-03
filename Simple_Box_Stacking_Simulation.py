import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random

class Box:
    def __init__(self, id, width, depth, height, color, weight=1.0, accessible=False):
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.color = color
        self.weight = weight
        self.accessible = accessible

class Room3D:
    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height
        self.grid = [[[None for _ in range(height)] for _ in range(depth)] for _ in range(width)]
        self.placed_boxes = []

    def can_place(self, x, y, z, box):
        if (x + box.width > self.width or
            y + box.depth > self.depth or
            z + box.height > self.height):
            return False

        for i in range(box.width):
            for j in range(box.depth):
                for k in range(box.height):
                    if self.grid[x + i][y + j][z + k] is not None:
                        return False

        if z > 0:
            for i in range(box.width):
                for j in range(box.depth):
                    if self.grid[x + i][y + j][z - 1] is None:
                        return False
        return True

    def place_box(self, x, y, z, box):
        for i in range(box.width):
            for j in range(box.depth):
                for k in range(box.height):
                    self.grid[x + i][y + j][z + k] = box.id
        self.placed_boxes.append((box, x, y, z))

    def get_placement_position(self, box):
        for x in reversed(range(self.width)):
            for y in range(self.depth):
                for z in range(self.height):
                    if self.can_place(x, y, z, box):
                        return (x, y, z)
        return None

    def simulate_robot_place(self, box):
        if box.weight > 10.0:
            print(f"❌ Box '{box.id}' is too heavy for the robot to lift (>{box.weight}kg).")
            return False
        pos = self.get_placement_position(box)
        if pos:
            self.place_box(*pos, box)
            print(f"✅ Robot placed box '{box.id}' at {pos}.")
            return True
        else:
            print(f"⚠️ No valid position for box '{box.id}'.")
            return False

    def get_room_state(self):
        return [(box.id, x, y, z) for box, x, y, z in self.placed_boxes]

    def draw(self):
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        for box, x, y, z in self.placed_boxes:
            self.draw_box(ax, x, y, z, box)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.depth)
        ax.set_zlim(0, self.height)
        ax.set_xlabel("Width (X)")
        ax.set_ylabel("Depth (Y)")
        ax.set_zlabel("Height (Z)")
        plt.title("Robot Box Stacking Simulation")
        plt.show()

    def draw_box(self, ax, x, y, z, box):
        x0, y0, z0 = x, y, z
        x1, y1, z1 = x + box.width, y + box.depth, z + box.height
        verts = [
            [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0)],
            [(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)],
            [(x0,y0,z0),(x1,y0,z0),(x1,y0,z1),(x0,y0,z1)],
            [(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)],
            [(x0,y0,z0),(x0,y1,z0),(x0,y1,z1),(x0,y0,z1)],
            [(x1,y0,z0),(x1,y1,z0),(x1,y1,z1),(x1,y0,z1)]
        ]
        ax.add_collection3d(Poly3DCollection(verts, facecolors=box.color, linewidths=1, edgecolors='black', alpha=0.9))

def generate_random_boxes(n):
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'lime', 'brown']
    boxes = []
    for i in range(n):
        w, d, h = random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)
        color = random.choice(colors)
        weight = round(random.uniform(1.0, 15.0), 1)
        accessible = random.choice([True, False])
        id = f"{color}_{w}x{d}x{h}_{i+1}"
        boxes.append(Box(id, w, d, h, color, weight, accessible))
    return boxes

# MAIN EXECUTION
if __name__ == "__main__":
    try:
        num_boxes = int(input("How many random boxes would you like to generate? "))
        room = Room3D(width=10, depth=10, height=10)
        boxes = generate_random_boxes(num_boxes)

        # Sort for efficient stacking
        boxes.sort(key=lambda b: (not b.accessible, -b.weight))

        # Simulate robot placing
        for box in boxes:
            room.simulate_robot_place(box)

        print("\n📦 Final Room State:")
        for box_id, x, y, z in room.get_room_state():
            print(f" - Box '{box_id}' at position ({x}, {y}, {z})")

        room.draw()
    except ValueError:
        print("❌ Please enter a valid number.")
