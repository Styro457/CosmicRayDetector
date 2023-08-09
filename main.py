from PIL import Image
import numpy as np

print("Loading program...")

threshold = 25
framesAmount = 100

count = 0


def check_image(img, index):
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
        if x > threshold:
            print("Found pixel above threshold: " + str(x) + " - " + index)
            global count
            count += 1
    # bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    # bitmap = np.dot((bitmap > 128).astype(float), 255)


for i in range(0, framesAmount):
    index = str(i)
    print("Loading image " + index + "...")
    img = Image.open("frames1/frame" + index + ".png")
    print("Analzying image " + index + "...")
    check_image(img, index)

print("Finished! Pixels above threshold found: " + str(count))
