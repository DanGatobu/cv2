import cv2
import numpy as np

img=cv2.imread("resouces/cadi.jpg")
imgresize=cv2.resize(img,(510,510))
width,height=3000,4000


print(img.shape)
points=np.float32([[897,2329],[2017,1641],[2433,2409],[1377,3081]])
points2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix= cv2.getPerspectiveTransform(points,points2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))
print(imgoutput.shape)

imgresized=cv2.resize(imgoutput,(510,510))


cv2.imshow("image",imgresize)
cv2.imshow("warp",imgresized)

cv2.waitKey(0)
