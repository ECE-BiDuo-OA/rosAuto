#!/usr/bin/env python
import rospy, random
import numpy as np
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped

xRef=3
yRef=2
vRef=0

Kp=1
Uv=0
Uw=0

pointsList=[]
index=0


def callback_newPath(data): 
    print("Kishor King")
    
    global pointsList,index
    pointsList=[]
    index=0
    
    for poseStamped in data.poses:
        x = poseStamped.pose.position.x
        y = poseStamped.pose.position.y
        pointsList.append([x, y])
    
    print(pointsList)

def callback_command(data):
    global xRef, yRef, Uv, Uw
    #print("\nxRef: {}\tyRef: {}".format(xRef,yRef))
    
    qz=data.pose.pose.orientation.z
    qw=data.pose.pose.orientation.w
    theta=np.arctan2(2 * qw * qz, 1 - 2 * qz * qz)
    
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    #print("x: {}\ty: {}\ttheta: {}".format(x,y,theta))
    
    phi=np.arctan2((yRef - y),(xRef-x))
    #print("phi: {}".format(phi))
    
    diff = theta - phi
    
    if diff >= np.pi:	diff -= 2*np.pi
    if diff < -np.pi:	diff += 2*np.pi
    #print("diff: {}".format(diff))
    
    Uw=-Kp * diff
    if abs(diff) <= 0.01: Uw = 0.0
    Uw = min(0.5, Uw)
    
    dist = np.sqrt((yRef-y)**2+(xRef-x)**2)
    if dist > 2: Uv = 1
    if dist <= 2: Uv = dist/2
            
    #print("Uw: {}\tUv: {}".format(Uw,Uv))
    
    #print("Distance to target: {}".format(dist))

    

def talker():
    global Uv, Uw
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odometry/filtered', Odometry, callback_command)
    rospy.Subscriber('/destination', Path, callback_newPath)
    
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
