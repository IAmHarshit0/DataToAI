import cv2 as cv

img = cv.imread('Photos/Bird.jpg')

# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resize = rescaleFrame(img, scale=1.5)
# cv.imshow("cat", resize)

def changeRes(width, height):
    # Live Video
    caputre.set(3, width)
    caputre.set(4,height)


caputre = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = caputre.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

caputre.release()
cv.destroyAllWindows()