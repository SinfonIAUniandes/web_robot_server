import rospy
from robot_toolkit_msgs.msg import vision_tools_msg
from robot_toolkit_msgs.srv import vision_tools_srv

def startPerceptionMessage():
    #Service vision calls
    #Start front Camera
    visionMessage = vision_tools_msg()
    visionMessage.camera_name = "front_camera".encode('ascii')#botoom
    visionMessage.command = "custom"
    visionMessage.resolution = 1
    visionMessage.frame_rate = 20
    visionMessage.color_space = 11
    visionToolsService(visionMessage)
    #Start bottom camera
    visionMessage = vision_tools_msg()
    visionMessage.camera_name = "bottom_camera".encode('ascii')#botoom
    visionMessage.command = "custom"
    visionMessage.resolution = 1
    visionMessage.frame_rate = 20
    visionMessage.color_space = 11
    visionToolsService(visionMessage)

def visionToolsService(msg):
    """
    Enables the vision Tools service from the toolkit of the robot.
    """
    print("Waiting for vision tools service")
    rospy.wait_for_service('/robot_toolkit/vision_tools_srv')
    try:
        vision = rospy.ServiceProxy('/robot_toolkit/vision_tools_srv', vision_tools_srv)
        visionService = vision(msg)
        print("Vision tools service connected!")
    except rospy.ServiceException as e:
        print("Vision call failed")