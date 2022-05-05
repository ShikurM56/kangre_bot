#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def cmd_vel_modifier():
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rate = rospy.Rate(10) # 10hz
    rospy.spin()

   

def callback(msg):
    pub = rospy.Publisher('cmd_vel_2', Twist, queue_size=10)

    newTwist = Twist()
    newTwist.linear.x = 3*msg.linear.x
    newTwist.angular.z = msg.angular.z/2
    pub.publish(newTwist)

if __name__ == '__main__':
    try:
        cmd_vel_modifier()
    except rospy.ROSInterruptException:
        pass
