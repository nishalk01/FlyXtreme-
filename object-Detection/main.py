import cv2
from detect import *
import numpy as np
import time
model = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb','ssd_v2.pbtxt')
cap=cv2.VideoCapture(0)
frame_h,frame_w=480,640
while True:
    ret,frame=cap.read()
    start=time.time()
    x,y,w,h,class_name=detect_(np.array(frame),model)
    end=time.time()
    print(end-start)
    cv2.rectangle(frame,(x,y),(w,h), (0,255,0), thickness=3)
    cv2.putText(frame,str(class_name),(x, int(y+.05*frame_h)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
