from bs4 import BeautifulSoup
import requests
import urllib
import numpy as np
import cv2
url = 'http://0.0.0.0:5004/'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content,'lxml') # choose lxml parser
# find the tag : <img ... >
image_tags = soup.findAll('img')
# print out image urls
print(image_tags)
for image_tag in image_tags:
    url=image_tag.get('src')
    print(url)
    resp=urllib.request.urlopen(url)
    image=np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow('s',image)
    cv2.waitKey(1)
