# Project Pickup Line

***"Real Artificial Intelligence stands at the convergence of hard logic, and flexible logic, the mind in my experience utilizes separate tools and communicates between them, such shall AI."***

## Overview

**Project Pickup Line** is a cutting-edge autonomous navigation system designed to demonstrate that it is possible to map out rooms, track objects, and enable robots or systems to autonomously navigate toward those objects without relying on AI technologies. Instead of AI-driven decision-making, **Project Pickup Line** leverages hardcoded systems to perform the logical computations. However, to elevate the project to the next level, artificial intelligence (AI) technologies such as Large Language Models (LLMs) and Computer Vision (CV) systems are integrated to enable voice control and interaction.

The core concept behind **Project Pickup Line** is to use AI as an interface and agent that acts as a bridge between the human user and the hardcoded logical systems. This allows the AI to interpret voice commands, and process environmental data, but the logic of navigation, decision-making, and mapping comes from well-structured, reliable, and transparent hardcoded systems.

## Key Features

* **Room Mapping**: The system maps out rooms using hardcoded algorithms, allowing for the precise identification of objects and rooms without requiring AI-based mapping solutions.

* **Object Identification & Tracking**: Objects within the room are identified and tracked by using predefined algorithms, avoiding the complexity and uncertainty associated with AI-driven object recognition systems.

* **Autonomous Navigation**: The system can autonomously navigate through a space to reach specific objects based on the predefined logical paths, algorithms, and mapping data. The logic engine ensures that the robot or system can find its way around with precision and reliability.

* **Voice Control**: By integrating AI technologies such as Large Language Models (LLMs) and Computer Vision (CV), users can control the system with natural language commands. The AI interprets voice commands (e.g., "Pick up the coffee mug on the table") and then communicates those instructions to the hardcoded logic system for processing.

* **AI as an Interface**: The AI does not perform the logical processing but instead serves as an intermediary. It translates human commands into a format the hardcoded logic system understands, forming a symbiotic relationship where the AI complements the logical computation without replacing it.

## Goals

* **Proving Autonomous Navigation Without AI**: Demonstrate that autonomous systems do not need AI technologies to handle tasks such as room mapping, object identification, and navigation. Hardcoded systems can handle these tasks effectively with greater transparency, stability, and reliability.

* **Symbiotic Relationship Between AI & Hardcoded Systems**: Show how AI can work with hardcoded systems in a way that each fulfills its purpose. AI provides a conversational interface and user interaction layer, while hardcoded systems execute the underlying logical tasks such as navigation and decision-making.

* **Real-World Applications**: Enable practical applications such as autonomous home assistants, smart room systems, and robots that can be used in real-world environments without being overly dependent on complex AI systems.

## Technical Details

### System Architecture

1. **Hardcoded Logical Systems**:

   * The navigation and room mapping are done using hardcoded systems based on algorithms such as grid-based pathfinding (e.g., A\* or Dijkstra’s algorithm) and object tracking systems that utilize sensors and predefined rules for locating and identifying objects.
   * Object location is computed by referencing a mapped grid of the room and its environmental features.
2. **AI Technologies (LLM & CV)**:

   * Large Language Models (LLMs) interpret voice commands and provide feedback to the user.
   * Computer Vision (CV) can be integrated to provide visual recognition of objects and environmental context. This can work with cameras to visually detect and verify object placements for better precision in object identification and task completion.
3. **Symbiotic Relationship**:

   * AI is used to interface with the user and provide voice interaction and interpretation of commands. It sends the commands to the logical system, which then processes them and guides the autonomous system.
   * The logic system uses precise, hardcoded computations to achieve accurate navigation and object manipulation, where AI fails due to its unpredictability or inaccuracy.

### Technology Stack

* **Python**: For implementing hardcoded systems, room mapping algorithms, and logic processing.
* **Speech Recognition**: To allow the system to accept voice commands via microphone input.
* **Computer Vision Libraries (OpenCV)**: For object detection and room analysis using cameras.
* **Navigation Algorithms**: Pathfinding algorithms such as A\* or Dijkstra’s for room mapping and navigation.
* **Natural Language Processing (NLP)**: For handling voice commands with LLMs, such as OpenAI’s GPT models for interpreting instructions.

## Usage

1. **Voice Commands**:

   * You can issue commands such as:

     * "Navigate to the red box."
     * "Stack the blue boxes next to the larger ones."
     * "Where did you put the larger boxes?"

   The AI will interpret these commands and use the logical system to perform the required task.

2. **Autonomous Navigation**:

   * The system will autonomously navigate to the specified object using the pre-configured room map and navigation algorithms.

3. **Object Tracking**:

   * Object positions will be continuously tracked and updated on the system’s map, ensuring real-time accuracy.

## Contributing

We welcome contributions to **Project Pickup Line**! If you have suggestions, bug reports, or want to enhance the system, feel free to fork the repository and create a pull request.

### Steps to Contribute

1. Fork the repository and clone it locally.
2. Make your changes or additions in a new branch.
3. Test your changes thoroughly.
4. Create a pull request with a detailed description of your changes.

## License

**Project Pickup Line** is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Project Pickup Line** combines the reliability of hardcoded logic with the flexibility of AI to create an efficient and robust autonomous navigation system, while pushing the boundaries of voice control and user interaction. Through this project, we show that AI can complement but not always replace the power of traditional computational systems in real-world applications.

## Requirements

* Python 3.8+
* IMU
* ROS (Robot Operating System) for robot control
* OpenCV for computer vision tasks
* Point Cloud Library (PCL) for 3D processing
* A compatible robotic manipulator with grippers and sensors for detetcion of pressure on grippers.
* Depth and RGB cameras

---

## Contributors

* **BMK** – Proof of concept development
* **Proffesor Alan Fern** – Project inspiration, OSU

---

## V1.0 of box stacking system 
![image](https://github.com/user-attachments/assets/29004706-4398-443b-9867-7dabdbd538ab)

## V1.1 of stacking with geospatial tags and constraints in generation.

![image](https://github.com/user-attachments/assets/31a60e31-c2ae-4981-b292-46f795a24b9e)

## V1.0 of the pointcloud generation system for testing enviromental detection.

![image](https://github.com/user-attachments/assets/6002c8cc-e76a-4da5-b0c6-d4afd00f37c5)

## The rebuilt walls from the noisy pointcloud with missing data points and objects inside.

![image](https://github.com/user-attachments/assets/13fe95ed-3133-4ff2-a02b-cd2097a2f4d7)

## V1.2 of the stacking system.
This version allows it to have constrainst such as (Place red only on yellow) or only stack red boxes, or locational systems using an integrated IMU which allows it to be later connected to a LLM which converts text to these forms of commands.
(NOTE this system can be utilized for any constraint such as shape, size, orientation, color, weight, location, anything.)

![image](https://github.com/user-attachments/assets/ad5927e4-bba3-4044-bfa1-6a8363b21210)

## V1.5 of the reconstruction system taht allows for the recognition of objects in a scene such as boxes or items and assigning them adaptive bounding boxes.
The goal of this system is to allow a stable refrence to the general location of objects in refrence to self location collected from markers such as other objects and walls.

![image](https://github.com/user-attachments/assets/8e539318-386f-4c24-a069-222eaf6206e4)

## V1.0 Goal deduction and transformance into JSON format to later be processed utilizing hardcoded systems of movement and stacking planning utilizing NUExtract-tiny-v1.5 which has seemed to work the best.

![image](https://github.com/user-attachments/assets/4789d481-c3c3-4ceb-a6c1-a42e02893408)

## V1.6 of the recponstruction system that rebuilds the bounding boxes of the boxes in the area instead of convex hulls, and then utilizes radial coordinates and labeling from the center of the room to craft a consistant local coordinate system.

![image](https://github.com/user-attachments/assets/0e136c9e-f702-4dc1-9189-b0da26a6a13f)





