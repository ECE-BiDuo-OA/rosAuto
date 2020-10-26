#!/usr/bin/env python
import rospy, random
import numpy as np
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose

xRef=2
yRef=2
vRef=0

Kp=1
Uv=0
Utheta=0

def callback(data):
    global xRef,yRef,Uv, Utheta
    x = data.x
    y = data.y
    theta = data.theta
    print("x: {}\ty: {}\ttheta: {}".format(x,y,theta))
    
    phi=np.arctan((yRef - y)/(xRef-x))
    diff = theta - phi
    w=-Kp * diff
    
    Utheta = theta+ 0.1 * w
    Uv=vRef
    print("Utheta: {}\tUv: {}".format(Utheta,Uv))
    

def talker():
    global Uv, Utheta
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
        speed.angular.z = Utheta
        #print(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
