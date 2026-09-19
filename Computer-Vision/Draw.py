import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('Blank', blank)

# 1. Paint
# blank[200:300, 200:300] = 0,255,0
# cv.imshow('Green', blank)

# 2. Rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
# cv.imshow('Recatngle', blank)

# 3. Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (255,0,0), thickness=3)
# cv.imshow('Circle', blank)

# 4. Line
# cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (200,300), (0,255,0), thickness=3)
# cv.imshow('Line', blank)

# 5. Text
cv.putText(blank, 'Hello World', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)