#!/bin/python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSHistoryPolicy, QoSProfile
from example_interfaces.msg import Int32

class sub_int(Node):

    def __init__(self):
        super().__init__('sub_int')
        sub_qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)

        self.create_subscription(Int32,'pub_int',self.sub_number,sub_qos)

    def sub_number(self,data):
        self.get_logger().info(str(data.data))

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = sub_int()
    rclpy.spin(ros_class)

    ros_class.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()