# 100daysof_ROS

# DAY 1:
Contains Basic hello world publisher and subcriber, the publisher publishes on talker node while the subcriber subcribes the pubisher ie;talker node.
First run the roscore and then rosrun 100daysOfros helloworldpub.py (PUBLISHER)
Then rosrun 100daysOfros helloworldlist.py (SUBCRIBER)

# DAY 2:
here I used geomerty_msgs msg file which contains POINT,QUARTERNION,POSITION,TWIST which are used for robot motion which we will see using turtlebot3 later on.
I publish the difference between initial position and final position using POINT and then a subcriber subcribes on that topic and publishes the difference between the coordinates
