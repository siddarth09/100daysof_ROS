from logging import disable
import rospy
from sensor_msgs.msg import Range


def callback(msg):
    distance=Range()
    if distance.min_range<distance.range:
        print("THE DISTANCE IS ", distance.range)

def sub():
    rospy.init_node('distance_finder',anonymous=True)
    rospy.Subscriber('ultrasound',Range,callback)
    rospy.spin()

if __name__=="__main__":
    try:
        sub()
    except rospy.ROSInterruptException:
        pass
