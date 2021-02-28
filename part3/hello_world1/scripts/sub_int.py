#!/bin/python3
import rospy
from std_msgs.msg import Int32

class hello_world:

    def __init__(self):
        rospy.Subscriber('pub_int',Int32,self.sub_number)

        rospy.init_node('sub_node')
        rospy.spin()
    
    def sub_number(self,data):
        rospy.loginfo(str(data.data))

if __name__=="__main__":
    try:
        hello_world()
    except rospy.ROSInitException:
        pass