
#include <dht.h>
#include <ros.h>
#include <std_msgs/Float64.h>
#define dht_apin A0 // Analog Pin sensor is connected to

dht DHT;
ros::NodeHandle nh;
std_msgs::Float64 temp;
ros::Publisher chatter('dht11',&temp);
 
void setup(){
 
  
  nh.initNode();
  nh.advertise(chatter);
 
}//end "setup()"
 
void loop(){
   
 
    DHT.read11(dht_apin);
    temp.data=DHT.temperature;
    
    
    chatter.publish(&temp);
    nh.spinOnce();
    delay(1000);
    
   
 
  
 
}
