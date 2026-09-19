import cv2 as cv 
import numpy as np

img = cv.imread('Photos/Bird.jpg')
cv.imshow('Bird', img)

# Translation 
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

# Rotation
def rotate(img, angle, rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint,angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotmat, dimensions)

rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resize', resized)

# Flip 
flipped = cv.flip(img, 0)
cv.imshow('Flipped', flipped)

cv.waitKey(0)