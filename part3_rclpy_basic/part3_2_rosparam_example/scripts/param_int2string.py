#!/bin/python3
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import QoSHistoryPolicy, QoSProfile
from example_interfaces.msg import Int32
from example_interfaces.msg import String

class param_int2string(Node):

    def __init__(self):
        
        super().__init__('pub_int2string')
        self.declare_parameter('get_number',-1)
        self.declare_parameter('set_number2str',None)

        self.number = self.get_parameter('get_number').value
        
        self.set_parameters([
            Parameter('set_number2str',Parameter.Type.STRING,str(self.number)),
        ])
        self.use_number()

    def use_number(self):
        self.get_logger().info("Usage : '$ rosrun rosparam_example param_int2string.py _get_number:=300'")
        self.get_logger().info("get:"+str(self.number))
        self.get_logger().info("set:"+self.get_parameter('set_number2str').value)
        self.get_logger().info('exit')

def ros_main(args = None):
    rclpy.init(args=args)
    ros_class = param_int2string()
    rclpy.spin(ros_class)

    ros_class.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    ros_main()