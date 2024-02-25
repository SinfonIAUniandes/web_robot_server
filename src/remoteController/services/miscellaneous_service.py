import os
import shutil

import rospy
from django.core.files.base import ContentFile
from robot_toolkit_msgs.msg import misc_tools_msg, leds_parameters_msg
from robot_toolkit_msgs.srv import misc_tools_srv, tablet_service_srv, battery_service_srv
from django.conf import settings

def startMiscMessage():
    """
    Starts a miscellaneous message service call by enabling all commands.

    This method creates a miscellaneous message object and sets its command attribute to "enable_all".
    It then calls the miscToolsService method passing the created miscellaneous message object.

    Note: This method should be used to enable all miscellaneous commands before invoking the miscToolsService.

    Returns:
        None
    """
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

def show_img_service(url):
    if settings.USE_PEPPER_ROBOT:
        ros_show_img(url)

def show_web_service(url):
    if settings.USE_PEPPER_ROBOT:
        ros_show_web(url)

def ros_show_web(url):
    """
    Shows a webpage in the robots tablet
    """
    print("Waiting for tablet tools service")
    rospy.wait_for_service('/pytoolkit/ALTabletService/show_web_view_srv')
    try:
        tablet = rospy.ServiceProxy('/pytoolkit/ALTabletService/show_web_view_srv', tablet_service_srv)
        tabletService = tablet(url)
        print("Tablet service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def ros_show_img(url):
    """
    Shows an image in the robots tablet
    """
    print("Waiting for tablet tools service")
    rospy.wait_for_service('/pytoolkit/ALTabletService/show_image_srv')
    try:
        tablet = rospy.ServiceProxy('/pytoolkit/ALTabletService/show_image_srv', tablet_service_srv)
        tabletService = tablet(url)
        print("Tablet service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")


def mock_battery_service():
    """
    MockBatteryService

    Returns a random integer between 0 and 100, representing the battery level.

    :return: A random integer between 0 and 100.
    """
    return 100


def ros_battery_service():
    """
    Function: rosBatteryService

    Description:
    This function waits for the battery tools service and retrieves the battery percentage using the ROS ServiceProxy.

    Parameters:
    None

    :return:
    The battery percentage as an integer value.
    """
    print("Waiting for battery service")
    rospy.wait_for_service('/pytoolkit/ALBatteryService/get_porcentage')
    print("Finished waiting for battery service")
    try:
        batteryS = rospy.ServiceProxy('/pytoolkit/ALBatteryService/get_porcentage', battery_service_srv)
        batteryService = batteryS()
        print("Battery service connected!")
        return batteryService.porcentage
    except rospy.ServiceException as e:
        print("Service call failed")
        return mockBatteryService()


def battery_service():
    """
    Returns the battery service based on the settings.

    :return: The battery service to be used.
    """
    if settings.USE_PEPPER_ROBOT:
        return ros_battery_service()
    return mock_battery_service()


def save_image(image):
    filename = image.name.replace(" ", "_")

    full_filename = os.path.join(settings.MEDIA_ROOT + "/img/", filename)
    file_output = open(full_filename, 'wb+')

    file_content = ContentFile(image.read())
    for chunk in file_content.chunks():
        file_output.write(chunk)
    file_output.close()
    return filename


def remove_images():
    images_folder = settings.MEDIA_ROOT + "/img/"
    for filename in os.listdir(images_folder):
        file_path = os.path.join(images_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))