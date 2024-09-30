import cv2
import numpy as np
img = cv2.imread('C:/Users/ARYAN PUND/Pictures/Camera Roll/WIN_20240810_14_33_39_Pro.jpg')

imghor = np.hstack((img,img))
imgver = np.vstack((img,img))
cv2.imshow("Horizontal", imghor)
cv2.imshow("Vertical",imgver)
cv2.waitKey(0)