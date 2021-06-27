import rospy
from rospy.exceptions import ROSInterruptException 
from std_msgs.msg import String

def publisher():
    rospy.init_node('publisher_node',anonymous=False)
    rate= rospy.Rate(1)
    pub=rospy.Publisher('talker',String,queue_size=10)
    while not rospy.is_shutdown():
        str1="HELLO SIDDARTH"
        rospy.loginfo(str1)
        pub.publish(str1)
        rate.sleep()

if __name__=="__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass