import numpy as np 
from math import *

class transformation:
    def __init__(self):
        self.length_of_link=0
        self.angle_of_twist=0
        self.offset_link=0
        self.joint_angle=0

    def x_transform(self,x,y,z,theta):
        mat_x=[[1,0,0,x],
            [0,cos(theta),-sin(theta),y],
            [0,sin(theta),cos(theta),z],
            [0,0,0,1]]
        mat_x = np.array(mat_x)
        return mat_x 
    def y_transform(self,x,y,z,theta):
        mat_x=[[cos(theta),0,sin(theta),0,x],
            [0,1,0,y],
            [-sin(theta),0,cos(theta),z],
            [0,0,0,1]]
        mat_x = np.array(mat_x)
        return mat_x 
    def z_transform(self,x,y,z,theta):
        mat_x=[[cos(theta),-sin(theta),0,x],
            [sin(theta),cos(theta),0,y],
            [0,0,1,z],
            [0,0,0,1]]
        mat_x = np.array(mat_x)
        return mat_x

     

    
    
if __name__=="__main__":
    robot=transformation()
    #for 3DOF arm
    t1=robot.z_transform(0,0,0,30)*robot.x_transform(0,0,0,-90)
    t2=robot.z_transform(0,0,0,30)*robot.x_transform(3,3,2,0)
    t3=robot.z_transform(0,0,0,30)*robot.x_transform(0,0,0,90)

    print("TRANSFORMATION :{}".format(t1*t2*t3))
    
    
    

    

        
    