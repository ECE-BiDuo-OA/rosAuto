#!/usr/bin/env python
import rospy, random
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose

def callback(data):
    Tx = data.x
    Ty = data.y
    
    print("x: {}\ty: {}".format(Tx,Ty))

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    
    rate = rospy.Rate(1) # 1hz
    
    try:
        minSpeed = rospy.get_param(rospy.search_param("minSpeed"))
        maxSpeed = rospy.get_param(rospy.search_param("maxSpeed"))
        assert minSpeed + maxSpeed +1
    except:
        minSpeed = -2
        maxSpeed = 2
        print("No param, min will be set to {} and max to {}".format(minSpeed,maxSpeed))
        

    while not rospy.is_shutdown():
        speed = Twist()
        speed.linear.x = random.randint(minSpeed, maxSpeed)
        speed.angular.z = random.randint(minSpeed, maxSpeed)
        #print(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
