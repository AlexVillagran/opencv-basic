import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frameMain = capture.read()

    if isTrue:

        frame_resized = rescaleFrame(frameMain, scale=.2)

        cv.imshow('Video', frameMain)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
