#!/bin/python3
import rospy
from std_msgs.msg import Int32

class hello_world:

    def __init__(self):
        self.number = 0

        self.pub = rospy.Publisher('pub_int', Int32, queue_size=1)
        rospy.init_node('pub_node')
        self.rate = rospy.Rate(2)
        self.pub_number()
    
    def pub_number(self):
        while not rospy.is_shutdown():
            rospy.loginfo(str(self.number))
            self.pub.publish(self.number)
            self.rate.sleep()
            self.number = self.number + 1

if __name__=="__main__":
    try:
        hello_world()
    except rospy.ROSInitException:
        pass