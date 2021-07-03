#this code can either be used on base station or on the robot 
import rospy
from learning_ros.msg import LDR

def callback_listener(msg):
    rospy.loginfo("THE INTENSITY REPORTED BY THE ROVER:{0}".format(msg.intensity))

def subcriber():
    rospy.init_node('Subcriber',anonymous=False)
    rospy.Subscriber('LDR_SENSOR',LDR,callback=callback_listener)
    rospy.spin()

if __name__=="__main__":
    subcriber()