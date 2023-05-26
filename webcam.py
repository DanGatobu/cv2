import cv2

cap=cv2.VideoCapture(0)# camera id use 0 to use default webcam#
cap.set(3,640) #id for width is 3#
cap.set(4,480) # id for height is 4#
cap.set(10,10) #id for brightness is 10#
while True:
    success,img = cap.read() # cap.read reaturns a boolean if the frame is read correctly then its true#
    cv2.imshow("video",img)
    
    if cv2.waitKey(1)==ord("q"):
        break 

