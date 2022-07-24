import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX

    lower_orange = np.array([5, 50, 50])
    upper_orange = np.array([15, 255, 255])
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_orange, upper_orange)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    result = cv2.putText(result, text='Press q to quit', org = (width//2 -90, 30), fontFace=font,fontScale=1, 
    color=(255,255,255), thickness=2, lineType=cv2.LINE_AA )
    result2 = cv2.bitwise_and(frame, frame, mask=mask2)

    cv2.imshow('frame', result)
    cv2.imshow('mask2', result2)
    # cv2.imshow('mask', mask)
    # cv2.imshow('mask2', mask2)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()