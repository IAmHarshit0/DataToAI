import cv2 as cv
import numpy as np 

img = cv.imread('Photos/Bird.jpg')

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(blur, 125, 175)

contours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

ret, threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', threshold)
# print(len(contours))

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,255,0), thickness=1)
cv.imshow('Contours', blank)

cv.waitKey(0)