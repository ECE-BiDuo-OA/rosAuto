#!/usr/bin/env python

import rospy,time
from mav_msgs.msg import RollPitchYawrateThrust
from nav_msgs.msg import Odometry
 
T=0
theta=0
phi=0

mass = 1.544

#simu params
xRef = -2
yRef = -2
zRef = 3
VxRef = 0
VyRef = 0
VzRef = 0
psiRef = 0

Kp = 1
Kd = 1

def callback_odom(data): 
    global mass, T, theta, phi, xRef, yRef, zRef, VxRef, VyRef, VzRef, psiRef, Kp, Kd
    
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
    print("x: {}\ty: {}\tz: {}".format(x,y,z))
   
    Vx = data.twist.twist.linear.x
    Vy = data.twist.twist.linear.y
    Vz = data.twist.twist.linear.z
    print("Vx: {}\tVy: {}\tVz: {}".format(Vx,Vy,Vz))

    ax = data.twist.twist.angular.x
    ay = data.twist.twist.angular.y
    az = data.twist.twist.angular.z
    print("ax: {}\tay: {}\taz: {}".format(ax,ay,az))
    
    psiVal = data.pose.pose.orientation.z
    print("psi: {}".format(psi))


    Ux = - Kp * (x - xRef) - Kd * (Vx - VxRef)
    Uy = - Kp * (y - yRef) - Kd * (Vy - VyRef)
    Uz = - Kp * (z - zRef) - Kd * (Vz - VzRef)
    print("Ux: {}\tUy: {}\tUz: {}".format(Ux,Uy,Uz))
    
    T=mass*(Uz+9.81)
    theta = mass*Ux/T
    phi=-mass*Uy/T
    print("T: {}\tTheta: {}\tPhi: {}".format(T, theta, phi))    
    print("")

def drone_control():
    global mass, T, theta, phi
    
    rospy.init_node('drone_control', anonymous=True)
    pub = rospy.Publisher('/firefly/command/roll_pitch_yawrate_thrust', RollPitchYawrateThrust, queue_size=10)
    sub = rospy.Subscriber('/firefly/odometry_sensor1/odometry',Odometry,callback_odom)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        msg = RollPitchYawrateThrust()
        msg.roll = phi	   		# rad	
        msg.pitch = theta  		# rad	
        msg.yaw_rate = 0        # rad/s
        
        msg.thrust.z = T
        pub.publish(msg)
        rate.sleep()
 
if __name__ == '__main__':
    #try:1
    time.sleep(2)
    drone_control()
    try:1
    except rospy.ROSInterruptException:
        pass
