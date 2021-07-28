import cv2
import math

'''BASIC IMAGE PROCESSING 
Here I will be performing 4 major processing techniques
1.scaling or resizing 
2.rotating the image
3.shifting 
4.edge detection
5.image threholding
6.color to black and white '''

#reading the image
img=cv2.imread('src/learning_ros/src/DAY28/jackal.jpeg')

#1.scaling
resized=cv2.resize(img,(800,500))

#2.Rotating the image
rotate=cv2.rotate(img,rotateCode=cv2.cv2.ROTATE_90_CLOCKWISE)

#3.Shifting
h,w,channels=img.shape
center=(w//2,h//2)
matrix=cv2.getRotationMatrix2D(center,-45,1.0)
shift=cv2.warpAffine(img,matrix,(img.shape[1],img.shape[0]))

#4.edge detection
edges=cv2.Canny(resized,100,200)

#5.Image thresholding
ret,threshold=cv2.threshold(img,50,255,cv2.THRESH_TOZERO)

#6.black and white
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#showing image
cv2.imshow('JACKAL UGV',resized)
cv2.imshow('rotated jackal',rotate)
cv2.imshow('shifted jackal',shift)
cv2.imshow('EDGES of jackal',edges)
cv2.imshow('Threshold jackal',threshold)
cv2.imshow('1990 jackal',grey)
cv2.waitKey(0)