
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg  import Pose

x=0
y=0
yaw=0

def callback(msg):
    global x,y,yaw
    x=msg.x
    y=msg.y
    yaw=msg.theta

def goto_goal():
    global x,y
    vel_msg=Twist()
    vel_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.init_node('goal',anonymous=True)
    print("GIVE YOUR INPUT")
    x_goal=float(input("ENTER THE Coordinate x"))
    y_goal=float(input("ENTER THE Coordinate y"))
    rate=rospy.Rate(1)
    while True:
        k_linear=0.5
        k_angular=4.0
        distance=abs(math.sqrt((x_goal-x)**2)+((y_goal-y)**2))
        linear_speed=distance*k_linear

        desired_angle=math.atan2(y_goal-y,x_goal-x)
        angular_speed=(desired_angle-yaw)*k_angular

        vel_msg.linear.x=linear_speed
        vel_msg.angular.z=angular_speed
        vel_publisher.publish(vel_msg)
        rate.sleep()
        print("X={0},Y={1},distance to the goal={2}".format(x,y,distance))
        if distance<0.01:
            print("REACHED")
            break

if __name__=="__main__":
    try:
        rospy.Subscriber('/turtle1/pose',Pose,callback)
        goto_goal()
    except rospy.ROSInterruptException:
        print("STOPPED")

