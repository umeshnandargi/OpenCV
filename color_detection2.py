import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX

    cx = int(width/2)
    cy = int(height/2)
    pixel_center = hsv[cx, cy]
    pixel_center_bgr = frame[cy, cx]

    hue = pixel_center[0]
    
    color = ""
    if hue<5:
        color = 'RED'
    elif hue< 22:
        color = 'ORANGE'
    elif hue< 35:
        color = 'YELLOW'
    elif hue< 78:
        color= "GREEN"
    elif hue<131:
        color = 'BLUE'
    elif hue< 167:
        color = "VIOLET"
    else:
        color = "RED"

    cv2.putText(frame, color , (cx - 200, 100), 0, 2, (0,0,0), 5, lineType=cv2.LINE_AA)
    cv2.putText(frame, 'press q to exit' , (cx - 200, height-50), 0, 1, (255,255,255), 3, lineType=cv2.LINE_AA)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    print(pixel_center, pixel_center_bgr)
    cv2.imshow("Frame", frame)
 
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()