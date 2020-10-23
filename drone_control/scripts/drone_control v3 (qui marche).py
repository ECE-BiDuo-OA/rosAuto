#!/usr/bin/env python

import rospy,time
from mav_msgs.msg import RollPitchYawrateThrust
from nav_msgs.msg import Odometry
 
T=0
theta=0
phi=0

mass = 1.544

def callback_odom(data): 
    global mass, T, theta, phi
    
    poseCovar = data.pose.pose.position
    twistCovar = data.twist.twist
    
    x = poseCovar.x
    y = poseCovar.y
    z = poseCovar.z
    print("x: {}\ty: {}\tz: {}".format(x,y,z))
   
    Vx = twistCovar.linear.x
    Vy = twistCovar.linear.y
    Vz = twistCovar.linear.z
    print("Vx: {}\tVy: {}\tVz: {}".format(Vx,Vy,Vz))

    ax = twistCovar.angular.x
    ay = twistCovar.angular.y
    az = twistCovar.angular.z
    print("ax: {}\tay: {}\taz: {}".format(ax,ay,az))
    
    psi = data.pose.pose.orientation.z
    print("psi: {}".format(psi))

    #simu params
    xRef = 2.0
    yRef = -2.0
    zRef = 3.0
    VxRef = 0
    VyRef = 0
    VzRef = 0
    
    Kp = 2
    Kd = 1

    Ux= - Kp * (x - xRef) - Kd * (Vx - VxRef)
    Uy= - Kp * (y - yRef) - Kd * (Vy - VyRef)
    Uz= - Kp * (z - zRef) - Kd * (Vz - VzRef)
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
        msg.yaw_rate = 0.0      # rad/s
        
        msg.thrust.z = T # m*(acc + g)
        pub.publish(msg)
        rate.sleep()
 
if __name__ == '__main__':
    #try:1
    time.sleep(2)
    drone_control()
    try:1
    except rospy.ROSInterruptException:
        pass
