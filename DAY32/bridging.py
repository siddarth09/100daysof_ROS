from numpy.core.fromnumeric import resize
import cv_bridge
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2
import sys
import numpy as np

class perception():

    def __init__(self) -> None:
        self.bridge=CvBridge()
        self.subcriber=rospy.Subscriber('/camera/rgb/image_raw',Image,self.image_cb)

    def image_cb(self,data):
        try:
            cv_image=self.bridge.imgmsg_to_cv2(data,'bgr8')
            resize=cv2.resize(cv_image,(800,400))
        except CvBridgeError as e:
            print(e)

        cv2.imshow('bridgged',resize)
        cv2.waitKey(0)
    
if __name__=="__main__":
    try:
        rospy.init_node('line_follower',anonymous=False)
        line_follower=perception()
        rospy.spin()
    except KeyboardInterrupt:
        print("SHUTDOWN")
    cv2.destroyAllWindows()
