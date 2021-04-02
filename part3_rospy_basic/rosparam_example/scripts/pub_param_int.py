#!/bin/python3
import rospy
from std_msgs.msg import Int32

class hello_world:

    def __init__(self):

        self.pub = rospy.Publisher('pub_int', Int32, queue_size=1)
        self.number = rospy.get_param("~number", -1)
        self.rate = rospy.Rate(2)
        self.pub_number()
    
    def pub_number(self):
        while not rospy.is_shutdown():
            rospy.loginfo(str(self.number))
            self.pub.publish(self.number)
            self.rate.sleep()

def rospy_init(args = None):
    try:
        rospy.init_node('pub_node',argv=args)
        hello_world()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()