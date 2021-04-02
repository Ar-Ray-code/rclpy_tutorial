#!/bin/python3
import rospy
from std_msgs.msg import Int32

class param_int2string:

    def __init__(self):

        self.number = rospy.get_param("~get_number", -1)
        rospy.set_param("~set_number2str",str(self.number))
        rospy.set_param("set_number2str",str(self.number))
        self.pub_number()
    
    def pub_number(self):
        while not rospy.is_shutdown():
            rospy.loginfo(str(self.number))
            rospy.loginfo("exit")
            exit(0)

def rospy_init(args = None):
    print("Usage : '$ rosrun rosparam_example param_int2string.py _get_number:=300'")
    try:
        rospy.init_node('pub_node',argv=args)
        param_int2string()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()