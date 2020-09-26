#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
import numpy
import math
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan

def callback_rgb_raw(msg):
    global best_line
    last_rho, last_theta = best_line
    bridge = cv_bridge.CvBridge()
    img_bgr = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    edges = cv2.Canny(img_bgr,100,200)
    lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 100, None, 0, 0)
    if lines is None:
        return
    min_dist = 999999
    best_rho   = 0
    best_theta = 0
    for l in lines:
        rho, theta = l[0][0], l[0][1]
        if theta < 0:
            theta+=math.pi
        if abs(theta - last_theta) < min_dist:
            min_dist   = abs(theta - last_theta)
            best_rho   = rho
            best_theta = theta
    if min_dist > 0.1:
        return
    best_line = [best_rho, best_theta]
    pt1 = (int(best_rho*math.cos(best_theta) + 1000*(-math.sin(best_theta))), int(best_rho*math.sin(best_theta) + 1000*(math.cos(best_theta))))
    pt2 = (int(best_rho*math.cos(best_theta) - 1000*(-math.sin(best_theta))), int(best_rho*math.sin(best_theta) - 1000*(math.cos(best_theta))))
    cv2.line(img_bgr, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    print(best_line)
    print min_dist
    cv2.imshow("Image BGR", img_bgr)
    cv2.waitKey(1)

def callback_laser_scan(msg):
    print("Laser scan received with " + str(len(msg.ranges)) + " received")

def main():
    print("INITIALIZING SIMPLE CONTROL BY MARCOSOFT...")
    rospy.init_node("lane_finder")
    rospy.Subscriber("/app/camera/rgb/image_raw", Image, callback_rgb_raw)
    loop = rospy.Rate(30)
    
    global best_line
    best_line = [0, 2.2]
    while not rospy.is_shutdown():
        loop.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.exceptions.ROSInterruptException:
        pass
