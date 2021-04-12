#!/bin/python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSHistoryPolicy, QoSProfile
from example_interfaces.msg import Int32

from original_msg_example.msg import ExampleMsg

class msg_output(Node):

    def __init__(self):
        super().__init__('msg_output')
        pub_qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)
        sub_qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)

        self.pub = self.create_publisher(ExampleMsg, 'pub_ExampleMsg',pub_qos)

        self.a = 0
        self.b = 0

        self.msg_data = ExampleMsg()

        self.create_subscription(Int32,'a',self.sub_a,sub_qos)
        self.create_subscription(Int32,'b',self.sub_b,sub_qos)

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
        self.get_logger().info(str(self.msg_data))
    
    def sub_a(self,data):
        self.a = data.data
        self.calc_four_arithmetic_operations()

    def sub_b(self,data):
        self.b = data.data
        self.calc_four_arithmetic_operations()

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = msg_output()
    rclpy.spin(ros_class)

    ros_class.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()