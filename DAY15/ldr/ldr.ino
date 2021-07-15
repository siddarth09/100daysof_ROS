#include <ros.h>
#include <learning_ros/LDR.h>

ros::NodeHandle nh;
learning_ros::LDR detect;

ros::Publisher pub("LDR_SENSOR",&detect);
int ledpin= 10;



void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.advertise(pub);
  pinMode(ledpin,OUTPUT);
  digitalWrite(ledpin,LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  detect.intensity=analogRead(A0);
  pub.publish(&detect);
  if (detect.intensity <= 200)
  {
    digitalWrite(ledpin,HIGH);
  }
  else
  {
    digitalWrite(ledpin,LOW);
  }
  nh.spinOnce();
  delay(500);
    
  }
  
