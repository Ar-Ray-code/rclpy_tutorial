#!/bin/python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class hello_world:
    def __init__(self):
        self.pub = rospy.Publisher("output_image",Image,queue_size=1)
        self.bridge = CvBridge()

        rospy.init_node('put_text_pubsub')
        rospy.Subscriber("camera/color/image_raw",Image,self.process_image)
        rospy.spin()

    def process_image(self,msg):
        try:
            img_rgb = self.bridge.imgmsg_to_cv2(msg,"rgb8")
            cv2.putText(img_rgb, 'Test', (150, 150), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 255), 5, cv2.LINE_AA)
            
            output_img = self.bridge.cv2_to_imgmsg(img_rgb,"rgb8")
            self.pub.publish(output_img)
        except Exception as err:
            print(err)

if __name__=="__main__":
    try:
        hello_world()
    except rospy.ROSInterruptException as err:
        print(err)

