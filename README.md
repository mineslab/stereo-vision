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
1. Jetson nano B01 developement board.
2. Two raspberry pi V2 camera (8MP sony IMX219 sensor)
3. 64gb memorycard with jetson OS installed
4. 5A 5V power supply (The stable power supply is important when utilizing cuda for both opencv and open3d, otherwise jetson board turn off automatically due to volatge drop caused by increased current consumption )

### Setting up stereo camera using two raspberry pi V2 8MP cameras.
Creating a stereo camera using two identical cameras involves setting up the cameras in such a way that they capture images from slightly different viewpoints, mimicking the separation of human eyes. Here's a general outline of how you can do it:

#### Selecting Cameras: 
Choose two identical cameras with similar specifications in terms of resolution, frame rate, and lens characteristics. It's essential to ensure that both cameras have a synchronized shutter mechanism to capture images simultaneously.
#### Mounting the Cameras: 
Mount the two cameras side by side on a stable platform. The distance between the cameras should approximate the interocular distance of human eyes, typically around 6-7 centimeters.
#### Calibrating Cameras:
Calibrate both cameras to ensure that they provide accurate and consistent measurements. Camera calibration involves determining intrinsic parameters (like focal length and lens distortion) and extrinsic parameters (like camera position and orientation).
#### Synchronization: 
Synchronize the shutter triggers of both cameras to capture images simultaneously. This synchronization is crucial for accurate stereo vision, ensuring that the images captured by both cameras correspond to the same instant in time.
#### Capturing Images: 
Configure both cameras to capture images simultaneously. Depending on the cameras you're using, you may need to use software provided by the camera manufacturer or develop your software to control the cameras and capture images.
#### Image Processing: 
Once you have captured images from both cameras, you'll need to process them to extract depth information. This process involves identifying corresponding points in the images (matching features) and calculating the disparity between these points. Various stereo vision algorithms, such as block matching, semi-global matching, or deep learning-based approaches, can be used for this purpose.
#### Depth Reconstruction: 
Using the calculated disparities, you can reconstruct the depth information of the scene. By triangulating corresponding points in the stereo image pairs, you can estimate the distance of objects from the cameras.
#### Integration: 
Integrate the stereo camera setup into your application or system. This might involve developing software to control the stereo camera, process the captured images, and utilize the depth information for specific tasks such as object detection, 3D reconstruction, or navigation.
