#!/usr/bin/env python
import rospy
from roboclaw import Roboclaw
from geometry_msgs.msg import Twist


def callback(data):
    right = data.linear.x + data.angular.z
    left = data.linear.x - data.angular.z
    map_right = (right - -1) * (121 - -121) / (1 - -1) - 121
    map_left = (left - -1) * (127 - -127) / (1 - -1) - 127
    print (map_right)
    print (map_left)
    if (map_right >= 0):
        roboclaw.ForwardM2(0x81, int(map_right))
    else:
        roboclaw.BackwardM2(0x81, int(abs(map_right)))
    if (map_left >=0):
        roboclaw.ForwardM1(0x81, int(map_left))
    else:
        roboclaw.BackwardM1(0x81, int(abs(map_left)))


def drive_firmware():
    rospy.init_node('drive_firmware', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    print("Entre al spin")
    rospy.spin()

if __name__ == '__main__':
# address of the RoboClaw as set in Motion Studio
    address = 0x81
# Creating the RoboClaw object, serial port and baudrate passed
    roboclaw = Roboclaw("/dev/ttyACM0", 38400)
# Starting communication with the RoboClaw hardware
    roboclaw.Open()
# Start motor 1 in the forward direction at half speed
    roboclaw.ForwardM1(address, 0) #Izquierda
    roboclaw.ForwardM2(address, 0) #Derecha
    print("Entre al firmware")
    drive_firmware()

