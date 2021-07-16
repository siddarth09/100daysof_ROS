import rospy
from geometry_msgs.msg import Twist

def callback(msg):
    print("THE MOTOR IS ROTATING AT ",msg.linear.x)

def sub():
    rospy.init_node("motor",anonymous=True)
    rospy.Subscriber('cmd_vel',Twist,callback)
    rospy.spin()

if __name__=="__main__":
    sub()