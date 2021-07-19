import rospy 
import time
import math
import tf
import roslib

def broadcaster(x,y,z,w):
    rospy.init_node('fram_a_to_frame_b',anonymous=True)
    rate=rospy.Rate(1)
    bc=tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        #broadcasting trasnformation between frame a and frame b
        #translation,rotation and time 
        quaternion=tf.transformations.quaternion_from_euler(x,y,z)
        translation=(1.0,2.0,3.0)
        Time=rospy.Time.now()

        bc.sendTransform(translation,quaternion,Time,"frame_b","frame_a")

if __name__=="__main__":
    broadcaster(0.8,0.1,0.3,0.6)
