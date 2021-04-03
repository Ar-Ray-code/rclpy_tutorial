#!/bin/python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSHistoryPolicy, QoSProfile
from example_interfaces.msg import Int32

class pub_int(Node):

    def __init__(self):
        self.number = 0

        super().__init__('pub_int')
        pub_qos = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, depth=1)

        self.pub = self.create_publisher(Int32, 'pub_int',pub_qos)
        self.declare_parameter('~pub_rate',2)
        param = self.get_parameter('~pub_rate')
        
        period = 1/param.get_parameter_value().type
        self.get_logger().info('period: '+str(period))
        
        self.create_timer(period,self.pub_number)
    
    def pub_number(self):
        msg = Int32()
        msg.data = self.number
        self.get_logger().info(str(msg.data))
        self.pub.publish(msg)
        self.number = self.number + 1

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = pub_int()
    rclpy.spin(ros_class)

    ros_class.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()