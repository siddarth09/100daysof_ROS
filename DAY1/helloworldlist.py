import rospy
from std_msgs.msg import String

def callback_listener(msg):
    rospy.loginfo(rospy.get_caller_id()+"  I HEARD  "+msg.data)

def subcriber():
    rospy.init_node('Subcriber',anonymous=False)
    rospy.Subscriber('talker',String,callback=callback_listener)
    rospy.spin()

if __name__=="__main__":
    subcriber()