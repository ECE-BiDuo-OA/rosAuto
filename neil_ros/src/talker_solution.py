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
    x=data.x
    y=data.y
    theta=data.theta
    print('x = {} y = {} theta = {}'.format(x,y,theta))

    phi = math.atan2(yp-y, xp-x)
    print('phi = ' + str(phi))

    #modulo
    delta = theta - phi
    if delta >= math.pi:	delta = delta - 2*math.pi
    if delta < -math.pi:	delta = delta + 2*math.pi

    omega = -kp*delta
    print('omega = ' + str(omega))

    dist = math.sqrt((yp-y)*(yp-y)+(xp-x)*(xp-x))
    if dist <= 0.1:
        vel = 0.0
    else:
        vel = velref

def talker():
    global vel, velref
    velref = rospy.get_param('~vel',1.0)

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose,callback_pose)
    rospy.Subscriber('/turtle1/destination',Point,callback_dest)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        speed = Twist()

        speed.linear.x = vel
        speed.angular.z = omega

        pub.publish(speed)
        print(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
