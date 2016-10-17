import numpy as np
import argparse
import imutils as imu
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

M = np.float32([[1, 0, 25],  # [1, 0, tx] where tx is pixels left or right
		[0, 1, 50]]) # [0, 1, ty] where ty is pixels up or down
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shfited Down and RIght", shifted)

M = np.float32([[1, 0, -50],  # [1, 0, tx] where tx is pixels left or right
		[0, 1, -90]]) # [0, 1, ty] where ty is pixels up or down
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shfited Up and Left", shifted)

shifted = imu.translate(image, -50, 90)
cv2.imshow("Shfited Down and Left", shifted)

cv2.waitKey(0)
