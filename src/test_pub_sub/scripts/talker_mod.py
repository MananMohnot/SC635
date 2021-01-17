#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String

def talker(greeting):
    pub = rospy.Publisher('chatter'.format(greeting), String, queue_size=10)
    rospy.init_node('talker_{}'.format(greeting), anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = ": {} {}".format(greeting, rospy.get_time()) 
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker(sys.argv[1])
    except rospy.ROSInterruptException:
        pass

