#!/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

from original_msg_srv.msg import ExampleMsg
from original_msg_srv.srv import CalcMsgSrv

class msg_output(Node):
    def __init__(self):
        super().__init__('msg_srv')

        service = self.create_service(CalcMsgSrv,'calc_ab',self.srv_ab)
    
    def calc_four_arithmetic_operations(self, input_a, input_b):
        msg_data = ExampleMsg()
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

    def srv_ab(self, request, response:CalcMsgSrv):
        response.result = self.calc_four_arithmetic_operations(request.a,request.b)
        return response

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = msg_output()
    rclpy.spin(ros_class)

    ros_class.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()