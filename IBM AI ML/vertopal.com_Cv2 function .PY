import cv2
img = cv2.imread('caps.jpg')
cv2.imshow('OutputImage',img)
cv2.waitKey(0)
import cv2
img= cv2.imread('caps.jpg')
cv2.imshow('output',img)
print(img.shape)
print("Height pixel values : ", img.shape[0])
print("Width pixel values : ", img.shape[1])
cv2.waitKey(0)
#cv2.destroyAllwindows()
img
#Example of converting RGB mage into gray scale:
import cv2
img= cv2.imread('caps.jpg')
print("SHAPE OF ORIGINAL IMAGE",img.shape)
cv2.imshow("original",img)
cv2.waitKey(0)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("SHAPE OF GRAY SCALE IMAGE",gray_img.shape)
# for showing image
cv2.imshow("GrayscaleImage",gray_img)
# for holding image
cv2.waitKey(0) 
# clear all windows
#cv2.destroyAllwindows() 
SHAPE OF ORIGINAL IMAGE (275, 183, 3)
SHAPE OF GRAY SCALE IMAGE (275, 183)
-1
gray_img
img
#Example of converting RGB image into HSV color space:
import cv2
img= cv2.imread('caps.jpg')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img_HSV.shape)
cv2.imshow('HSVImage',img_HSV)
cv2.imshow('HueChannel', img_HSV[:, :,0])
cv2.imshow('SaturationChannel', img_HSV[:, :,1])
cv2.imshow('ValueChannel', img_HSV[:, :,2])
cv2.waitKey(0)
(275, 183, 3)
-1
#Example of image translation:
import cv2
import numpy as np
#for reading image
img = cv2.imread("caps.jpg")
height, width = img.shape[:2]
print(height)
print(width)
quarter_height, quarter_width = height/3,width/3
print(quarter_height)
print(quarter_width)
n = np.float32([[0,1, quarter_width], [1,0, quarter_height]])
print(n)
# We use warpAffine function to shift the image
img_translation = cv2.warpAffine(img, n, (width, height))
cv2.imshow('originalimage',img)
cv2.waitKey(0)
cv2.imshow('AfterTranslation',img_translation)
cv2.waitKey(0)
crop=img[70:170,50:130]
cv2.imshow("cropped",crop)
cv2.waitKey(0)
r=100.0/img.shape[1]
dim=(100,int(img.shape[0]*r))
dim=(100,20)
resize=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("resize",resize)
cv2.waitKey(0)
print(img.shape)
275
183
91.66666666666667
61.0
[[ 0. 1. 61. ]
 [ 1. 0. 91.666664]]
(275, 183, 3)
import cv2
import numpy as np
img = cv2.imread("caps.jpg")
height,width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width,height), 65, .8)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width,height))
cv2.imshow('Rotated Image',rotated_image)
cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rotated_image.jpg", rotated_image)
True