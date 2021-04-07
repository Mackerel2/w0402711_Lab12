import numpy as np
import cv2 as cv
import sys

img1 = cv.imread('Person1.jpg')
img2 = cv.imread('Person2.jpg')

res = cv.resize(img1,None,fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)
res2 = cv.resize(img2,None,fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)
alpha = 0.2
dst = cv.addWeighted(img1, 1-alpha, img2, alpha, 0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()