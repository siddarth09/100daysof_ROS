import rospy
from learning_ros.msg import LDR

def get_intensity():
    rospy.init_node('ldr_node',anonymous=True)
    pub=rospy.Publisher('LDR_SENSOR',LDR,queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        brightness=LDR()
        brightness.intensity=600
        pub.publish(brightness)
        rospy.loginfo("INTENSITY IS PUBLISHED")
        rate.sleep()
    

if __name__=="__main__":
    try:
        get_intensity()
    except rospy.ROSInternalException:
        rospy.loginfo("ros master stopped")