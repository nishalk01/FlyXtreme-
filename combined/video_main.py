from flask import Flask, render_template, Response
from camera import VideoCamera
import numpy as np
import cv2
import time
from detect import *
model = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb','ssd_v2.pbtxt')
frame_h,frame_w=480,640
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
def gen(camera):
    while True:
        i = camera.get_frame()
        x,y,w,h,class_name=detect_(np.array(i),model)
        cv2.rectangle(i,(x,y),(w,h), (255,0,0), thickness=2)
        cv2.putText(i,str(class_name),(x, int(y+.05*frame_h)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
        ret, jpeg = cv2.imencode('.jpg', i)
        frame=jpeg.tobytes()
        #cv2.imshow('frame',i)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
         #break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    #flask run -h 192.168.1.100
    app.run(host='192.168.43.123',
port=5001, debug=True)
