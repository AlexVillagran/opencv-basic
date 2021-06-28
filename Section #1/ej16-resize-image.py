import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

cv.waitKey(0)