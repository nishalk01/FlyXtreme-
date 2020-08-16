import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

crit_throttle = 1000
centx, centy = 0, 0
f = open("val.txt", "w")

#def make_720p():
    #vc.set(3, 1280)
    #vc.set(4, 720)

def change_res(width, height):
    vc.set(3, width)
    vc.set(4, height)

#make_720p()
change_res(1280, 720)

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
    print(str(frame.shape))  

    
    cv2.circle(frame,(centx, centy), 1, (0,0,255), -1)
    centx = centx + 10
    centy = centy + 10
    if(centy == iw ) :
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
    elif (centx <= int(0.5*iw)) :
        yval = "R"
        yaw = (centx)*crit_throttle
    else :
        yval = "L"
        yaw = (iw - centx)*crit_throttle

    if ( int(centy) == 0 | int(centy) > int(ih) ) :
        pval = "N"
        pitch = 0
    elif (centy <= int(0.5*ih)) :
        pval = "U"
        pitch = (centy)*crit_throttle
    else :
        pval = "D"
        pitch = (ih - centy)*crit_throttle

    print ( yval,yaw)
    #f.write("x: \t y: \t yval: \t yaw: \t")
    f.write("\n")
    f.write(str(centy))
    f.write("\t")
    f.write(str(ih))
    f.write("\n")
    f.write(str(pval))
    f.write("\n")
    f.write(str(pitch))
    f.write("\n")

    #writeval = ("x:",centx,"y:",centy,"yval:",yval,"yaw:",yaw, "pitch: ", pitch, "pval :", pval)
    #f.write(str(writeval))
    f.write("\n")
    
    
f.close()    
vc.release()
cv2.destroyWindow("preview")