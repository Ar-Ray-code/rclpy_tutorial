#!/bin/python3
import rospy
from std_msgs.msg import Int32
from original_msg_example.msg import example_msg

from original_msg_example.srv import calc_msg_srv, calc_msg_srvResponse

class msg_output:
    def __init__(self):
        service = rospy.Service('calc_ab',calc_msg_srv,self.srv_ab)
        rospy.spin()
    
    def calc_four_arithmetic_operations(self, input_a, input_b):
        msg_data = example_msg()
        msg_data.a              = input_a
        msg_data.b              = input_b
        msg_data.sum_ab         = input_a + input_b
        msg_data.diff_ab        = input_a - input_b
        msg_data.product_ab     = input_a * input_b

        if(input_b == 0):
            msg_data.quotient_ab   = 0
            msg_data.remainder_ab  = 0
        else:
            msg_data.quotient_ab    = input_a // input_b
            msg_data.remainder_ab   = input_a % input_b
        return msg_data

    def srv_ab(self,request):
        result = self.calc_four_arithmetic_operations(request.a,request.b)
        return calc_msg_srvResponse(result)

def rospy_init(args = None):
    try:
        rospy.init_node('msg_output',argv=args)
        msg_output()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()
