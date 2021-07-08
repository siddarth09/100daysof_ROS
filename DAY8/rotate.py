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

def rotating():
    velocity_msgs=Twist()
    rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    print("GIVE YOUR INPUT")
    angular_speed_degree=float(input("ENTER THE SPEED OF ROTATION"))
    relative_degree=float(input("ENTER THE DEGREE OF ROTATION"))
    clockwise=input("CLOCKWISE:?")

    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_msgs.angular.z=-abs(angular_speed)
    else:
        velocity_msgs.angular.z=abs(angular_speed)
    loop_rate=rospy.Rate(1)
    t0=rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("TURTLE IS ROTATING")
        velocity_publisher.publish(velocity_msgs)
        t1=rospy.Time.now().to_sec()
        current_degree=angular_speed*(t1-t0)
        loop_rate.sleep()

        print(current_degree)
        if current_degree>relative_degree:
            rospy.loginfo("REACHED")
            break
    velocity_msgs.angular.z=0
    velocity_publisher.publish(velocity_msgs)

    

if __name__=="__main__":
    try:
        position_topic='/turtle1/pose'
        rospy.Subscriber(position_topic,Pose,callback)
        rotating()
    except rospy.ROSInterruptException:
        print("STOPPED")
