# Triangle Detector ROS 2 Node

This repository contains a ROS 2 (Crystal-compatible) Python node that uses a trained YOLOv8 model to detect sticks in an image, build triangle meshes from their positions, and publish the optimal centroid and triangle geometry for robotic earth injection or spatial computation.

## Features
- Runs YOLOv8 inference using Ultralytics
- Calculates triangle meshes from detected sticks
- Selects optimal triangle (smallest area)
- Publishes:
  - `/triangle_centroid` (geometry_msgs/Point)
  - `/triangle_vertices` (std_msgs/Float32MultiArray)
- Records output using ros2 bag

## File Structure
```
triangle_detector_ws/
├── src/
│   └── triangle_detector/
│       ├── triangle_detector/
│       │   └── triangle_detector_node.py
│       ├── resource/
│       ├── package.xml
│       ├── setup.py
│       └── setup.cfg
├── test.jpg
├── best.pt
├── data.yaml
```

## Quickstart (Docker/Local)
```bash
# Start ROS 2 environment (e.g., inside Docker or local Crystal setup)
source /opt/ros/crystal/setup.bash

# Build the workspace
colcon build
source install/setup.bash

# Run the node
ros2 run triangle_detector triangle_detector_node

# Record the data to a bag file
ros2 bag record /triangle_centroid /triangle_vertices
```

## ROS Topics
| Topic | Type | Description |
|-------|------|-------------|
| `/triangle_centroid` | `geometry_msgs/Point` | Centroid of the smallest triangle |
| `/triangle_vertices` | `std_msgs/Float32MultiArray` | Flattened triangle vertices (x1, y1, x2, y2, x3, y3) |

## Input Files
- `test.jpg`: input image to analyze
- `best.pt`: YOLOv8 trained model weights
- `data.yaml`: YOLO class map (should contain `sticks` label)

## Requirements
- ROS 2 Crystal
- Python 3.6+
- Packages:
  - `ultralytics`
  - `opencv-python`
  - `PyYAML`
  - `rclpy`
  - `geometry_msgs`, `std_msgs`

## Future Improvements
- Real-time image stream via camera
- Add image publishing (`sensor_msgs/Image`)
- Export to Grasshopper or 3D printing tools
- Package as installable Python module

## Credits
Developed as part of an academic research project on AI-driven robotic fabrication. Powered by YOLOv8, ROS 2, and OpenCV.
