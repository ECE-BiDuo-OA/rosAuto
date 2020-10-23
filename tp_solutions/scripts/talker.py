#!/usr/bin/env python
#J. Marzat - ONERA, ECE Paris, 2020

import rospy, math
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose

xp = 2.0
yp = 3.0
kp = 1.0
omega = 0.0
vel = 0.0
velref = 0.0

def callback_dest(data):
    global xp, yp
    xp = data.x
    yp = data.y

def callback_pose(data):
    global vel, velref, omega
    phi = math.atan2(yp-data.y, xp-data.x)
    print('x = ' + str(data.x) + 'y = ' + str(data.y) + 'theta = ' + str(data.theta))
    delta = data.theta - phi
    #modulo
    if delta >= math.pi:	delta = delta - 2*math.pi
    if delta < -math.pi:	delta = delta + 2*math.pi
    omega = -kp*delta
    dist = math.sqrt((yp-data.y)*(yp-data.y)+(xp-data.x)*(xp-data.x))
    if dist <= 0.1: 
	vel = 0.0 
    else: 
	vel = velref
    print('phi = ' + str(phi))
    print('omega = ' + str(omega))

def talker():
    global vel, velref
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub_turtle = rospy.Subscriber('/turtle1/pose',Pose,callback_pose)
    sub_dest = rospy.Subscriber('/turtle1/destination',Point,callback_dest)
    velref = rospy.get_param('~vel',1.0)
    rate = rospy.Rate(10) # 10hz
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
