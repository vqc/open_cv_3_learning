from matplotlib import pyplot as plt
import argparse
import cv2

# cv2.calcHist(images, channels, mask, histSize, ranges)
# images: list of images we want to compute histogram for
# channels: list of indexes specifying channel to compute histogram
#    e.g. grayscale [0], all of r g b [0, 1, 2]
# mask: if mask provided, will compute mask for masked pixels only, else None
# histSize: number of bins, one int for each channel, e.g. [32] or [32, 255, 35]
# ranges: the range of possible pixel values. if RGB [0, 256] other color 
#    spaces may have different range values

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

