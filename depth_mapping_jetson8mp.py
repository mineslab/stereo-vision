import cv2
import numpy as np
from matplotlib import pyplot as plt
from CustomCalibrateCamera.Stereo_Calib_Camera import stereoCalibrateCamera
from CustomCalibrateCamera.Stereo_Calib_Camera import getStereoCameraParameters

import Camera.jetsonCam as jetCam
cam1 = jetCam.jetsonCam()
cam2 = jetCam.jetsonCam()


cam1.open(sensor_id=1,
          sensor_mode=3,
          flip_method=0,
          display_height=540,
          display_width=960,
        )
cam2.open(sensor_id=0,
          sensor_mode=3,
          flip_method=0,
          display_height=540,
          display_width=960,
        )

cam1.start()
cam2.start()
#stereoCalibrateCamera(cam1,cam2,'CustomCalibrateCamera/jetson_stereo_8MP',24)
lod_data = getStereoCameraParameters('CustomCalibrateCamera/jetson_stereo_8MP.npz')



camera_matrix_left = lod_data[0]
dist_coeffs_left =  lod_data[1]
camera_matrix_right =  lod_data[2]
dist_coeffs_right =  lod_data[3]
R =  lod_data[4]
T =  lod_data[5]
#print camera matrix
print("RAW camera matrix")
print(camera_matrix_right)
print(camera_matrix_left)


ret,img_s = cam1.read()
if ret:
  image_size = (img_s.shape[1],img_s.shape[0])
  print(image_size)
  
else:
  cam1.stop()
  cam2.stop()
  cam1.release()
  cam2.release()
  exit()

#stereo rectify
R1,R2,P1,P2,Q,roi1,roi2= cv2.stereoRectify(camera_matrix_left,dist_coeffs_left, camera_matrix_right, dist_coeffs_right, image_size, R, T)


# Create a StereoBM object
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)




# Load rectification maps
map1_left, map2_left = cv2.initUndistortRectifyMap( camera_matrix_left, dist_coeffs_left, R1, P1, image_size, cv2.CV_16SC2)
map1_right, map2_right = cv2.initUndistortRectifyMap(camera_matrix_right, dist_coeffs_right, R2, P2, image_size, cv2.CV_16SC2)

while True:
   # Read stereo images
   ret,image_left = cam1.read()
   ret, image_right = cam2.read()
   
   cv2.imshow('image_left',image_left)
   cv2.imshow('image_right',image_right)
   # Remap the images using rectification maps
   rectified_left = cv2.remap(image_left, map1_left, map2_left, cv2.INTER_LINEAR)
   rectified_right = cv2.remap(image_right, map1_right, map2_right, cv2.INTER_LINEAR)

   #cv2.imshow('image_left_r',rectified_left)
   #cv2.imshow('image_right_r',rectified_right)
   # Convert images to grayscale
   gray_left = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2GRAY)
   gray_right = cv2.cvtColor(rectified_right, cv2.COLOR_BGR2GRAY)

   # Compute disparity map
   disparity = stereo.compute(gray_left, gray_right)
   #print(disparity)
   # Convert disparity to depth (using the formula: depth = baseline * focal_length / disparity)
   baseline = np.linalg.norm(T)  # Magnitude of translation vector
   focal_length = camera_matrix_left[0, 0]  # Focal length (assuming both cameras have the same)
   
   #baseline = 70
   #focal_length = 3.4 
   depth_map = (baseline * focal_length) / disparity

   #print(focal_length)
   #print(baseline)
   #print(depth_map)
   # Display the depth map
   cv2.imshow('Depth Map', (depth_map / np.max(depth_map)).astype(np.uint8))
   #cv2.imshow('dispar',disparity*100)
   cv2.imshow('dep',(depth_map *(-100)).astype(np.uint8))
   k=cv2.waitKey(10)
   if k == ord('x'):
     break

cv2.destroyAllWindows()
cam1.stop()
cam2.stop()
cam1.release()
cam2.release()


