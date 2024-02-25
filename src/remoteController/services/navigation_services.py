import rospy
from robot_toolkit_msgs.msg import depth_to_laser_msg
from robot_toolkit_msgs.srv import navigation_tools_srv
from geometry_msgs.msg import Twist

def startNavigationMessage():
    #Service navigation call
    depthToLaserMessage = depth_to_laser_msg()
    depthToLaserMessage.resolution=0
    depthToLaserMessage.scan_time=0.0
    depthToLaserMessage.range_min=0.0
    depthToLaserMessage.range_max=0.0
    depthToLaserMessage.scan_height=0.0
    navigationMessage = navigation_tools_srv()
    navigationMessage.command = "enable_all"
    navigationMessage.tf_enable= False
    navigationMessage.tf_frequency= 0.0
    navigationMessage.odom_enable= False
    navigationMessage.odom_frequency= 0.0
    navigationMessage.laser_enable= False
    navigationMessage.laser_frequency= 0.0
    navigationMessage.cmd_vel_enable= False
    navigationMessage.security_timer= 0.0
    navigationMessage.move_base_enable=False
    navigationMessage.goal_enable= False
    navigationMessage.robot_pose_suscriber_enable= False
    navigationMessage.path_enable= False
    navigationMessage.path_frequency= 0.0
    navigationMessage.robot_pose_publisher_enable= False
    navigationMessage.robot_pose_publisher_frequency= 0.0
    navigationMessage.result_enable= False
    navigationMessage.depth_to_laser_enable= False
    navigationMessage.depth_to_laser_parameters= depthToLaserMessage
    navigationMessage.free_zone_enable= False
    navigationToolsService(navigationMessage)

def navigationToolsService(msg):
    """
    Enables the navigation Tools service from the toolkit of the robot.
    """
    print("Waiting for navigation tools service")
    rospy.wait_for_service('/robot_toolkit/navigation_tools_srv')
    try:
        navigation = rospy.ServiceProxy('/robot_toolkit/navigation_tools_srv', navigation_tools_srv)
        navigationService = navigation(msg)
        print("Navigation tools service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def aux_mov(direction, speedP):
    speed = float(speedP)/100
    geometry_msg = Twist()
    geometry_msg.linear.x = 0
    geometry_msg.linear.y = 0
    if direction=='up':
        geometry_msg.linear.x = speed
    if direction=='down':
        geometry_msg.linear.x = -speed
    if direction=='left':
        geometry_msg.linear.y = speed
    if direction=='right':
        geometry_msg.linear.y = -speed
    geometry_msg.linear.z = 0
    geometry_msg.angular.x = 0
    geometry_msg.angular.y = 0
    geometry_msg.angular.z = 0
    if direction=='rotateR':
        geometry_msg.angular.z = -speed
    if direction=='rotateL':
        geometry_msg.angular.z = speed
    return geometry_msg

def aux_joy(verticalAxis, horizontalAxis):
    geometry_msg = Twist()
    geometry_msg.linear.x = (-1)*float(verticalAxis)
    geometry_msg.linear.y = (-1)*float(horizontalAxis)
    geometry_msg.linear.z = 0
    geometry_msg.angular.x = 0
    geometry_msg.angular.y = 0
    geometry_msg.angular.z = 0
    return geometry_msg