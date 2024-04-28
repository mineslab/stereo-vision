# Stereo camera depth estimation and Visualization using open3D with cuda support
Brief: Stereo vision based depth estimation with opencv and jetson nano with cuda support and visualization with point cloud and open3d

## Stereo vision

Stereo vision, often referred to as stereopsis, is a remarkable aspect of human visual perception and a fundamental concept in computer vision and robotics. It's the ability of the brain to perceive depth by processing the slightly different images captured by our two eyes. Each eye sees the world from a slightly different perspective, due to their separation, and the brain combines these two perspectives to create a three-dimensional representation of the environment.
This phenomenon is crucial for tasks such as depth perception, object recognition, and spatial awareness. In technology, stereo vision is mimicked through stereo cameras or sensor arrays, which capture images or data from two slightly different viewpoints, akin to human eyes. By analyzing the disparities between these viewpoints, algorithms can calculate depth information, enabling machines to perceive and understand the three-dimensional structure of the world around them.
Applications of stereo vision span various fields, including autonomous vehicles, robotics, augmented reality, medical imaging, and surveillance systems. Its ability to accurately perceive depth makes it a powerful tool for tasks that require spatial understanding and interaction with the physical world. As technology advances, stereo vision continues to play a pivotal role in enhancing machine perception and enabling intelligent systems to operate more effectively in complex environments.

## Steps involved
1. Required hardwares.
2. Setting up stereo camera using two raspberry pi V2 8MP cameras.
3. Calibrating the stereo camera.
4. Stereo depth estimation with cpu, visualization of depth with heat map.
5. Stereo depth estimation with cuda acceleration, visualization of depth with heat map.
6. Stereo depth estimation with cuda acceleration, visualization of depth with point cloud and open3d.

### 1. Required hardwares.
1. Jetson nano B01 developement board.
2. Two raspberry pi V2 camera (8MP sony IMX219 sensor)
3. 64gb memorycard with jetson OS installed
4. 5A 5V power supply (The stable power supply is important when utilizing cuda for both opencv and open3d, otherwise jetson board turn off automatically due to volatge drop caused by increased current consumption )

### Setting up stereo camera using two raspberry pi V2 8MP cameras.
Creating a stereo camera using two identical cameras involves setting up the cameras in such a way that they capture images from slightly different viewpoints, mimicking the separation of human eyes. Here's a general outline of how you can do it:

1. #### Selecting Cameras: Choose two identical cameras with similar specifications in terms of resolution, frame rate, and lens characteristics. It's essential to ensure that both cameras have a synchronized shutter mechanism to capture images simultaneously.
2. #### Mounting the Cameras: 
Mount the two cameras side by side on a stable platform. The distance between the cameras should approximate the interocular distance of human eyes, typically around 6-7 centimeters.

3. #### Calibrating Cameras:
Calibrate both cameras to ensure that they provide accurate and consistent measurements. Camera calibration involves determining intrinsic parameters (like focal length and lens distortion) and extrinsic parameters (like camera position and orientation).

4. #### Synchronization: 
Synchronize the shutter triggers of both cameras to capture images simultaneously. This synchronization is crucial for accurate stereo vision, ensuring that the images captured by both cameras correspond to the same instant in time.

5. #### Capturing Images: 
Configure both cameras to capture images simultaneously. Depending on the cameras you're using, you may need to use software provided by the camera manufacturer or develop your software to control the cameras and capture images.

6. #### Image Processing: 
Once you have captured images from both cameras, you'll need to process them to extract depth information. This process involves identifying corresponding points in the images (matching features) and calculating the disparity between these points. Various stereo vision algorithms, such as block matching, semi-global matching, or deep learning-based approaches, can be used for this purpose.

7. #### Depth Reconstruction: 
Using the calculated disparities, you can reconstruct the depth information of the scene. By triangulating corresponding points in the stereo image pairs, you can estimate the distance of objects from the cameras.

### 2. Calibrating the stereo camera.
In the stereo camera calibration process, several parameters are identified or determined to ensure accurate reconstruction of 3D scenes from the stereo image pairs. These parameters can be categorized into intrinsic and extrinsic parameters:
#### Intrinsic Parameters: These parameters characterize the internal properties of each camera, including:
1. Focal Length (fx, fy): The distance from the camera's optical center to the imaging plane, usually expressed in pixels. 
2. Optical Center (cx, cy): The coordinates of the principal point, where the optical axis intersects the imaging plane.
3. Lens Distortion: Distortions caused by imperfections in the camera lens, typically modeled using radial and tangential distortion coefficients.
4. Image Sensor Format: The physical dimensions of the camera's image sensor, which affect the field of view and image distortion.
#### Extrinsic Parameters: These parameters describe the spatial relationship between the two cameras in the stereo setup, including:
1. Rotation Matrix (R): Describes the rotation of one camera relative to the other.
2. Translation Vector (T): Represents the translation of one camera relative to the other in 3D space.
3. Stereo Baseline: The distance between the optical centers of the two cameras, which affects the depth perception capability.
4. Stereo Alignment: The alignment of the two cameras relative to each other, ensuring that their imaging planes are parallel and their optical axes are properly oriented.

During the calibration process, a set of calibration images containing known calibration patterns (such as chessboard patterns or dot grids) are captured using both cameras. These images are then used to estimate the intrinsic and extrinsic parameters through optimization techniques such as nonlinear least squares optimization.
The calibration algorithm analyzes the correspondences between points on the calibration pattern as seen by both cameras and iteratively adjusts the camera parameters to minimize the reprojection error—the difference between the observed image points and the corresponding points predicted by the calibrated camera model.
Once the calibration process is complete, the identified intrinsic and extrinsic parameters are used to rectify stereo image pairs, undistort images, and compute the disparity map necessary for depth reconstruction in stereo vision applications. Overall, accurate calibration is essential for ensuring precise and reliable depth estimation and 3D reconstruction in stereo camera systems.
