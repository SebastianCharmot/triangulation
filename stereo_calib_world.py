import cv2 as cv
import numpy as np 

imgpoints_black = np.array([(954,353),(1486,373),
                     (453,787),(1674,917),
                     
                     (727,413),(730,478),(797,485),
                     (1628,450),(1542,525),(1622,526),
                     
                     (1150,504)], dtype=np.float32) # 2d points in image plane.


imgpoints_blue = np.array([(560,322),(1085,314),
                    (385,852),(1598,765),
                    
                    (422,400),(430,473),(507,471),
                    (1313,376),(1246,450),(1308,446),
                    
                    (888,460)], dtype=np.float32)

real_world_pts = np.array([(-76.25,137,0),(76.25,137,0),
                           (76.25,-137,0),(76.25,-137,0),

                            (-91.5,0,15.25),(-91.5,0,0),(-76.25,0,0),
                            (91.5,0,15.25),(91.5,0,0),(76.25,0,0),

                            (0,0,0)], dtype=np.float32)

width = 1920
height = 1080

criteria=(cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)

stereocalibration_flags = cv.CALIB_FIX_INTRINSIC

def stereo_calibrate(mtx0, dist0, mtx1, dist1):
    ret, CM1, dist0, CM2, dist1, R, T, E, F = cv.stereoCalibrate([real_world_pts], [imgpoints_black], [imgpoints_blue], mtx0, dist0,
                                                                 mtx1, dist1, (width, height), criteria = criteria, flags = stereocalibration_flags)
    print('rmse: ', ret)
    cv.destroyAllWindows()
    return R, T

mtx0 = np.load('camera_calibration_long_ass.npz')['mtx']
dist0 = np.load('camera_calibration_long_ass.npz')['dist']
mtx1 = np.load('camera_calibration_long_ass.npz')['mtx']
dist1 = np.load('camera_calibration_long_ass.npz')['dist']

R,T = stereo_calibrate(mtx0=mtx0,dist0=dist0,
                 mtx1=mtx1,dist1=dist1)

np.savez('stereo_calib_R_T_world.npz', R=R, T=T)