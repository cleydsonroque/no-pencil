import operator
import math
import cv2
img = cv2.imread('img.png')
# height, width, channels = img.shape
img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# retval, dst = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('dst', dst)
cv2.imshow('gray',img)
cv2.waitKey(0)