#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():

    pub = rospy.Publisher('name_publish',String , queue_size=50)
    rate =rospy.Rate(1)

    msg_to_publish = String()

    counter =0

    while not rospy.is_shutdown():
        string_to_publish = "Manan_Gyandev"     
        msg_to_publish.data = string_to_publish
        pub.publish(msg_to_publish)
        rate.sleep()

if __name__== "__main__":
    rospy.init_node("simple_name")
    publisher()
