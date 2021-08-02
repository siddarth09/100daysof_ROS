import rospy
from  sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


pub=None
vel_msg=Twist()
def obstacle(msg):
    print(msg.ranges[0])
    if msg.ranges[0]<0.8:
        if msg.ranges[90]<=msg.ranges[270]:
            vel_msg.linear.x=0
            vel_msg.angular.z=-0.5

        elif msg.ranges[90]>msg.ranges[270]:
            vel_msg.linear.x=0
            vel_msg.angular.z=0.5
    else:
        vel_msg.linear.x=0.3
        vel_msg.angular.z=0.0

    pub.publish(vel_msg)

if __name__=="__main__":
    rospy.init_node('obstacle_avoider')
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    rospy.Subscriber('/scan',LaserScan,obstacle)
    rate=rospy.Rate(1)
    
    rospy.spin()