import cv2 as cv
import numpy as np


black = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Black', black)

cv.rectangle(black, (0, 0), (250, 250), (0, 250, 0), thickness=2)
cv.imshow("Rectangle Border", black)

cv.rectangle(black, (0, 0), (250, 250), (0, 250, 0), thickness=cv.FILLED)
cv.imshow("Rectangle FILLED", black)


cv.rectangle(black, (0, 0), (250, 250), (0, 250, 0), thickness=-1)
cv.imshow("Rectangle FILLED VALUE NEGATIVE", black)

# Set Size shape
cv.rectangle(black, (0, 0), (black.shape[1]//2, black.shape[0]//2), (0, 250, 0), thickness=-1)
cv.imshow("Rectangle Size Shape", black)

cv.waitKey(0)
