import rospy
from geometry_msgs.msg import Twist

def pub():
    rospy.init_node('motor_controller',anonymous=True)
    publisher=rospy.Publisher('cmd_vel',Twist,queue_size=10)
    velocity_msg=Twist()
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        for i in range(256):
            velocity_msg.linear.x=i
            publisher.publish(velocity_msg)
            rospy.loginfo(velocity_msg)
        rate.sleep()

if __name__=="__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        pass