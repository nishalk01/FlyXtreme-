import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def nothing(*arg):
        pass
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
  ret,img=cap.read()
  mask = fgbg.apply(img)
  contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
  biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
  x,y,w,h = cv2.boundingRect(biggest_contour)
  centerCoord = (int(x+w/2), int(y+w/2))
  print(centerCoord)
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
  img = cv2.circle(img, centerCoord, 10,(0,255,0),2)
  cv2.imshow('img',img)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
