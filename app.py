import cv2
from math import floor
import numpy as np

img = cv2.imread("Image/frame_170.png")
cv2.imshow("Input Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
roi = gray[floor(0.2 * gray.shape[0]):floor(0.95 * gray.shape[0]), floor(0.15 * gray.shape[1]):floor(0.75 * gray.shape[1])]
#cv2.imshow("ROI", roi)

kernel1 = np.ones((1, 1), np.uint8)
dilation = cv2.dilate(roi, kernel1, iterations=3)
#cv2.imshow('Dilation', dilation)

erosion = cv2.erode(dilation, kernel1, iterations=2)
#cv2.imshow('Erode', erosion)

ret, thresh = cv2.threshold(erosion, 79, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow("Thresh Img", thresh)

kernel2 = np.ones((1, 1), np.uint8)
dilation = cv2.dilate(thresh, kernel2, iterations=1)
#erosion = cv2.erode(dilation, kernel, iterations=7)
cv2.imshow('Dilation', dilation)

cv2.waitKey(0)
cv2.destroyWindow()