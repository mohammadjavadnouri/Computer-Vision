import cv2
import numpy as np

path1 = r'C:\Users\MJ\Desktop\photo_2020-02-26_12-32-58.jpg'
path2 = r'C:\Users\MJ\Desktop\setare.jpg'

# Reading an image in default mode 
image1 = cv2.imread(path1) 
image2 = cv2.imread(path2)
image1plus2 = cv2.addWeighted(image1,0.4,image2,0.6,0)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('image1plusimage2',image1plus2)
print(image1.shape)
print(image1.size)
cv2.waitKey(3000)
cv2.destroyAllWindows()
