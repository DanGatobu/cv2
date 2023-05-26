import cv2
import numpy as np
img = cv2.imread("resouces/test.png")
kernel= np.ones((5,5),np.uint8)                   #np.one returns an array with just ones
imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #cvtcolour converts an image into different color spaces#
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,40,50)
imgDilation= cv2.dilate(imgCanny,kernel,iterations=1)
imgeroded=cv2.erode(imgCanny,kernel,iterations=1 )
cv2.imshow("grayimage",imgGray)
cv2.imshow("blurimage",imgBlur)
cv2.imshow("cannyimage",imgCanny)
cv2.imshow("Dilation image",imgDilation)
cv2.imshow("Eroded image",imgeroded)

cv2.waitKey(0)