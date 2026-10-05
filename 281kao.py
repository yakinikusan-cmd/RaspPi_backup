import cv2
cascade = cv2.CascadeClassifier("/usr/local/share/opencv4/data/haarcascades/haarcascade_frontalface_alt.xml")
raw_image = cv2.imread("/home/pi/ドキュメント/python/image/faces.jpg")
gray_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
facerect = cascade.detectMultiScale(gray_image,scaleFactor=1.3,minNeighbors=1,minSize=(10,10))
detect_image = raw_image
for rect in facerect:
    detect_image = cv2.rectangle(detect_image,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(100,100,100),10)
cv2.imshow("detect",detect_image)
cv2.waitKey()
cv2.destroyAllWindows()