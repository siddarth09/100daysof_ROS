#include <ros.h>
#include <sensor_msgs/Range.h>
#include <ros/time.h>

ros::NodeHandle nh;
sensor_msgs::Range range;
ros::Publisher pub("ultrasound",&range);

int echopin=9;
int trigpin=5;
long duration;
int distance;


void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  pinMode(trigpin, OUTPUT); 
  pinMode(echopin, INPUT);
  pinMode(3,OUTPUT);
  nh.advertise(pub);
  range.radiation_type=sensor_msgs::Range::ULTRASOUND;
  range.min_range= 5.60;
  range.max_range= 140.60;
  

}

void loop() {
  // put your main code here, to run repeatedly:
  range.range=getSonar();
  pub.publish(&range);
  nh.spinOnce();
  delay(1000);
  }
  
float getSonar() {
  unsigned long ping;
  float distance;
  float timeOut=range.max_range*60;
  digitalWrite(trigpin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigpin, LOW);
  ping = pulseIn(echopin, HIGH, timeOut);
  distance = (float)ping * 340 / 2 / 10000; // calculate the distance according to the time
  if (distance<15)
  {
    digitalWrite(3,HIGH);
  }
  else
  {
    digitalWrite(3,LOW);
  }
  
  return distance; // return the distance value
}
