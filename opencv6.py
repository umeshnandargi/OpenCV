import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()