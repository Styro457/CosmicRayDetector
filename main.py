print()

from PIL import Image
import numpy as np

threshold = 25

def check_image(img, i):
    ary = np.array(img)

    # Split the three channels
    r, g, b = np.split(ary, 3, axis=2)
    r = r.reshape(-1)
    g = r.reshape(-1)
    b = r.reshape(-1)

    # Standard RGB to grayscale
    bitmap = list(map(lambda x: 0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2],
                      zip(r, g, b)))
    for x in bitmap:
      if(x > threshold):
        print("PIXELLLL: " + str(x) + " - "+ str(i))
    #bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    #bitmap = np.dot((bitmap > 128).astype(float), 255)


for i in range(46, 47):
    check_image(Image.open("frames1/frame" + str(i) + ".png"), i)
