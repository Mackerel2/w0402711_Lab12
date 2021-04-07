import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot open camera")
    exit()
while True:
    # Capture frame by frame
    ret, frame = cap.read()
    #if frame is read correctly ret is true
    if not ret:
        print("Can;t receive frame (Stream end?). Exiting ..")
        break
    #our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #Display the resulting frame
    cv.imshow('frame', gray)
    #cv.imshow('frame',frame)
    
    if cv.waitKey(1) == ord('q'):
        break
#When everything done release the capture
cap.release()
cv.destroyAllWindows()