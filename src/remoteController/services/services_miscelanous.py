import random

import rospy
from robot_toolkit_msgs.msg import misc_tools_msg, leds_parameters_msg
from robot_toolkit_msgs.srv import misc_tools_srv, tablet_service_srv, battery_service_srv
from django.conf import settings

def startMiscMessage():
    #Service misc call
    miscMessage = misc_tools_msg()
    miscMessage.command = "enable_all"
    miscToolsService(miscMessage)

def miscToolsService(msg):
    """
    Enables the misc Tools service from the toolkit of the robot.
    """
    print("Waiting for misc tools service")
    rospy.wait_for_service('/robot_toolkit/misc_tools_srv')
    try:
        misc = rospy.ServiceProxy('/robot_toolkit/misc_tools_srv', misc_tools_srv)
        miscService = misc(msg)
        print("Misc tools service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def genMsg(red, green, blue):
    leds_msg = leds_parameters_msg()
    leds_msg.name="FaceLeds".encode('ascii')
    leds_msg.red = int(red)
    leds_msg.green = int(green)
    leds_msg.blue = int(blue)
    leds_msg.time = 0
    return leds_msg

def tabletService(url):
    """
    Changes what's being displayed in the robots tablet
    """
    print("Waiting for tablet tools service")
    rospy.wait_for_service('/pytoolkit/ALTabletService/show_image_srv')
    try:
        tablet = rospy.ServiceProxy('/pytoolkit/ALTabletService/show_image_srv', tablet_service_srv)
        tabletService = tablet(url)
        print("Tablet service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def tabletServiceWeb(url):
    """
    Changes what's being displayed in the robots tablet
    """
    print("Waiting for tablet tools service")
    rospy.wait_for_service('/pytoolkit/ALTabletService/show_web_view_srv')
    try:
        tablet = rospy.ServiceProxy('/pytoolkit/ALTabletService/show_web_view_srv', tablet_service_srv)
        tabletService = tablet(url)
        print("Tablet service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")


def mockBatteryService():
    """
    MockBatteryService

    Returns a random integer between 0 and 100, representing the battery level.

    :return: A random integer between 0 and 100.
    """
    return random.randint(0, 100)


def rosBatteryService():
    """
    Function: rosBatteryService

    Description:
    This function waits for the battery tools service and retrieves the battery percentage using the ROS ServiceProxy.

    Parameters:
    None

    :return:
    The battery percentage as an integer value.
    """
    print("Waiting for battery tools service")
    rospy.wait_for_service('/pytoolkit/ALBatteryService/get_porcentage')
    try:
        batteryS = rospy.ServiceProxy('/pytoolkit/ALBatteryService/get_porcentage', battery_service_srv)
        batteryService = batteryS()
        print("Battery service connected!")
        return batteryService.porcentage
    except rospy.ServiceException as e:
        print("Service call failed")


def batteryService():
    """
    Returns the battery service based on the settings.

    :return: The battery service to be used.
    """
    if settings.USE_PEPPER_ROBOT:
        return rosBatteryService()
    return mockBatteryService()

