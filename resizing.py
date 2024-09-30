import cv2
import numpy as np
img = cv2.imread("C:/Users/ARYAN PUND/Pictures/Camera Roll/p.jpg")
print(img.shape)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)
imgCropped = img[0:200,200:500]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Crop",imgCropped)
cv2.waitKey(0)
