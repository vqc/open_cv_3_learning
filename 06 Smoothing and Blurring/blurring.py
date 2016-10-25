import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('original', image)

# method #1 averaging
# define a kxk (k is always odd) window
# window will slide from left to right and from top to bottom
# pixel in center will be set to the average of all other pixels surrounding it

# this sliding window is called a convolution kernel or "kernel"
# as kernel gets bigger, the more blurred the picture gets

blurred = np.hstack([
            cv2.blur(image, (3, 3)),
            cv2.blur(image, (5, 5)),
            cv2.blur(image, (7, 7)),
          ])

cv2.imshow("averaged", blurred)

blurred = np.hstack([
            cv2.GaussianBlur(image, (3, 3), 0), # last val is std dev in x axis
            cv2.GaussianBlur(image, (5, 5), 0), # when set to zero, it is
            cv2.GaussianBlur(image, (7, 7), 0), # calculated for us
          ])

cv2.imshow("Gaussian", blurred)
# gaussian is more natural than averaged

blurred = np.hstack([
            cv2.medianBlur(image, 3),
            cv2.medianBlur(image, 5),
            cv2.medianBlur(image, 7),
          ])

cv2.imshow("Median", blurred)
# Median replaces the center with the median pixel from surroundings
# instead of a mean. the median exists is an actual pixel value in the
# surroundings.
# median is good for reducing detail noise.
# whereas the other blurs have more of a "motion blur" 

blurred = np.hstack([
            cv2.bilateralFilter(image, 5, 21, 21),
            cv2.bilateralFilter(image, 7, 31, 31),
            cv2.bilateralFilter(image, 9, 41, 41),
          ])

cv2.imshow("Bilateral", blurred)
# preserve edges and reduce edges.


cv2.waitKey(0)
