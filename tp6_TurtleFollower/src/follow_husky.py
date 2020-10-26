#!/usr/bin/env python
import rospy, random
import numpy as np
from geometry_msgs.msg import Twist, Point
from nav_msgs import Odometry
from turtlesim.msg import Pose

xRef=3
yRef=2
vRef=0

Kp=1
Uv=0
Uw=0

def callback_newRef(data):
    global xRef, yRef
    xRef = data.x
    yRef = data.y

def callback_command(data):
    global xRef, yRef, Uv, Uw
    print("\nxRef: {}\tyRef: {}".format(xRef,yRef))
    
    qz=data.pose.pose.orientation.z
    qw=data.pose.pose.orientation.w
    phi=np.arctan2(2 * qw * qz, 1 - 2 * qz * qz)
    print("phi: {}".format(phi))
    
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    theta = data.theta
    print("x: {}\ty: {}\ttheta: {}".format(x,y,theta))
    
    diff = theta - phi
    
    if diff >= np.pi:	diff -= 2*np.pi
    if diff < -np.pi:	diff += 2*np.pi
    print("diff: {}".format(diff))
    
    Uw=-Kp * diff
    if abs(diff) <= 0.01: Uw = 0.0
    
    dist = np.sqrt((yRef-y)**2+(xRef-x)**2)
    Uv=min(dist,1)
    if dist <= 0.01: Uv = 0.0
            
    print("Uw: {}\tUv: {}".format(Uw,Uv))
    
    print("Distance to target: {}".format(dist))
    

def talker():
    global Uv, Uw
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Odometry, queue_size=10)
    rospy.Subscriber('/odometry/filtered', Pose, callback_command)
    rospy.Subscriber('/turtle1/destination', Point, callback_newRef)
    
    rate = rospy.Rate(10) # 1hz

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
