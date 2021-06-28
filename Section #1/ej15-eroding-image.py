import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

#Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges Blur', canny)

#Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding

eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

cv.waitKey(0)