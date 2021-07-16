#include <ros.h>
#include <geometry_msgs/Twist.h>

int in3=8;
int in4=7;
int ena=3;
int pwm;

ros::NodeHandle nh;
geometry_msgs::Twist msg;

void cb(const geometry_msgs::Twist &msg)
{
   pwm=msg.linear.x;
   analogWrite(ena,pwm);
   digitalWrite(in3,HIGH);
   digitalWrite(in4,LOW);
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &cb);

void setup()
{
  pinMode(ena,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}
void loop()
{
  nh.spinOnce();
  delay(1000);
}
