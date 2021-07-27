import cv2

#reading a image
img=cv2.imread('src/learning_ros/src/DAY27/jackal.jpeg')
#print(img)
#BASIC OPERATIONS ON IMAGES

#1. EXRACTING RGB VALUES

(b,g,r)=img[100,100]
print('BLUE',b)
print('GREEN',g)
print('RED',r)

#2.Getting the shape of the image
h,w,channels=img.shape
print("HEIGHT OF THE IMAGE",h)
print("WIDTH OF THE IMAGE",w)
print("NUMBER OF CHANNELS",channels)

#3.resizing the image
resize=cv2.resize(img,(800,400))

#4.getting rotation matrix
center=(w//2,h//2)
matrix=cv2.getRotationMatrix2D(center,-45,1.0)
print(matrix)

#5.DRAW A RECTANGLE
cpyimage=img.copy()
rectangle=cv2.rectangle(resize,(216,115),(466,343),(0,255,0),2)

#6.TEXT
text=cv2.putText(resize,'DOG',(216,115),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)


#showing the image
cv2.imshow('final',resize)
cv2.waitKey(0)


cv2.destroyAllWindows()