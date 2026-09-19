import cv2 as cv

img = cv.imread('Photos/Bird.jpg')

cv.imshow('Cat', img)

cv.waitkey(0)

# caputre = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = caputre.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# caputre.release()
# cv.destroyAllWindows()



