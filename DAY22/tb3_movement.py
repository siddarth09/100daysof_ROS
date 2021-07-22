import actionlib
import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal

def gotogoal():
    print("ENTER THE GOAL TO BE REACHED")
    x=float(input())
    y=float(input())
    velocity_msg=Twist()
    velocity_publisher=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    #giving parameter
    velocity_msg.linear.x=2
    rate=rospy.Rate(1)
    print("INITIAL POSE")

    ac=actionlib.SimpleActionClient('move_base',MoveBaseAction)

    goal=MoveBaseGoal()
    while (not ac.wait_for_server(rospy.Duration(5))):
        rospy.loginfo("WAITING FOR THE SERVER TO START")
    print("CURRENT VELOCITY:",velocity_msg.linear.x)

    #setup frame parameters for the bot
    goal.target_pose.header.frame_id='map'
    goal.target_pose.header.stamp=rospy.Time.now()

    #setup intital pose
    goal.target_pose.pose.position=Point(x,y,0)#contains a point in free space
    goal.target_pose.pose.orientation.x=0.0
    goal.target_pose.pose.orientation.y=0.0
    goal.target_pose.pose.orientation.z=0.0
    goal.target_pose.pose.orientation.w=1.0

    rospy.loginfo("SENDING GOAL INFORMATION")
    ac.send_goal(goal)
    ac.wait_for_result(rospy.Duration(60))
    velocity_publisher.publish(velocity_msg)
    rate.sleep()

    
        

    if (ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("REACHED THE DESTINATION")
        return True
    else:
        rospy.loginfo("THE BOT DIDN'T REACH ITS DESTINATION")
        return False

def posecallback(odom_msg):
    print("POSITION")
    print("px=",odom_msg.pose.pose.position.x)
    print("py=",odom_msg.pose.pose.position.y)
    print("---------------------------------")

if __name__=="__main__":

    rospy.init_node('map_navigation',anonymous=False)
    '''position_topic='/odom'
    rospy.Subscriber(position_topic,Odometry,posecallback)'''
    
    gotogoal()
    rospy.spin()
