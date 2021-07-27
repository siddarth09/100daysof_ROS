# 100daysof_ROS

reference book: https://drive.google.com/file/d/1nckp9GA5Iex9uFXzxjMVUoxUfa3sxZWE/view?usp=sharing

# DAY 1:
Contains Basic hello world publisher and subcriber, the publisher publishes on talker node while the subcriber subcribes the pubisher ie;talker node.
First run the roscore and then rosrun 100daysOfros helloworldpub.py (PUBLISHER)
Then rosrun 100daysOfros helloworldlist.py (SUBCRIBER)

# DAY 2:
here I used geomerty_msgs msg file which contains POINT,QUARTERNION,POSITION,TWIST which are used for robot motion which we will see using turtlebot3 later on.
I publish the difference between initial position and final position using POINT and then a subcriber subcribes on that topic and publishes the difference between the coordinates.

# DAY 3:
here i have used a custom message LDR, which can be used with sensors either with a rasberry pi or arduino(rosserial). The ldrpub gets the sensor value (which i will be doing on day 20 with sensors) and publishes, while the ldrlist subcribes to LDR_SENSOR topic and displays the value.

# DAY 4:
today I created a custom srv file to use for my calculator, the calserver gets the request from calclient, calculates according to the operation the user needs and sends back the response for the client.

# DAY 5:
Following the same procedure for srv file, today I created a DHT11 srv file for dht11 server and client operations. 

# DAY 6:
Teleoppub.py can be used to control the turtle to move in any direction as possible.To start turtlesim we can use, rosrun turtlesim turtlesim_node.

# DAY 7:
we can use the code to tell the turtle to swim in a straight line, the straight.py publishes on cmd_vel topic and subcribes to pose topic for X and Y corrdinates
the distance is measured using euclidean distance formula.
# DAY 8:
using the geometry_msgs and turtlesim's Pose msg we use the publisher and subcriber to communicate and help the turtle rotate around its fixed axis

# DAY 9:
we tell the turtle to move to specific goal using geometry_msg topic 

# DAY 10:
Using Day 6 and 7 algorithms, I have a created a basic algorithm to make the turtle swim and draw a square pattern, here I have also used how to use LAUNCH files

# DAY 11:
Today we wil start with arduino and rosserial, we use rosserial command to connect with the avr to control led pins attached.

# DAY 12:
We connect the DHT11 and create a publisher node, then we subcribe to the publisher of dht11 to display the temperature data recieved.

# DAY 13:
Ultrasound sensors, Today we take the input from the ultrasound sensor and publish the range, the sensor_msgs/Range collects the information.The subscriber node is created to lock on the ultrasound sensor to retrieve the sensor data.
# DAY 14:
Servo motors, the servo is subcribed to "servo" topic while the publisher node publishes the angle of rotation, the servo motor starts rotating.

# DAY 15:
LDR, Using the msg file created on DAY 3, I used this to get the intensity form LDR sensor.

# DAY 16:
speed control of DC Motors with pwm passed though geometry_msgs msg file.The subscriber gets the speed of the motor at that period of time and displays it 

# DAY 17:
basic conversion of roll,pitch and yaw into quarternion coordinate format using tf package.

# DAY 18:
Built map using SLAM(gmapping) techniques for turtlebot3 maze.

# DAY 19:
when a robot is moving or a manipulator is grasping, many frames are acting at different origins, to get the transformation data of a target frame from a source frame. We use static transforms to get the translation and rotation of the target frame to the source frame.Here the broadcaster node finds the above-mentioned transform and sends the data to the base station.

# DAY 20:
Used turtlebot3 nav stack to navigate the waffle around the world using rviz

# DAY 21:
used turtlebot3 SLAM stack to map the house using gmapping methods.

# DAY 22:
Today I used go to goal,algorithm used for turtlesim.The waffle bot will move to a specific location but here it will not avoid any obstacles.

# DAY 23:
Using laser scan data sent by the Lidar on the bot, we get the data while the bot is moving with teleoperation.

# DAY 24:
Simple ways to get the position data, using nav_msgs/Odometry. we will see more of this use cases when we start Lidar based navigation.

# DAY 25:
action server and client, are used for asynchronous way of communication, here the dishwasher example is used for simple action server and aaction client mechanishm 

# DAY 26:
I used the same concept of action server and action client, with an example of pizza delivery 

# DAY 27:
Used open cv to perfom simple operations on images 




