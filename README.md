# Stereo camera depth estimation and Visualization using open3D with cuda support
Brief: Stereo vision based depth estimation with opencv and jetson nano with cuda support and visualization with point cloud and open3d

## Stereo vision

Stereo vision, often referred to as stereopsis, is a remarkable aspect of human visual perception and a fundamental concept in computer vision and robotics. It's the ability of the brain to perceive depth by processing the slightly different images captured by our two eyes. Each eye sees the world from a slightly different perspective, due to their separation, and the brain combines these two perspectives to create a three-dimensional representation of the environment.
This phenomenon is crucial for tasks such as depth perception, object recognition, and spatial awareness. In technology, stereo vision is mimicked through stereo cameras or sensor arrays, which capture images or data from two slightly different viewpoints, akin to human eyes. By analyzing the disparities between these viewpoints, algorithms can calculate depth information, enabling machines to perceive and understand the three-dimensional structure of the world around them.
Applications of stereo vision span various fields, including autonomous vehicles, robotics, augmented reality, medical imaging, and surveillance systems. Its ability to accurately perceive depth makes it a powerful tool for tasks that require spatial understanding and interaction with the physical world. As technology advances, stereo vision continues to play a pivotal role in enhancing machine perception and enabling intelligent systems to operate more effectively in complex environments.

## Steps involved
1. Required hardwares.
2. Setting up stereo camera using two raspberry pi V2 8MP cameras.
3. calibrating the stereo camera.
4. Stereo depth estimation with cpu, visualization of depth with heat map.
5. Stereo depth estimation with cuda acceleration, visualization of depth with heat map.
6. Stereo depth estimation with cuda acceleration, visualization of depth with point cloud and open3d.

### Required hardwares.
