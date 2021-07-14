import rospy
from std_msgs.msg import Int16

def pub():
    angle=Int16()
    rospy.init_node('servo_pub',anonymous=True)
    pub=rospy.Publisher('servo',Int16,queue_size=10)
    rate=rospy.Rate(1)
    servo_angle=0
    rospy.loginfo("THE SERVO IS ROTATING")
    while not rospy.is_shutdown():
        angle.data=servo_angle

        pub.publish(angle)
        for i in range(180):
            servo_angle=i+30
            angle.data=servo_angle
            rospy.loginfo(angle.data)
            pub.publish(angle)
            
            if i==150:
                servo_angle=0
                angle.data=servo_angle
                pub.publish(angle)
                break
        
        rate.sleep()

    
if __name__=="__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        print("CLOSED")