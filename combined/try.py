#from main import get_frames
from  camera import  VideoCamera
print("pass")
import numpy as  np
import cv2
cam=VideoCamera()
while True:
  img=cam.get_frame()

#cap.release()
#cv2.destroyAllWindows()
