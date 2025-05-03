---

# Autonomous Robotic Gripping and Control System

## Overview

This project proposes an autonomous control system for a robotic manipulator that utilizes 3D point cloud data and intelligent language-based instructions. The system is designed to identify, grasp, and manipulate objects in a structured environment, enabling efficient interaction with objects based on natural language commands and spatial awareness.

---

## Project Goals

### 1. **Gripping System and Object Detection**

* **3D Point Cloud Processing:**

  * Use point cloud data to identify objects in the environment.
  * Segment objects via island grouping and generate non-triangular meshes.

* **Bounding Box Generation:**

  * Create bounding boxes around each detected object with configurable tolerances.

* **Center of Gravity Estimation:**

  * Calculate the center of gravity to determine the optimal gripping points for objects.

* **Flat-Plane Contact Optimization:**

  * Identify flat surfaces on the object most aligned with the planar orientation of the robot's grippers.

* **Grip Feedback System:**

  * Utilize three pressure sensors per gripper (on each robotic arm) to confirm a secure grip across multiple contact points.

---

### 2. **Multimodal Perception and Language Interface**

* **LLM Integration (e.g., ChatGPT, LLaMA):**

  * Implement a multi-layered LLM system with an initial speech-to-text layer to interpret user commands.
  * Example: A user may say "Grab the green box," and the system parses this command into structured constraints.

    * Format: Action, Object(s), Goal Location/Relation.

* **Visual Recognition Pipeline:**

  * Use an RGB camera combined with a depth camera to:

    * Detect and label objects by color.
    * Match resolution and align depth data to RGB midpoints.
    * Annotate bounding boxes in reference to environmental landmarks (e.g., walls, orientation, cardinal directions).

---

### 3. **Environment Awareness and State Tracking**

* **State Management:**

  * Maintain internal states such as moving, standing, still, crouched, grabbing, box\_grabbed.
  * These states inform real-time planning and feedback to ensure smooth interaction with the environment.

* **Logical Constraint Handling:**

  * Convert natural language instructions into actionable logic.
  * Examples of commands:

    * "Stack the blue box on the red box" → `stack(blue_box, red_box)`
    * "Place the red box near the north wall" → `place(red_box, location=north_wall)`

* **Action Execution:**

  * Use parsed logic to generate executable commands like:

    * `walk(0.5ft_forward)`
    * `crouch()`
    * `grab(box_id)`

---

### 4. **Object Sorting and Planning**

* **Stacking Planner:**

  * Implement a system to determine the correct order of stacking based on object attributes:

    * **Color**
    * **Size**
    * **Basic Geometric Shape**

* **Decision Making:**

  * The system makes decisions using the current object metadata and spatial awareness to plan tasks such as stacking and placement.

---

## Project Checklist and Milestones

### **1. Gripping System and Object Detection:**

* [ ] Integrate point cloud processing pipeline for object detection.
* [ ] Implement bounding box generation around objects.
* [ ] Develop center of gravity estimation algorithm.
* [ ] Optimize flat-plane contact for gripper alignment.
* [ ] Test and calibrate pressure sensor feedback for secure gripping.

### **2. Multimodal Perception and Language Interface:**

* [ ] Integrate speech-to-text layer for natural language processing.
* [ ] Implement object detection using RGB and depth camera combination.
* [ ] Annotate bounding boxes and link to environmental landmarks.
* [ ] Parse natural language commands into actionable logic for the robot.

### **3. Environment Awareness and State Tracking:**

* [ ] Develop internal state management system for robot actions.
* [ ] Convert natural language instructions into logical actions.
* [ ] Implement real-time state tracking for environment awareness.

### **4. Object Sorting and Planning:**

* [ ] Build the object sorting and stacking planner based on color, size, and shape.
* [ ] Ensure spatial awareness is used for correct placement and ordering of objects.

---

## How to Use

1. **Installation:**
   Follow the installation steps below to set up the necessary dependencies and hardware setup for running the system.

2. **Running the System:**
   To begin using the system, simply launch the program and speak your commands (e.g., "Grab the green box" or "Stack the blue box on the red box").

3. **Command Syntax:**

   * **Grab Object:** `Grab [object_name]`
   * **Place Object:** `Place [object_name] [location]`
   * **Stack Objects:** `Stack [object_name] on [object_name]`

---

## Requirements

* Python 3.8+
* ROS (Robot Operating System) for robot control
* OpenCV for computer vision tasks
* Point Cloud Library (PCL) for 3D processing
* A compatible robotic manipulator with grippers and sensors
* Depth and RGB cameras

---

## Contributors

* **BMK** – Proof of concept development
* **Proffesor Alan Fern** – Project inspiration, OSU

---

##V1.0 of box stacking system ![image](https://github.com/user-attachments/assets/29004706-4398-443b-9867-7dabdbd538ab)

