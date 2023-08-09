#from PIL import Image

#img = Image.open("haha.jpg")
#img = img.tobitmap()
import cv2

vidcap = cv2.VideoCapture('video1.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames1/frame%d.png" % count, image)
  success,image = vidcap.read()
  #success = False
  #print('Read a new frame: ', success)
  count += 1
