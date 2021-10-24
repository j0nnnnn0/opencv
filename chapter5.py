import cv2
import numpy as np

# Warp perspective (to get birds eye view)

img = cv2.imread("resources/cards.jpg")

# Define the width and height of the image
width, height = 250,350

#Declare points of the part of the image we want to capture
# this is the points of the king of spades
pts1 = np.float32([[111,219], [287,188],[154,482], [352,440]])
# Define the points origin
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
# Set the matrix of the transform
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# Define the output of the warped image
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)