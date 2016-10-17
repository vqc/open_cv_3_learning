import numpy as np
import cv2
import imutils as imu
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

new_width = 150
ratio = new_width / image.shape[1] # new width divided by old width to get ratio
new_dimensions = (new_width, int(image.shape[0] * ratio)) # (new_width, new_height)

resized = cv2.resize(image, new_dimensions, interpolation = cv2.INTER_AREA)
# in addition to INTER_AREA, can use INTER_LINEAR, INTER_CUBIC, INTER_NEAREST
cv2.imshow("Resize (width)", resized)

resized = imu.resize(image, 200)
cv2.imshow("IMU Resize width 200", resized)

resized = imu.resize(image, 500)
cv2.imshow("IMU Resize width 500", resized)

resized = imu.resize(image, None, 500)
cv2.imshow("IMU Resize height 500", resized)

resized = imu.resize(image, 500, 500)
cv2.imshow("IMU Resize height 500", resized)

cv2.waitKey(0)
