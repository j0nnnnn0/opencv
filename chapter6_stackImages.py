import cv2
import numpy as np
 
 
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray&#91;0])
    rowsAvailable = isinstance(imgArray&#91;0], list)
    width = imgArray&#91;0]&#91;0].shape&#91;1]
    height = imgArray&#91;0]&#91;0].shape&#91;0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray&#91;x]&#91;y].shape&#91;:2] == imgArray&#91;0]&#91;0].shape &#91;:2]:
                    imgArray&#91;x]&#91;y] = cv2.resize(imgArray&#91;x]&#91;y], (0, 0), None, scale, scale)
                else:
                    imgArray&#91;x]&#91;y] = cv2.resize(imgArray&#91;x]&#91;y], (imgArray&#91;0]&#91;0].shape&#91;1], imgArray&#91;0]&#91;0].shape&#91;0]), None, scale, scale)
                if len(imgArray&#91;x]&#91;y].shape) == 2: imgArray&#91;x]&#91;y]= cv2.cvtColor( imgArray&#91;x]&#91;y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = &#91;imageBlank]*rows
        hor_con = &#91;imageBlank]*rows
        for x in range(0, rows):
            hor&#91;x] = np.hstack(imgArray&#91;x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray&#91;x].shape&#91;:2] == imgArray&#91;0].shape&#91;:2]:
                imgArray&#91;x] = cv2.resize(imgArray&#91;x], (0, 0), None, scale, scale)
            else:
                imgArray&#91;x] = cv2.resize(imgArray&#91;x], (imgArray&#91;0].shape&#91;1], imgArray&#91;0].shape&#91;0]), None,scale, scale)
            if len(imgArray&#91;x].shape) == 2: imgArray&#91;x] = cv2.cvtColor(imgArray&#91;x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
 
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
imgStack = stackImages(0.5,(&#91;img,imgGray,img],&#91;img,img,img]))
 
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
cv2.imshow("ImageStack",imgStack)
 
cv2.waitKey(0)