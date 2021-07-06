# 100daysof_ROS

# DAY 1:
Contains Basic hello world publisher and subcriber, the publisher publishes on talker node while the subcriber subcribes the pubisher ie;talker node.
First run the roscore and then rosrun 100daysOfros helloworldpub.py (PUBLISHER)
Then rosrun 100daysOfros helloworldlist.py (SUBCRIBER)

# DAY 2:
here I used geomerty_msgs msg file which contains POINT,QUARTERNION,POSITION,TWIST which are used for robot motion which we will see using turtlebot3 later on.
I publish the difference between initial position and final position using POINT and then a subcriber subcribes on that topic and publishes the difference between the coordinates

# DAY 3:
here i have used a custom message LDR, which can be used with sensors either with a rasberry pi or arduino(rosserial). The ldrpub gets the sensor value (which i will be doing on day 20 with sensors) and publishes, while the ldrlist subcribes to LDR_SENSOR topic and displays the value 

# DAY 4:
today I created a custom srv file to use for my calculator, the calserver gets the request from calclient, calculates according to the operation the user needs and sends back the response for the client.

# DAY 5:
Following the same procedure for srv file, today I created a DHT11 srv file for dht11 server and client operations 

# DAY 6:
Teleoppub.py can be used to control the turtle to move in any direction as possible.To start turtlesim we can use, rosrun turtlesim turtlesim_node



