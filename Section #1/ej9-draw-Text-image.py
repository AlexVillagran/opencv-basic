import cv2 as cv
import numpy as np


black = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Black', black)

cv.putText(black, 'Hello world', (225, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 1)
cv.imshow('Text', black)


cv.putText(black, 'My name is... ', (100, 400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100, 140, 0), 2)
cv.imshow('Text', black)

cv.waitKey(0)
