#!/usr/bin/env python
## 2020 J. Marzat, ONERA & ECE Paris

import rospy, random
from std_msgs.msg import Float32

def speed_observer():
    rospy.init_node('speed_observer',anonymous=True,disable_signals=False)
    pubvel = rospy.Publisher('/vel', Float32, queue_size=10)
    pubvel_noisy = rospy.Publisher('/vel_noisy', Float32, queue_size=10)
    pubvel_obs = rospy.Publisher('/vel_obs', Float32, queue_size=10)
    Te = 0.005 	#pas de temps 'continu'
    rate = rospy.Rate(1/Te)
    #init
    vel = 0.0 	
    count = 0.0;
    
    #Noise params
    input_noise = 0.1
    output_noise = 0.2

    #observer
    L = 0.1	#gain
    v_obs = 2.0	#init

    #simu params
    time_limit = 5
    ref = 2.0
    kp = 1.0

    rospy.sleep(1)
    pubvel.publish(0.0)	
    pubvel_noisy.publish(0.0)
    pubvel_obs.publish(0.0)

    while not rospy.is_shutdown():
	u = random.uniform(-5.0,5.0)	#random input
	vel = vel + Te*u		#system integration

	#add noise on input and output
	u_noisy = u + random.gauss(0,input_noise)	
	v_noisy = vel + random.gauss(0,output_noise) 

	#observer
	v_obs = (1-L)*(v_obs + Te*u_noisy) + L*v_noisy

	pubvel.publish(vel)
	pubvel_noisy.publish(v_noisy)
	pubvel_obs.publish(v_obs)
	count += Te
	if count > time_limit:	#stop simu on Timeout
		pubvel.publish(0.0)
		pubvel_noisy.publish(0.0)
		pubvel_obs.publish(0.0)		
		rospy.signal_shutdown("Timeout")
	rate.sleep()

if __name__ == '__main__':
    try:
        speed_observer()
    except rospy.ROSInterruptException:
        pass
