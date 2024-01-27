import rospy
from robot_toolkit_msgs.msg import motion_tools_msg, set_angles_msg, animation_msg
from robot_toolkit_msgs.srv import motion_tools_srv

def startManipulationMessage():
    #Service motion call
    motionMessage = motion_tools_msg()
    motionMessage.command = "enable_all"
    motionToolsService(motionMessage)
    
def motionToolsService(msg):
    """
    Enables the motion Tools service from the toolkit of the robot.
    """
    print("Waiting for motion tools service")
    rospy.wait_for_service('/robot_toolkit/motion_tools_srv')
    try:
        motion = rospy.ServiceProxy('/robot_toolkit/motion_tools_srv', motion_tools_srv)
        motionService = motion(msg)
        print("Motion tools service connected!")
    except rospy.ServiceException as e:
        print("Service call failed")

def genMsg(animation):
    anim_msg = animation_msg()
    anim_msg.family = "animations"
    anim_msg.animation_name = animation
    return anim_msg

def genHeadMsg(angle0,angle1):
    jointMsg = set_angles_msg()
    jointMsg.names = ["HeadPitch".encode('ascii'),"HeadYaw".encode('ascii')]
    jointMsg.angles = [float(angle0),float(angle1)]
    jointMsg.fraction_max_speed = [0.1,0.1]
    return jointMsg