import cv2

img = cv2.imread('img.png')
img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# im_color = cv2.applyColorMap(img, cv2.COLORMAP_JET)
mask = cv2.inRange(hsv,(0, 0, 40), (180, 18, 230))



cv2.imshow('hsv', mask)
cv2.waitKey(0)