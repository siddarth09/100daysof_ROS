import rospy
import time
import math
import tf
import roslib

def listener():
    rospy.init_node('listener_node')
    rate=rospy.Rate(10)
    listener=tf.TransformListener()
    listener.waitForTransform("frame_b","frame_a",rospy.Time(),rospy.Duration(10))
    while not rospy.is_shutdown():
        try:
            (translation,rotation)=listener.lookupTransform("frame_b","frame_a",rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rpy=tf.transformations.euler_from_quaternion(rotation)
        print("TRANSFORMATION")
        print("-------------------")
        print("TRANSLATION =",translation[0],translation[1],translation[2])
        print("ROLL=",rpy[0], "PITCH=",rpy[1], "YAW=",rpy[2])
        rate.sleep()


if __name__=="__main__":
    listener()
    