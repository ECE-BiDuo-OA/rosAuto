#!/usr/bin/env python
import rospy, random
import numpy as np
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry, Path
from turtlesim.msg import Pose
from geometry_msgs.msg import PoseStamped

xRef=3
yRef=2
vRef=0

Kp=1
Uv=0
Uw=0
pth=Path()

def callback_newRef(data):
    global xRef, yRef
    xRef = data.x
    yRef = data.y

def callback_command(data):
    global xRef, yRef, Uv, Uw
    print("\nxRef: {}\tyRef: {}".format(xRef,yRef))
    
    qz=data.pose.pose.orientation.z
    qw=data.pose.pose.orientation.w
    theta=np.arctan2(2 * qw * qz, 1 - 2 * qz * qz)
    
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    print("x: {}\ty: {}\ttheta: {}".format(x,y,theta))
    
    phi=np.arctan2((yRef - y),(xRef-x))
    print("phi: {}".format(phi))
    
    diff = theta - phi
    
    if diff >= np.pi:	diff -= 2*np.pi
    if diff < -np.pi:	diff += 2*np.pi
    print("diff: {}".format(diff))
    
    Uw=-Kp * diff
    if abs(diff) <= 0.01: Uw = 0.0
    Uw = min(0.5, Uw)
    
    dist = np.sqrt((yRef-y)**2+(xRef-x)**2)
    if dist > 2: Uv = 1
    if dist <= 2: Uv = dist/2
            
    print("Uw: {}\tUv: {}".format(Uw,Uv))
    
    print("Distance to target: {}".format(dist))

def createPath():
    global pth
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

    

def talker():
    global Uv, Uw
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odometry/filtered', Odometry, callback_command)
    rospy.Subscriber('/destination', Point, callback_newRef)
    
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
        createPath()
        talker()
    except rospy.ROSInterruptException:
        pass
