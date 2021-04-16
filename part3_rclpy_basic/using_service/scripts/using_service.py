#!/bin/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
from rclpy.qos import QoSHistoryPolicy, QoSProfile

from original_msg_srv.msg import ExampleMsg
from original_msg_srv.srv import CalcMsgSrv

class using_srv(Node):

    def __init__(self):

        super().__init__('pub_int')
        pub_qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)
        sub_qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)

        self.a = 0
        self.b = 0

        self.msg_data = ExampleMsg()
        self.pub = self.create_publisher(ExampleMsg, 'pub_ExampleMsg', pub_qos)

        self.calc_module = self.create_client(CalcMsgSrv, 'calc_ab')

        self.create_subscription(Int32, 'a', self.sub_a, sub_qos)
        self.create_subscription(Int32, 'b', self.sub_b, sub_qos)
    
    def calc_by_service(self):

        while not self.calc_module.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        send_data = CalcMsgSrv()
        send_data.a = self.a
        send_data.b = self.b
        sub_data = self.calc_module.call_async(send_data)

        self.get_logger().info(str(sub_data))
    
    def sub_a(self,data):
        self.a = data.data
        self.calc_by_service()

    def sub_b(self,data):
        self.b = data.data
        self.calc_by_service()

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = using_srv()
    rclpy.spin(ros_class)

    ros_class.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()