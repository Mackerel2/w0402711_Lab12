import cv2 as cv
import sys
img = cv.imread('download.jpg')
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
if img is None:
    sys.exit("The image could not be read")
cv.imshow("OpenCV Image", img)
cv.waitKey(0)
cv.destroyAllWindows()