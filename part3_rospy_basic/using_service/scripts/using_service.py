#!/bin/python3
import rospy
from std_msgs.msg import Int32
from original_msg_example.msg import example_msg
from original_msg_example.srv import calc_msg_srv

class msg_output:

    def __init__(self):
        self.a = 0
        self.b = 0

        self.msg_data = example_msg()
        self.pub = rospy.Publisher('pub_example_msg', example_msg, queue_size=1)

        rospy.Subscriber('a',Int32,self.sub_a)
        rospy.Subscriber('b',Int32,self.sub_b)

        rospy.spin()
    
    def calc_by_service(self):
        calc_module = rospy.ServiceProxy('calc_ab', calc_msg_srv)
        sub_data = calc_module(self.a,self.b)
        rospy.loginfo(sub_data)
    
    def sub_a(self,data):
        self.a = data.data
        self.calc_by_service()

    def sub_b(self,data):
        self.b = data.data
        self.calc_by_service()

def rospy_init(args = None):
    try:
        rospy.init_node('msg_output',argv=args)
        msg_output()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()
