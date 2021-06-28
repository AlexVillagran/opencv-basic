import cv2 as cv
import numpy as np

#1  Paint image black
black = np.zeros((500, 500), dtype='uint8')
cv.imshow('Black', black)

#2. Paint set color image
green = np.zeros((500, 500, 3), dtype='uint8')
green[:] = 0, 255, 0
cv.imshow('Green', green)

#3. Paint Red Part area Green
green[200: 300, 300:400] = 0, 0, 255
cv.imshow('Green && Red', green)

cv.waitKey(0)
