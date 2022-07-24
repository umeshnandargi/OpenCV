import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width,height), color=(255,0,0), thickness=5)
    img = cv2.line(img, (width,0), (0,height), color=(0,0,255), thickness=5)
    img = cv2.rectangle(img, pt1=(100,100), pt2=(200,200), color=(128,128,128), thickness=-1)
    img = cv2.circle(img, center=(width//2, height//2), radius=60, color=(0,255,0), thickness=5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, text='Press q to quit', org = (width//2 -90, 30), fontFace=font,fontScale=1, color=(0,0,0), thickness=2, lineType=cv2.LINE_AA )
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()