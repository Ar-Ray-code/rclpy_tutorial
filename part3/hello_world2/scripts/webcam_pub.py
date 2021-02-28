#!/bin/python3
import rospy

import sensor_msgs
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

class hello_world:

    def __init__(self):
        self.bridge = CvBridge
        self.number = 0
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            rospy.loginfo("Cannot Open WebCamera!")
            exit(1)

        self.pub = rospy.Publisher('pub_image', Image, queue_size=1)
        rospy.init_node('pub_node')
        self.rate = rospy.Rate(10)
        self.pub_image()
    
    
    def pub_image(self):
        while not rospy.is_shutdown():
            try:
                _, image = self.cap.read()
                print(type(image))
                self.imgmsg = self.bridge.cv2_to_imgmsg(image,'bgr8')
            except CvBridgeError:
                print(CvBridgeError)

            self.pub.publish(self.imgmsg)
            self.rate.sleep()

if __name__=="__main__":
    try:
        hello_world()
    except rospy.ROSInitException:
        pass