import numpy as np
import argparse
import cv2
import imutils as imu

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print(image.shape)
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
center = ( w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 degrees", rotated)

rotated = imu.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)

rotated = imu.rotate(image, 45)
cv2.imshow("Rotated by 45 degrees, imutil", rotated)

cv2.waitKey(0)
