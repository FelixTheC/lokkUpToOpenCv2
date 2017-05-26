#! /usr/env/python3

import cv2

img = cv2.imread('galaxy.jpg', 1)
print(type(img)) #a numpy narray
print(img) # show the arrays/list
print(img.shape) #the resolution
print(img.ndim)

#string -> the title of the window
cv2.imshow('Galaxy', img)
#cv.waitKey(0) closing only by user
cv2.waitKey(4000) # waits 2 secondes
cv2.destroyAllWindows()
