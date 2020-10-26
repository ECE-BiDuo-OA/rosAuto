#!/usr/bin/env python
import rospy, random
import numpy as np
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose

xRef=3
yRef=2
vRef=0

Kp=1
Uv=0
Uw=0

def callback(data):
    global xRef, yRef, Uv, Uw
    x = data.x
    y = data.y
    theta = data.theta
    print("x: {}\ty: {}\ttheta: {}".format(x,y,theta))
    
    phi=np.arctan2((yRef - y),(xRef-x))
    diff = theta - phi
    
    if diff >= np.pi:	diff -= 2*np.pi
    if diff < -np.pi:	diff += 2*np.pi
    print("diff: {}".format(diff))
    
    Uw=-Kp * diff
    if diff <= 0.01: Uw = 0.0
    
    dist = np.sqrt((yRef-y)**2+(xRef-x)**2)
    Uv=min(dist,1)
    if dist <= 0.01: Uv = 0.0
            
    print("Uw: {}\tUv: {}".format(Uw,Uv))
    
    print("Distance to target: {}".format(dist))
    

def talker():
    global Uv, Uw
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    
    rate = rospy.Rate(10) # 1hz
    
    try:
        minSpeed = rospy.get_param(rospy.search_param("minSpeed"))
        maxSpeed = rospy.get_param(rospy.search_param("maxSpeed"))
        assert minSpeed + maxSpeed +1
    except:
        minSpeed = -2
        maxSpeed = 2
        print("No param, min will be set to {} and max to {}".format(minSpeed,maxSpeed))
        

    while not rospy.is_shutdown():
        speed = Twist()
        speed.linear.x = Uv
        speed.angular.z = Uw
        #print(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
