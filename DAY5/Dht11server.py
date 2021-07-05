import rospy
from learning_ros.srv import DHT11,DHT11Request,DHT11Response
import math


def sensor_callback(req):
    print("THE TEMPERATURE AND HUMIDITY IS CALCULATED")
    temperature=round(((req.x-32)*5/9),2)
    humidity=req.y
    return DHT11Response(temperature,humidity)

def get_value():
    rospy.init_node('sensor')
    s= rospy.Service('dht11',DHT11,sensor_callback)
    print("DHT11 Started sensing ")
    rospy.spin()
if __name__=="__main__":
    get_value()
