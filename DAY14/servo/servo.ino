#include <ros.h>
#include <Servo.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;

Servo servo;

void cb( const std_msgs::Int16& angle)
{
  servo.write(angle.data);
  digitalWrite(13,HIGH);
}
ros::Subscriber<std_msgs::Int16> sub("servo", cb);

void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  servo.attach(10);

}

void loop() {
  // put your main code here, to run repeatedly"
  nh.spinOnce();
  delay(100);
}
