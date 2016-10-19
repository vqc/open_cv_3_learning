import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

cropped = image[30:120, 24:335]
# starting at (240, 30) and ending at (335, 120)
# in order to crop, NumPy expects four indexes
# start y, end y
# start x, end x
# remember that np works on rows (height) first, then columns (width)
cv2.imshow("cropped", cropped)

cv2.waitKey(0)
