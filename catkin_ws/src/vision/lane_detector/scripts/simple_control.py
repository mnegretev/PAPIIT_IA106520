#!/usr/bin/env python
import rospy
import cv2
import cv_bridge
import numpy
import math
from std_msgs.msg import Int16
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan

def callback_rgb_raw(msg):
    global best_line
    last_rho   = best_line[0]
    last_theta = best_line[1]
    bridge = cv_bridge.CvBridge()
    img_bgr = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    edges = cv2.Canny(img_bgr,100,200)
    lines = cv2.HoughLines(edges, 1, numpy.pi / 180, 90, None, 0, 0)
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
    if min_dist > 0.2:
        return
    pt1 = (int(best_rho*math.cos(best_theta) + 1000*(-math.sin(best_theta))), int(best_rho*math.sin(best_theta) + 1000*(math.cos(best_theta))))
    pt2 = (int(best_rho*math.cos(best_theta) - 1000*(-math.sin(best_theta))), int(best_rho*math.sin(best_theta) - 1000*(math.cos(best_theta))))
    A = pt1[1] - pt2[1]
    B = pt2[0] - pt1[0]
    C = -A*pt1[0] - B*pt1[1]
    best_line = [best_rho, best_theta, A, B, C]
    cv2.line(img_bgr, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    cv2.imshow("Image BGR", img_bgr)
    cv2.waitKey(1)

def callback_laser_scan(msg):
    print("Laser scan received with " + str(len(msg.ranges)) + " received")

def main():
    print("INITIALIZING SIMPLE CONTROL BY MARCOSOFT...")
    rospy.init_node("lane_finder")
    rospy.Subscriber("/app/camera/rgb/image_raw", Image, callback_rgb_raw)
    pub_steering = rospy.Publisher("/AutoNOMOS_mini/manual_control/steering", Int16, queue_size=1)
    pub_speed    = rospy.Publisher("/AutoNOMOS_mini/manual_control/speed"   , Int16, queue_size=1)
    msg_steering = Int16()
    msg_speed    = Int16()
    loop = rospy.Rate(30)
    
    global best_line
    best_line  = [0, 2.2863812,1,0,0]
    goal_angle = 2.2863812
    goal_dist  = 300.0
    while not rospy.is_shutdown():
        A = best_line[2]
        B = best_line[3]
        C = best_line[4]
        error_theta = goal_angle - best_line[1]
        dist = abs(A*320 + B*480 + C)/math.sqrt(A**2 + B**2)
        error_dist = goal_dist - dist 
        msg_steering.data = int(90 + error_dist/1.5 - 1.5*error_theta*180/math.pi)
        if error_dist > 50:
            msg_speed.data = -100
        else:
            msg_speed.data = -400
        print error_dist
        #print msg_steering.data
        pub_steering.publish(msg_steering)
        pub_speed   .publish(msg_speed)
        loop.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.exceptions.ROSInterruptException:
        pass
