import cv2
print("package imported")
img=cv2.imread("resouces/test.png")
cv2.imshow("Output",img)
cv2.waitKey(0)