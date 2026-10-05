import cv2
import numpy as np
raw_image = cv2.imread("/home/pi/ダウンロード/ball.png")
img_hsv = cv2.cvtColor(raw_image, cv2.COLOR_BGR2HSV_FULL)
arr = np.zeros((350, 350, 3))
color = [0,0,0,0]
for i in img_hsv:
    for j in i:
        if (45 < j[0])and(j[0] < 75):
            color[0] += 1
            arr[i][j][0]= 255
            arr[i][j][1]=220
            arr[i][j][2]=0
        elif (170 < j[0])and(j[0] < 270):
            color[1] += 1
            arr[i][j][0]= 255
        elif (0 < j[0])and(j[0] < 30)or(330 < j[0])and(j[0] < 360):
            color[2] += 1
            arr[i][j][1]= 255
        else:
            color[3] +=1


print(color)
cv2.show(arr)
cv2.waitKey()
cv2.destroyAllWindows()