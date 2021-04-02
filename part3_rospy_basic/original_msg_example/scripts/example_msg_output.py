#!/bin/python3
import rospy
from std_msgs.msg import Int32
from original_msg_example.msg import example_msg

class msg_output:

    def __init__(self):
        self.a = 0
        self.b = 0

        self.msg_data = example_msg()
        self.pub = rospy.Publisher('pub_example_msg', example_msg, queue_size=1)

        rospy.Subscriber('a',Int32,self.sub_a)
        rospy.Subscriber('b',Int32,self.sub_b)

        rospy.spin()
    
    def calc_four_arithmetic_operations(self):
        self.msg_data.a              = self.a
        self.msg_data.b              = self.b
        self.msg_data.sum_ab         = self.a + self.b
        self.msg_data.diff_ab        = self.a - self.b
        self.msg_data.product_ab     = self.a * self.b
        if(self.b == 0):
            self.msg_data.quotient_ab   = -0
            self.msg_data.remainder_ab  = -0
        else:
            self.msg_data.quotient_ab    = self.a // self.b
            self.msg_data.remainder_ab   = self.a % self.b
        self.pub.publish(self.msg_data)
        rospy.loginfo(self.msg_data)
    
    def sub_a(self,data):
        self.a = data.data
        self.calc_four_arithmetic_operations()

    def sub_b(self,data):
        self.b = data.data
        self.calc_four_arithmetic_operations()

def rospy_init(args = None):
    try:
        rospy.init_node('msg_output',argv=args)
        msg_output()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()
