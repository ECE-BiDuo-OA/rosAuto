#!/usr/bin/env python

import rospy
from mav_msgs.msg import RollPitchYawrateThrust
from nav_msgs.msg import Odometry

kp = 2.0
kd = 3.0
ax = 0.0
ay = 0.0
az = 0.0

def callback_odom(data):
    global kp, kd, ax, ay, az
    px = data.pose.pose.position.x
    py = data.pose.pose.position.y
    pz = data.pose.pose.position.z
    vx = data.twist.twist.linear.x
    vy = data.twist.twist.linear.y
    vz = data.twist.twist.linear.z
    
    xref = 0.5
    yref = -0.5
    zref = 1.0

    sat = 0.2

    ax = (-kp*(px-xref) - kd*vx)/9.81 #to check 1/g
    ay = (-kp*(py-yref) - kd*vy)/9.81 #to check 1/g
    if ax > sat: ax=sat
    if ax < -sat: ax = -sat
    if ay > sat: ay=sat
    if ay < -sat: ay = -sat
    az = -kp*(pz-zref) - kd*vz

def rpyt_pub():
    global ax,ay,az
    rospy.init_node('rpyt_pub', anonymous=True)
    pub = rospy.Publisher('/firefly/command/roll_pitch_yawrate_thrust', RollPitchYawrateThrust, queue_size=10)
    sub = rospy.Subscriber('/firefly/odometry_sensor1/odometry',Odometry,callback_odom)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = RollPitchYawrateThrust()
	msg.roll = -ay	    # rad	
	msg.pitch = ax      # rad	
	msg.yaw_rate = 0.0  # rad/s
 	mav_offset = 15.15
	msg.thrust.z = az + mav_offset # basically m*g + acc
        pub.publish(msg)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        rpyt_pub()
    except rospy.ROSInterruptException:
        pass
