#!/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class sub_int(Node):

    def __init__(self):
        super().__init__('sub_int')
        self.create_subscription(Int32,'pub_int',self.sub_number,10)

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