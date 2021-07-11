#include <ros.h>
#include <std_msgs/Empty.h>

ros::NodeHandle  nh;
int blue=7;
int red=6;
int green=5;

void callback(const std_msgs::Empty& toggle_msg)
{
  digitalWrite(blue,HIGH);
  delay(500);
  digitalWrite(red,HIGH);
  delay(500);
  digitalWrite(green,HIGH);
  delay(500);
  digitalWrite(blue,LOW);
  delay(500);
  digitalWrite(red,LOW);
  delay(500);
  digitalWrite(green,LOW);
  delay(500);
  
  
}

ros::Subscriber<std_msgs::Empty> sub("toggle",&callback);



void setup() {
  // put your setup code here, to run once:
  pinMode(blue,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  nh.initNode();
  nh.subscribe(sub);

}

void loop() {
  // put your main code here, to run repeatedly:
 
  nh.spinOnce();
  delay(500);
  }
