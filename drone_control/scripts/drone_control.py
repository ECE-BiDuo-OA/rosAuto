#!/usr/bin/env python

import rospy
from mav_msgs.msg import RollPitchYawrateThrust
from nav_msgs.msg import Odometry

def callback_odom(data):    
    #process odometry and compute control here
    poseCovar = data.pose.pose.position
    twistCovar = data.twist.twist
    
    x = poseCovar.x
    y = poseCovar.y
    z = poseCovar.z
   
    lx = twistCovar.linear.x
    ly = twistCovar.linear.y
    lz = twistCovar.linear.z

    ax = twistCovar.angular.x
    ay = twistCovar.angular.y
    az = twistCovar.angular.z
    
    print("x: {}\ty: {}\tz: {}".format(x,y,z))
    print("lx: {}\tly: {}\tlz: {}".format(lx,ly,lz))
    print("ax: {}\tay: {}\taz: {}".format(ax,ay,az))
    print("")

def drone_control():
    rospy.init_node('drone_control', anonymous=True)
    pub = rospy.Publisher('/firefly/command/roll_pitch_yawrate_thrust', RollPitchYawrateThrust, queue_size=10)
    sub = rospy.Subscriber('/firefly/odometry_sensor1/odometry',Odometry,callback_odom)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = RollPitchYawrateThrust()
	msg.roll = 0.0	   		# rad	
	msg.pitch = 0.0    		# rad	
	msg.yaw_rate = 0.0  		# rad/s
	mass = 1.544
	msg.thrust.z = mass*(0.0 + 9.81) # m*(g + acc)
        pub.publish(msg)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        drone_control()
    except rospy.ROSInterruptException:
        pass
