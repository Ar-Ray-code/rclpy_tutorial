#!/bin/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
from rclpy.qos import QoSHistoryPolicy, QoSProfile

from original_msg_srv.msg import ExampleMsg
from original_msg_srv.srv import CalcMsgSrv
import time

class using_srv(Node):
    def __init__(self):
        super().__init__('pub_int')
        self.a = 0
        self.b = 0

        qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)

        self.pub = self.create_publisher(ExampleMsg, 'pub_ExampleMsg', qos)
        self.sub_a = self.create_subscription(Int32, '/a', self.callback_a, qos)
        self.sub_b = self.create_subscription(Int32, '/b', self.callback_b, qos)

    def reset_client(self):
        self.calc_module = self.create_client(CalcMsgSrv, '/calc_ab')
        while not self.calc_module.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = CalcMsgSrv.Request()

    def callback_a(self, msg:Int32):
        self.a = msg.data

    def callback_b(self, msg:Int32):
        self.b = msg.data
    
    def calc_by_service(self):
        self.req.a = self.a
        self.req.b = self.b
        self.future = self.calc_module.call_async(self.req)

# def using_srv_fnc(a:int, b:int, ros_class:using_srv):
#     ros_class.calc_by_service()
#     while rclpy.ok():
#         rclpy.spin_once(ros_class)
#         if ros_class.future.done():
#             try:
#                 response = ros_class.future.result().result
#                 ros_class.pub.publish(response)
#                 print(response)
#                 rclpy.spin_once(ros_class)
#             except Exception as e:
#                 print(e)
#         break

class srv_main:
    def __init__(self):
        self.ros_class = using_srv()

    # def loop(self):
    #     self.using_srv_fnc()
    
    def using_srv_fnc(self):
        self.ros_class.reset_client()
        self.ros_class.calc_by_service()
        while rclpy.ok():
            rclpy.spin_once(self.ros_class)
            if self.ros_class.future.done():
                try:
                    response = self.ros_class.future.result().result
                    self.ros_class.pub.publish(response)
                    self.ros_class.get_logger().info(str(response))
                    rclpy.spin_once(self.ros_class)
                except Exception as e:
                    print(e)
            break

def ros_main(args = None):
    rclpy.init(args=args)
    # input_a = 0
    # input_b = 0
    main = srv_main()

    # ros_class = using_srv()
    while rclpy.ok():
        main.using_srv_fnc()
        # input_a = input_a + 2
        # input_b = input_b + 1
        # using_srv_fnc(input_a, input_b, ros_class)
        time.sleep(0.1)
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()