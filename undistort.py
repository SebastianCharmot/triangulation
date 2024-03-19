import cv2 as cv
import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image_path = "footage/black_bounce/0.png"
img = mpimg.imread(image_path)

print(img.shape)

# cv.imwrite('original.png', img)

w = 1920
h = 1080

mtx0 = np.load('camera_calibration_long_ass.npz')['mtx']
dist0 = np.load('camera_calibration_long_ass.npz')['dist']

newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx0, dist0, (w,h), 1, (w,h))

# undistort
dst = cv.undistort(img, mtx0, dist0, None, newcameramtx)

 
# crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('black_undistort.png', dst)

plt.imshow(dst)
plt.savefig('black_undistort.png')