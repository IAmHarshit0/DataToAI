import cv2 as cv 
import numpy as np

img = cv.imread('Photos/Bird.jpg')
cv.imshow('Bird', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

# Median Blur 
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 35, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)