#!/usr/bin/env python
## 2020 J. Marzat, ONERA & ECE Paris

import rospy
from std_msgs.msg import Float32

def speed():
    rospy.init_node('speed',anonymous=True,disable_signals=False)
    pubvel = rospy.Publisher('/vel', Float32, queue_size=10)
    pubveld = rospy.Publisher('/veld', Float32, queue_size=10)
    pubref = rospy.Publisher('/ref', Float32, queue_size=10)
    Te = 0.005 	#pas de temps 'continu'
    rate = rospy.Rate(1/Te)
    #init
    vel = 0.0
    veld = 0.0 	
    count = 0.0;
    
    #simu params
    time_limit = 5
    ref = 2.0
    kp = 1.0
    dt = 0.1

    step = 0
    rospy.sleep(1)
    pubvel.publish(vel)
    pubveld.publish(veld)
    pubref.publish(0.0)


    while not rospy.is_shutdown():
	u = kp*(ref-vel)		#controller
	vel = vel + Te*u		#system integration

	pubvel.publish(vel)
	pubref.publish(ref)
	count += Te

	if int(count/dt) > step:	#zero-order hold
                ud = kp*(ref - veld)
		veld = veld + dt*ud
		step = int(count/dt)
		pubveld.publish(veld)		

	if count > time_limit:		#stop simu on Timeout
		pubvel.publish(0.0)
		pubref.publish(0.0)
		pubveld.publish(veld)
		pubveld.publish(0.0)
		rospy.signal_shutdown("Timeout")

	rate.sleep()

if __name__ == '__main__':
    try:
        speed()
    except rospy.ROSInterruptException:
        pass
