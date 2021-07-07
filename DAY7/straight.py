import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

x=0
y=0
yaw=0

def callback(msg):
    global x
    global y,yaw
    x=msg.x
    y=msg.y
    yaw=msg.theta

def moving_straight():
    global x,y
    rospy.init_node('turtlesim_node',anonymous=True)
    vel_msg=Twist()
    vel_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    a=x
    b=y
    print(a,"\n",b)
    print("LESSSSS GO")
    speed=float(input("SPEED:"))
    distance=float(input("DISTANCE:"))
    forward=input("FORWARD/BACKWARD ?:")

    if forward:
        vel_msg.linear.x=abs(speed)
    else:
        vel_msg.linear.x=-abs(speed)

    distance_moved=0.0
    rate=rospy.Rate(1)
    while True:
        rospy.loginfo("TURTLE MOVING")
        vel_publisher.publish(vel_msg)
        distance_moved=abs(math.sqrt((x-a)**2)+((y-b)**2))
        print(distance_moved)
        print(x,"\t",y)
        if distance_moved>distance:
            rospy.loginfo("REACHED")
            break
    vel_msg.linear.x=0
    vel_publisher.publish(vel_msg)


if __name__=="__main__":
    try:
        position_topic='/turtle1/pose'
        rospy.Subscriber(position_topic,Pose,callback)
        moving_straight()
    except rospy.ROSInterruptException:
        print("STOPPED")
