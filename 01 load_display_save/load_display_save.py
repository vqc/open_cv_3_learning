import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) # returns a NumPy array representing the array
print("height (rows): {} pixels".format(image.shape[0]))
print("width (cols): {} pixels".format(image.shape[1]))
print("channels: {} pixels".format(image.shape[2]))

cv2.imshow("Image", image) # first param is the name of the window, 2nd param is the image
cv2.waitKey(0) # pauses execution until any keypress 

cv2.imwrite("newimage.jpg", image)
