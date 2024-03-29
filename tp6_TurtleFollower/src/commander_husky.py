#!/usr/bin/env python
import rospy, random
import time
import numpy as np
from geometry_msgs.msg import Point

def commander():
    rospy.init_node('commander', anonymous=True)
    pub = rospy.Publisher('/destination', Point, queue_size=10)
    
    #rate = rospy.Rate(10) # 1hz
    
    while not rospy.is_shutdown():
        pt = Point()
        pt.x=np.random.randint(-5,5)
        pt.y=np.random.randint(-5,5)
        print("New x:{},\tNew y:{}".format(pt.x,pt.y))
        
        pub.publish(pt)
        time.sleep(20)
        #rate.sleep()

if __name__ == '__main__':
    try:
        time.sleep(5)
        commander()
    except rospy.ROSInterruptException:
        pass
