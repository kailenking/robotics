#!/usr/bin/env python3
#
import rospy
from duckietown_msgs.msg import Twist2DStamped
from time import sleep

def projectsquare():
    pub = rospy.Publisher('car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)
    rospy.init_node('project3')
    msg = Twist2DStamped(header=None, v=1, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=6)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=1, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=6)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=1, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=6)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=1, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=6)
    pub.publish(msg)
    sleep(1)
    msg = Twist2DStamped(header=None, v=0, omega=0)
    pub.publish(msg)
    sleep(1)


if __name__ == '__main__':
    try:
     projectsquare()
    except rospy.ROSInterruptException:
       pass
