import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

flip = cv.flip(img, 0)
cv.imshow('Flip 1', flip)

flip2 = cv.flip(img, 1)
cv.imshow('Flip 2', flip2)

flip3 = cv.flip(img, -1)
cv.imshow('Flip 3', flip3)

cv.waitKey(0)
