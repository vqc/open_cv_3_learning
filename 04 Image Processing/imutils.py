import numpy as np
import cv2

def translate(image, x, y):
  M = np.float32([[1, 0, x], 
                  [0, 1, y]])
  shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
  return shifted

def rotate(image, angle, center = None, scale = 1.0):
  (h, w) = image.shape[0:2]
  if center is None:
    center = (w//2, h//2)
  M = cv2.getRotationMatrix2D(center, angle, scale)
  rotated = cv2.warpAffine(image, M, (w, h))
  return rotated

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
  (old_h, old_w) = image.shape[0:2]
  if width is None and height is None:
    return image
  if width is not None and height is not None:
    resized = cv2.resize(image, (width, height), interpolation = inter)
    return resized
  if width is None:
    ratio = height / float(old_h)
    new_dimensions = (int(old_w*ratio), height)
  else:
    ratio = width / float(old_w)
    new_dimensions = (width, int(old_h*ratio))

  resized = cv2.resize(image, new_dimensions, interpolation = inter)
  return resized
