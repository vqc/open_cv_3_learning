from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def plot_histogram(image, title, mask = None):
  chans = cv2.split(image)
  colors = ("b", "g", "r")
  plt.figure()
  plt.title(title)
  plt.xlabel("Bins")
  plt.ylabel("# of pixels")

  for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

#original image and histograph
image = cv2.imread(args['image'])
cv2.imshow("original", image)
plot_histogram(image, "histogram for original")

#apply a mask
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("applyig the mask", masked_image)
plot_histogram(masked_image, "histogram for masked", mask = mask)



cv2.waitKey(0)


plt.show()
