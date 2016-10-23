import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(B, G, R) = cv2.split(image)

cv2.imshow("R", R)
cv2.imshow("G", G)
cv2.imshow("B", B)

merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype="uint8")

red = cv2.merge([zeros, zeros, R])
green = cv2.merge([zeros, G, zeros])
blue = cv2.merge([B, zeros, zeros])

cv2.imshow("red", red)
cv2.imshow("green", green)
cv2.imshow("blue", blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
