#!/usr/bin/env python
import rospy, math
from geometry_msgs.msg import Twist, Point

def talker():
    vel = 2
    omega = 2
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	speed = Twist()
	speed.linear.x = vel
	speed.angular.z = omega
	#print(speed)
	pub.publish(speed)
	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
