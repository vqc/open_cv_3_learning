from matplotlib import	pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

chans = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title("'flattened' color histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")

for (chan, color) in zip(chans, colors):
  hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
  plt.plot(hist, color = color)
  plt.xlim([0, 256])


fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, 
                    [8, 8], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2d color histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[2], chans[0]], [0, 1], None, 
                    [8, 8], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2d color histogram for R and B")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[2], chans[1]], [0, 1], None, 
                    [8, 8], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2d color histogram for R and G")
plt.colorbar(p)

hist = cv2.calcHist([image], [0, 1, 2], None, 
                    [8, 8, 8], [0, 256, 0, 256, 0, 256])

plt.show()

cv2.waitKey(0)

