#!/bin/python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class hello_world:
    def __init__(self):
        self.bridge = CvBridge()
        cv2.namedWindow("window",cv2.WINDOW_AUTOSIZE)
        rospy.init_node('put_text_sub')
        rospy.Subscriber("camera/color/image_raw",Image,self.process_image)
        rospy.spin()
    
    def __del__(self):
        cv2.destroyAllWindows()

    def process_image(self,msg):
        try:
            img_rgb = self.bridge.imgmsg_to_cv2(msg,"bgr8")
            cv2.putText(img_rgb, 'Test', (150, 150), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 255), 5, cv2.LINE_AA)
            cv2.imshow("window", img_rgb)
            cv2.waitKey(1)
        except Exception as err:
            print(err)

if __name__=="__main__":
    try:
        hello_world()
    except rospy.ROSInterruptException as err:
        print(err)

