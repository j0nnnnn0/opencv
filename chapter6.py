import cv2
import numpy as np
from chapter6_stackImages import stackImages

# Join images together 

img = cv2.imread('resources/lena.png')
# cv2.imshow("image", img)

# #Stacking img horizontally
# imgHor = np.hstack((img,img))

# # Stacking img vertically
# imgVer = np.vstack((img,img))

# Using the function stackImages to handle images of different types
imgStack = stackImages(0.5,([img,img,img]))

# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)
cv2.imshow("ImageStack", imgStack)



cv2.waitKey(0)