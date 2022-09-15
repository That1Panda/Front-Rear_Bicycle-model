#!/usr/bin/env python3

import cmd
from dis import dis
from re import X
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math 
from time import *



x=0
y=0
yaw=0


def poseCallback(pose_message):
    global x
    global y
    global yaw
    x=pose_message.x
    y=pose_message.y
    yaw=pose_message.theta


def go_to_goal():
    global x
    global y
    global yaw
    #xg,yg=int(input("Enter Value of x: ")),int(input("Enter Value of y: "))
    Ll,Lr=0.5,0.5
    v,Delta,time=float(input("Enter Value of v: ")),float(input("Enter Value of Delta: ")),int(input("time: "))
    Delta=math.radians(Delta)
    velocity_message=Twist()
    cmd_vel_topic="/turtle1/cmd_vel"
    
    tic = perf_counter()
    tics=0
    while(time>=tics and Delta>0) ^ rospy.is_shutdown():

        Delta=Delta-0.00001
        print(Delta)
        Epsi=velocity_message.angular.z
        
        Beta=math.atan((  (Ll/(Ll+Lr)) *math.tan(Delta)))
        vx=math.cos(Beta+Epsi)
        vy=math.sin(Beta+Epsi)
        
        yaw=(-v*math.tan(Delta)*math.cos(Beta))/(Ll+Lr)
        velocity_message.linear.x=vx
        velocity_message.linear.y=vy 
        velocity_message.angular.z=yaw

        velocity_publisher.publish(velocity_message)
        
                
        tic2=perf_counter()
        tics=tic2-tic
    
    
        
      
        # if(distance<0.01):
        #     go_to_goal()


    
    go_to_goal()
if __name__=="__main__":
    rospy.init_node("turtlesim_motion_pose",anonymous=True)

    cmd_vel_topic="/turtle1/cmd_vel"
    velocity_publisher=rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)

    position_topic="/turtle1/pose"
    pose_subscriber=rospy.Subscriber(position_topic,Pose,poseCallback)
    sleep(2)
    go_to_goal()
