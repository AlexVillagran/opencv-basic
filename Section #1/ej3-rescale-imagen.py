import cv2 as cv


def rescaleImage(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('../Resources/Photos/cat.jpg')


img_resized = rescaleImage(img, scale=.5)
img_resized_default = rescaleImage(img)

cv.imshow('Cat', img)
cv.imshow('Cat Resized 50%', img_resized)
cv.imshow('Cat Resized Default 75%', img_resized_default)
cv.waitKey(0)
