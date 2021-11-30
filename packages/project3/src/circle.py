#!/usr/bin/env python3
#
import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def projectcircle():
    pub = rospy.Publisher('car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
    rospy.init_node('project3')
    msg = Twist2DStamped(header=None, v=0.5, omega=-4.0)
    pub.publish(msg)
    sleep(10)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)

if __name__ == '__main__':
    try:
     projectcircle()
    except rospy.ROSInterruptException:
       pass



