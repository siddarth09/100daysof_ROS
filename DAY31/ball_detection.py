import cv2
import numpy as np

#step 1: read RGB
img=cv2.imread('src/learning_ros/src/DAY32/tennis.jpg')
resize=cv2.resize(img,(700,500))

#step 2: convert to HSV
hsv=cv2.cvtColor(resize,cv2.COLOR_BGR2HSV)

#step3: Defining upper and lower range
#since the ball is greenish yellow

yellow_lower=(30,120,45)
yellow_upper=(60,255,255)
def get_contours(contours):
    M=cv2.moments(contours)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
    return cx,cy
#defining mask 
mask=cv2.inRange(hsv,yellow_lower,yellow_upper)

#contour detection 

contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

black_image=np.zeros([mask.shape[0],mask.shape[1],3],'uint8')

for c in contours:
    area=cv2.contourArea(c)
    perimeter=cv2.arcLength(c,True)
    print("AREA:{0},PERIMETER:{1}".format(area,perimeter))
    ((x,y),radius)=cv2.minEnclosingCircle(c)
    cx,cy=get_contours(c)
    if area>500:
        cv2.drawContours(resize,[c],-1,(150,250,255),2)
        cv2.circle(resize,(cx,cy),(int)(radius),(0,0,255),1)



cv2.imshow('ball detected',resize)
cv2.waitKey(0)


cv2.destroyAllWindows()
