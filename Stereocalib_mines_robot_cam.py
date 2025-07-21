import cv2
from StereoCameraCalibrate.Stereo_Calib_Camera import stereoCalibrateCamera
from StereoCameraCalibrate.Stereo_Calib_Camera import getStereoCameraParameters
from StereoCameraCalibrate.Stereo_Calib_Camera import getStereoSingleCameraParameters


cam1 = cv2.VideoCapture('/dev/video0')
cam2 = cv2.VideoCapture('/dev/video2')

# Camera Calibration
stereoCalibrateCamera(cam1, cam2, 'mines_robot_cam', 25, (7, 7)) # chessboard square size = 25mm, chessboard grid size = (7, 7)

# Load the calibrated parameters
lod_data = getStereoCameraParameters('mines_robot_cam.npz')
lod_datac1 = getStereoSingleCameraParameters('mines_robot_cam_c1.npz')
lod_datac2 = getStereoSingleCameraParameters('mines_robot_cam_c2.npz')

camera_matrix_left = lod_data[0]
dist_coeffs_left =  lod_data[1]
camera_matrix_right =  lod_data[2]
dist_coeffs_right =  lod_data[3]
R =  lod_data[4]
T =  lod_data[5]

#print camera matrix
print(lod_datac1[0])
print(lod_datac2[0])
print(lod_datac1[1])
print(lod_datac2[1])

cv2.destroyAllWindows()
cam1.release()
cam2.release()


