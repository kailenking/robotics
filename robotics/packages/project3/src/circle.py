#!/usr/bin/env python 3

import rospy
from duckietown_msgs.msg
import Twist2Dstamped

def projectcircle():

pub = rospy.Publisher('/duck19/car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
rospy.init_node('project3')
rate = rospy.Rate(10)
msg = Twist2Dstamped()
msg.v = 1
msg.omega = 0

if __name__ == '__main__':
try:
projectcircle()
except rospy.ROSInterruptException:
pass

