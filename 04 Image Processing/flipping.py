import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("flipped horizontally", flipped)


flipped = cv2.flip(image, 0)
cv2.imshow("flipped vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("flipped horizontally and vertically", flipped)

cv2.waitKey(0)
