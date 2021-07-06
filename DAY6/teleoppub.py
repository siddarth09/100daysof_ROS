import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

x=0
y=0
z=0
yaw=0
def move_inline(speed):
    velocity_msgs=Twist()
    rospy.init_node('turtlesim',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    global x,y
    a=x
    b=y
    rospy.loginfo("TURTLE STARTING")
    rate=rospy.Rate(1)
    
    while not rospy.is_shutdown():
        velocity_msgs.linear.x=abs(speed)
        print(velocity_msgs.linear.x)
        velocity_msgs.linear.y=0
        velocity_msgs.linear.z=0

        velocity_msgs.angular.z=0.30
        velocity_msgs.angular.y=0
        velocity_msgs.angular.x=9
        velocity_publisher.publish(velocity_msgs)
        rate.sleep()

    
    
    
    
def callback(pose_message):
    global x
    global y,yaw

    x=pose_message.x
    y=pose_message.y
    yaw=pose_message.theta

if __name__=="__main__":

    try:
        position_topic="/turtle1/pose"
        pose_subscriber=rospy.Subscriber(position_topic,Pose,callback)
        move_inline(0.4)
        time.sleep(2)
        
    except rospy.ROSInterruptException:
        pass