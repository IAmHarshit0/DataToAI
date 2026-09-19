import cv2 as cv

img = cv.imread('Photos/Bird.jpg')
# cv.imshow('Bird', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Dilate
dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize', resized)

# Cropping
cropped = img[50:100, 25:100]
cv.imshow('Crop', cropped)

cv.waitKey(0)
