import cv2 as cv
import numpy as np


black = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Black', black)

cv.circle(black, (black.shape[1]//2, black.shape[0]//2), 40, (0, 0, 255), thickness=1)
cv.imshow('Circle Border', black)

cv.circle(black, (black.shape[1]//2, black.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle FILLED', black)

cv.waitKey(0)
