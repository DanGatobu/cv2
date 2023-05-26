import cv2
cap=cv2.VideoCapture("resouces/traping.mp4")
while True:
    success,img = cap.read() # cap.read reaturns a boolean if the frame is read correctly then its true#
    cv2.imshow("video",img)
    
    if cv2.waitKey(1)==ord("q"):
        break 
# ord is a function used to convert a single unicode character to its integer equivalent#
