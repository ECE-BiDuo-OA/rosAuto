#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Vector3Stamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

global xGPS, yGPS, vxGPS, vyGPS, oldvxGPS, oldvyGPS
global realx, realy
xGPS = yGPS = vxGPS = vyGPS = realx = realy =0

def callbackImu(data):
    theta=data.orientation.w
    time=data.header.stamp
    #print("theta={:.3f} time={}".format(theta,time))

def callbackGPS(data):
    global xGPS, yGPS, vxGPS, vyGPS, oldvxGPS, oldvyGPS
    dt=0.020 #seconds
    
    oldvxGPS=vxGPS
    oldvyGPS=vyGPS
    
    vxGPS=data.vector.x
    vyGPS=data.vector.y
    
    xGPS += (oldvxGPS+vxGPS) * dt/2
    yGPS += (oldvyGPS+vyGPS) * dt/2
    
    
    

def callbackHuskyVel(data):
    vx=data.twist.twist.linear.x
    vy=data.twist.twist.linear.y
    wx=data.twist.twist.angular.x
    wy=data.twist.twist.angular.y
    #print("vx={:.3f} vy={:.3f}".format(vx,vy))
    #print("wx={:.3f} wy={:.3f}".format(wx,wy))
    
def solution(data):
    global realx, realy
    realx=data.pose.pose.position.x
    realy=data.pose.pose.position.y
    

def localisateur():
    global xGPS, yGPS, realx, realy

    rospy.init_node('localisateur', anonymous=True)
    #pub = rospy.Publisher('/destination', Point, queue_size=10)
    rospy.Subscriber('/imu/data', Imu, callbackImu)
    rospy.Subscriber('/navsat/vel', Vector3Stamped, callbackGPS)
    rospy.Subscriber('/husky_velocity_controller/odom', Odometry, callbackHuskyVel)
    rospy.Subscriber('/odometry/filtered', Odometry, solution)
    
    #rate = rospy.Rate(10) # 1hz
    
    while not rospy.is_shutdown():
        print("")
        print("xGPS={:.3f} yGPS={:.3f}".format(xGPS,yGPS))
        print("realx={:.3f} realy={:.3f}".format(realx,realy))
        
        time.sleep(1)
        #rate.sleep()

if __name__ == '__main__':
    try:
        localisateur()
    except rospy.ROSInterruptException:
        pass
