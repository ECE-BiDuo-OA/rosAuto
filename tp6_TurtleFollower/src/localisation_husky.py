#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Vector3Stamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

global xGPS, yGPS, vxGPS, vyGPS, oldvxGPS, oldvyGPS
global realx, realy
global theta, v
xGPS = yGPS = vxGPS = vyGPS = realx = realy = theta = v = oldvxGPS = oldvyGPS= 0

def callbackImu(data):
    global theta
    theta=data.orientation.w
    #print("theta={:.3f}".format(theta))

def callbackGPS(data):
    global xGPS, yGPS, oldvxGPS, oldvyGPS, vxGPS, vyGPS
    dt=0.020 #seconds
    
    oldvxGPS=vxGPS
    oldvyGPS=vyGPS
    
    vxGPS=data.vector.x
    vyGPS=data.vector.y
    
    xGPS += (oldvxGPS+vxGPS) * dt/2
    yGPS += (oldvyGPS+vyGPS) * dt/2

def callbackHuskyVel(data):
    global v
    v=data.twist.twist.linear.x
    #print("v={:.3f}".format(v))
    
def solution(data):
    global realx, realy
    realx=data.pose.pose.position.x
    realy=data.pose.pose.position.y
    

def localisateur():
    global xGPS, yGPS, realx, realy, theta, v

    rospy.init_node('localisateur', anonymous=True)
    #pub = rospy.Publisher('/destination', Point, queue_size=10)
    rospy.Subscriber('/imu/data', Imu, callbackImu)
    rospy.Subscriber('/navsat/vel', Vector3Stamped, callbackGPS)
    rospy.Subscriber('/husky_velocity_controller/odom', Odometry, callbackHuskyVel)
    rospy.Subscriber('/odometry/filtered', Odometry, solution)
    
    #rate = rospy.Rate(10) # 1hz
    
    xGPS = yGPS = xOdom = yOdom = 0
    while not rospy.is_shutdown():
        xOdom += v*np.cos(theta)
        yOdom += v*np.sin(theta)
        
        
        print("      x      y")
        print("real {:.3f} {:.3f}".format(realx,realy))
        print("GPS  {:.3f} {:.3f}".format(xGPS,yGPS))
        print("Odom {:.3f} {:.3f}".format(xOdom,yOdom))
        
        time.sleep(1)
        #rate.sleep()

if __name__ == '__main__':
    try:
        localisateur()
    except rospy.ROSInterruptException:
        pass
