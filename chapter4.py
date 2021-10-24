import cv2
import numpy as np

# Draw shapes and text on images

#Set color of image
img = np.zeros((512,512,3),np.uint8) # 0 to 255 (RGB)
#print(img.shape)
# img[:] = 255,0,0 #Set whole image in blue for width:height

#Create a line
#cv2.line(img,(0,0), (300,300), (0,255,0), 3) # start, end, colour, thickness
cv2.line(img,(0,0), (img.shape[1],img.shape[0]), (0,255,0), 3) # using the img.shape for start, end, colour, thickness

# Create a rectangle and fill it
cv2.rectangle(img,(0,0), (250,350), (0,0,255), cv2.FILLED)

# Create a circle and fill it
cv2.circle(img, (200,400), 105, (160,160,0), cv2.FILLED)

# Add text to image
cv2.putText(img, "OPENCV ", (300,100),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,150,0),3)


cv2.imshow("Image", img)


cv2.waitKey(0)