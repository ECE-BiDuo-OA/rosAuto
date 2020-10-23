#!/usr/bin/env python
## 2020 J. Marzat, ONERA & ECE Paris

import rospy, math
from std_msgs.msg import Float32

def speed():
    rospy.init_node('speed',anonymous=True,disable_signals=False)
    pubtheta = rospy.Publisher('/theta', Float32, queue_size=10)
    pubrotvel = rospy.Publisher('/dtheta',Float32, queue_size=10)
    pubref = rospy.Publisher('/ref', Float32, queue_size=10)
    Te = 0.005 	#pas de temps 'continu'
    rate = rospy.Rate(1/Te)
    #init
    theta = 1.0;	
    dtheta = 0.0;
    count = 0.0;
    
    #simu params
    time_limit = 5.0
    g = 9.81
    l = 1.0
    ref_theta = 0.0
    ref_dtheta = 0.0
    kp = -4.0
    kd = -1.0

    rospy.sleep(1)
    pubtheta.publish(0.0)
    pubref.publish(0.0)
    pubrotvel.publish(0.0) 

    while not rospy.is_shutdown():
	u = kp*(ref_theta-theta) + kd*(ref_dtheta - dtheta)	#controller
	theta = theta + Te*dtheta		#First-order system integration
	dtheta = dtheta + Te*(g/l)*(math.sin(theta)-u)

	pubtheta.publish(theta)
	pubref.publish(ref_theta)
	pubrotvel.publish(dtheta) 
	
	count += Te
	if count > time_limit:	#stop simu on Timeout
		pubtheta.publish(0.0)
		pubrotvel.publish(0.0)
		pubref.publish(0.0)
		rospy.signal_shutdown("Timeout")

	rate.sleep()

if __name__ == '__main__':
    try:
        speed()
    except rospy.ROSInterruptException:
        pass
