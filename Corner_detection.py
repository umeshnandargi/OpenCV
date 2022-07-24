import cv2
import random
import numpy as np

img = cv2.imread('assets\myimage.jpeg', -1)
img = cv2.resize(img, (0,0), fx=2, fy=2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)
corners= cv2.goodFeaturesToTrack(gray, 100, 0.01,10)
corners = np.int0(corners)

for corner in corners:
    x , y = corner.ravel()
    cv2.circle(img, (x,y), 5, (255,0,00), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple   (map(lambda x: int(x), np.random.randint(0,255,size=3)))
        cv2.line(img, corner1, corner2, color, 1)

# for i in range(128):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0,255), random.randint(0, 255), random.randint(0,255)]

# slice = img[50:100,100:200]
# img[100:150,150:250] = slice

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()