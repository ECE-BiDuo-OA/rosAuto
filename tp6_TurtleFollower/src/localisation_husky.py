#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Vector3Stamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

def callbackImu(data):
    theta=data.pose.pose.orientation.w
    print("theta={:.3f}".format(tetha))

def callbackGPS(data):
    x=data.Vector3.x
    y=data.Vector3.y
    print("x={:.3f} y={:.3f}".format(x,y))

def callbackHuskyVel(data):
    vx=data.twist.twist.linear.x
    vy=data.twist.twist.linear.y
    wx=data.twist.twist.angular.x
    wy=data.twist.twist.angular.y
    print("v={:.3f} w={:.3f}".format(v,w))
    
def solution(data):
    x=data.pose.pose.position.x
    y=data.pose.pose.position.y
    print("x={:.3f} y={:.3f}".format(x,y))

def localisateur():
    rospy.init_node('localisateur', anonymous=True)
    #pub = rospy.Publisher('/destination', Point, queue_size=10)
    rospy.Subscriber('/imu/data', Imu, callbackImu)
    rospy.Subscriber('/navsat/vel', Vector3Stamped, callbackGPS)
    rospy.Subscriber('/husky_velocity_controller/odom', Odometry, callbackHuskyVel)
    rospy.Subscriber('/odometry/filtered', Odometry, solution)
    
    #rate = rospy.Rate(10) # 1hz
    
    while not rospy.is_shutdown():
        
        time.sleep(1)
        #rate.sleep()

if __name__ == '__main__':
    try:
        localisateur()
    except rospy.ROSInterruptException:
        pass
