import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
