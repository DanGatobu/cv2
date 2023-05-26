import cv2
import numpy as np

img=cv2.imread("resouces/shao.jpg")

print(img.shape) # find size of image

imgresize=cv2.resize(img,(800,600)) #width first  first then width usually height  * width

imgcrop= img[30:500,200:1000]  #height first
cv2.imshow("image",img)
cv2.imshow("resized",imgresize)
cv2.imshow("cropped",imgcrop)

cv2.waitKey(0)