#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Point,PoseStamped
from nav_msgs.msg import Odometry, Path

def commander():
    rospy.init_node('commander', anonymous=True)
    pub = rospy.Publisher('/destination', Path, queue_size=10)
    
    pth = Path()
    pth.header.frame_id = "/map"
    pth.header.stamp = rospy.Time.now()
    
    pose = PoseStamped()
    pose.pose.position.x = 0
    pose.pose.position.y = 0
    pth.poses.append(pose)
    
    pub.publish(pth)
    print("test path sent")
    time.sleep(5)
    
    multiplicateur=5
    
    while 1:      
        print("Creating path")  
        pth = Path()
        pth.header.frame_id = "/map"
        pth.header.stamp = rospy.Time.now()
        
        pose = PoseStamped()
        pose.pose.position.x = 0
        pose.pose.position.y = 0
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 0
        pose.pose.position.y = 1*multiplicateur
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 1*multiplicateur
        pose.pose.position.y = 1*multiplicateur
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 2*multiplicateur
        pose.pose.position.y = 3*multiplicateur
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 0.5*multiplicateur
        pose.pose.position.y = 4*multiplicateur
        pth.poses.append(pose)
        
        pub.publish(pth)
        print("Path sent")
        time.sleep(300)
        

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass
