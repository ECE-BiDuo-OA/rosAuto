#!/usr/bin/env python
import rospy

if __name__ == '__main__':
	try:
		rospy.init_node('hello_ros',anonymous=True)
		rospy.loginfo("Hello, ROS!")
	except rospy.ROSInterruptException:
		pass
