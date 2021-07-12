import rospy
from rospy.topics import Subscriber
from std_msgs.msg import Float64

def callback(msg):
    print("Temperature = ",msg.data)
    

def Sub():
    rospy.init_node('DHT11',anonymous=True)
    rospy.Subscriber('chatter',Float64,callback)
    rospy.spin()

if __name__=="__main__":
    Sub()