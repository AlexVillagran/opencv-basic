import cv2 as cv
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

#Coverting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)


