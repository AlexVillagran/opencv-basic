import cv2 as cv
import numpy as np


black = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Black', black)

cv.line(black, (0, 0), (black.shape[1]//2, black.shape[0]//2),(255, 255, 255), thickness=3)
cv.imshow('Line 1', black)

cv.line(black, (100, 300), (300,400),(255, 255, 255), thickness=3)
cv.imshow('Line 2', black)

cv.waitKey(0)
