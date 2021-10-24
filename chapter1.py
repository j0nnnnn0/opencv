import cv2
import numpy as np

#import an imagine and display with infinite wait time
#img = cv2.imread("resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

#import a video
#cap = cv2.VideoCapture("resources/test_video.mp4")

# # import webcam
# cap = cv2.VideoCapture(0) # id of webcam
# cap.set(3, 640) # set width
# cap.set(4, 480) # set height
# cap.set(10, 100) # set the brightness

# # as a video is a set of photos, we use a loop to display each photos in a video
# # we set q to quit
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#import photo
img = cv2.imread("resources/lena.png")

# set kernel for image dialation
kernel = np.ones((5,5), np.uint8) # values can be from 0 to 255 (grey scale)

#set to grey scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur function for grey image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7),0) # set blurness, has to be odd number
# edge detector (canny - a reversed image)
imgCanny = cv2.Canny(img, 100, 100)
# dialate
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# Erode
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erosion Image", imgErode)
cv2.waitKey(0)



