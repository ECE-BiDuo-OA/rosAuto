#!/usr/bin/env python
#J. Marzat - ONERA, ECE Paris, 2020

import rospy, math
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose

xp = 2.0
yp = 3.0
kp = 0.5
omega = 0.0
vel = 0.0
velref = 0.0

def callback_dest(data):
    global xp, yp
    xp = data.x
    yp = data.y

def callback_pose(data):
    global vel, velref, omega
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    q = data.pose.pose.orientation
    theta = math.atan2(2*q.w*q.z,1-2*q.z*q.z)
    phi = math.atan2(yp-y, xp-x)
    print('x = ' + str(x) + 'y = ' + str(y) + 'theta = ' + str(theta))
    delta = theta - phi
    #modulo
    if delta >= math.pi:	delta = delta - 2*math.pi
    if delta < -math.pi:	delta = delta + 2*math.pi
    dist = math.sqrt((yp-y)*(yp-y)+(xp-x)*(xp-x))
    if dist <= 0.2: 
	    vel = 0.0
	omega = 0.0    
    else: 
	vel = velref
	omega = -kp*delta
    print('phi = ' + str(phi))
    print('omega = ' + str(omega))

def talker():
    global vel, velref
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)
    sub_turtle = rospy.Subscriber('/odometry/filtered',Odometry,callback_pose)
    sub_dest = rospy.Subscriber('/destination',Point,callback_dest)
    velref = rospy.get_param('~vel',0.5)
    rate = rospy.Rate(20) # 10hz
    while not rospy.is_shutdown():
	speed = Twist()
	speed.linear.x = vel
	speed.angular.z = omega
	print(speed)
	pub.publish(speed)
	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
