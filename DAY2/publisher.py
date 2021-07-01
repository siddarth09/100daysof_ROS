import rospy
from geometry_msgs.msg import Point
import math

def coordinates():
    rospy.init_node('pub',anonymous=False)
    pub=rospy.Publisher('point',Point,queue_size=5)
    rate=rospy.Rate(1)

    

    pose=Point()
    x_=4.3
    y_=3.6
    z_=0.0

    #get final x,y,z from user

    x=float(input("ENTER final x"))
    y=float(input("ENTER final y"))

    X=x-x_
    Y=y-y_
    pose.x=X
    pose.y=Y
    pose.z=z_
    rospy.loginfo("COORDINATES ARE GETTING PUBLISHED")

    while not rospy.is_shutdown():
        pub.publish(pose)
        rospy.loginfo("COORDINATES ARE PUBLISHED")
        rate.sleep()
        
    
if __name__=="__main__":
    try:
        coordinates()
    except rospy.ROSInterruptException:
        rospy.loginfo("STOPPED")

   


    
