import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

cropped = img[50:200, 200:400]

cv.imshow('Resized', cropped)

cv.waitKey(0)