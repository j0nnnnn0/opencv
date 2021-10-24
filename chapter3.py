import cv2
import numpy as np


#import photo
img = cv2.imread("resources/lambo.png")
print(img.shape)

# Resize an image
imgResize = cv2.resize(img, (300,200)) #width, height
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)

# Crop an image
imgCropped = img[0:200, 200:500] # height, width
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)