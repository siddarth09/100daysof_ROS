import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf
import time
from std_srvs.srv import Empty

def posecallback(odom_msg):
    print("POSITION")
    print("px=",odom_msg.pose.pose.position.x)
    print("py=",odom_msg.pose.pose.position.y)
    print("---------------------------------")
    print("VELOCITY")
    print("vx=",odom_msg.twist.twist.linear.x)
    print("vy=",odom_msg.twist.twist.angular.y)
    print("----------------------------------")
    print("ORIENTATION")
    print("x=",odom_msg.pose.pose.orientation.x)
    print("y=",odom_msg.pose.pose.orientation.y)
    print("z=",odom_msg.pose.pose.orientation.z)
    print("w=",odom_msg.pose.pose.orientation.w)

    quaternion=(odom_msg.pose.pose.orientation.x,
                odom_msg.pose.pose.orientation.y,
                odom_msg.pose.pose.orientation.z,
                odom_msg.pose.pose.orientation.w)

    rpy=tf.transformations.euler_from_quaternion(quaternion)
    roll=rpy[0]
    pitch=rpy[1]
    yaw=rpy[2]

    print("ROLL= {0}, PITCH= {1}, YAW= {2}".format(math.degrees(roll),math.degrees(pitch),math.degrees(yaw)))





if __name__=="__main__":

    try:
        rospy.init_node("position_data",anonymous=True)
        position_topic='/odom'
        subcriber=rospy.Subscriber(position_topic,Odometry,posecallback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("node_terminated")