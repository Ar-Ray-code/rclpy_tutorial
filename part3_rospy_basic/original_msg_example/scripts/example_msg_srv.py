#!/bin/python3
import rospy
from std_msgs.msg import Int32
from original_msg_example.msg import example_msg

from original_msg_example.srv import calc_msg, calc_msgResponse

class msg_output:

    def __init__(self):
        self.a = 0
        self.b = 0

        self.msg_data = example_msg()
        self.pub = rospy.Publisher('pub_example_msg', example_msg, queue_size=1)

        rospy.Subscriber('a',Int32,self.sub_a)
        rospy.Subscriber('b',Int32,self.sub_b)

        ## srv
        service = rospy.Service('calc_ab',calc_msg,self.srv_ab)

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
    
    def sub_a(self,data):
        self.a = data.data
        self.calc_four_arithmetic_operations()
        self.pub.publish(self.msg_data)
        rospy.loginfo(self.msg_data)

    def sub_b(self,data):
        self.b = data.data
        self.calc_four_arithmetic_operations()
        self.pub.publish(self.msg_data)
        rospy.loginfo(self.msg_data)

    def srv_ab(self,request):
        self.a = request.a
        self.b = request.b
        self.calc_four_arithmetic_operations()
        return calc_msgResponse(self.msg_data)

def rospy_init(args = None):
    try:
        rospy.init_node('msg_output',argv=args)
        msg_output()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()
