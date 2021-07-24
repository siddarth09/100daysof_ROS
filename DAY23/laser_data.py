import rospy 
from sensor_msgs.msg import LaserScan
import math

def sensor_cb(msg):
    print("-----------------------------")
    print("GETTING LASER DATA:")
    print("start angle of scan :",math.degrees(msg.angle_min))
    print("end angle of scan :",math.degrees(msg.angle_max))
    print("RANGE :",max(msg.ranges))
    print("MAX RANGE:",msg.range_max)
    print("-----------------------------")
    print("RANGE at 0",msg.ranges[0])
    print("-----------------------------")
    print("RANGE at 90",msg.ranges[360-1])
    
if __name__=="__main__":
    rospy.init_node('scan_data')
    rospy.Subscriber('/scan',LaserScan,sensor_cb)
    rospy.spin()