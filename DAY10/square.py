import math
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

x=0
y=0
yaw=0

def moving_straight(speed,distance,forward):
    global x,y
    rospy.init_node('my_node',anonymous=True)
    vel_msg=Twist()
    vel_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    a=x
    b=y
    

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
def rotating(angular_speed_degree,relative_degree,clockwise):
    velocity_msgs=Twist()
    #rospy.init_node('turtlesim_node',anonymous=True)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    

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


def square():
    moving_straight(1.0,2.0,True)
    rotating(5.0,1.45,True)
    moving_straight(1.0,2.0,True)
    rotating(5.0,1.45,True)
    moving_straight(1.0,2.0,True)
    rotating(5.0,1.45,True)
    moving_straight(1.0,2.0,True)
    rotating(5.0,1.45,True)
    rospy.loginfo("SQUARE FINISHED")




def callback(msg):
    global x
    global y,yaw
    x=msg.x
    y=msg.y
    yaw=msg.theta

if __name__=="__main__":
    try:
        position_topic='/turtle1/pose'
        rospy.Subscriber(position_topic,Pose,callback)
        square()
        
    except rospy.ROSInterruptException:
        print("STOPPED")