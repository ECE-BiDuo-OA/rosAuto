#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Point,PoseStamped
from nav_msgs.msg import Odometry, Path

def commander():
    rospy.init_node('commander', anonymous=True)
    pub = rospy.Publisher('/destination', Path, queue_size=10)
    
    while 1:        
        pth = Path()
        pth.header.frame_id = "/map"
        pth.header.stamp = rospy.Time.now()
        
        pose = PoseStamped()
        pose.pose.position.x = 0
        pose.pose.position.y = 0
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 0
        pose.pose.position.y = 1
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 1
        pose.pose.position.y = 1
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 2
        pose.pose.position.y = 3
        pth.poses.append(pose)
        
        pose = PoseStamped()
        pose.pose.position.x = 0.5
        pose.pose.position.y = 4
        pth.poses.append(pose)
        
        pub.publish(pth)
        print("Path sent")
        time.sleep(5)
        

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass
