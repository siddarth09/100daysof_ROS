import rospy
from geometry_msgs.msg import Point

def sub_callback(msg):

    rospy.loginfo("the difference between coordinates are {0} and {1}".format(msg.x,msg.y))


def sub():
    rospy.init_node('sub',anonymous=False)
    rospy.Subscriber('point',Point,callback=sub_callback)
    rospy.spin()

if __name__=="__main__":
    sub()