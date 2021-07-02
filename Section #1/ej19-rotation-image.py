import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')

cv.imshow('Park', img)


# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated 45', rotated)

rotated2 = rotate(img, -45)
cv.imshow('Rotated -45', rotated2)

rotated3 = rotate(img, 90)
cv.imshow('Rotated Rotated', rotated3)

cv.waitKey(0)