import cv2
class VideoCamera(object):
    def __init__(self):
        url="http://192.168.43.1:8080/video"
        self.video=cv2.VideoCapture(url)
        #self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return image
