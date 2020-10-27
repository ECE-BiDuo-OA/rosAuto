#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Point,PoseStamped
from nav_msgs.msg import Odometry, Path

def commander():
    rospy.init_node('commander', anonymous=True)
    pub = rospy.Publisher('/destination', Point, queue_size=10)
    
    time.sleep(5)
    
    pth = Path()
    pth.header.frame_id = "/map"
    pth.header.stamp = rospy.Time.now()
    
    pose = PoseStamped()
    pose.pose.position.x = 5
    pose.pose.position.y = 5
    msg.poses.append(pose)
    
    pose.pose.position.x = 2
    pose.pose.position.y = 2
    pth.poses.append(pose)
    
    pub.publish(pth)
        

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass
