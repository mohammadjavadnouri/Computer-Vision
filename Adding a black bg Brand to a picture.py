import cv2
import numpy as np

path1 = r'C:\Users\MJ\Desktop\photo_2020-02-26_12-32-58.jpg'
path2 = r'C:\Users\MJ\Desktop\setare.jpg'

# Reading an image in default mode 
image1 = cv2.imread(path1) 
image2 = cv2.imread(path2)

# Adding image 1 and 2 together
image1plus2 = cv2.addWeighted(image1,0.4,image2,0.6,0)

#Showing them:
cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('image1plusimage2',image1plus2)

# Put logo on top-left corner, So create a ROI
rows,cols,channels = image2.shape
roi = image1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
image2gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(image2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
image1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
image2_fg = cv2.bitwise_and(image2,image2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(image1_bg,image2_fg)
image1[0:rows, 0:cols ] = dst


cv2.imshow('Final',image1)

print(image1.shape)
print(image1.size)
cv2.waitKey(3000)
cv2.destroyAllWindows()
