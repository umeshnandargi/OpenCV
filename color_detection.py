import cv2
import numpy as np
import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour,spec= webcolors.CSS3)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

url = 'http://192.168.0.101:8080/video'

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # print(width,height)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cx = int(width/2)
    cy = int(height/2)

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    
    requested_colour = (r,g,b)
    actual_name, closest_name = get_colour_name(requested_colour)

    if actual_name:
        color = actual_name
    else:
        color = closest_name
    
    cv2.putText(frame, color , (cx - 200, 100), font , 2, (0,0,0),5,  lineType=cv2.LINE_AA)
    cv2.putText(frame, 'press q to exit' , (cx - 200, height-50), font, 1, (255,255,255),3, lineType=cv2.LINE_AA)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()