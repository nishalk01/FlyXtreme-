import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    #print(type(frame))
    ih, iw, ic = frame.shape
    centy, centx = 0.25*ih, 0.75*iw

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    else:
        linev1 = cv2.line(img=frame, pt1=(int(0.35*iw), 0), pt2=(int(0.35*iw), ih), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
        linev2 = cv2.line(img=frame, pt1=(int(0.65*iw), 0), pt2=(int(0.65*iw), ih), color=(0, 255, 0), thickness=1, lineType=8, shift=0)
        lineh1 = cv2.line(img=frame, pt1=(0, int(0.35*ih)), pt2=(iw, int(0.35*ih)), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
        lineh2 = cv2.line(img=frame, pt1=(0, int(0.65*ih)), pt2=(iw, int(0.65*ih)), color=(0, 255, 0), thickness=1, lineType=8, shift=0)
        if (int(centx) < int(0.35*iw)) :
            print("roll-lft")
        else :
            print("roll-right")
vc.release()
cv2.destroyWindow("preview")