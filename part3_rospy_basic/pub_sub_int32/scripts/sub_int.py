#!/bin/python3
import rospy
from std_msgs.msg import Int32

class hello_world:

    def __init__(self):
        rospy.Subscriber('pub_int',Int32,self.sub_number)
        rospy.spin()
    
    def sub_number(self,data):
        rospy.loginfo(str(data.data))

def rospy_init(args = None):
    try:
        rospy.init_node('sub_node',argv=args)
        hello_world()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()