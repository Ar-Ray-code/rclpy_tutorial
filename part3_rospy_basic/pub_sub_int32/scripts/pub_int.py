#!/bin/python3
import rospy
from std_msgs.msg import Int32

class hello_world:

    def __init__(self):
        self.number = 0

        self.pub = rospy.Publisher('pub_int', Int32, queue_size=1)
        hz = rospy.get_param("~pub_rate", 2)
        self.rate = rospy.Rate(hz)
        self.pub_number()
    
    def pub_number(self):
        while not rospy.is_shutdown():
            rospy.loginfo(str(self.number))
            self.pub.publish(self.number)
            self.rate.sleep()
            self.number = self.number + 1

def rospy_init(args = None):
    try:
        rospy.init_node('pub_node',argv=args)
        hello_world()
    except rospy.ROSInitException as e:
        print(e)

if __name__=="__main__":
    rospy_init()