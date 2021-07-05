import rospy
from learning_ros.srv import DHT11,DHT11Request,DHT11Response

def calci_client(x,y):
    rospy.init_node('client_node',anonymous=True)
    rospy.wait_for_service('dht11',timeout=40)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            client=rospy.ServiceProxy('dht11',DHT11)
            response=client(x,y)
            
            return response.Temp,response.Humidity
        except rospy.ServiceException as e:
            print("SERVICE FAILED %s"%e)


if __name__=="__main__":

    x=int(input("ENTER THE Temperature in farenheit:"))
    y=int(input("ENTER THE Humidity:"))

    


    print("REQUESTING ")
    t,h=calci_client(x,y)
    print("TEMP(c)={0}\n Humidity(%)={1}".format(t,h))

