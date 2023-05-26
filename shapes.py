import cv2
import numpy as np

img= np.zeros ((512,512,3),np.uint8)
img[:] = 255,0,0 #bgr
cv2.line(img,(0,0),(300,300),(0,255,0),3) # (img.shape[1],img.shape[0]) will display a line across the whole image
cv2.rectangle(img,(0,0),(250,300),(0,0,255),2,cv2.FILLED)
cv2.circle(img,(240,240),30,(255,255,7),5)
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_PLAIN,1,(16,70,0),1)
print(img.shape)
cv2.imshow("image",img)
cv2.waitKey(0)