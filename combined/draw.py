import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

crit_throttle = 1000
centx, centy = 0, 0
f = open("val.txt", "w")

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    #print(type(frame))
    ih, iw, ic = frame.shape
    f.write(str(frame.shape))
    

    
    cv2.circle(frame,(centx, centy), 1, (0,0,255), -1)
    centx = centx + 10
    centy = centy + 10
    if(centy == ih ) :
        break
    print ( centx,centy)
    mid = (0.5*iw,0.5*ih)
    f.write(str(mid))


    key = cv2.waitKey(20)
    if key == 27: # exit on ESC

        break
    else:
        linev = cv2.line(img=frame, pt1=(int(0.5*iw), 0), pt2=(int(0.5*iw), ih), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
        #linev2 = cv2.line(img=frame, pt1=(int(0.65*iw), 0), pt2=(int(0.65*iw), ih), color=(0, 255, 0), thickness=1, lineType=8, shift=0)
        lineh = cv2.line(img=frame, pt1=(0, int(0.5*ih)), pt2=(iw, int(0.5*ih)), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
        #lineh2 = cv2.line(img=frame, pt1=(0, int(0.65*ih)), pt2=(iw, int(0.65*ih)), color=(0, 255, 0), thickness=1, lineType=8, shift=0)
        
    if ( int(centx) == 0 | int(centx) > int(iw) ) :
        yval = "N"
        yaw = 0
    elif (centx <= int(0.5*ih)) :
        yval = "R"
        yaw = (centx)*crit_throttle
    else :
        yval = "L"
        yaw = (ih - centx)*crit_throttle

    print ( yval,yaw)
    #f.write("x: \t y: \t yval: \t yaw: \t")
    writeval = ("x:",centx,"y:",centy,"yval:",yval,"yaw:",yaw)
    f.write(str(writeval))
    f.write("\n")
    
f.close()    
vc.release()
cv2.destroyWindow("preview")