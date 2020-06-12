#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
import numpy
from sensor_msgs.msg import Image

def callback_rgb_raw(msg):
    bridge = cv_bridge.CvBridge()
    img_bgr = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    cv2.imshow("Image BGR", img_bgr)
    cv2.waitKey(1)

def main():
    print("INITIALIZING SIMPLE CONTROL BY MARCOSOFT...")
    rospy.init_node("lane_finder")
    rospy.Subscriber("/app/camera/rgb/image_raw", Image, callback_rgb_raw)
    loop = rospy.Rate(30)
    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.exceptions.ROSInterruptException:
        pass
